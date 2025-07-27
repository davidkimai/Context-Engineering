#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Context-Engineering: RAG Recipes for Retrieval-Augmented Generation
===================================================================

This module demonstrates practical implementations of Retrieval-Augmented
Generation (RAG) patterns for enhancing LLM contexts with external knowledge.
We focus on minimal, efficient implementations that highlight the key concepts
without requiring complex infrastructure.

Key concepts covered:
1. Basic RAG pipeline construction
2. Context window management and chunking strategies 
3. Embedding and retrieval techniques
4. Measuring retrieval quality and relevance
5. Context integration patterns
6. Advanced RAG variations

Usage:
    # In Jupyter or Colab:
    %run 04_rag_recipes.py
    # or
    from rag_recipes import SimpleRAG, ChunkedRAG, HybridRAG
"""

import os
import re
import json
import time
import numpy as np
import logging
import tiktoken
from typing import Dict, List, Tuple, Any, Optional, Union, Callable, TypeVar
from dataclasses import dataclass
import matplotlib.pyplot as plt
from IPython.display import display, Markdown, HTML

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Check for required libraries
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logger.warning("OpenAI package not found. Install with: pip install openai")

try:
    import dotenv
    dotenv.load_dotenv()
    ENV_LOADED = True
except ImportError:
    ENV_LOADED = False
    logger.warning("python-dotenv not found. Install with: pip install python-dotenv")

try:
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    logger.warning("scikit-learn not found. Install with: pip install scikit-learn")

try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False
    logger.warning("NumPy not found. Install with: pip install numpy")

try:
    import faiss
    FAISS_AVAILABLE = True
except ImportError:
    FAISS_AVAILABLE = False
    logger.warning("FAISS not found. Install with: pip install faiss-cpu or faiss-gpu")

# Constants
DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_EMBEDDING_MODEL = "text-embedding-ada-002"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 500
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200
DEFAULT_TOP_K = 3


# Basic Data Structures
# =====================

@dataclass
class Document:
    """Represents a document or chunk of text with metadata."""
    content: str
    metadata: Dict[str, Any] = None
    embedding: Optional[List[float]] = None
    id: Optional[str] = None
    
    def __post_init__(self):
        """Initialize default values if not provided."""
        if self.metadata is None:
            self.metadata = {}
        
        if self.id is None:
            # Generate a simple ID based on content hash
            import hashlib
            self.id = hashlib.md5(self.content.encode()).hexdigest()[:8]


# Helper Functions
# ===============

def setup_client(api_key=None, model=DEFAULT_MODEL):
    """
    Set up the API client for LLM interactions.

    Args:
        api_key: API key (if None, will look for OPENAI_API_KEY in env)
        model: Model name to use

    Returns:
        tuple: (client, model_name)
    """
    if api_key is None:
        api_key = os.environ.get("OPENAI_API_KEY")
        if api_key is None and not ENV_LOADED:
            logger.warning("No API key found. Set OPENAI_API_KEY env var or pass api_key param.")
    
    if OPENAI_AVAILABLE:
        client = OpenAI(api_key=api_key)
        return client, model
    else:
        logger.error("OpenAI package required. Install with: pip install openai")
        return None, model


def count_tokens(text: str, model: str = DEFAULT_MODEL) -> int:
    """
    Count tokens in text string using the appropriate tokenizer.

    Args:
        text: Text to tokenize
        model: Model name to use for tokenization

    Returns:
        int: Token count
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))
    except Exception as e:
        # Fallback for when tiktoken doesn't support the model
        logger.warning(f"Could not use tiktoken for {model}: {e}")
        # Rough approximation: 1 token ≈ 4 chars in English
        return len(text) // 4


def generate_embedding(
    text: str,
    client=None,
    model: str = DEFAULT_EMBEDDING_MODEL
) -> List[float]:
    """
    Generate an embedding vector for the given text.

    Args:
        text: Text to embed
        client: API client (if None, will create one)
        model: Embedding model name

    Returns:
        list: Embedding vector
    """
    if client is None:
        client, _ = setup_client()
        if client is None:
            # Return dummy embedding if no client available
            return [0.0] * 1536  # Default size for many embedding models
    
    try:
        response = client.embeddings.create(
            model=model,
            input=[text]
        )
        return response.data[0].embedding
    except Exception as e:
        logger.error(f"Error generating embedding: {e}")
        # Return dummy embedding on error
        return [0.0] * 1536


def generate_response(
    prompt: str,
    client=None,
    model: str = DEFAULT_MODEL,
    temperature: float = DEFAULT_TEMPERATURE,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    system_message: str = "You are a helpful assistant."
) -> Tuple[str, Dict[str, Any]]:
    """
    Generate a response from the LLM and return with metadata.

    Args:
        prompt: The prompt to send
        client: API client (if None, will create one)
        model: Model name
        temperature: Temperature parameter
        max_tokens: Maximum tokens to generate
        system_message: System message to use

    Returns:
        tuple: (response_text, metadata)
    """
    if client is None:
        client, model = setup_client(model=model)
        if client is None:
            return "ERROR: No API client available", {"error": "No API client"}
    
    prompt_tokens = count_tokens(prompt, model)
    system_tokens = count_tokens(system_message, model)
    
    metadata = {
        "prompt_tokens": prompt_tokens,
        "system_tokens": system_tokens,
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "timestamp": time.time()
    }
    
    try:
        start_time = time.time()
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        latency = time.time() - start_time
        
        response_text = response.choices[0].message.content
        response_tokens = count_tokens(response_text, model)
        
        metadata.update({
            "latency": latency,
            "response_tokens": response_tokens,
            "total_tokens": prompt_tokens + system_tokens + response_tokens,
            "token_efficiency": response_tokens / (prompt_tokens + system_tokens) if (prompt_tokens + system_tokens) > 0 else 0,
            "tokens_per_second": response_tokens / latency if latency > 0 else 0
        })
        
        return response_text, metadata
    
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        metadata["error"] = str(e)
        return f"ERROR: {str(e)}", metadata


def format_metrics(metrics: Dict[str, Any]) -> str:
    """
    Format metrics dictionary into a readable string.
    
    Args:
        metrics: Dictionary of metrics
        
    Returns:
        str: Formatted metrics string
    """
    # Select the most important metrics to show
    key_metrics = {
        "prompt_tokens": metrics.get("prompt_tokens", 0),
        "response_tokens": metrics.get("response_tokens", 0),
        "total_tokens": metrics.get("total_tokens", 0),
        "latency": f"{metrics.get('latency', 0):.2f}s",
        "token_efficiency": f"{metrics.get('token_efficiency', 0):.2f}"
    }
    
    return " | ".join([f"{k}: {v}" for k, v in key_metrics.items()])


def display_response(
    prompt: str,
    response: str,
    retrieved_context: Optional[str] = None,
    metrics: Dict[str, Any] = None,
    show_prompt: bool = True,
    show_context: bool = True
) -> None:
    """
    Display a prompt-response pair with metrics in a notebook.
    
    Args:
        prompt: The prompt text
        response: The response text
        retrieved_context: Retrieved context (optional)
        metrics: Metrics dictionary (optional)
        show_prompt: Whether to show the prompt text
        show_context: Whether to show the retrieved context
    """
    if show_prompt:
        display(HTML("<h4>Query:</h4>"))
        display(Markdown(f"```\n{prompt}\n```"))
    
    if retrieved_context and show_context:
        display(HTML("<h4>Retrieved Context:</h4>"))
        display(Markdown(f"```\n{retrieved_context}\n```"))
    
    display(HTML("<h4>Response:</h4>"))
    display(Markdown(response))
    
    if metrics:
        display(HTML("<h4>Metrics:</h4>"))
        display(Markdown(f"```\n{format_metrics(metrics)}\n```"))


# Document Processing Functions
# ============================

def text_to_chunks(
    text: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    model: str = DEFAULT_MODEL
) -> List[Document]:
    """
    Split text into overlapping chunks of specified token size.
    
    Args:
        text: Text to split
        chunk_size: Maximum tokens per chunk
        chunk_overlap: Number of tokens to overlap between chunks
        model: Model to use for tokenization
        
    Returns:
        list: List of Document objects
    """
    if not text:
        return []
    
    # Get tokenizer
    try:
        encoding = tiktoken.encoding_for_model(model)
    except:
        logger.warning(f"Could not get tokenizer for {model}. Using approximate chunking.")
        return _approximate_text_to_chunks(text, chunk_size, chunk_overlap)
    
    # Tokenize the text
    tokens = encoding.encode(text)
    
    # Create chunks
    chunks = []
    i = 0
    while i < len(tokens):
        # Extract chunk tokens
        chunk_end = min(i + chunk_size, len(tokens))
        chunk_tokens = tokens[i:chunk_end]
        
        # Decode back to text
        chunk_text = encoding.decode(chunk_tokens)
        
        # Create document
        chunks.append(Document(
            content=chunk_text,
            metadata={
                "start_idx": i,
                "end_idx": chunk_end,
                "chunk_size": len(chunk_tokens)
            }
        ))
        
        # Move to next chunk, considering overlap
        i += max(1, chunk_size - chunk_overlap)
    
    return chunks


def _approximate_text_to_chunks(
    text: str,
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP
) -> List[Document]:
    """
    Split text into chunks using a simple character-based approximation.
    
    Args:
        text: Text to split
        chunk_size: Approximate characters per chunk (assumes ~4 chars/token)
        chunk_overlap: Approximate characters to overlap
        
    Returns:
        list: List of Document objects
    """
    # Convert token sizes to character sizes (approximate)
    char_size = chunk_size * 4
    char_overlap = chunk_overlap * 4
    
    # Split by paragraphs first (to avoid breaking in the middle of paragraphs if possible)
    paragraphs = text.split('\n\n')
    
    chunks = []
    current_chunk = []
    current_size = 0
    
    for paragraph in paragraphs:
        paragraph_size = len(paragraph)
        
        # If adding this paragraph would exceed the chunk size
        if current_size + paragraph_size > char_size and current_chunk:
            # Create a chunk from the current text
            chunk_text = '\n\n'.join(current_chunk)
            chunks.append(Document(
                content=chunk_text,
                metadata={"approx_size": current_size}
            ))
            
            # Start a new chunk with overlap
            # Find the paragraphs that should be included in the overlap
            overlap_size = 0
            overlap_paragraphs = []
            
            for p in reversed(current_chunk):
                p_size = len(p)
                if overlap_size + p_size <= char_overlap:
                    overlap_paragraphs.insert(0, p)
                    overlap_size += p_size
                else:
                    break
            
            current_chunk = overlap_paragraphs
            current_size = overlap_size
        
        # Add the current paragraph
        current_chunk.append(paragraph)
        current_size += paragraph_size
    
    # Add the last chunk if there's anything left
    if current_chunk:
        chunk_text = '\n\n'.join(current_chunk)
        chunks.append(Document(
            content=chunk_text,
            metadata={"approx_size": current_size}
        ))
    
    return chunks


def extract_document_batch_embeddings(
    documents: List[Document],
    client=None,
    model: str = DEFAULT_EMBEDDING_MODEL,
    batch_size: int = 10
) -> List[Document]:
    """
    Generate embeddings for a batch of documents efficiently.
    
    Args:
        documents: List of Document objects to embed
        client: API client (if None, will create one)
        model: Embedding model to use
        batch_size: Number of documents to embed in each API call
        
    Returns:
        list: Updated Document objects with embeddings
    """
    if not documents:
        return []
    
    if client is None:
        client, _ = setup_client()
        if client is None:
            logger.error("No API client available for embeddings")
            return documents
    
    # Process in batches
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i+batch_size]
        batch_texts = [doc.content for doc in batch]
        
        try:
            # Generate embeddings for the batch
            response = client.embeddings.create(
                model=model,
                input=batch_texts
            )
            
            # Update documents with embeddings
            for j, doc in enumerate(batch):
                if j < len(response.data):
                    doc.embedding = response.data[j].embedding
                else:
                    logger.warning(f"Missing embedding for document {i+j}")
        except Exception as e:
            logger.error(f"Error generating batch embeddings: {e}")
    
    return documents


def similarity_search(
    query_embedding: List[float],
    documents: List[Document],
    top_k: int = DEFAULT_TOP_K
) -> List[Tuple[Document, float]]:
    """
    Find the most similar documents to a query embedding.
    
    Args:
        query_embedding: Query embedding vector
        documents: List of Document objects with embeddings
        top_k: Number of results to return
        
    Returns:
        list: List of (document, similarity_score) tuples
    """
    if not NUMPY_AVAILABLE:
        logger.error("NumPy required for similarity search")
        return []
    
    # Filter out documents without embeddings
    docs_with_embeddings = [doc for doc in documents if doc.embedding is not None]
    
    if not docs_with_embeddings:
        logger.warning("No documents with embeddings found")
        return []
    
    # Convert embeddings to numpy arrays
    query_embedding_np = np.array(query_embedding).reshape(1, -1)
    doc_embeddings = np.array([doc.embedding for doc in docs_with_embeddings])
    
    # Calculate cosine similarities
    if SKLEARN_AVAILABLE:
        similarities = cosine_similarity(query_embedding_np, doc_embeddings)[0]
    else:
        # Fallback to manual cosine similarity calculation
        norm_query = np.linalg.norm(query_embedding_np)
        norm_docs = np.linalg.norm(doc_embeddings, axis=1)
        dot_products = np.dot(query_embedding_np, doc_embeddings.T)[0]
        similarities = dot_products / (norm_query * norm_docs)
    
    # Create (document, similarity) pairs
    doc_sim_pairs = list(zip(docs_with_embeddings, similarities))
    
    # Sort by similarity (descending) and take top_k
    sorted_pairs = sorted(doc_sim_pairs, key=lambda x: x[1], reverse=True)
    return sorted_pairs[:top_k]


def create_faiss_index(documents: List[Document]) -> Any:
    """
    Create a FAISS index from document embeddings for efficient similarity search.
    
    Args:
        documents: List of Document objects with embeddings
        
    Returns:
        object: FAISS index or None if FAISS not available
    """
    if not FAISS_AVAILABLE:
        logger.error("FAISS required for indexing")
        return None
    
    # Filter out documents without embeddings
    docs_with_embeddings = [doc for doc in documents if doc.embedding is not None]
    
    if not docs_with_embeddings:
        logger.warning("No documents with embeddings found")
        return None
    
    # Get embedding dimension from first document
    embedding_dim = len(docs_with_embeddings[0].embedding)
    
    # Create FAISS index
    index = faiss.IndexFlatL2(embedding_dim)
    
    # Add embeddings to index
    embeddings = np.array([doc.embedding for doc in docs_with_embeddings], dtype=np.float32)
    index.add(embeddings)
    
    return index, docs_with_embeddings


def faiss_similarity_search(
    query_embedding: List[float],
    faiss_index: Any,
    documents: List[Document],
    top_k: int = DEFAULT_TOP_K
) -> List[Tuple[Document, float]]:
    """
    Find the most similar documents using a FAISS index.
    
    Args:
        query_embedding: Query embedding vector
        faiss_index: FAISS index (from create_faiss_index)
        documents: List of Document objects corresponding to the index
        top_k: Number of results to return
        
    Returns:
        list: List of (document, similarity_score) tuples
    """
    if not FAISS_AVAILABLE:
        logger.error("FAISS required for similarity search")
        return []
    
    if faiss_index is None:
        logger.error("FAISS index is None")
        return []
    
    # Unpack the index and documents if returned from create_faiss_index
    if isinstance(faiss_index, tuple):
        index, docs_with_embeddings = faiss_index
    else:
        index = faiss_index
        docs_with_embeddings = documents
    
    # Convert query to numpy array
    query_np = np.array([query_embedding], dtype=np.float32)
    
    # Search the index
    distances, indices = index.search(query_np, top_k)
    
    # Create (document, similarity) pairs
    # Convert L2 distance to similarity score (higher is better)
    results = []
    for i in range(len(indices[0])):
        idx = indices[0][i]
        if idx < len(docs_with_embeddings):
            # Convert L2 distance to similarity (1 / (1 + distance))
            similarity = 1.0 / (1.0 + distances[0][i])
            results.append((docs_with_embeddings[idx], similarity))
    
    return results


# RAG System Base Class
# =====================

class RAGSystem:
    """
    Base class for Retrieval-Augmented Generation systems.
    Provides common functionality and interfaces.
    """
    
    def __init__(
        self,
        client=None,
        model: str = DEFAULT_MODEL,
        embedding_model: str = DEFAULT_EMBEDDING_MODEL,
        system_message: str = "You are a helpful assistant that answers based on the retrieved context.",
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        verbose: bool = False
    ):
        """
        Initialize the RAG system.
        
        Args:
            client: API client (if None, will create one)
            model: Model name to use for generation
            embedding_model: Model name to use for embeddings
            system_message: System message to use
            max_tokens: Maximum tokens to generate
            temperature: Temperature parameter
            verbose: Whether to print debug information
        """
        self.client, self.model = setup_client(model=model) if client is None else (client, model)
        self.embedding_model = embedding_model
        self.system_message = system_message
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.verbose = verbose
        
        # Initialize document store
        self.documents = []
        
        # Initialize history and metrics tracking
        self.history = []
        self.metrics = {
            "total_prompt_tokens": 0,
            "total_response_tokens": 0,
            "total_tokens": 0,
            "total_latency": 0,
            "retrieval_latency": 0,
            "queries": 0
        }
    
    def _log(self, message: str) -> None:
        """
        Log a message if verbose mode is enabled.
        
        Args:
            message: Message to log
        """
        if self.verbose:
            logger.info(message)
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the document store.
        
        Args:
            documents: List of Document objects to add
        """
        self.documents.extend(documents)
    
    def add_texts(
        self,
        texts: List[str],
        metadatas: Optional[List[Dict[str, Any]]] = None
    ) -> None:
        """
        Add texts to the document store with optional metadata.
        
        Args:
            texts: List of text strings to add
            metadatas: List of metadata dictionaries (optional)
        """
        if metadatas is None:
            metadatas = [{} for _ in texts]
        
        # Create Document objects
        documents = [
            Document(content=text, metadata=metadata)
            for text, metadata in zip(texts, metadatas)
        ]
        
        self.add_documents(documents)
    
    def _retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Retrieve relevant documents for a query.
        
        Args:
            query: Query string
            top_k: Number of results to return
            
        Returns:
            list: List of (document, similarity_score) tuples
        """
        # This is a placeholder - subclasses should implement this
        raise NotImplementedError("Subclasses must implement _retrieve")
    
    def _format_context(
        self,
        retrieved_documents: List[Tuple[Document, float]]
    ) -> str:
        """
        Format retrieved documents into a context string.
        
        Args:
            retrieved_documents: List of (document, similarity_score) tuples
            
        Returns:
            str: Formatted context string
        """
        context_parts = []
        
        for i, (doc, score) in enumerate(retrieved_documents):
            # Format the document with metadata
            source_info = ""
            if doc.metadata:
                # Extract source information if available
                source = doc.metadata.get("source", "")
                if source:
                    source_info = f" (Source: {source})"
            
            context_parts.append(f"[Document {i+1}{source_info}]\n{doc.content}\n")
        
        return "\n".join(context_parts)
    
    def _create_prompt(
        self,
        query: str,
        context: str
    ) -> str:
        """
        Create a prompt combining the query and retrieved context.
        
        Args:
            query: User query
            context: Retrieved context
            
        Returns:
            str: Formatted prompt
        """
        return f"""Answer the following question based on the retrieved context. If the context doesn't contain relevant information, say so instead of making up an answer.

Retrieved Context:
{context}

Question: {query}

Answer:"""
    
    def query(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Process a query through the RAG pipeline.
        
        Args:
            query: Query string
            top_k: Number of results to return
            
        Returns:
            tuple: (response, details)
        """
        self._log(f"Processing query: {query}")
        
        # Retrieve relevant documents
        start_time = time.time()
        retrieved_docs = self._retrieve(query, top_k)
        retrieval_latency = time.time() - start_time
        
        # Format context from retrieved documents
        context = self._format_context(retrieved_docs)
        
        # Create prompt
        prompt = self._create_prompt(query, context)
        
        # Generate response
        response, metadata = generate_response(
            prompt=prompt,
            client=self.client,
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            system_message=self.system_message
        )
        
        # Update metrics
        self.metrics["total_prompt_tokens"] += metadata.get("prompt_tokens", 0)
        self.metrics["total_response_tokens"] += metadata.get("response_tokens", 0)
        self.metrics["total_tokens"] += metadata.get("total_tokens", 0)
        self.metrics["total_latency"] += metadata.get("latency", 0)
        self.metrics["retrieval_latency"] += retrieval_latency
        self.metrics["queries"] += 1
        
        # Add to history
        query_record = {
            "query": query,
            "retrieved_docs": [(doc.content, score) for doc, score in retrieved_docs],
            "context": context,
            "prompt": prompt,
            "response": response,
            "metrics": {
                **metadata,
                "retrieval_latency": retrieval_latency
            },
            "timestamp": time.time()
        }
        self.history.append(query_record)
        
        # Create details dictionary
        details = {
            "query": query,
            "retrieved_docs": retrieved_docs,
            "context": context,
            "response": response,
            "metrics": {
                **metadata,
                "retrieval_latency": retrieval_latency
            }
        }
        
        return response, details
    
    def get_summary_metrics(self) -> Dict[str, Any]:
        """
        Get summary metrics for all queries.
        
        Returns:
            dict: Summary metrics
        """
        summary = self.metrics.copy()
        
        # Add derived metrics
        if summary["queries"] > 0:
            summary["avg_latency_per_query"] = summary["total_latency"] / summary["queries"]
            summary["avg_retrieval_latency"] = summary["retrieval_latency"] / summary["queries"]
            
        if summary["total_prompt_tokens"] > 0:
            summary["overall_efficiency"] = (
                summary["total_response_tokens"] / summary["total_prompt_tokens"]
            )
        
        return summary
    
    def display_query_results(self, details: Dict[str, Any], show_context: bool = True) -> None:
        """
        Display the query results in a notebook.
        
        Args:
            details: Query details from query()
            show_context: Whether to show the retrieved context
        """
        display(HTML("<h2>RAG Query Results</h2>"))
        
        # Display query
        display(HTML("<h3>Query</h3>"))
        display(Markdown(details["query"]))
        
        # Display retrieved documents
        if show_context and "retrieved_docs" in details:
            display(HTML("<h3>Retrieved Documents</h3>"))
            
            for i, (doc, score) in enumerate(details["retrieved_docs"]):
                display(HTML(f"<h4>Document {i+1} (Score: {score:.4f})</h4>"))
                
                # Display metadata if available
                if doc.metadata:
                    display(HTML("<p><em>Metadata:</em></p>"))
                    display(Markdown(f"```json\n{json.dumps(doc.metadata, indent=2)}\n```"))
                
                # Display content
                display(Markdown(f"```\n{doc.content}\n```"))
        
        # Display response
        display(HTML("<h3>Response</h3>"))
        display(Markdown(details["response"]))
        
        # Display metrics
        if "metrics" in details:
            display(HTML("<h3>Metrics</h3>"))
            metrics = details["metrics"]
            
            # Format metrics
            display(Markdown(f"""
            - Prompt tokens: {metrics.get('prompt_tokens', 0)}
            - Response tokens: {metrics.get('response_tokens', 0)}
            - Total tokens: {metrics.get('total_tokens', 0)}
            - Generation latency: {metrics.get('latency', 0):.2f}s
            - Retrieval latency: {metrics.get('retrieval_latency', 0):.2f}s
            - Total latency: {metrics.get('latency', 0) + metrics.get('retrieval_latency', 0):.2f}s
            """))
    
    def visualize_metrics(self) -> None:
        """
        Create visualization of metrics across queries.
        """
        if not self.history:
            logger.warning("No history to visualize")
            return
        
        # Extract data for plotting
        queries = list(range(1, len(self.history) + 1))
        prompt_tokens = [h["metrics"].get("prompt_tokens", 0) for h in self.history]
        response_tokens = [h["metrics"].get("response_tokens", 0) for h in self.history]
        generation_latencies = [h["metrics"].get("latency", 0) for h in self.history]
        retrieval_latencies = [h["metrics"].get("retrieval_latency", 0) for h in self.history]
        total_latencies = [g + r for g, r in zip(generation_latencies, retrieval_latencies)]
        
        # Create figure
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("RAG System Metrics by Query", fontsize=16)
        
        # Plot 1: Token usage
        axes[0, 0].bar(queries, prompt_tokens, label="Prompt Tokens", color="blue", alpha=0.7)
        axes[0, 0].bar(queries, response_tokens, bottom=prompt_tokens, 
                       label="Response Tokens", color="green", alpha=0.7)
        axes[0, 0].set_title("Token Usage")
        axes[0, 0].set_xlabel("Query")
        axes[0, 0].set_ylabel("Tokens")
        axes[0, 0].legend()
        axes[0, 0].grid(alpha=0.3)
        
        # Plot 2: Latency breakdown
        axes[0, 1].bar(queries, retrieval_latencies, label="Retrieval", color="orange", alpha=0.7)
        axes[0, 1].bar(queries, generation_latencies, bottom=retrieval_latencies, 
                      label="Generation", color="red", alpha=0.7)
        axes[0, 1].set_title("Latency Breakdown")
        axes[0, 1].set_xlabel("Query")
        axes[0, 1].set_ylabel("Seconds")
        axes[0, 1].legend()
        axes[0, 1].grid(alpha=0.3)
        
        # Plot 3: Retrieval count
        if any("retrieved_docs" in h for h in self.history):
            doc_counts = [len(h.get("retrieved_docs", [])) for h in self.history]
            axes[1, 0].plot(queries, doc_counts, marker='o', color="purple", alpha=0.7)
            axes[1, 0].set_title("Retrieved Documents Count")
            axes[1, 0].set_xlabel("Query")
            axes[1, 0].set_ylabel("Count")
            axes[1, 0].grid(alpha=0.3)
        
        # Plot 4: Cumulative tokens
        cumulative_tokens = np.cumsum([h["metrics"].get("total_tokens", 0) for h in self.history])
        axes[1, 1].plot(queries, cumulative_tokens, marker='^', color="brown", alpha=0.7)
        axes[1, 1].set_title("Cumulative Token Usage")
        axes[1, 1].set_xlabel("Query")
        axes[1, 1].set_ylabel("Total Tokens")
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()


# RAG System Implementations
# =========================

class SimpleRAG(RAGSystem):
    """
    A simple RAG system that uses embeddings for similarity search.
    """
    
    def __init__(self, **kwargs):
        """Initialize the simple RAG system."""
        super().__init__(**kwargs)
        
        # Whether documents have been embedded
        self.documents_embedded = False
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the document store and reset embedding flag.
        
        Args:
            documents: List of Document objects to add
        """
        super().add_documents(documents)
        self.documents_embedded = False
    
    def _ensure_documents_embedded(self) -> None:
        """Ensure all documents have embeddings."""
        if self.documents_embedded:
            return
        
        docs_to_embed = [doc for doc in self.documents if doc.embedding is None]
        
        if docs_to_embed:
            self._log(f"Generating embeddings for {len(docs_to_embed)} documents")
            extract_document_batch_embeddings(
                docs_to_embed, 
                client=self.client,
                model=self.embedding_model
            )
        
        self.documents_embedded = True
    
    def _retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Retrieve relevant documents for a query using embedding similarity.
        
        Args:
            query: Query string
            top_k: Number of results to return
            
        Returns:
            list: List of (document, similarity_score) tuples
        """
        # Ensure documents are embedded
        self._ensure_documents_embedded()
        
        if not self.documents:
            self._log("No documents in the document store")
            return []
        
        # Generate query embedding
        query_embedding = generate_embedding(
            query,
            client=self.client,
            model=self.embedding_model
        )
        
        # Perform similarity search
        results = similarity_search(
            query_embedding,
            self.documents,
            top_k
        )
        
        return results


class ChunkedRAG(SimpleRAG):
    """
    A RAG system that chunks documents before indexing.
    """
    
    def __init__(
        self,
        chunk_size: int = DEFAULT_CHUNK_SIZE,
        chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
        **kwargs
    ):
        """
        Initialize the chunked RAG system.
        
        Args:
            chunk_size: Maximum tokens per chunk
            chunk_overlap: Number of tokens to overlap between chunks
            **kwargs: Additional args passed to RAGSystem
        """
        super().__init__(**kwargs)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Original documents before chunking
        self.original_documents = []
        
        # Whether to use FAISS for retrieval (if available)
        self.use_faiss = FAISS_AVAILABLE
        self.faiss_index = None
    
    def add_documents(self, documents: List[Document]) -> None:
        """
        Add documents to the store, chunk them, and reset embedding flag.
        
        Args:
            documents: List of Document objects to add
        """
        # Store original documents
        self.original_documents.extend(documents)
        
        # Chunk each document
        chunked_docs = []
        for doc in documents:
            chunks = text_to_chunks(
                doc.content,
                chunk_size=self.chunk_size,
                chunk_overlap=self.chunk_overlap,
                model=self.model
            )
            
            # Copy metadata to chunks and add parent reference
            for i, chunk in enumerate(chunks):
                chunk.metadata.update(doc.metadata)
                chunk.metadata["parent_id"] = doc.id
                chunk.metadata["chunk_index"] = i
                chunk.metadata["parent_content"] = doc.content[:100] + "..." if len(doc.content) > 100 else doc.content
            
            chunked_docs.extend(chunks)
        
        # Add chunked documents to store
        super().add_documents(chunked_docs)
        
        # Reset FAISS index if using FAISS
        if self.use_faiss:
            self.faiss_index = None
    
    def _ensure_documents_embedded(self) -> None:
        """Ensure all documents have embeddings and build FAISS index if needed."""
        super()._ensure_documents_embedded()
        
        # Build FAISS index if using FAISS
        if self.use_faiss and self.faiss_index is None and self.documents:
            self._log("Building FAISS index")
            self.faiss_index = create_faiss_index(self.documents)
    
    def _retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Retrieve relevant document chunks using embedding similarity or FAISS.
        
        Args:
            query: Query string
            top_k: Number of results to return
            
        Returns:
            list: List of (document, similarity_score) tuples
        """
        # Ensure documents are embedded and FAISS index is built if needed
        self._ensure_documents_embedded()
        
        if not self.documents:
            self._log("No documents in the document store")
            return []
        
        # Generate query embedding
        query_embedding = generate_embedding(
            query,
            client=self.client,
            model=self.embedding_model
        )
        
        # Use FAISS for retrieval if available
        if self.use_faiss and self.faiss_index is not None:
            results = faiss_similarity_search(
                query_embedding,
                self.faiss_index,
                self.documents,
                top_k
            )
        else:
            # Fall back to basic similarity search
            results = similarity_search(
                query_embedding,
                self.documents,
                top_k
            )
        
        return results


class HybridRAG(ChunkedRAG):
    """
    A RAG system that combines embedding similarity with keyword search.
    """
    
    def __init__(
        self,
        keyword_weight: float = 0.3,
        **kwargs
    ):
        """
        Initialize the hybrid RAG system.
        
        Args:
            keyword_weight: Weight for keyword search (0.0 to 1.0)
            **kwargs: Additional args passed to ChunkedRAG
        """
        super().__init__(**kwargs)
        self.keyword_weight = max(0.0, min(1.0, keyword_weight))
        self.embedding_weight = 1.0 - self.keyword_weight
    
    def _keyword_search(
        self,
        query: str,
        documents: List[Document],
        top_k: int = DEFAULT_TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Perform keyword search on documents.
        
        Args:
            query: Query string
            documents: List of Document objects
            top_k: Number of results to return
            
        Returns:
            list: List of (document, similarity_score) tuples
        """
        # Simple keyword matching
        query_terms = set(query.lower().split())
        
        results = []
        for doc in documents:
            content = doc.content.lower()
            
            # Count matching terms and calculate score
            matches = sum(1 for term in query_terms if term in content)
            score = matches / len(query_terms) if query_terms else 0.0
            
            results.append((doc, score))
        
        # Sort by score (descending) and take top_k
        sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
        return sorted_results[:top_k]
    
    def _retrieve(
        self,
        query: str,
        top_k: int = DEFAULT_TOP_K
    ) -> List[Tuple[Document, float]]:
        """
        Retrieve relevant document chunks using hybrid search.
        
        Args:
            query: Query string
            top_k: Number of results to return
            
        Returns:
            list: List of (document, similarity_score) tuples
        """
        # Ensure documents are embedded
        self._ensure_documents_embedded()
        
        if not self.documents:
            self._log("No documents in the document store")
            return []
        
        # Generate query embedding
        query_embedding = generate_embedding(
            query,
            client=self.client,
            model=self.embedding_model
        )
        
        # Get semantic search results
        if self.use_faiss and self.faiss_index is not None:
            semantic_results = faiss_similarity_search(
                query_embedding
