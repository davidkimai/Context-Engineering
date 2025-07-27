"""
Context-Engineering Scoring Functions
------------------------------------

This module provides scoring functions to evaluate context quality and model responses
in context engineering applications. It includes metrics for:

1. Relevance - How well content relates to the query or objective
2. Coherence - How logically consistent and well-structured the content is
3. Comprehensiveness - How complete the information is
4. Conciseness - How efficiently information is presented
5. Accuracy - How factually correct the information is
6. Token Efficiency - How effectively the token budget is used
7. Field Resonance - How well content aligns with neural field patterns

Usage:
    # Score model response relevance
    relevance_score = score_relevance(response, query)
    
    # Score context coherence
    coherence_score = score_coherence(context)
    
    # Get comprehensive scoring for a response
    scores = score_response(response, query, context, reference=None)
"""

import math
import re
import time
import json
import logging
from typing import Dict, List, Any, Optional, Union, Tuple, Set, Callable
from collections import Counter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("scoring_functions")

# ------------------------------------------------------------------------------
# Text Processing Utilities
# ------------------------------------------------------------------------------

def tokenize(text: str) -> List[str]:
    """
    Simple tokenization function for text.
    
    Args:
        text: Input text
        
    Returns:
        List of tokens
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^\w\s]', ' ', text.lower())
    
    # Split into tokens
    return text.split()

def count_tokens(text: str) -> int:
    """
    Estimate the number of tokens in text.
    This is a rough approximation for planning purposes.
    
    Args:
        text: Input text
        
    Returns:
        Estimated token count
    """
    # Rough approximation: average token is ~4 characters
    # More accurate would be to use the specific tokenizer for your model
    return len(text) // 4

def extract_sentences(text: str) -> List[str]:
    """
    Extract sentences from text.
    
    Args:
        text: Input text
        
    Returns:
        List of sentences
    """
    # Split on sentence boundaries
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    
    # Remove empty sentences
    return [s.strip() for s in sentences if s.strip()]

def jaccard_similarity(set1: Set[str], set2: Set[str]) -> float:
    """
    Calculate Jaccard similarity between two sets.
    
    Args:
        set1: First set
        set2: Second set
        
    Returns:
        Jaccard similarity (0.0 to 1.0)
    """
    if not set1 or not set2:
        return 0.0
        
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    
    return intersection / union

def cosine_similarity(vec1: Dict[str, int], vec2: Dict[str, int]) -> float:
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vec1: First vector as word frequency dictionary
        vec2: Second vector as word frequency dictionary
        
    Returns:
        Cosine similarity (0.0 to 1.0)
    """
    if not vec1 or not vec2:
        return 0.0
        
    # Find common words
    common_words = set(vec1.keys()).intersection(set(vec2.keys()))
    
    # Calculate dot product
    dot_product = sum(vec1[word] * vec2[word] for word in common_words)
    
    # Calculate magnitudes
    mag1 = math.sqrt(sum(val ** 2 for val in vec1.values()))
    mag2 = math.sqrt(sum(val ** 2 for val in vec2.values()))
    
    # Avoid division by zero
    if mag1 == 0 or mag2 == 0:
        return 0.0
        
    return dot_product / (mag1 * mag2)

def get_word_frequency(text: str) -> Dict[str, int]:
    """
    Get word frequency dictionary from text.
    
    Args:
        text: Input text
        
    Returns:
        Word frequency dictionary
    """
    tokens = tokenize(text)
    return dict(Counter(tokens))

# ------------------------------------------------------------------------------
# Basic Scoring Functions
# ------------------------------------------------------------------------------

def score_relevance(response: str, query: str, method: str = "cosine") -> float:
    """
    Score the relevance of a response to a query.
    
    Args:
        response: Model response
        query: Original query
        method: Similarity method ("cosine" or "jaccard")
        
    Returns:
        Relevance score (0.0 to 1.0)
    """
    if not response or not query:
        return 0.0
        
    if method == "jaccard":
        # Jaccard similarity on token sets
        response_tokens = set(tokenize(response))
        query_tokens = set(tokenize(query))
        
        return jaccard_similarity(response_tokens, query_tokens)
        
    else:  # Default to cosine
        # Cosine similarity on word frequencies
        response_freq = get_word_frequency(response)
        query_freq = get_word_frequency(query)
        
        return cosine_similarity(response_freq, query_freq)

def score_coherence(text: str) -> float:
    """
    Score the coherence of text based on sentence flow and structure.
    
    Args:
        text: Input text
        
    Returns:
        Coherence score (0.0 to 1.0)
    """
    # Extract sentences
    sentences = extract_sentences(text)
    
    if len(sentences) <= 1:
        return 1.0  # Single sentence is coherent by default
        
    # Measure inter-sentence similarity
    total_similarity = 0.0
    
    for i in range(len(sentences) - 1):
        sent1 = sentences[i]
        sent2 = sentences[i + 1]
        
        # Get word sets
        words1 = set(tokenize(sent1))
        words2 = set(tokenize(sent2))
        
        # Calculate similarity
        similarity = jaccard_similarity(words1, words2)
        total_similarity += similarity
    
    # Average similarity
    avg_similarity = total_similarity / (len(sentences) - 1)
    
    # Check for transition words/phrases
    transition_words = [
        "however", "therefore", "thus", "consequently", "furthermore",
        "in addition", "moreover", "similarly", "in contrast", "nonetheless",
        "despite", "although", "because", "since", "as a result"
    ]
    
    transition_count = 0
    for sentence in sentences[1:]:  # Skip first sentence
        if any(word in sentence.lower() for word in transition_words):
            transition_count += 1
    
    transition_ratio = transition_count / (len(sentences) - 1) if len(sentences) > 1 else 0
    
    # Combine metrics (weighted average)
    coherence = (avg_similarity * 0.7) + (transition_ratio * 0.3)
    
    return coherence

def score_comprehensiveness(response: str, reference: Optional[str] = None, key_points: Optional[List[str]] = None) -> float:
    """
    Score the comprehensiveness of a response.
    
    Args:
        response: Model response
        reference: Optional reference answer
        key_points: Optional list of key points that should be covered
        
    Returns:
        Comprehensiveness score (0.0 to 1.0)
    """
    if not response:
        return 0.0
        
    # If reference is provided
    if reference:
        # Compare coverage of key terms
        response_terms = set(tokenize(response))
        reference_terms = set(tokenize(reference))
        
        # How many reference terms are covered
        coverage = len(response_terms.intersection(reference_terms)) / len(reference_terms) if reference_terms else 0
        
        return coverage
        
    # If key points are provided
    elif key_points:
        # Check how many key points are mentioned
        mentioned = 0
        for point in key_points:
            point_tokens = set(tokenize(point))
            response_tokens = set(tokenize(response))
            
            # Calculate overlap
            overlap = jaccard_similarity(point_tokens, response_tokens)
            
            if overlap > 0.3:  # Threshold for considering a point mentioned
                mentioned += 1
        
        return mentioned / len(key_points) if key_points else 0
        
    else:
        # No reference or key points, use length as a proxy
        # This is a weak proxy but better than nothing
        token_count = count_tokens(response)
        
        # Assume 150 tokens is comprehensive, scale accordingly
        return min(1.0, token_count / 150)

def score_conciseness(response: str, reference: Optional[str] = None, key_points: Optional[List[str]] = None) -> float:
    """
    Score the conciseness of a response.
    
    Args:
        response: Model response
        reference: Optional reference answer
        key_points: Optional list of key points that should be covered
        
    Returns:
        Conciseness score (0.0 to 1.0)
    """
    if not response:
        return 0.0
        
    # Get response token count
    response_tokens = count_tokens(response)
    
    # If reference is provided
    if reference:
        # Get reference token count
        reference_tokens = count_tokens(reference)
        
        # Comprehensiveness score
        comprehensiveness = score_comprehensiveness(response, reference)
        
        # Perfect conciseness would be having the same comprehensiveness with fewer tokens
        if response_tokens <= reference_tokens:
            # Response is more concise than reference
            conciseness = 1.0
        else:
            # Response is less concise than reference
            token_ratio = reference_tokens / response_tokens
            # Scale by comprehensiveness
            conciseness = token_ratio * comprehensiveness
        
        return conciseness
        
    # If key points are provided
    elif key_points:
        # Check how many key points are mentioned
        coverage = score_comprehensiveness(response, key_points=key_points)
        
        # Assume 30 tokens per key point is concise
        expected_tokens = len(key_points) * 30
        
        if response_tokens <= expected_tokens:
            # Response is more concise than expected
            conciseness = 1.0
        else:
            # Response is less concise than expected
            token_ratio = expected_tokens / response_tokens
            # Scale by coverage
            conciseness = token_ratio * coverage
        
        return conciseness
        
    else:
        # No reference or key points, use token density as a proxy
        # This is a weak proxy but better than nothing
        
        # Count unique substantive words (excluding common stop words)
        stop_words = {
            "the", "a", "an", "and", "or", "but", "is", "are", "was", "were",
            "in", "on", "at", "to", "for", "with", "by", "about", "as", "of"
        }
        
        tokens = tokenize(response)
        substantive_tokens = [t for t in tokens if t not in stop_words]
        unique_substantive = set(substantive_tokens)
        
        # Calculate information density
        if response_tokens > 0:
            density = len(unique_substantive) / response_tokens
            
            # Scale to 0-1 range (empirically, 0.5 is a good density)
            conciseness = min(1.0, density * 2.0)
        else:
            conciseness = 0.0
        
        return conciseness

def score_accuracy(response: str, reference: Optional[str] = None, facts: Optional[List[str]] = None) -> float:
    """
    Score the factual accuracy of a response.
    
    Args:
        response: Model response
        reference: Optional reference answer
        facts: Optional list of facts that should be included
        
    Returns:
        Accuracy score (0.0 to 1.0)
    """
    if not response:
        return 0.0
        
    # If reference is provided
    if reference:
        # This is a simplified approach - in a real application, you might
        # use a more sophisticated NLI or fact-checking approach
        
        # Get important facts from reference (simplified as sentences)
        reference_facts = extract_sentences(reference)
        
        if not reference_facts:
            return 0.0
            
        # Check each fact against the response
        response_tokens = set(tokenize(response))
        
        correct_facts = 0
        for fact in reference_facts:
            fact_tokens = set(tokenize(fact))
            
            # Calculate token overlap
            overlap = len(fact_tokens.intersection(response_tokens)) / len(fact_tokens) if fact_tokens else 0
            
            if overlap > 0.7:  # High overlap suggests the fact is included
                correct_facts += 1
        
        return correct_facts / len(reference_facts)
        
    # If specific facts are provided
    elif facts:
        if not facts:
            return 0.0
            
        # Check each fact against the response
        response_lower = response.lower()
        
        correct_facts = 0
        for fact in facts:
            # Simple check if the fact is contained in the response
            # A more sophisticated approach would check for semantic equivalence
            if fact.lower() in response_lower:
                correct_facts += 1
        
        return correct_facts / len(facts)
        
    else:
        # No reference or facts provided
        # We can't assess accuracy without a gold standard
        logger.warning("Cannot assess accuracy without reference or facts")
        return 0.5  # Return neutral score

def score_token_efficiency(response: str, max_tokens: int = 500) -> float:
    """
    Score the token efficiency of a response.
    
    Args:
        response: Model response
        max_tokens: Maximum token budget
        
    Returns:
        Efficiency score (0.0 to 1.0)
    """
    if not response:
        return 0.0
        
    # Count tokens in response
    token_count = count_tokens(response)
    
    if token_count > max_tokens:
        # Response exceeds token budget
        return 0.0
        
    # Calculate information density
    tokens = tokenize(response)
    unique_tokens = set(tokens)
    
    # Unique token ratio
    unique_ratio = len(unique_tokens) / token_count if token_count > 0 else 0
    
    # Token utilization ratio
    utilization_ratio = token_count / max_tokens
    
    # Ideal utilization is around 80-90% of budget
    if utilization_ratio > 0.9:
        utilization_score = 1.0 - ((utilization_ratio - 0.9) * 10)  # Penalize for being too close to limit
    else:
        utilization_score = utilization_ratio / 0.9  # Scale so 90% utilization = 1.0
    
    # Combine metrics (weighted average)
    efficiency = (unique_ratio * 0.7) + (utilization_score * 0.3)
    
    return efficiency

# ------------------------------------------------------------------------------
# Neural Field Scoring Functions
# ------------------------------------------------------------------------------

def score_field_resonance(response: str, field: Any) -> float:
    """
    Score how well a response resonates with a neural field.
    
    Args:
        response: Model response
        field: Neural field object
        
    Returns:
        Resonance score (0.0 to 1.0)
    """
    try:
        # Try to use field's built-in measurement
        return field.measure_resonance(response)
    except (AttributeError, TypeError):
        try:
            # Try to get attractors from field
            attractors = _get_field_attractors(field)
            if not attractors:
                return 0.5  # Neutral score if no attractors
                
            # Calculate resonance with each attractor
            total_resonance = 0.0
            total_weight = 0.0
            
            for attractor_pattern, attractor_strength in attractors:
                # Simple token overlap for resonance
                response_tokens = set(tokenize(response))
                attractor_tokens = set(tokenize(attractor_pattern))
                
                overlap = jaccard_similarity(response_tokens, attractor_tokens)
                
                # Weight by attractor strength
                total_resonance += overlap * attractor_strength
                total_weight += attractor_strength
            
            # Average resonance
            if total_weight > 0:
                avg_resonance = total_resonance / total_weight
            else:
                avg_resonance = 0.0
                
            return avg_resonance
            
        except Exception as e:
            logger.warning(f"Failed to calculate field resonance: {e}")
            return 0.5  # Neutral score on failure

def score_field_coherence(response: str, field: Any) -> float:
    """
    Score how coherent a response is with a neural field's structure.
    
    Args:
        response: Model response
        field: Neural field object
        
    Returns:
        Coherence score (0.0 to 1.0)
    """
    try:
        # Try to use field's built-in measurement
        return field.measure_coherence(response)
    except (AttributeError, TypeError):
        try:
            # Try to get patterns from field
            patterns = _get_field_patterns(field)
            if not patterns:
                return 0.5  # Neutral score if no patterns
                
            # Split response into sentences
            sentences = extract_sentences(response)
            if not sentences:
                return 0.0
                
            # Calculate coherence for each sentence with field patterns
            sentence_coherence = []
            
            for sentence in sentences:
                # Calculate resonance with patterns
                sentence_tokens = set(tokenize(sentence))
                
                max_resonance = 0.0
                for pattern, _ in patterns:
                    pattern_tokens = set(tokenize(pattern))
                    resonance = jaccard_similarity(sentence_tokens, pattern_tokens)
                    max_resonance = max(max_resonance, resonance)
                
                sentence_coherence.append(max_resonance)
            
            # Overall coherence combines average and consistency
            avg_coherence = sum(sentence_coherence) / len(sentence_coherence)
            consistency = 1.0 - (max(sentence_coherence) - min(sentence_coherence))
            
            coherence = (avg_coherence * 0.7) + (consistency * 0.3)
            
            return coherence
            
        except Exception as e:
            logger.warning(f"Failed to calculate field coherence: {e}")
            return 0.5  # Neutral score on failure

def score_field_stability_impact(response: str, field: Any, before_state: Optional[Dict[str, Any]] = None) -> float:
    """
    Score the impact of a response on field stability.
    
    Args:
        response: Model response
        field: Neural field object after response
        before_state: Optional field state before response
        
    Returns:
        Stability impact score (0.0 to 1.0)
    """
    try:
        # Try to use field's built-in measurement
        current_stability = field.measure_stability()
        
        if before_state:
            # Calculate stability change
            prev_stability = before_state.get("stability", 0.5)
            stability_change = current_stability - prev_stability
            
            # Positive change is good, negative change is bad
            if stability_change >= 0:
                # Improvement in stability
                return min(1.0, 0.5 + stability_change)
            else:
                # Decrease in stability
                return max(0.0, 0.5 + stability_change)
        else:
            # No previous state, just use current stability
            return current_stability
            
    except (AttributeError, TypeError):
        logger.warning("Cannot calculate stability impact without field support")
        return 0.5  # Neutral score

def _get_field_attractors(field: Any) -> List[Tuple[str, float]]:
    """Extract attractors from a field object."""
    try:
        # Try to access attractors directly
        return [(attractor['pattern'], attractor['strength']) 
                for attractor in field.attractors.values()]
    except (AttributeError, TypeError):
        # Try alternative methods
        try:
            return field.get_attractors()
        except (AttributeError, TypeError):
            return []

def _get_field_patterns(field: Any) -> List[Tuple[str, float]]:
    """Extract patterns from a field object."""
    try:
        # Try to access state directly
        return [(pattern, strength) for pattern, strength in field.state.items()]
    except (AttributeError, TypeError):
        # Try alternative methods
        try:
            return field.get_patterns()
        except (AttributeError, TypeError):
            return []

# ------------------------------------------------------------------------------
# Protocol Scoring Functions
# ------------------------------------------------------------------------------

def score_protocol_adherence(response: str, protocol: Any) -> float:
    """
    Score how well a response adheres to a protocol structure.
    
    Args:
        response: Model response
        protocol: Protocol object or definition
        
    Returns:
        Adherence score (0.0 to 1.0)
    """
    # Extract protocol steps
    steps = _extract_protocol_steps(protocol)
    if not steps:
        return 0.0
        
    # Check for evidence of each step in the response
    step_scores = []
    
    for step in steps:
        step_name = step.get("name", "")
        step_keywords = _extract_step_keywords(step)
        
        if step_keywords:
            # Check for keywords in response
            response_lower = response.lower()
            matches = sum(1 for keyword in step_keywords if keyword.lower() in response_lower)
            score = matches / len(step_keywords)
        else:
            # No keywords, check for step name
            score = 1.0 if step_name.lower() in response.lower() else 0.0
        
        step_scores.append(score)
    
    # Overall adherence score
    adherence = sum(step_scores) / len(step_scores)
    
    # Bonus for following sequence
    sequence_bonus = 0.0
    response_sentences = extract_sentences(response)
    
    # Check if steps appear in the correct order
    last_step_pos = -1
    steps_in_order = 0
    
    for i, step in enumerate(steps):
        step_name = step.get("name", "").lower()
        step_keywords = [kw.lower() for kw in _extract_step_keywords(step)]
        
        # Find position of step in response
        step_pos = -1
        for j, sentence in enumerate(response_sentences):
            sentence_lower = sentence.lower()
            if step_name in sentence_lower or any(kw in sentence_lower for kw in step_keywords):
                step_pos = j
                break
        
        if step_pos > last_step_pos and step_pos >= 0:
            steps_in_order += 1
            last_step_pos = step_pos
    
    if len(steps) > 1:
        sequence_bonus = steps_in_order / (len(steps) - 1)
    
    # Combine scores
    final_score = (adherence * 0.7) + (sequence_bonus * 0.3)
    
    return final_score

def _extract_protocol_steps(protocol: Any) -> List[Dict[str, Any]]:
    """Extract steps from a protocol object or definition."""
    if isinstance(protocol, dict):
        # Protocol is a dictionary
        return protocol.get("process", [])
    else:
        # Try to access protocol attributes
        try:
            return protocol.process_steps
        except AttributeError:
            try:
                return protocol.process
            except AttributeError:
                return []

def _extract_step_keywords(step: Dict[str, Any]) -> List[str]:
    """Extract keywords from a protocol step."""
    keywords = []
    
    # Add step name
    if "name" in step:
        keywords.append(step["name"])
    
    # Add other values that might be keywords
    for key, value in step.items():
        if key != "name" and isinstance(value, str):
            keywords.append(value)
    
    return keywords

def score_protocol_output_match(response: str, protocol: Any) -> float:
    """
    Score how well a response matches the expected protocol output.
    
    Args:
        response: Model response
        protocol: Protocol object or definition
        
    Returns:
        Output match score (0.0 to 1.0)
    """
    # Extract expected output schema
    output_schema = _extract_protocol_output(protocol)
    if not output_schema:
        return 0.5  # Neutral score if no schema
    
    # Try to extract structured output from response
    extracted_output = _extract_structured_output(response)
    if not extracted_output:
        return 0.0  # No structured output found
    
    # Check coverage of expected keys
    expected_keys = set(output_schema.keys())
    actual_keys = set(extracted_output.keys())
    
    # Calculate key coverage
    if expected_keys:
        key_coverage = len(expected_keys.intersection(actual_keys)) / len(expected_keys)
    else:
        key_coverage = 0.0
    
    # Check for format adherence
    format_adherence = 1.0
    
    for key in expected_keys.intersection(actual_keys):
        expected_format = output_schema[key]
        actual_value = extracted_output[key]
        
        # Simple format check based on expected format
        if isinstance(expected_format, str) and "<" in expected_format and ">" in expected_format:
            # This is a variable reference, can't check format
            pass
        elif isinstance(expected_format, dict) and isinstance(actual_value, dict):
            # Check nested structure
            expected_nested_keys = set(expected_format.keys())
            actual_nested_keys = set(actual_value.keys())
            
            if expected_nested_keys:
                nested_coverage = len(expected_nested_keys.intersection(actual_nested_keys)) / len(expected_nested_keys)
                format_adherence *= nested_coverage
        elif isinstance(expected_format, list) and isinstance(actual_value, list):
            # Check list structure
            format_adherence *= 1.0  # Can't easily check list format
        elif type(expected_format) != type(actual_value):
            # Type mismatch
            format_adherence *= 0.5
    
    # Combine scores
    output_match = (key_coverage * 0.7) + (format_adherence * 0.3)
    
    return output_match

def _extract_protocol_output(protocol: Any) -> Dict[str, Any]:
    """Extract output schema from a protocol object or definition."""
    if isinstance(protocol, dict):
        # Protocol is a dictionary
        return protocol.get("output", {})
    else:
        # Try to access protocol attributes
        try:
            return protocol.output_schema
        except AttributeError:
            try:
                return protocol.output
            except AttributeError:
                return {}

def _extract_structured_output(response: str) -> Dict[str, Any]:
    """Extract structured output from a response."""
    # Try to find JSON output
    json_pattern = r'```(?:json)?\s*({[\s\S]*?})\s*```'
    json_matches = re.findall(json_pattern, response)
    
    if json_matches:
        try:
            return json.loads(json_matches[0])
        except json.JSONDecodeError:
            pass
    
    # Try to find key-value pairs
    output = {}
    
    # Look for "Output:" or "Result:" section
    output_section_pattern = r'(?:Output|Result):\s*\n([\s\S]*?)(?:\n\n|\Z)'
    section_matches = re.findall(output_section_pattern, response)
    
    if section_matches:
        section = section_matches[0]
        
        # Extract key-value pairs
        for line in section.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                output[key.strip()] = value.strip()
    
    return output

# ------------------------------------------------------------------------------
# Comprehensive Scoring
# ------------------------------------------------------------------------------

def score_response(response: str, query: str, context: Optional[Dict[str, Any]] = None, 
                 reference: Optional[str] = None, field: Optional[Any] = None,
                 protocol: Optional[Any] = None) -> Dict[str, float]:
    """
    Comprehensive scoring of a model response.
    
    Args:
        response: Model response
        query: Original query
        context: Optional context dictionary
        reference: Optional reference answer
        field: Optional neural field
        protocol: Optional protocol
        
    Returns:
        Dictionary of scores
    """
    scores = {}
    
    # Basic scores
    scores["relevance"] = score_relevance(response, query)
    scores["coherence"] = score_coherence(response)
    scores["comprehensiveness"] = score_comprehensiveness(response, reference)
    scores["conciseness"] = score_conciseness(response, reference)
    scores["accuracy"] = score_accuracy(response, reference)
    scores["token_efficiency"] = score_token_efficiency(response)
    
    # Field scores if field is provided
    if field:
        scores["field_resonance"] = score_field_resonance(response, field)
        scores["field_coherence"] = score_field_coherence(response, field)
    
    # Protocol scores if protocol is provided
    if protocol:
        scores["protocol_adherence"] = score_protocol_adherence(response, protocol)
        scores["protocol_output_match"] = score_protocol_output_match(response, protocol)
    
    # Calculate overall score
    # Different weights for different aspects based on importance
    weights = {
        "relevance": 0.20,
        "coherence": 0.15,
        "comprehensiveness": 0.15,
        "conciseness": 0.10,
        "accuracy": 0.20,
        "token_efficiency": 0.10,
        "field_resonance": 0.05,
        "field_coherence": 0.05,
        "protocol_adherence": 0.05,
        "protocol_output_match": 0.05
    }
    
    # Only use scores that exist
    overall_score = 0.0
    total_weight = 0.0
    
    for metric, score in scores.items():
        if metric in weights:
            overall_score += score * weights[metric]
            total_weight += weights[metric]
    
    if total_weight > 0:
        scores["overall"] = overall_score / total_weight
    else:
        scores["overall"] = 0.0
    
    return scores

# ------------------------------------------------------------------------------
# Usage Examples
# ------------------------------------------------------------------------------

def basic_scoring_example():
    """Example of basic scoring functions."""
    query = "Explain how neural networks work in simple terms."
    
    response = """
    Neural networks are computational models inspired by the human brain. 
    They consist of interconnected nodes called neurons, organized in layers.
    Each neuron receives input, applies a transformation, and passes the output to the next layer.
    Through training with data, neural networks learn to recognize patterns and make predictions.
    The strength of connections between neurons is adjusted during training to minimize errors.
    This process, called backpropagation, is what enables neural networks to learn from examples.
    """
    
    reference = """
    Neural networks are computational systems inspired by the human brain's structure.
    They consist of layers of nodes (neurons) that process information.
    Information flows from input layers through hidden layers to output layers.
    Each connection between neurons has a weight that adjusts during training.
    Neural networks learn by processing examples and adjusting weights to reduce errors.
    This training process allows them to recognize patterns and make predictions on new data.
    Applications include image recognition, language processing, and game playing.
    """
    
    # Score relevance
    relevance = score_relevance(response, query)
    print(f"Relevance score: {relevance:.2f}")
    
    # Score coherence
    coherence = score_coherence(response)
    print(f"Coherence score: {coherence:.2f}")
    
    # Score comprehensiveness
    comprehensiveness = score_comprehensiveness(response, reference)
    print(f"Comprehensiveness score: {comprehensiveness:.2f}")
    
    # Score conciseness
    conciseness = score_conciseness(response, reference)
    print(f"Conciseness score: {conciseness:.2f}")
    
    # Score accuracy
    accuracy = score_accuracy(response, reference)
    print(f"Accuracy score: {accuracy:.2f}")
    
    # Score token efficiency
    token_efficiency = score_token_efficiency(response)
    print(f"Token efficiency score: {token_efficiency:.2f}")
    
    # Comprehensive scoring
    scores = score_response(response, query, reference=reference)
    print("\nComprehensive scores:")
    for metric, score in scores.items():
        print(f"- {metric}: {score:.2f}")

if __name__ == "__main__":
    # Example usage
    basic_scoring_example()
