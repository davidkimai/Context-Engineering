#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Context-Engineering: Recursive Patterns for Self-Improving Contexts
==================================================================

This module explores recursive patterns in context engineering - approaches
that enable LLMs to extend, refine, and evolve their own context. These patterns
create feedback loops within prompts, allowing for iterative improvement,
self-verification, and emergent capabilities beyond what's explicitly coded.

Key concepts covered:
1. Basic recursive patterns (self-reflection, bootstrapping)
2. Field protocols and shells as recursive frameworks
3. Symbolic residue and state tracking
4. Boundary collapse and gradient systems
5. Emergent attractors and resonance

Usage:
    # In Jupyter or Colab:
    %run 07_recursive_patterns.py
    # or
    from recursive_patterns import RecursivePattern, FieldProtocol, SymbolicResidue
"""

import os
import re
import json
import time
import uuid
import hashlib
import logging
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


def display_recursive_pattern(
    pattern_name: str,
    input_data: Any,
    iterations: List[Dict[str, Any]],
    final_output: Any,
    metrics: Dict[str, Any] = None
) -> None:
    """
    Display a recursive pattern's execution in a notebook.
    
    Args:
        pattern_name: Name of the recursive pattern
        input_data: Initial input data
        iterations: List of iteration data
        final_output: Final output data
        metrics: Optional metrics dictionary
    """
    display(HTML(f"<h2>Recursive Pattern: {pattern_name}</h2>"))
    
    # Display input
    display(HTML("<h3>Initial Input</h3>"))
    if isinstance(input_data, str):
        display(Markdown(input_data))
    else:
        display(Markdown(f"```json\n{json.dumps(input_data, indent=2)}\n```"))
    
    # Display iterations
    display(HTML("<h3>Recursive Iterations</h3>"))
    
    for i, iteration in enumerate(iterations):
        display(HTML(f"<h4>Iteration {i+1}</h4>"))
        
        # Display prompt if available
        if "prompt" in iteration:
            display(HTML("<p><em>Prompt:</em></p>"))
            display(Markdown(f"```\n{iteration['prompt']}\n```"))
        
        # Display response if available
        if "response" in iteration:
            display(HTML("<p><em>Response:</em></p>"))
            display(Markdown(iteration["response"]))
        
        # Display state if available
        if "state" in iteration:
            display(HTML("<p><em>State:</em></p>"))
            if isinstance(iteration["state"], str):
                display(Markdown(iteration["state"]))
            else:
                display(Markdown(f"```json\n{json.dumps(iteration['state'], indent=2)}\n```"))
        
        # Display metrics if available
        if "metrics" in iteration:
            display(HTML("<p><em>Metrics:</em></p>"))
            display(Markdown(f"```\n{format_metrics(iteration['metrics'])}\n```"))
    
    # Display final output
    display(HTML("<h3>Final Output</h3>"))
    if isinstance(final_output, str):
        display(Markdown(final_output))
    else:
        display(Markdown(f"```json\n{json.dumps(final_output, indent=2)}\n```"))
    
    # Display overall metrics
    if metrics:
        display(HTML("<h3>Overall Metrics</h3>"))
        display(Markdown(f"```\n{format_metrics(metrics)}\n```"))


# Base Classes for Recursive Patterns
# =================================

class RecursivePattern:
    """
    Base class for recursive patterns - approaches that enable LLMs
    to extend, refine, and evolve their own context.
    """
    
    def __init__(
        self,
        name: str,
        description: str = "",
        client=None,
        model: str = DEFAULT_MODEL,
        system_message: str = "You are a helpful assistant.",
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        max_iterations: int = 5,
        verbose: bool = False
    ):
        """
        Initialize the recursive pattern.
        
        Args:
            name: Pattern name
            description: Pattern description
            client: API client (if None, will create one)
            model: Model name to use
            system_message: System message to use
            max_tokens: Maximum tokens to generate
            temperature: Temperature parameter
            max_iterations: Maximum number of recursive iterations
            verbose: Whether to print debug information
        """
        self.name = name
        self.description = description
        self.client, self.model = setup_client(model=model) if client is None else (client, model)
        self.system_message = system_message
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.max_iterations = max_iterations
        self.verbose = verbose
        
        # Initialize state
        self.state = {}
        self.iterations = []
        
        # Initialize metrics tracking
        self.metrics = {
            "total_prompt_tokens": 0,
            "total_response_tokens": 0,
            "total_tokens": 0,
            "total_latency": 0,
            "iterations": 0
        }
    
    def _log(self, message: str) -> None:
        """
        Log a message if verbose mode is enabled.
        
        Args:
            message: Message to log
        """
        if self.verbose:
            logger.info(message)
    
    def _generate_recursive_prompt(self, iteration: int, **kwargs) -> str:
        """
        Generate a prompt for the current iteration of the recursive pattern.
        
        Args:
            iteration: Current iteration number
            **kwargs: Additional variables for prompt generation
            
        Returns:
            str: Generated prompt
        """
        # This is a placeholder - subclasses should implement this
        raise NotImplementedError("Subclasses must implement _generate_recursive_prompt")
    
    def _call_llm(
        self,
        prompt: str,
        custom_system_message: Optional[str] = None
    ) -> Tuple[str, Dict[str, Any]]:
        """
        Call the LLM and update metrics.
        
        Args:
            prompt: Prompt to send
            custom_system_message: Override system message (optional)
            
        Returns:
            tuple: (response_text, metadata)
        """
        system_msg = custom_system_message if custom_system_message else self.system_message
        
        response, metadata = generate_response(
            prompt=prompt,
            client=self.client,
            model=self.model,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            system_message=system_msg
        )
        
        # Update metrics
        self.metrics["total_prompt_tokens"] += metadata.get("prompt_tokens", 0)
        self.metrics["total_response_tokens"] += metadata.get("response_tokens", 0)
        self.metrics["total_tokens"] += metadata.get("total_tokens", 0)
        self.metrics["total_latency"] += metadata.get("latency", 0)
        self.metrics["iterations"] += 1
        
        return response, metadata
    
    def _process_response(self, response: str, iteration: int) -> Any:
        """
        Process the LLM response for the current iteration.
        
        Args:
            response: LLM response text
            iteration: Current iteration number
            
        Returns:
            Any: Processed output
        """
        # Default implementation returns the response as is
        return response
    
    def _update_state(
        self,
        iteration: int,
        prompt: str,
        response: str,
        processed_output: Any,
        metrics: Dict[str, Any]
    ) -> None:
        """
        Update the state based on the current iteration results.
        
        Args:
            iteration: Current iteration number
            prompt: Prompt sent to LLM
            response: Raw LLM response
            processed_output: Processed iteration output
            metrics: Iteration metrics
        """
        # Create iteration record
        iteration_record = {
            "iteration": iteration,
            "prompt": prompt,
            "response": response,
            "output": processed_output,
            "state": self.state.copy(),
            "metrics": metrics,
            "timestamp": time.time()
        }
        
        # Add to iterations history
        self.iterations.append(iteration_record)
        
        # Update current state
        self.state["current_iteration"] = iteration
        self.state["last_prompt"] = prompt
        self.state["last_response"] = response
        self.state["last_output"] = processed_output
    
    def _should_continue(self, iteration: int, current_output: Any) -> bool:
        """
        Determine whether to continue the recursive pattern.
        
        Args:
            iteration: Current iteration number
            current_output: Current iteration output
            
        Returns:
            bool: True if the pattern should continue, False otherwise
        """
        # Default implementation continues until max_iterations is reached
        return iteration < self.max_iterations
    
    def run(self, input_data: Any) -> Tuple[Any, List[Dict[str, Any]]]:
        """
        Run the recursive pattern with the given input.
        
        Args:
            input_data: Initial input data
            
        Returns:
            tuple: (final_output, iterations_history)
        """
        # Initialize state with input
        self.state = {"input": input_data}
        self.iterations = []
        
        self._log(f"Starting recursive pattern: {self.name}")
        
        # Initial output is the input
        current_output = input_data
        iteration = 0
        
        # Recursive iteration loop
        while True:
            iteration += 1
            self._log(f"Iteration {iteration}/{self.max_iterations}")
            
            # Generate prompt for current iteration
            prompt = self._generate_recursive_prompt(
                iteration=iteration,
                input=input_data,
                current_output=current_output,
                **self.state
            )
            
            # Call LLM
            response, metrics = self._call_llm(prompt)
            
            # Process response
            processed_output = self._process_response(response, iteration)
            
            # Update state
            self._update_state(iteration, prompt, response, processed_output, metrics)
            
            # Update current output
            current_output = processed_output
            
            # Check if we should continue
            if not self._should_continue(iteration, current_output):
                self._log(f"Stopping at iteration {iteration}")
                break
        
        return current_output, self.iterations
    
    def get_summary_metrics(self) -> Dict[str, Any]:
        """
        Get summary metrics for all iterations.
        
        Returns:
            dict: Summary metrics
        """
        summary = self.metrics.copy()
        
        # Add derived metrics
        if summary["iterations"] > 0:
            summary["avg_latency_per_iteration"] = summary["total_latency"] / summary["iterations"]
            
        if summary["total_prompt_tokens"] > 0:
            summary["overall_efficiency"] = (
                summary["total_response_tokens"] / summary["total_prompt_tokens"]
            )
        
        return summary
    
    def display_execution(self) -> None:
        """Display the recursive pattern execution in a notebook."""
        display_recursive_pattern(
            pattern_name=self.name,
            input_data=self.state.get("input"),
            iterations=self.iterations,
            final_output=self.state.get("last_output"),
            metrics=self.get_summary_metrics()
        )
    
    def visualize_metrics(self) -> None:
        """
        Create visualization of metrics across iterations.
        """
        if not self.iterations:
            logger.warning("No iterations to visualize")
            return
        
        # Extract data for plotting
        iterations = list(range(1, len(self.iterations) + 1))
        prompt_tokens = [it["metrics"].get("prompt_tokens", 0) for it in self.iterations]
        response_tokens = [it["metrics"].get("response_tokens", 0) for it in self.iterations]
        latencies = [it["metrics"].get("latency", 0) for it in self.iterations]
        efficiencies = [it["metrics"].get("token_efficiency", 0) for it in self.iterations]
        
        # Create figure
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f"Recursive Pattern Metrics: {self.name}", fontsize=16)
        
        # Plot 1: Token usage
        axes[0, 0].bar(iterations, prompt_tokens, label="Prompt Tokens", color="blue", alpha=0.7)
        axes[0, 0].bar(iterations, response_tokens, bottom=prompt_tokens, 
                       label="Response Tokens", color="green", alpha=0.7)
        axes[0, 0].set_title("Token Usage by Iteration")
        axes[0, 0].set_xlabel("Iteration")
        axes[0, 0].set_ylabel("Tokens")
        axes[0, 0].legend()
        axes[0, 0].grid(alpha=0.3)
        
        # Plot 2: Latency
        axes[0, 1].plot(iterations, latencies, marker='o', color="red", alpha=0.7)
        axes[0, 1].set_title("Latency by Iteration")
        axes[0, 1].set_xlabel("Iteration")
        axes[0, 1].set_ylabel("Seconds")
        axes[0, 1].grid(alpha=0.3)
        
        # Plot 3: Token efficiency
        axes[1, 0].plot(iterations, efficiencies, marker='s', color="purple", alpha=0.7)
        axes[1, 0].set_title("Token Efficiency (Response/Prompt)")
        axes[1, 0].set_xlabel("Iteration")
        axes[1, 0].set_ylabel("Ratio")
        axes[1, 0].grid(alpha=0.3)
        
        # Plot 4: Cumulative tokens
        cumulative_tokens = np.cumsum([it["metrics"].get("total_tokens", 0) for it in self.iterations])
        axes[1, 1].plot(iterations, cumulative_tokens, marker='^', color="orange", alpha=0.7)
        axes[1, 1].set_title("Cumulative Token Usage")
        axes[1, 1].set_xlabel("Iteration")
        axes[1, 1].set_ylabel("Total Tokens")
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()


# Recursive Pattern Implementations
# ===============================

class SelfReflection(RecursivePattern):
    """
    A recursive pattern that implements self-reflection and
    continuous improvement through meta-cognitive processes.
    """
    
    def __init__(
        self,
        reflection_template: str = "Analyze your previous response:\n\n{previous_response}\n\nIdentify strengths and weaknesses. How can you improve your response to better address the original query:\n\n{original_query}",
        improvement_threshold: float = 0.8,
        **kwargs
    ):
        """
        Initialize the self-reflection pattern.
        
        Args:
            reflection_template: Template for reflection prompts
            improvement_threshold: Threshold for stopping based on improvement
            **kwargs: Additional args passed to RecursivePattern
        """
        name = kwargs.pop("name", "Self-Reflection Pattern")
        description = kwargs.pop("description", "A pattern for continuous improvement through meta-cognitive processes")
        
        super().__init__(name=name, description=description, **kwargs)
        
        self.reflection_template = reflection_template
        self.improvement_threshold = improvement_threshold
        
        # Initialize reflection-specific state
        self.state["improvement_scores"] = []
    
    def _generate_recursive_prompt(self, iteration: int, **kwargs) -> str:
        """
        Generate a prompt for the current iteration of self-reflection.
        
        Args:
            iteration: Current iteration number
            **kwargs: Additional variables for prompt generation
            
        Returns:
            str: Generated prompt
        """
        input_query = kwargs.get("input")
        
        if iteration == 1:
            # First iteration: generate initial response
            prompt = f"Please respond to the following query:\n\n{input_query}"
        else:
            # Subsequent iterations: reflect and improve
            previous_response = kwargs.get("current_output", "")
            
            prompt = self.reflection_template.format(
                previous_response=previous_response,
                original_query=input_query
            )
        
        return prompt
    
    def _process_response(self, response: str, iteration: int) -> Dict[str, Any]:
        """
        Process the response for the current iteration of self-reflection.
        
        Args:
            response: LLM response text
            iteration: Current iteration number
            
        Returns:
            dict: Processed output with response and metadata
        """
        if iteration == 1:
            # First iteration: just store the initial response
            processed = {
                "iteration": iteration,
                "response": response,
                "improvement_score": 0.0
            }
        else:
            # Extract improved response and potential improvement score
            # Look for an improvement score pattern like "Improvement: X/10"
            score_pattern = r"(?:improvement|quality)\s*(?:score|rating)?:?\s*(\d+(?:\.\d+)?)\s*(?:\/\s*10)?"
            score_match = re.search(score_pattern, response.lower())
            
            improvement_score = float(score_match.group(1)) / 10 if score_match else 0.5
            
            # Store processed output
            processed = {
                "iteration": iteration,
                "response": response,
                "improvement_score": improvement_score
            }
            
            # Update improvement scores
            self.state["improvement_scores"].append(improvement_score)
        
        return processed
    
    def _should_continue(self, iteration: int, current_output: Any) -> bool:
        """
        Determine whether to continue the self-reflection.
        
        Args:
            iteration: Current iteration number
            current_output: Current iteration output
            
        Returns:
            bool: True if the pattern should continue, False otherwise
        """
        # Stop if we've reached max iterations
        if iteration >= self.max_iterations:
            return False
        
        # Continue if this is the first iteration
        if iteration == 1:
            return True
        
        # Check improvement score
        improvement_score = current_output.get("improvement_score", 0.0)
        
        # Stop if we've reached the improvement threshold
        if improvement_score >= self.improvement_threshold:
            self._log(f"Reached improvement threshold: {improvement_score:.2f}")
            return False
        
        return True


class RecursiveBootstrapping(RecursivePattern):
    """
    A recursive pattern that bootstraps its own capabilities
    by generating increasingly sophisticated strategies.
    """
    
    def __init__(
        self,
        bootstrap_template: str = "Based on your current approach to solving this problem:\n\n{current_approach}\n\nGenerate a more sophisticated strategy that builds upon your current approach and addresses its limitations.",
        sophistication_levels: List[str] = None,
        **kwargs
    ):
        """
        Initialize the recursive bootstrapping pattern.
        
        Args:
            bootstrap_template: Template for bootstrapping prompts
            sophistication_levels: Optional predefined levels of sophistication
            **kwargs: Additional args passed to RecursivePattern
        """
        name = kwargs.pop("name", "Recursive Bootstrapping Pattern")
        description = kwargs.pop("description", "A pattern for bootstrapping increasingly sophisticated strategies")
        
        super().__init__(name=name, description=description, **kwargs)
        
        self.bootstrap_template = bootstrap_template
        self.sophistication_levels = sophistication_levels or [
            "basic", "intermediate", "advanced", "expert", "innovative"
        ]
        
        # Initialize bootstrapping-specific state
        self.state["sophistication_level"] = 0
    
    def _generate_recursive_prompt(self, iteration: int, **kwargs) -> str:
        """
        Generate a prompt for the current iteration of bootstrapping.
        
        Args:
            iteration: Current iteration number
            **kwargs: Additional variables for prompt generation
            
        Returns:
            str: Generated prompt
        """
        input_problem = kwargs.get("input")
        
        if iteration == 1:
            # First iteration: generate initial basic approach
            level = self.sophistication_levels[0]
            prompt = f"""You are solving the following problem:

{input_problem}

Start by developing a {level} approach to solve this problem. 
Focus on foundational concepts and straightforward techniques."""
        else:
            # Subsequent iterations: bootstrap to more sophisticated approach
            current_approach = kwargs.get("current_output", {}).get("approach", "")
            
            # Get current and next sophistication level
            level_idx = min(iteration - 1, len(self.sophistication_levels) - 1)
            current_level = self.sophistication_levels[level_idx - 1]
            next_level = self.sophistication_levels[level_idx]
            
            prompt = f"""You are solving the following problem:

{input_problem}

Your current {current_level} approach is:

{current_approach}

Now, bootstrap from this {current_level} approach to develop a {next_level} approach 
that builds upon your current strategy and addresses its limitations. 
Your new approach should be more sophisticated, nuanced, and effective."""
        
        return prompt
    
    def _process_response(self, response: str, iteration: int) -> Dict[str, Any]:
        """
        Process the response for the current iteration of bootstrapping.
        
        Args:
            response: LLM response text
            iteration: Current iteration number
            
        Returns:
            dict: Processed output with approach and metadata
        """
        # Get sophistication level
        level_idx = min(iteration - 1, len(self.sophistication_levels) - 1)
        level = self.sophistication_levels[level_idx]
        
        # Store processed output
        processed = {
            "iteration": iteration,
            "level": level,
            "approach": response
        }
        
        # Update sophistication level
        self.state["sophistication_level"] = level_idx
        
        return processed


class SymbolicResidue(RecursivePattern):
    """
    A recursive pattern that tracks, integrates, and evolves
    symbolic residue across iterations.
    """
    
    def __init__(
        self,
        residue_template: str = "Process the following input while surfacing and integrating symbolic residue:\n\nInput: {input}\n\nCurrent symbolic residue: {symbolic_residue}",
        **kwargs
    ):
        """
        Initialize the symbolic residue pattern.
        
        Args:
            residue_template: Template for residue processing prompts
            **kwargs: Additional args passed to RecursivePattern
        """
        name = kwargs.pop("name", "Symbolic Residue Pattern")
        description = kwargs.pop("description", "A pattern for tracking and integrating symbolic residue")
        
        super().__init__(name=name, description=description, **kwargs)
        
        self.residue_template = residue_template
        
        # Initialize residue-specific state
        self.state["symbolic_residue"] = []
        self.state["residue_compression"] = 0.0
        self.state["resonance_score"] = 0.0
    
    def _generate_recursive_prompt(self, iteration: int, **kwargs) -> str:
        """
        Generate a prompt for the current iteration of residue processing.
        
        Args:
            iteration: Current iteration number
            **kwargs: Additional variables for prompt generation
            
        Returns:
            str: Generated prompt
        """
        input_data = kwargs.get("input")
        symbolic_residue = self.state.get("symbolic_residue", [])
        
        # Format symbolic residue as text
        residue_text = "\n".join([f"- {item}" for item in symbolic_residue]) if symbolic_residue else "None yet"
        
        if iteration == 1:
            # First iteration: initial residue surfacing
            prompt = f"""Process the following input and surface any symbolic residue or patterns:

Input: {input_data}

Symbolic residue refers to fragments, patterns, or echoes that emerge from the processing 
but aren't directly part of the output. Surface this residue explicitly.

Your response should include:
1. The processed output
2. A section titled "Surfaced Symbolic Residue" listing any residue identified
3. A resonance score (0.0-1.0) indicating how strongly the residue resonates with the input"""
        else:
            # Subsequent iterations: integrate and evolve residue
            prompt = f"""Process the following input while integrating existing symbolic residue:

Input: {input_data}

Current symbolic residue:
{residue_text}

Residue compression: {self.state.get('residue_compression', 0.0):.2f}
Resonance score: {self.state.get('resonance_score', 0.0):.2f}

Integrate the existing residue into your processing, then surface new or evolved residue.

Your response should include:
1. The processed output with integrated residue
2. A section titled "Evolved Symbolic Residue" listing any updated residue
3. A residue compression score (0.0-1.0) indicating how well the residue is being compressed
4. A resonance score (0.0-1.0) indicating how strongly the residue resonates with the input"""
        
        return prompt
    
    def _process_response(self, response: str, iteration: int) -> Dict[str, Any]:
        """
        Process the response for the current iteration of residue processing.
        
        Args:
            response: LLM response text
            iteration: Current iteration number
            
        Returns:
            dict: Processed output with output and residue information
        """
        # Extract main output (everything before the residue section)
        output_pattern = r"(.*?)(?:Surfaced|Evolved) Symbolic Residue:"
        output_match = re.search(output_pattern, response, re.DOTALL)
        main_output = output_match.group(1).strip() if output_match else response
        
        # Extract symbolic residue
        residue_pattern = r"(?:Surfaced|Evolved) Symbolic Residue:(.*?)(?:Residue compression:|Resonance score:|$)"
        residue_match = re.search(residue_pattern, response, re.DOTALL)
        
        if residue_match:
            residue_text = residue_match.group(1).strip()
            # Extract individual residue items (assuming bullet or numbered list)
            residue_items = re.findall(r"(?:^|\n)[-*\d]+\.\s*(.*?)(?=\n[-*\d]+\.\s*|\n\n|$)", residue_text, re.DOTALL)
            
            if not residue_items:
                # Try alternative pattern for non-bulleted lists
                residue_items = [line.strip() for line in residue_text.split("\n") if line.strip()]
        else:
            residue_items = []
        
        # Extract compression score
        compression_pattern = r"Residue compression:?\s*(\d+(?:\.\d+)?)"
        compression_match = re.search(compression_pattern, response, re.IGNORECASE)
        compression_score = float(compression_match.group(1)) if compression_match else 0.0
        
        # Extract resonance score
        resonance_pattern = r"Resonance score:?\s*(\d+(?:\.\d+)?)"
        resonance_match = re.search(resonance_pattern, response, re.IGNORECASE)
        resonance_score = float(resonance_match.group(1)) if resonance_match else 0.0
        
        # Update state
        self.state["symbolic_residue"] = residue_items
        self.state["residue_compression"] = compression_score
        self.state["resonance_score"] = resonance_score
        
        # Store processed output
        processed = {
            "iteration": iteration,
            "output": main_output,
            "symbolic_residue": residue_items,
            "residue_compression": compression_score,
            "resonance_score": resonance_score
        }
        
        return processed
    
    def _should_continue(self, iteration: int, current_output: Any) -> bool:
        """
        Determine whether to continue the residue processing.
        
        Args:
            iteration: Current iteration number
            current_output: Current iteration output
            
        Returns:
            bool: True if the pattern should continue, False otherwise
        """
        # Stop if we've reached max iterations
        if iteration >= self.max_iterations:
            return False
        
        # Check resonance score
        resonance_score = current_output.get("resonance_score", 0.0)
