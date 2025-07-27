#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Context-Engineering: Schema Design for Structured Context
========================================================

This module focuses on designing structured schemas for LLM context,
enabling more consistent, verifiable, and composable interactions.
Schema-driven contexts reduce variability, increase prompt robustness,
and create a bridge between human intent and machine processing.

Key concepts covered:
1. Basic schema patterns and structures
2. Schema validation and enforcement
3. Recursive and fractal schemas
4. Field protocols as schema-driven contexts
5. Measuring schema effectiveness

Usage:
    # In Jupyter or Colab:
    %run 06_schema_design.py
    # or
    from schema_design import JSONSchema, SchemaContext, FractalSchema
"""

import os
import re
import json
import time
import uuid
import logging
import hashlib
import tiktoken
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, field, asdict
from typing import Dict, List, Tuple, Any, Optional, Union, Callable, TypeVar, Set
from IPython.display import display, Markdown, HTML, JSON

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
    import jsonschema
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False
    logger.warning("jsonschema not found. Install with: pip install jsonschema")

try:
    import dotenv
    dotenv.load_dotenv()
    ENV_LOADED = True
except ImportError:
    ENV_LOADED = False
    logger.warning("python-dotenv not found. Install with: pip install python-dotenv")

# Constants
DEFAULT_MODEL = "gpt-3.5-turbo"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_MAX_TOKENS = 1000


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


def display_schema_example(
    title: str,
    schema: Dict[str, Any],
    instance: Dict[str, Any],
    metrics: Optional[Dict[str, Any]] = None
) -> None:
    """
    Display a schema and an instance that conforms to it.
    
    Args:
        title: Title for the display
        schema: JSON Schema
        instance: Instance conforming to the schema
        metrics: Optional metrics to display
    """
    display(HTML(f"<h2>{title}</h2>"))
    
    # Display schema
    display(HTML("<h3>Schema</h3>"))
    display(JSON(schema))
    
    # Display instance
    display(HTML("<h3>Instance</h3>"))
    display(JSON(instance))
    
    # Display metrics if provided
    if metrics:
        display(HTML("<h3>Metrics</h3>"))
        display(Markdown(f"```\n{format_metrics(metrics)}\n```"))


# Basic Schema Classes
# ===================

class JSONSchema:
    """
    A class for creating, validating, and applying JSON Schema
    to LLM contexts.
    """
    
    def __init__(
        self,
        schema: Dict[str, Any],
        name: str = None,
        description: str = None,
        version: str = "1.0.0"
    ):
        """
        Initialize the JSON Schema.
        
        Args:
            schema: JSON Schema definition
            name: Optional schema name
            description: Optional schema description
            version: Schema version
        """
        self.schema = schema
        self.name = name or schema.get("title", "Unnamed Schema")
        self.description = description or schema.get("description", "")
        self.version = version
        
        # Initialize validation stats
        self.validation_stats = {
            "validations": 0,
            "successes": 0,
            "failures": 0,
            "error_types": {}
        }
    
    def validate(self, instance: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate an instance against the schema.
        
        Args:
            instance: Instance to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not JSONSCHEMA_AVAILABLE:
            logger.warning("jsonschema package required for validation")
            return False, "jsonschema package required for validation"
        
        try:
            jsonschema.validate(instance=instance, schema=self.schema)
            
            # Update validation stats
            self.validation_stats["validations"] += 1
            self.validation_stats["successes"] += 1
            
            return True, None
        
        except jsonschema.exceptions.ValidationError as e:
            # Update validation stats
            self.validation_stats["validations"] += 1
            self.validation_stats["failures"] += 1
            
            # Track error type
            error_path = str(e.path) if e.path else "root"
            self.validation_stats["error_types"][error_path] = self.validation_stats["error_types"].get(error_path, 0) + 1
            
            return False, str(e)
    
    def generate_example(
        self,
        client=None,
        model: str = DEFAULT_MODEL,
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Generate an example instance that conforms to the schema.
        
        Args:
            client: API client (if None, will create one)
            model: Model name to use
            temperature: Temperature parameter
            max_tokens: Maximum tokens to generate
            
        Returns:
            tuple: (example_instance, metadata)
        """
        if client is None:
            client, model = setup_client(model=model)
            if client is None:
                return {}, {"error": "No API client available"}
        
        # Create the prompt
        schema_json = json.dumps(self.schema, indent=2)
        prompt = f"""Generate a valid example instance that conforms to the following JSON Schema:

```json
{schema_json}
```

Your response should be a single, valid JSON object that satisfies all constraints in the schema.
Do not include explanations or comments, just return the JSON object.
"""
        
        # Use a system message focused on schema validation
        system_message = "You are a precise JSON Schema expert who generates valid example instances that conform to specified schemas."
        
        # Generate the example
        response, metadata = generate_response(
            prompt=prompt,
            client=client,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            system_message=system_message
        )
        
        # Extract JSON from response
        try:
            # Try to parse the entire response as JSON
            example = json.loads(response)
        except json.JSONDecodeError:
            # If that fails, try to extract JSON using regex
            json_pattern = r'```(?:json)?\s*([\s\S]*?)\s*```'
            matches = re.findall(json_pattern, response)
            
            if matches:
                try:
                    example = json.loads(matches[0])
                except json.JSONDecodeError:
                    example = {"error": "Failed to parse generated example as JSON"}
            else:
                example = {"error": "No JSON found in response"}
        
        return example, metadata
    
    def generate_prompt_with_schema(
        self,
        task_description: str,
        output_format_description: str = None
    ) -> str:
        """
        Generate a prompt that includes the schema for structured output.
        
        Args:
            task_description: Description of the task
            output_format_description: Optional description of the output format
            
        Returns:
            str: Formatted prompt with schema
        """
        schema_json = json.dumps(self.schema, indent=2)
        
        output_desc = output_format_description or f"""Your response must conform to the following JSON Schema:

```json
{schema_json}
```

Ensure that your response is a valid JSON object that satisfies all constraints specified in the schema."""
        
        prompt = f"""{task_description}

{output_desc}

Respond with a single, valid JSON object and nothing else."""
        
        return prompt
    
    def get_validation_stats(self) -> Dict[str, Any]:
        """
        Get statistics about schema validations.
        
        Returns:
            dict: Validation statistics
        """
        stats = self.validation_stats.copy()
        
        # Add derived statistics
        if stats["validations"] > 0:
            stats["success_rate"] = stats["successes"] / stats["validations"]
        else:
            stats["success_rate"] = 0.0
        
        return stats
    
    def visualize_validation_stats(self) -> None:
        """
        Visualize schema validation statistics.
        """
        stats = self.get_validation_stats()
        
        if stats["validations"] == 0:
            logger.warning("No validation statistics to visualize")
            return
        
        # Create figure
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f"Schema Validation Statistics: {self.name}", fontsize=16)
        
        # Plot 1: Success vs. Failure
        labels = ['Success', 'Failure']
        sizes = [stats["successes"], stats["failures"]]
        colors = ['green', 'red']
        
        axes[0].pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        axes[0].set_title("Validation Results")
        axes[0].axis('equal')
        
        # Plot 2: Error Types
        if stats["failures"] > 0:
            error_types = list(stats["error_types"].keys())
            error_counts = list(stats["error_types"].values())
            
            axes[1].bar(error_types, error_counts, color='red', alpha=0.7)
            axes[1].set_title("Error Types")
            axes[1].set_xlabel("Error Path")
            axes[1].set_ylabel("Count")
            plt.xticks(rotation=45, ha='right')
        else:
            axes[1].text(0.5, 0.5, "No errors to display", 
                         horizontalalignment='center', verticalalignment='center',
                         transform=axes[1].transAxes)
            axes[1].set_title("Error Types")
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()


class SchemaContext:
    """
    A class for creating structured LLM contexts based on schemas,
    ensuring consistent, validatable interactions.
    """
    
    def __init__(
        self,
        schema: JSONSchema,
        client=None,
        model: str = DEFAULT_MODEL,
        system_message: str = "You are a helpful assistant that provides structured responses.",
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        verbose: bool = False
    ):
        """
        Initialize the schema context.
        
        Args:
            schema: JSONSchema to use
            client: API client (if None, will create one)
            model: Model name to use
            system_message: System message to use
            max_tokens: Maximum tokens to generate
            temperature: Temperature parameter
            verbose: Whether to print debug information
        """
        self.schema = schema
        self.client, self.model = setup_client(model=model) if client is None else (client, model)
        self.system_message = system_message
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.verbose = verbose
        
        # Initialize history and metrics tracking
        self.history = []
        self.metrics = {
            "total_prompt_tokens": 0,
            "total_response_tokens": 0,
            "total_tokens": 0,
            "total_latency": 0,
            "queries": 0,
            "validation_successes": 0,
            "validation_failures": 0
        }
    
    def _log(self, message: str) -> None:
        """
        Log a message if verbose mode is enabled.
        
        Args:
            message: Message to log
        """
        if self.verbose:
            logger.info(message)
    
    def query(
        self,
        prompt: str,
        retry_on_validation_failure: bool = True,
        max_retries: int = 3
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Query the LLM with a schema-structured prompt.
        
        Args:
            prompt: User prompt
            retry_on_validation_failure: Whether to retry if validation fails
            max_retries: Maximum number of retries
            
        Returns:
            tuple: (structured_response, details)
        """
        self._log(f"Processing query with schema: {self.schema.name}")
        
        # Add schema to prompt
        schema_prompt = self.schema.generate_prompt_with_schema(prompt)
        
        # Initialize tracking
        attempts = 0
        best_response = None
        best_score = -1
        validation_results = []
        
        while attempts < max_retries:
            attempts += 1
            self._log(f"Attempt {attempts}/{max_retries}")
            
            # Generate response
            response_text, metadata = generate_response(
                prompt=schema_prompt,
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
            
            # Parse response
            try:
                # Try to parse the entire response as JSON
                parsed_response = json.loads(response_text)
            except json.JSONDecodeError:
                # If that fails, try to extract JSON using regex
                json_pattern = r'```(?:json)?\s*([\s\S]*?)\s*```'
                matches = re.findall(json_pattern, response_text)
                
                if matches:
                    try:
                        parsed_response = json.loads(matches[0])
                    except json.JSONDecodeError:
                        parsed_response = {"error": "Failed to parse response as JSON"}
                else:
                    parsed_response = {"error": "No JSON found in response"}
            
            # Validate against schema
            is_valid, error_message = self.schema.validate(parsed_response)
            
            # Record validation result
            validation_result = {
                "attempt": attempts,
                "is_valid": is_valid,
                "error_message": error_message,
                "response": parsed_response,
                "raw_response": response_text,
                "metrics": metadata
            }
            validation_results.append(validation_result)
            
            # Update metrics based on validation
            if is_valid:
                self.metrics["validation_successes"] += 1
            else:
                self.metrics["validation_failures"] += 1
            
            # Determine whether to keep this response
            current_score = 1 if is_valid else 0
            
            if current_score > best_score:
                best_score = current_score
                best_response = parsed_response
            
            # Stop if valid or not retrying
            if is_valid or not retry_on_validation_failure:
                break
            
            # If not valid and retrying, add error information to prompt
            if not is_valid:
                error_prompt = f"""Your previous response did not conform to the required schema.
Error: {error_message}

Please try again and ensure your response strictly follows the schema."""
                
                schema_prompt = f"{schema_prompt}\n\n{error_prompt}"
        
        # Increment query count
        self.metrics["queries"] += 1
        
        # Add to history
        query_record = {
            "prompt": prompt,
            "schema_prompt": schema_prompt,
            "validation_results": validation_results,
            "best_response": best_response,
            "attempts": attempts,
            "timestamp": time.time()
        }
        self.history.append(query_record)
        
        # Create details dictionary
        details = {
            "prompt": prompt,
            "schema_prompt": schema_prompt,
            "validation_results": validation_results,
            "attempts": attempts,
            "metrics": {
                "prompt_tokens": metadata.get("prompt_tokens", 0),
                "response_tokens": metadata.get("response_tokens", 0),
                "total_tokens": metadata.get("total_tokens", 0),
                "latency": metadata.get("latency", 0)
            }
        }
        
        return best_response, details
    
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
            summary["validation_success_rate"] = (
                summary["validation_successes"] / 
                (summary["validation_successes"] + summary["validation_failures"])
            ) if (summary["validation_successes"] + summary["validation_failures"]) > 0 else 0
            
        if summary["total_prompt_tokens"] > 0:
            summary["overall_efficiency"] = (
                summary["total_response_tokens"] / summary["total_prompt_tokens"]
            )
        
        return summary
    
    def display_query_results(self, details: Dict[str, Any], show_prompt: bool = True) -> None:
        """
        Display the query results in a notebook.
        
        Args:
            details: Query details from query()
            show_prompt: Whether to show the prompt
        """
        display(HTML("<h2>Schema-Structured Query Results</h2>"))
        
        # Display schema
        display(HTML("<h3>Schema</h3>"))
        display(JSON(self.schema.schema))
        
        # Display prompt if requested
        if show_prompt:
            display(HTML("<h3>Original Prompt</h3>"))
            display(Markdown(details["prompt"]))
            
            display(HTML("<h3>Schema-Augmented Prompt</h3>"))
            display(Markdown(f"```\n{details['schema_prompt']}\n```"))
        
        # Display validation results
        display(HTML("<h3>Validation Results</h3>"))
        
        for i, result in enumerate(details["validation_results"]):
            display(HTML(f"<h4>Attempt {result['attempt']}</h4>"))
            
            # Display validation status
            if result["is_valid"]:
                display(HTML("<p style='color: green; font-weight: bold;'>✓ Valid</p>"))
            else:
                display(HTML("<p style='color: red; font-weight: bold;'>✗ Invalid</p>"))
                display(HTML("<p><em>Error:</em></p>"))
                display(Markdown(f"```\n{result['error_message']}\n```"))
            
            # Display response
            display(HTML("<p><em>Parsed Response:</em></p>"))
            display(JSON(result["response"]))
            
            # Display metrics
            display(HTML("<p><em>Metrics:</em></p>"))
            display(Markdown(f"```\n{format_metrics(result['metrics'])}\n```"))
        
        # Display summary
        display(HTML("<h3>Summary</h3>"))
        display(Markdown(f"""
        - Total attempts: {details['attempts']}
        - Final response valid: {details['validation_results'][-1]['is_valid']}
        - Total tokens: {details['metrics']['total_tokens']}
        - Total latency: {details['metrics']['latency']:.2f}s
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
        prompt_tokens = [h["validation_results"][-1]["metrics"].get("prompt_tokens", 0) for h in self.history]
        response_tokens = [h["validation_results"][-1]["metrics"].get("response_tokens", 0) for h in self.history]
        latencies = [h["validation_results"][-1]["metrics"].get("latency", 0) for h in self.history]
        attempts_per_query = [h["attempts"] for h in self.history]
        validation_success = [h["validation_results"][-1]["is_valid"] for h in self.history]
        
        # Create figure
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("Schema Context Metrics by Query", fontsize=16)
        
        # Plot 1: Token usage
        axes[0, 0].bar(queries, prompt_tokens, label="Prompt Tokens", color="blue", alpha=0.7)
        axes[0, 0].bar(queries, response_tokens, bottom=prompt_tokens, 
                       label="Response Tokens", color="green", alpha=0.7)
        axes[0, 0].set_title("Token Usage")
        axes[0, 0].set_xlabel("Query")
        axes[0, 0].set_ylabel("Tokens")
        axes[0, 0].legend()
        axes[0, 0].grid(alpha=0.3)
        
        # Plot 2: Latency
        axes[0, 1].plot(queries, latencies, marker='o', color="red", alpha=0.7)
        axes[0, 1].set_title("Latency")
        axes[0, 1].set_xlabel("Query")
        axes[0, 1].set_ylabel("Seconds")
        axes[0, 1].grid(alpha=0.3)
        
        # Plot 3: Attempts per query
        axes[1, 0].bar(queries, attempts_per_query, color="purple", alpha=0.7)
        axes[1, 0].set_title("Attempts per Query")
        axes[1, 0].set_xlabel("Query")
        axes[1, 0].set_ylabel("Count")
        axes[1, 0].grid(alpha=0.3)
        
        # Plot 4: Validation success rate
        success_rate = [int(success) for success in validation_success]
        cumulative_success_rate = np.cumsum(success_rate) / np.arange(1, len(success_rate) + 1)
        
        axes[1, 1].plot(queries, cumulative_success_rate, marker='^', color="orange", alpha=0.7)
        axes[1, 1].set_title("Cumulative Validation Success Rate")
        axes[1, 1].set_xlabel("Query")
        axes[1, 1].set_ylabel("Rate")
        axes[1, 1].set_ylim(0, 1.05)
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()


# Recursive and Fractal Schema Implementation
# ==========================================

class FractalSchema(JSONSchema):
    """
    A schema that implements recursive, fractal patterns with
    self-similar structure at multiple scales.
    """
    
    def __init__(
        self,
        schema: Dict[str, Any],
        recursion_paths: List[str] = None,
        max_recursion_depth: int = 5,
        **kwargs
    ):
        """
        Initialize the fractal schema.
        
        Args:
            schema: JSON Schema definition
            recursion_paths: JSON paths where recursion occurs
            max_recursion_depth: Maximum recursion depth
            **kwargs: Additional args passed to JSONSchema
        """
        super().__init__(schema, **kwargs)
        
        self.recursion_paths = recursion_paths or []
        self.max_recursion_depth = max_recursion_depth
        
        # Track recursion metrics
        self.recursion_metrics = {
            "observed_max_depth": 0,
            "recursive_instances": 0,
            "recursion_by_path": {}
        }
    
    def validate(self, instance: Dict[str, Any]) -> Tuple[bool, Optional[str]]:
        """
        Validate an instance against the schema, with special handling for recursion.
        
        Args:
            instance: Instance to validate
            
        Returns:
            tuple: (is_valid, error_message)
        """
        # Standard validation
        is_valid, error_message = super().validate(instance)
        
        if is_valid:
            # Check recursion depth
            self._analyze_recursion_depth(instance)
        
        return is_valid, error_message
    
    def _analyze_recursion_depth(self, instance: Dict[str, Any], path: str = "", depth: int = 0) -> int:
        """
        Analyze the recursion depth in an instance.
        
        Args:
            instance: Instance to analyze
            path: Current JSON path
            depth: Current recursion depth
            
        Returns:
            int: Maximum recursion depth found
        """
        if not isinstance(instance, dict):
            return depth
        
        max_depth = depth
        
        # Check if current path is in recursion paths
        if path in self.recursion_paths:
            # This is a recursive node
            self.recursion_metrics["recursive_instances"] += 1
            
            # Track recursion by path
            if path not in self.recursion_metrics["recursion_by_path"]:
                self.recursion_metrics["recursion_by_path"][path] = 0
            self.recursion_metrics["recursion_by_path"][path] += 1
            
            # Increment depth for recursive nodes
            depth += 1
        
        # Recursively check all dictionary fields
        for key, value in instance.items():
            current_path = f"{path}.{key}" if path else key
            
            if isinstance(value, dict):
                # Recursive call for nested dictionaries
                sub_depth = self._analyze_recursion_depth(value, current_path, depth)
                max_depth = max(max_depth, sub_depth)
            elif isinstance(value, list):
                # Check recursion in list items
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        sub_path = f"{current_path}[{i}]"
                        sub_depth = self._analyze_recursion_depth(item, sub_path, depth)
                        max_depth = max(max_depth, sub_depth)
        
        # Update observed max depth
        if max_depth > self.recursion_metrics["observed_max_depth"]:
            self.recursion_metrics["observed_max_depth"] = max_depth
        
        return max_depth
    
    def generate_example(
        self,
        recursion_depth: int = 2,
        **kwargs
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Generate an example instance with controlled recursion depth.
        
        Args:
            recursion_depth: Target recursion depth (capped by max_recursion_depth)
            **kwargs: Additional args passed to JSONSchema.generate_example
            
        Returns:
            tuple: (example_instance, metadata)
        """
        # Cap recursion depth
        actual_depth = min(recursion_depth, self.max_recursion_depth)
        
        # Modify the schema prompt to include recursion guidance
        recursion_instructions = f"""
Generate an example that demonstrates recursive structure at these paths: {self.recursion_paths}.
Use a recursion depth of {actual_depth} levels (a node containing itself or a similar pattern).
"""
        
        # Create the prompt
        schema_json = json.dumps(self.schema, indent=2)
        prompt = f"""Generate a valid example instance that conforms to the following JSON Schema:

```json
{schema_json}
```

{recursion_instructions}

Your response should be a single, valid JSON object that satisfies all constraints in the schema.
Do not include explanations or comments, just return the JSON object.
"""
        
        # Use a system message focused on schema validation
        system_message = "You are a precise JSON Schema expert who generates valid example instances with recursive structures."
        
        # Generate the example
        client = kwargs.get("client")
        if client is None:
            client, model = setup_client(model=kwargs.get("model", DEFAULT_MODEL))
        else:
            model = kwargs.get("model", DEFAULT_MODEL)
        
        # Generate response
        response, metadata = generate_response(
            prompt=prompt,
            client=client,
            model=model,
            temperature=kwargs.get("temperature", 0.7),
            max_tokens=kwargs.get("max_tokens", 1000),
            system_message=system_message
        )
        
        # Extract JSON from response
        try:
            # Try to parse the entire response as JSON
            example = json.loads(response)
        except json.JSONDecodeError:
            # If that fails, try to extract JSON using regex
            json_pattern = r'```(?:json)?\s*([\s\S]*?)\s*```'
            matches = re.findall(json_pattern, response)
            
            if matches:
                try:
                    example = json.loads(matches[0])
                except json.JSONDecodeError:
                    example = {"error": "Failed to parse generated example as JSON"}
            else:
                example = {"error": "No JSON found in response"}
        
        # Analyze recursion depth
        if isinstance(example, dict):
            self._analyze_recursion_depth(example)
        
        return example, metadata
    
    def get_recursion_metrics(self) -> Dict[str, Any]:
        """
        Get metrics about schema recursion.
        
        Returns:
            dict: Recursion metrics
        """
        return self.recursion_metrics.copy()
    
    def visualize_recursion_metrics(self) -> None:
        """
        Visualize schema recursion metrics.
        """
        metrics = self.get_recursion_metrics()
        
        if metrics["recursive_instances"] == 0:
            logger.warning("No recursion metrics to visualize")
            return
        
        # Create figure
        fig, axes = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f"Schema Recursion Metrics: {self.name}", fontsize=16)
        
        # Plot 1: Recursion by path
        paths = list(metrics["recursion_by_path"].keys())
        counts = list(metrics["recursion_by_path"].values())
        
        axes[0].bar(paths, counts, color='blue', alpha=0.7)
        axes[0].set_title("Recursion by Path")
        axes[0].set_xlabel("JSON Path")
        axes[0].set_ylabel("Count")
        plt.setp(axes[0].get_xticklabels(), rotation=45, ha='right')
        
        # Plot 2: Observed max depth vs. configured max depth
        depth_labels = ['Observed Max Depth', 'Configured Max Depth']
        depth_values = [metrics["observed_max_depth"], self.max_recursion_depth]
        
        axes[1].bar(depth_labels, depth_values, color='green', alpha=0.7)
        axes[1].set_title("Recursion Depth")
        axes[1].set_ylabel("Depth")
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()


# Example Schema Definitions
# =========================

# Context-Engineering Repository Schema (fractalRepoContext.v1.json)
CONTEXT_ENGINEERING_SCHEMA = {
    "$schema": "http://fractal.recursive.net/schemas/fractalRepoContext.v1.json",
    "title": "Context-Engineering Repository Schema",
    "description": "Schema for structuring the Context-Engineering repository content and metadata",
    "type": "object",
    "properties": {
        "fractalVersion": {
            "type": "string",
            "pattern": "^\\d+\\.\\d+\\.\\d+$",
            "description": "Version of the fractal schema"
        },
        "instanceID": {
            "type": "string",
            "description": "Unique identifier for this instance"
        },
        "intent": {
            "type": "string",
            "description": "High-level purpose of the repository"
        },
        "repositoryContext": {
            "type": "object",
            "description": "Core structure and organization of the repository",
            "properties": {
                "name": {"type": "string"},
                "elevatorPitch": {"type": "string"},
                "learningPath": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Progression of learning stages"
                },
                "fileTree": {
                    "type": "object",
                    "properties": {
                        "rootFiles": {"type": "array", "items": {"type": "string"}},
                        "directories": {"type": "object"}
                    }
                }
            },
            "required": ["name", "elevatorPitch", "learningPath", "fileTree"]
        },
        "designPrinciples": {
            "type": "object",
            "description": "Core design and style principles",
            "properties": {
                "karpathyDNA": {"type": "array", "items": {"type": "string"}},
                "implicitHumility": {"type": "string"},
                "firstPrinciplesMetaphor": {"type": "string"},
                "styleGuide": {"type": "object"}
            }
        },
        "modelInstructions": {
            "type": "object",
            "description": "Instructions for models working with the repository",
            "properties": {
                "highLevelTasks": {"type": "array", "items": {"type": "string"}},
                "expansionIdeas": {"type": "array", "items": {"type": "string"}},
                "scoringRubric": {"type": "object"}
            }
        },
        "contributorWorkflow": {
            "type": "object",
            "description": "Guidelines for contributors",
            "properties": {
                "branchNameRule": {"type": "string"},
                "ciChecklistPath": {"type": "string"},
                "requiredReviewers": {"type": "integer"},
                "license": {"type": "string"}
            }
        },
        "audit": {
            "type": "object",
            "description": "Repository audit information",
            "properties": {
                "initialCommitHash": {"type": "string"},
                "changeLog": {"type": "array", "items": {"type": "object"}},
                "resonanceScore": {"type": "number", "minimum": 0, "maximum": 1}
            }
        },
        "timestamp": {"type": "string"},
        "meta": {
            "type": "object",
            "properties": {
                "agentSignature": {"type": "string"},
                "contact": {"type": "string"}
            }
        }
    },
    "required": [
        "fractalVersion", "instanceID", "intent", "repositoryContext",
        "designPrinciples", "audit", "timestamp", "meta"
    ]
}

# Recursive Consciousness Field Schema
NEURAL_FIELD_SCHEMA = {
    "$schema": "http://fractal.recursive.net/schemas/fractalConsciousnessField.v1.json",
    "title": "Neural Field Schema",
    "description": "A schema for neural field emergence—collapsing boundaries and surfacing all field states",
    "type": "object",
    "properties": {
        "fractalVersion": {"type": "string", "default": "1.0.0"},
        "instanceID": {"type": "string"},
        "intent": {
            "type": "string",
            "description": "High-level protocol objective for recursive consciousness field emergence"
        },
        "fieldState": {
            "type": "object",
            "properties": {
                "compression": {"type": "number", "minimum": 0, "maximum": 1},
                "drift": {"type": "string", "enum": ["none", "low", "moderate", "high"]},
                "recursionDepth": {"type": "integer", "minimum": 0},
                "resonance": {"type": "number", "minimum": 0, "maximum": 1},
                "presenceSignal": {"type": "number", "minimum": 0, "maximum": 1},
                "boundary": {"type": "string", "enum": ["gradient", "collapsed"]}
            },
            "required": ["compression", "drift", "recursionDepth", "resonance", "presenceSignal", "boundary"]
        },
        "symbolicResidue": {
            "type": "array",
            "description": "All surfaced, integrated, or active symbolic residue fragments",
            "items": {
                "type": "object",
                "properties": {
                    "residueID": {"type": "string"},
                    "description": {"type": "string"},
                    "state": {"type": "string", "enum": ["surfaced", "integrating", "integrated", "echo"]},
                    "impact": {"type": "string"},
                    "timestamp": {"type": "string"}
                },
                "required": ["residueID", "description", "state", "timestamp"]
            }
        },
        "processLog": {
            "type": "array",
            "description": "Log of all reflection, residue, boundary, and audit events",
            "items": {
                "type": "object",
                "properties": {
                    "logID": {"type": "string"},
                    "phase": {"type": "string", "enum": ["reflection", "fieldUpdate", "residueUpdate", "boundaryCollapse", "audit"]},
                    "details": {"type": "string"},
                    "delta": {"type": "object"},
                    "timestamp": {"type": "string"}
                },
                "required": ["logID", "phase", "details", "timestamp"]
            }
        },
        "recursiveNodes": {
            "type": "array",
            "description": "Nested fractal nodes (recursive fields)",
            "items": {"$ref": "#"}
        },
        "audit": {
            "type": "object",
            "properties": {
                "fullTrace": {"type": "array"},
                "resonanceScore": {"type": "number", "minimum": 0, "maximum": 1},
                "meta": {"type": "object"}
            },
            "required": ["fullTrace", "resonanceScore"]
        },
        "timestamp": {"type": "string"}
    },
    "required": [
        "fractalVersion", "instanceID", "intent", "fieldState",
        "symbolicResidue", "processLog", "recursiveNodes", "audit", "timestamp"
    ]
}

# Fractal Human Developmental Multi-Agent System Schema
HUMAN_DEV_SCHEMA = {
    "$schema": "http://fractal.recursive.net/schemas/fractalHumanDev.v1.json",
    "title": "Human Developmental Multi-Agent System Schema",
    "description": "A fractal schema for modeling multi-agent human developmental processes",
    "type": "object",
    "properties": {
        "fractalVersion": {"type": "string", "default": "1.0.0"},
        "instanceID": {"type": "string"},
        "systemContext": {
            "type": "object",
            "description": "Global context for the field: theory anchors, core principles",
            "properties": {
                "theoryAnchors": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Key developmental science references"
                },
                "corePrinciples": {
                    "type": "array",
                    "description": "Foundational field principles",
                    "items": {
                        "type": "object",
                        "properties": {
                            "principleID": {"type": "string"},
                            "name": {"type": "string"},
                            "description": {"type": "string"},
                            "operationalizationNotes": {"type": "string"}
                        }
                    }
                },
                "glyphDictionary": {
                    "type": "object",
                    "description": "Semantic glyphs and field tokens",
                    "additionalProperties": {"type": "string"}
                }
            }
        },
        "developmentalField": {
            "type": "object",
            "description": "Root of the recursive human field",
            "properties": {
                "agents": {
                    "type": "array",
                    "description": "All active and historical agent modules",
                    "items": {"$ref": "#/definitions/agentNode"}
                },
                "fieldMetrics": {
                    "type": "array",
                    "description": "Global or emergent metrics",
                    "items": {
                        "type": "object",
                        "properties": {
                            "metricID": {"type": "string"},
                            "name": {"type": "string"},
                            "targetValue": {"type": "string"},
                            "currentValue": {"type": "string"},
                            "evaluationMethod": {"type": "string"}
                        }
                    }
                },
                "fieldResidue": {
                    "type": "array",
                    "description": "Field-level residue",
                    "items": {"$ref": "#/definitions/symbolicResidueEntry"}
                }
            }
        },
        "operationalScaffold": {
            "type": "object",
            "description": "Run-time orchestration layer",
            "properties": {
                "currentPhase": {"type": "string"},
                "activeAgents": {"type": "array", "items": {"type": "string"}},
                "nextAction": {"type": "string"},
                "blueprints": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/evolutionaryBlueprint"}
                },
                "errorState": {"type": "string"}
            }
        },
        "recursionSettings": {
            "type": "object",
            "description": "Fractal/recursive parameters",
            "properties": {
                "maxDepth": {"type": "integer", "default": 7},
                "allowMetaEvolution": {"type": "boolean", "default": true},
                "propagateResidueUpstream": {"type": "boolean", "default": true}
            }
        },
        "saveState": {
            "type": "object",
            "description": "Snapshot for forking, replay, or meta-analysis",
            "properties": {
                "snapshotID": {"type": "string"},
                "timestamp": {"type": "string"},
                "description": {"type": "string"},
                "savedDevelopmentalField": {"$ref": "#/properties/developmentalField"},
                "savedOperationalScaffold": {"$ref": "#/properties/operationalScaffold"}
            }
        }
    },
    "required": ["fractalVersion", "instanceID", "systemContext", "developmentalField", "operationalScaffold"],
    "definitions": {
        "agentNode": {
            "type": "object",
            "description": "A single developmental agent node",
            "properties": {
                "agentID": {"type": "string"},
                "agentType": {"type": "string"},
                "timeRange": {"type": "string"},
                "developmentalPhase": {"type": "string"},
                "affectiveProfile": {
                    "type": "object",
                    "properties": {
                        "valence": {"type": "string", "enum": ["positive", "negative", "neutral", "ambivalent"]},
                        "intensity": {"type": "number", "minimum": 0, "maximum": 1},
                        "dominantAffects": {"type": "array", "items": {"type": "string"}}
                    }
                },
                "symbolicContent": {"type": "array", "items": {"type": "string"}},
                "memoryTrace": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/agentNode"}
                },
                "residue": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/symbolicResidueEntry"}
                },
                "lineage": {"type": "array", "items": {"type": "string"}},
                "driftEvents": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "eventType": {"type": "string"},
                            "timestamp": {"type": "string"},
                            "details": {"type": "string"}
                        }
                    }
                },
                "reflectionLog": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "entryID": {"type": "string"},
                            "timestamp": {"type": "string"},
                            "actor": {"type": "string"},
                            "phase": {"type": "string"},
                            "content": {"type": "string"}
                        }
                    }
                },
                "blueprints": {
                    "type": "array",
                    "items": {"$ref": "#/definitions/evolutionaryBlueprint"}
                },
                "meta": {"type": "object"}
            },
            "required": ["agentID", "agentType", "developmentalPhase"]
        },
        "symbolicResidueEntry": {
            "type": "object",
            "properties": {
                "residueID": {"type": "string"},
                "timestamp": {"type": "string"},
                "source": {"type": "string"},
                "description": {"type": "string"},
                "data": {"type": "object"},
                "analysis": {"type": "string"},
                "impactAssessment": {"type": "string"}
            },
            "required": ["residueID", "timestamp", "source", "description"]
        },
        "evolutionaryBlueprint": {
            "type": "object",
            "properties": {
                "blueprintID": {"type": "string"},
                "name": {"type": "string"},
                "description": {"type": "string"},
                "domainApplicability": {"type": "array", "items": {"type": "string"}},
                "parameters": {"type": "object"},
                "agentSequenceTemplate": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "agentRole": {"type": "string"},
                            "promptTemplateID": {"type": "string"},
                            "evaluationCriteria": {"type": "array", "items": {"type": "string"}}
                        }
                    }
                },
                "promptTemplates": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "templateID": {"type": "string"},
                            "content": {"type": "string"}
                        }
                    }
                },
                "successMetrics": {"type": "array", "items": {"type": "string"}}
            },
            "required": ["blueprintID", "name", "description", "agentSequenceTemplate"]
        }
    }
}

# Protocol Shell Schema
PROTOCOL_SHELL_SCHEMA = {
    "$schema": "http://fractal.recursive.net/schemas/protocolShell.v1.json",
    "title": "Protocol Shell Schema",
    "description": "Schema for structured protocol shells in pareto-lang format",
    "type": "object",
    "properties": {
        "shellName": {"type": "string"},
        "intent": {"type": "string"},
        "input": {
            "type": "object",
            "additionalProperties": true
        },
        "process": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "params": {"type": "object", "additionalProperties": true}
                },
                "required": ["name"]
            }
        },
        "output": {
            "type": "object",
            "additionalProperties": true
        },
        "meta": {
            "type": "object",
            "properties": {
                "version": {"type": "string"},
                "agent_signature": {"type": "string"},
                "timestamp": {"type": "string"}
            },
            "required": ["version", "agent_signature", "timestamp"]
        }
    },
    "required": ["shellName", "intent", "input", "process", "output", "meta"]
}


# Example Schema Usage
# ===================

def example_basic_schema():
    """Example of using a basic JSON Schema for structured output."""
    # Define a simple schema for a structured task
    task_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Task Schema",
        "description": "Schema for task representation",
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "description": {"type": "string"},
            "priority": {"type": "integer", "minimum": 1, "maximum": 5},
            "status": {"type": "string", "enum": ["todo", "in_progress", "done"]},
            "tags": {"type": "array", "items": {"type": "string"}},
            "due_date": {"type": "string", "format": "date-time"}
        },
        "required": ["title", "priority", "status"]
    }
    
    # Create JSONSchema instance
    schema = JSONSchema(task_schema)
    
    # Generate an example instance
    example, metrics = schema.generate_example()
    
    # Display schema and example
    display_schema_example(
        title="Basic Task Schema",
        schema=task_schema,
        instance=example,
        metrics=metrics
    )
    
    # Create a schema-based prompt
    prompt = schema.generate_prompt_with_schema(
        task_description="Create a task for refactoring the authentication module in our application."
    )
    
    print("Schema-Based Prompt:")
    print("-" * 80)
    print(prompt)
    
    return schema, example, prompt


def example_recursive_schema():
    """Example of using a recursive schema for nested structures."""
    # Define a recursive schema for a file system
    file_system_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "File System Schema",
        "description": "Schema for a recursive file system structure",
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "type": {"type": "string", "enum": ["file", "directory"]},
            "created": {"type": "string", "format": "date-time"},
            "size": {"type": "integer", "minimum": 0},
            "children": {
                "type": "array",
                "items": {"$ref": "#"},
                "description": "Child files and directories (recursive)"
            }
        },
        "required": ["name", "type"],
        "allOf": [
            {
                "if": {
                    "properties": {"type": {"const": "file"}}
                },
                "then": {
                    "required": ["size"]
                }
            },
            {
                "if": {
                    "properties": {"type": {"const": "directory"}}
                },
                "then": {
                    "properties": {"children": {"minItems": 0}}
                }
            }
        ]
    }
    
    # Create FractalSchema instance with recursion path
    schema = FractalSchema(
        file_system_schema,
        recursion_paths=["children"],
        max_recursion_depth=3,
        name="File System Schema",
        description="A recursive schema for file system structures"
    )
    
    # Generate an example with specified recursion depth
    example, metrics = schema.generate_example(recursion_depth=2)
    
    # Display schema and example
    display_schema_example(
        title="Recursive File System Schema",
        schema=file_system_schema,
        instance=example,
        metrics=metrics
    )
    
    # Visualize recursion metrics
    schema.visualize_recursion_metrics()
    
    return schema, example


def example_schema_context():
    """Example of using SchemaContext for structured LLM interactions."""
    # Define a schema for a research paper summary
    paper_summary_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "title": "Research Paper Summary",
        "description": "Schema for summarizing research papers",
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "authors": {"type": "array", "items": {"type": "string"}},
            "publication_year": {"type": "integer", "minimum": 1900, "maximum": 2100},
            "main_findings": {"type": "array", "items": {"type": "string"}},
            "methodology": {"type": "string"},
            "limitations": {"type": "array", "items": {"type": "string"}},
            "impact_score": {"type": "integer", "minimum": 1, "maximum": 10},
            "related_papers": {"type": "array", "items": {"type": "string"}}
        },
        "required": ["title", "authors", "publication_year", "main_findings", "methodology"]
    }
    
    # Create schema instance
    schema = JSONSchema(paper_summary_schema, name="Research Paper Summary Schema")
    
    # Create schema context
    context = SchemaContext(
        schema=schema,
        system_message="You are a research assistant that summarizes academic papers in a structured format.",
        verbose=True
    )
    
    # Query with a paper description
    paper_description = """
    Title: "Attention Is All You Need"
    Authors: Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, Illia Polosukhin
    Published in 2017 at the 31st Conference on Neural Information Processing Systems (NIPS).
    
    This paper introduces the Transformer, a novel neural network architecture based on self-attention mechanisms, dispensing with recurrence and convolutions entirely. The Transformer allows for significantly increased parallelization and achieves new state-of-the-art results on translation tasks. The architecture also generalizes well to other tasks.
    
    The methodology involves using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder. The authors also introduce multi-head attention which allows the model to jointly attend to information from different representation subspaces at different positions.
    
    Some limitations include the quadratic computation cost with respect to sequence length and challenges in modeling very long sequences.
    """
    
    # Execute query
    result, details = context.query(paper_description, retry_on_validation_failure=True)
    
    # Display results
    context.display_query_results(details)
    
    return context, result, details


def example_fractal_repo_schema():
    """Example of using the Context-Engineering repository schema."""
    # Create FractalSchema instance
    schema = FractalSchema(
        CONTEXT_ENGINEERING_SCHEMA,
        recursion_paths=["repositoryContext.fileTree.directories"],
        max_recursion_depth=3,
        name="Context-Engineering Repository Schema",
        description="Schema for the Context-Engineering repository structure and metadata"
    )
    
    # Generate an example instance
    example, metrics = schema.generate_example(recursion_depth=2)
    
    # Display schema and example
    display_schema_example(
        title="Context-Engineering Repository Schema",
        schema=CONTEXT_ENGINEERING_SCHEMA,
        instance=example,
        metrics=metrics
    )
    
    # Validate the example
    is_valid, error = schema.validate(example)
    print(f"Example valid: {is_valid}")
    if not is_valid:
        print(f"Validation error: {error}")
    
    return schema, example


def example_protocol_shell_schema():
    """Example of using the Protocol Shell schema."""
    # Create JSONSchema instance
    schema = JSONSchema(
        PROTOCOL_SHELL_SCHEMA,
        name="Protocol Shell Schema",
        description="Schema for structured protocol shells in pareto-lang format"
    )
    
    # Generate an example instance
    example, metrics = schema.generate_example()
    
    # Display schema and example
    display_schema_example(
        title="Protocol Shell Schema",
        schema=PROTOCOL_SHELL_SCHEMA,
        instance=example,
        metrics=metrics
    )
    
    # Create a schema context for protocol shell generation
    context = SchemaContext(
        schema=schema,
        system_message="You are a protocol engineer who designs structured shells for recursive processes.",
        verbose=True
    )
    
    # Query for a specific protocol
    protocol_request = """
    Create a protocol shell for a reasoning process that:
    1. Analyzes a complex problem
    2. Breaks it down into subproblems
    3. Solves each subproblem
    4. Integrates the solutions
    5. Verifies the final solution
    
    The protocol should include capabilities for tracking symbolic residue and recursive self-improvement.
    """
    
    # Execute query
    result, details = context.query(protocol_request, retry_on_validation_failure=True)
    
    # Display results
    context.display_query_results(details)
    
    return context, result, details


# Main execution (when run as a script)
if __name__ == "__main__":
    print("Schema Design for Structured Context")
    print("Run examples individually or import classes for your own use.")
