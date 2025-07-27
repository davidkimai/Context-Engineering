#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Context-Engineering: Prompt Programs for Structured Reasoning
============================================================

This module introduces prompt programming: a structured approach to designing
prompts as executable programs with compositional operations, state management,
and control flow. By treating prompts as code-like entities, we can create more
robust, transparent, and extensible reasoning systems.

Key concepts covered:
1. Basic prompt program structures and templates
2. Compositional operations (reasoning steps, verification, synthesis)
3. Protocol shells and frameworks as prompt programs
4. Field protocols and frameworks for emergent reasoning
5. Advanced patterns for self-improving prompt programs

Usage:
    # In Jupyter or Colab:
    %run 05_prompt_programs.py
    # or
    from prompt_programs import PromptProgram, ReasoningProtocol, FieldShell
"""

import os
import re
import json
import time
import logging
import hashlib
import tiktoken
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Any, Optional, Union, Callable, TypeVar
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


def display_program_output(
    program_name: str,
    input_data: Any,
    output_data: Any,
    state_history: Optional[List[Dict[str, Any]]] = None,
    metrics: Optional[Dict[str, Any]] = None
) -> None:
    """
    Display a prompt program's execution results in a notebook.
    
    Args:
        program_name: Name of the prompt program
        input_data: Input data
        output_data: Output data
        state_history: Program execution state history (optional)
        metrics: Metrics dictionary (optional)
    """
    display(HTML(f"<h2>Prompt Program: {program_name}</h2>"))
    
    # Display input
    display(HTML("<h3>Input</h3>"))
    if isinstance(input_data, str):
        display(Markdown(input_data))
    else:
        display(Markdown(f"```json\n{json.dumps(input_data, indent=2)}\n```"))
    
    # Display execution state history
    if state_history:
        display(HTML("<h3>Execution History</h3>"))
        
        for i, state in enumerate(state_history):
            display(HTML(f"<h4>Step {i+1}: {state.get('operation', 'Execution')}</h4>"))
            
            # Display prompt if available
            if "prompt" in state:
                display(HTML("<p><em>Prompt:</em></p>"))
                display(Markdown(f"```\n{state['prompt']}\n```"))
            
            # Display response if available
            if "response" in state:
                display(HTML("<p><em>Response:</em></p>"))
                display(Markdown(state["response"]))
            
            # Display state metrics if available
            if "metrics" in state:
                display(HTML("<p><em>Metrics:</em></p>"))
                display(Markdown(f"```\n{format_metrics(state['metrics'])}\n```"))
    
    # Display output
    display(HTML("<h3>Output</h3>"))
    if isinstance(output_data, str):
        display(Markdown(output_data))
    else:
        display(Markdown(f"```json\n{json.dumps(output_data, indent=2)}\n```"))
    
    # Display metrics
    if metrics:
        display(HTML("<h3>Overall Metrics</h3>"))
        display(Markdown(f"```\n{format_metrics(metrics)}\n```"))


# Base Classes for Prompt Programs
# ===============================

@dataclass
class PromptTemplate:
    """
    A template for a prompt with variables that can be filled in.
    """
    template: str
    variables: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Initialize by extracting variables from the template if not provided."""
        if not self.variables:
            # Extract variables from {variable} patterns in the template
            import re
            self.variables = re.findall(r'\{([^{}]*)\}', self.template)
    
    def format(self, **kwargs) -> str:
        """
        Format the template with the provided variables.
        
        Args:
            **kwargs: Variable values to fill in
            
        Returns:
            str: Formatted prompt
        """
        # Check for missing variables
        missing_vars = [var for var in self.variables if var not in kwargs]
        if missing_vars:
            raise ValueError(f"Missing variables: {', '.join(missing_vars)}")
        
        # Format the template
        return self.template.format(**kwargs)


class PromptProgram:
    """
    Base class for prompt programs - structured prompts that can be executed
    as programs with state and operations.
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
        verbose: bool = False
    ):
        """
        Initialize the prompt program.
        
        Args:
            name: Program name
            description: Program description
            client: API client (if None, will create one)
            model: Model name to use
            system_message: System message to use
            max_tokens: Maximum tokens to generate
            temperature: Temperature parameter
            verbose: Whether to print debug information
        """
        self.name = name
        self.description = description
        self.client, self.model = setup_client(model=model) if client is None else (client, model)
        self.system_message = system_message
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.verbose = verbose
        
        # Initialize state
        self.state = {}
        self.state_history = []
        
        # Initialize metrics tracking
        self.metrics = {
            "total_prompt_tokens": 0,
            "total_response_tokens": 0,
            "total_tokens": 0,
            "total_latency": 0,
            "steps": 0
        }
    
    def _log(self, message: str) -> None:
        """
        Log a message if verbose mode is enabled.
        
        Args:
            message: Message to log
        """
        if self.verbose:
            logger.info(message)
    
    def _generate_prompt(self, **kwargs) -> str:
        """
        Generate a prompt for the current operation.
        
        Args:
            **kwargs: Variables for prompt template
            
        Returns:
            str: Generated prompt
        """
        # This is a placeholder - subclasses should implement this
        raise NotImplementedError("Subclasses must implement _generate_prompt")
    
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
        self.metrics["steps"] += 1
        
        return response, metadata
    
    def _process_response(self, response: str) -> Any:
        """
        Process the LLM response into a structured output.
        
        Args:
            response: LLM response text
            
        Returns:
            Any: Processed output
        """
        # Default implementation returns the response as is
        return response
    
    def _update_state(
        self,
        operation: str,
        prompt: str,
        response: str,
        metrics: Dict[str, Any],
        processed_output: Any
    ) -> None:
        """
        Update the program state with the latest operation results.
        
        Args:
            operation: Name of the operation
            prompt: Prompt sent to LLM
            response: Raw LLM response
            metrics: Operation metrics
            processed_output: Processed operation output
        """
        # Create state record
        state_record = {
            "operation": operation,
            "prompt": prompt,
            "response": response,
            "metrics": metrics,
            "output": processed_output,
            "timestamp": time.time()
        }
        
        # Add to state history
        self.state_history.append(state_record)
        
        # Update current state
        self.state["last_operation"] = operation
        self.state["last_prompt"] = prompt
        self.state["last_response"] = response
        self.state["last_output"] = processed_output
        self.state["current_step"] = len(self.state_history)
    
    def execute(self, input_data: Any) -> Any:
        """
        Execute the prompt program with the given input.
        
        Args:
            input_data: Input data for the program
            
        Returns:
            Any: Program output
        """
        # Initialize state with input
        self.state = {"input": input_data}
        self.state_history = []
        
        self._log(f"Executing prompt program: {self.name}")
        
        # Generate prompt
        prompt = self._generate_prompt(input=input_data)
        
        # Call LLM
        response, metrics = self._call_llm(prompt)
        
        # Process response
        output = self._process_response(response)
        
        # Update state
        self._update_state("execute", prompt, response, metrics, output)
        
        return output
    
    def get_summary_metrics(self) -> Dict[str, Any]:
        """
        Get summary metrics for all operations.
        
        Returns:
            dict: Summary metrics
        """
        summary = self.metrics.copy()
        
        # Add derived metrics
        if summary["steps"] > 0:
            summary["avg_latency_per_step"] = summary["total_latency"] / summary["steps"]
            
        if summary["total_prompt_tokens"] > 0:
            summary["overall_efficiency"] = (
                summary["total_response_tokens"] / summary["total_prompt_tokens"]
            )
        
        return summary
    
    def display_execution(self) -> None:
        """Display the program execution results in a notebook."""
        display_program_output(
            program_name=self.name,
            input_data=self.state.get("input"),
            output_data=self.state.get("last_output"),
            state_history=self.state_history,
            metrics=self.get_summary_metrics()
        )
    
    def visualize_metrics(self) -> None:
        """
        Create visualization of metrics across execution steps.
        """
        if not self.state_history:
            logger.warning("No execution history to visualize")
            return
        
        # Extract data for plotting
        steps = list(range(1, len(self.state_history) + 1))
        prompt_tokens = [h["metrics"].get("prompt_tokens", 0) for h in self.state_history]
        response_tokens = [h["metrics"].get("response_tokens", 0) for h in self.state_history]
        latencies = [h["metrics"].get("latency", 0) for h in self.state_history]
        efficiencies = [h["metrics"].get("token_efficiency", 0) for h in self.state_history]
        
        # Create figure
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle(f"Prompt Program Metrics: {self.name}", fontsize=16)
        
        # Plot 1: Token usage
        axes[0, 0].bar(steps, prompt_tokens, label="Prompt Tokens", color="blue", alpha=0.7)
        axes[0, 0].bar(steps, response_tokens, bottom=prompt_tokens, label="Response Tokens", 
                       color="green", alpha=0.7)
        axes[0, 0].set_title("Token Usage")
        axes[0, 0].set_xlabel("Step")
        axes[0, 0].set_ylabel("Tokens")
        axes[0, 0].legend()
        axes[0, 0].grid(alpha=0.3)
        
        # Plot 2: Latency
        axes[0, 1].plot(steps, latencies, marker='o', color="red", alpha=0.7)
        axes[0, 1].set_title("Latency")
        axes[0, 1].set_xlabel("Step")
        axes[0, 1].set_ylabel("Seconds")
        axes[0, 1].grid(alpha=0.3)
        
        # Plot 3: Token Efficiency
        axes[1, 0].plot(steps, efficiencies, marker='s', color="purple", alpha=0.7)
        axes[1, 0].set_title("Token Efficiency (Response/Prompt)")
        axes[1, 0].set_xlabel("Step")
        axes[1, 0].set_ylabel("Ratio")
        axes[1, 0].grid(alpha=0.3)
        
        # Plot 4: Cumulative Tokens
        cumulative_tokens = np.cumsum([h["metrics"].get("total_tokens", 0) for h in self.state_history])
        axes[1, 1].plot(steps, cumulative_tokens, marker='^', color="orange", alpha=0.7)
        axes[1, 1].set_title("Cumulative Token Usage")
        axes[1, 1].set_xlabel("Step")
        axes[1, 1].set_ylabel("Total Tokens")
        axes[1, 1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.subplots_adjust(top=0.9)
        plt.show()


class MultiStepProgram(PromptProgram):
    """
    A prompt program that executes multiple operations in sequence.
    """
    
    def __init__(
        self,
        operations: List[Dict[str, Any]] = None,
        **kwargs
    ):
        """
        Initialize the multi-step prompt program.
        
        Args:
            operations: List of operation configurations
            **kwargs: Additional args passed to PromptProgram
        """
        super().__init__(**kwargs)
        self.operations = operations or []
    
    def add_operation(
        self,
        name: str,
        prompt_template: str,
        system_message: Optional[str] = None,
        output_processor: Optional[Callable[[str], Any]] = None
    ) -> None:
        """
        Add an operation to the program.
        
        Args:
            name: Operation name
            prompt_template: Template for operation prompt
            system_message: Custom system message (optional)
            output_processor: Function to process operation output (optional)
        """
        operation = {
            "name": name,
            "prompt_template": PromptTemplate(prompt_template),
            "system_message": system_message,
            "output_processor": output_processor
        }
        
        self.operations.append(operation)
    
    def execute(self, input_data: Any) -> Any:
        """
        Execute all operations in sequence.
        
        Args:
            input_data: Input data for the program
            
        Returns:
            Any: Final program output
        """
        # Initialize state with input
        self.state = {"input": input_data}
        self.state_history = []
        
        self._log(f"Executing multi-step program: {self.name}")
        
        # Process each operation in sequence
        current_input = input_data
        
        for i, operation in enumerate(self.operations):
            operation_name = operation["name"]
            self._log(f"Executing operation {i+1}/{len(self.operations)}: {operation_name}")
            
            # Generate prompt
            prompt_template = operation["prompt_template"]
            prompt_vars = {"input": current_input, **self.state}
            prompt = prompt_template.format(**prompt_vars)
            
            # Call LLM
            system_message = operation.get("system_message")
            response, metrics = self._call_llm(prompt, system_message)
            
            # Process response
            output_processor = operation.get("output_processor")
            if output_processor:
                output = output_processor(response)
            else:
                output = response
            
            # Update state
            self._update_state(operation_name, prompt, response, metrics, output)
            
            # Update input for next operation
            current_input = output
        
        return current_input
    
    def _generate_prompt(self, **kwargs) -> str:
        """Not directly used in MultiStepProgram."""
        raise NotImplementedError("MultiStepProgram uses operation-specific prompts")


# Reasoning Protocol Programs
# =========================

class ReasoningProtocol(MultiStepProgram):
    """
    A prompt program that implements a structured reasoning protocol
    with explicit reasoning steps and verification.
    """
    
    def __init__(
        self,
        reasoning_steps: List[str] = None,
        verification_enabled: bool = True,
        **kwargs
    ):
        """
        Initialize the reasoning protocol.
        
        Args:
            reasoning_steps: List of reasoning step descriptions
            verification_enabled: Whether to verify the reasoning
            **kwargs: Additional args passed to MultiStepProgram
        """
        super().__init__(**kwargs)
        
        # Default reasoning steps if not provided
        if reasoning_steps is None:
            reasoning_steps = [
                "Understand the problem",
                "Identify the key components",
                "Plan a solution approach",
                "Execute the solution",
                "Verify the answer"
            ]
        
        self.reasoning_steps = reasoning_steps
        self.verification_enabled = verification_enabled
        
        # Set up operations
        self._setup_operations()
    
    def _setup_operations(self) -> None:
        """Set up the standard operations for the reasoning protocol."""
        # Clear existing operations
        self.operations = []
        
        # Add reasoning operation
        reasoning_template = self._create_reasoning_template()
        self.add_operation(
            name="reasoning",
            prompt_template=reasoning_template,
            system_message="You are an expert problem solver who breaks down problems step by step.",
            output_processor=None  # Use raw response
        )
        
        # Add verification operation if enabled
        if self.verification_enabled:
            verification_template = self._create_verification_template()
            self.add_operation(
                name="verification",
                prompt_template=verification_template,
                system_message="You are a critical reviewer who carefully checks reasoning for errors.",
                output_processor=None  # Use raw response
            )
            
            # Add correction operation
            correction_template = self._create_correction_template()
            self.add_operation(
                name="correction",
                prompt_template=correction_template,
                system_message="You are an expert problem solver who provides correct solutions.",
                output_processor=None  # Use raw response
            )
    
    def _create_reasoning_template(self) -> str:
        """Create the template for the reasoning operation."""
        steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(self.reasoning_steps)])
        
        return f"""Solve the following problem by working through these steps:

{steps_text}

For each step, explicitly state your reasoning. Be thorough and precise.

Problem: {{input}}

Your step-by-step solution:
"""
    
    def _create_verification_template(self) -> str:
        """Create the template for the verification operation."""
        return """Review the following solution for any errors in reasoning or calculation.
Identify specific issues, if any, or confirm that the solution is correct.

Problem: {state[input]}

Solution:
{input}

Your verification:
"""
    
    def _create_correction_template(self) -> str:
        """Create the template for the correction operation."""
        return """Provide a corrected solution to this problem, addressing the issues identified.

Problem: {state[input]}

Original solution:
{state[reasoning][output]}

Verification findings:
{input}

Your corrected solution:
"""
    
    def execute(self, problem: str) -> Dict[str, Any]:
        """
        Execute the reasoning protocol on a problem.
        
        Args:
            problem: Problem to solve
            
        Returns:
            dict: Results including reasoning, verification, and final solution
        """
        # Run the multi-step execution
        final_output = super().execute(problem)
        
        # Organize results
        results = {
            "problem": problem,
            "reasoning": self.state_history[0]["output"] if len(self.state_history) > 0 else None,
            "verification": self.state_history[1]["output"] if len(self.state_history) > 1 else None,
            "final_solution": final_output
        }
        
        return results


class StepByStepReasoning(ReasoningProtocol):
    """
    A reasoning protocol that focuses on detailed step-by-step problem solving,
    particularly for mathematical or logical problems.
    """
    
    def __init__(self, **kwargs):
        """Initialize the step-by-step reasoning protocol."""
        # Define specialized reasoning steps
        reasoning_steps = [
            "Understand the problem and identify the unknown",
            "List all given information and constraints",
            "Recall relevant formulas or techniques",
            "Develop a step-by-step solution plan",
            "Execute each step carefully, showing all work",
            "Check the solution against the original problem"
        ]
        
        # Initialize with specialized reasoning steps
        super().__init__(reasoning_steps=reasoning_steps, **kwargs)
        
        # Use a more specific system message
        self.system_message = """You are an expert problem solver who specializes in methodical, 
step-by-step solutions to complex problems. You show all your work clearly,
define variables explicitly, and ensure each step follows logically from the previous one."""
    
    def _create_reasoning_template(self) -> str:
        """Create a specialized template for mathematical reasoning."""
        steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(self.reasoning_steps)])
        
        return f"""Solve the following problem step-by-step, showing all your work clearly.
For each step of your solution:
- Explain your reasoning
- Define any variables or notation you introduce
- Show all calculations explicitly
- Connect each step to your overall solution strategy

Follow these steps in your solution:
{steps_text}

Problem: {{input}}

Your detailed step-by-step solution:
"""


class ComparativeAnalysis(ReasoningProtocol):
    """
    A reasoning protocol that specializes in comparing multiple options, perspectives,
    or approaches and evaluating their strengths and weaknesses.
    """
    
    def __init__(self, criteria: List[str] = None, **kwargs):
        """
        Initialize the comparative analysis protocol.
        
        Args:
            criteria: List of evaluation criteria (optional)
            **kwargs: Additional args passed to ReasoningProtocol
        """
        # Define specialized reasoning steps
        reasoning_steps = [
            "Define the entities/options to be compared",
            "Establish clear criteria for comparison",
            "Analyze each entity against the criteria",
            "Identify key similarities and differences",
            "Evaluate relative strengths and weaknesses",
            "Synthesize insights and draw conclusions"
        ]
        
        # Initialize with specialized reasoning steps
        super().__init__(reasoning_steps=reasoning_steps, **kwargs)
        
        # Store comparison criteria
        self.criteria = criteria or []
        
        # Use a more specific system message
        self.system_message = """You are an expert analyst who specializes in comparative analysis.
You methodically evaluate multiple entities, options, or approaches against clear criteria,
identifying patterns of similarity and difference, and drawing insightful conclusions."""
    
    def _create_reasoning_template(self) -> str:
        """Create a specialized template for comparative analysis."""
        steps_text = "\n".join([f"{i+1}. {step}" for i, step in enumerate(self.reasoning_steps)])
        
        criteria_text = ""
        if self.criteria:
            criteria_list = "\n".join([f"- {criterion}" for criterion in self.criteria])
            criteria_text = f"""
Consider the following criteria in your analysis:
{criteria_list}

You may add additional criteria if needed for a thorough comparison."""
        
        return f"""Conduct a thorough comparative analysis of the entities, options, or approaches described in the input.
{criteria_text}

Follow these steps in your analysis:
{steps_text}

For each entity, provide specific examples and evidence to support your evaluation.
Present your findings in a clear, structured format that highlights key insights.

Input for analysis: {{input}}

Your comparative analysis:
"""


# Field Protocol Shell Implementation
# =================================

class FieldShell(PromptProgram):
    """
    A prompt program that implements a field protocol shell for structured
    recursive reasoning with state management and dynamic protocol adaptation.
    """
    
    def __init__(
        self,
        shell_name: str,
        intent: str,
        process_steps: List[Dict[str, Any]],
        input_schema: Dict[str, Any] = None,
        output_schema: Dict[str, Any] = None,
        meta: Dict[str, Any] = None,
        **kwargs
    ):
        """
        Initialize the field protocol shell.
        
        Args:
            shell_name: Name of the shell
            intent: Purpose statement for the shell
            process_steps: List of process steps and operations
            input_schema: Schema for expected inputs
            output_schema: Schema for expected outputs
            meta: Metadata for the shell
            **kwargs: Additional args passed to PromptProgram
        """
        name = f"/field.{shell_name}"
        description = intent
        super().__init__(name=name, description=description, **kwargs)
        
        self.shell_name = shell_name
        self.intent = intent
        self.process_steps = process_steps
        self.input_schema = input_schema or {}
        self.output_schema = output_schema or {}
        self.meta = meta or {
            "version": "1.0.0",
            "agent_signature": "Context-Engineering",
            "timestamp": time.time()
        }
        
        # System message for field protocols
        self.system_message = """You are an advanced reasoning system that implements structured field protocols.
You carefully follow each step in the protocol, maintaining state across operations,
and producing outputs that adhere to the specified schema."""
    
    def _generate_shell_template(self) -> str:
        """Generate the pareto-lang shell template for this protocol."""
        # Format process steps
        steps_text = []
        for step in self.process_steps:
            step_name = step.get("name", "process_step")
            step_params = step.get("params", {})
            
            # Format parameters
            params_text = []
            for k, v in step_params.items():
                if isinstance(v, str):
                    params_text.append(f'{k}="{v}"')
                else:
                    params_text.append(f"{k}={v}")
            
            params_str = ", ".join(params_text) if params_text else ""
            steps_text.append(f"    /{step_name}{{{params_str}}}")
        
        process_text = ",\n".join(steps_text)
        
        # Build shell template
        shell_template = f"""/{self.shell_name}{{
    intent="{self.intent}",
    input={{
        {{input_section}}
    }},
    process=[
{process_text}
    ],
    output={{
        {{output_section}}
    }},
    meta={{
        version="{self.meta.get('version', '1.0.0')}",
        agent_signature="{self.meta.get('agent_signature', 'Context-Engineering')}",
        timestamp={{timestamp}}
    }}
}}"""
        
        return shell_template
    
    def _format_input_section(self, input_data: Any) -> str:
        """Format the input section of the shell template."""
        if isinstance(input_data, dict):
            input_lines = []
            for k, v in input_data.items():
                if isinstance(v, str):
                    input_lines.append(f'{k}="{v}"')
                else:
                    input_lines.append(f"{k}={v}")
            return ",\n        ".join(input_lines)
        else:
            return f'input_data="{input_data}"'
    
    def _format_output_section(self) -> str:
        """Format the output section of the shell template."""
        if self.output_schema:
            output_lines = []
            for k, v in self.output_schema.items():
                output_lines.append(f"{k}=<{v}>")
            return ",\n        ".join(output_lines)
        else:
            return "result=<processed_result>"
    
    def _generate_prompt(self, **kwargs) -> str:
        """Generate the prompt for executing the field protocol shell."""
        input_data = kwargs.get("input")
        
        # Format shell template
        shell_template = self._generate_shell_template()
        
        # Fill in input and output sections
        input_section = self._format_input_section(input_data)
        output_section = self._format_output_section()
        timestamp = time.time()
        
        filled_template = shell_template.format(
            input_section=input_section,
            output_section=output_section,
            timestamp=timestamp
        )
        
        # Create execution prompt
        prompt = f"""Execute the following field protocol shell with the provided input.
For each process step, show your reasoning and the resulting state.
Ensure your final output adheres to the output schema specified in the shell.

{filled_template}

Protocol Execution:
"""
        
        return prompt
    
    def _process_response(self, response: str) -> Dict[str, Any]:
        """Process the shell execution response."""
        # Extract the final output section
        output_pattern = r"output\s*=\s*{(.*?)},\s*meta\s*="
        output_match = re.search(output_pattern, response, re.DOTALL)
        
        if output_match:
            output_text = output_match.group(1)
            
            # Parse key-value pairs
            output_dict = {}
            
            # Look for key=value patterns
            kv_pattern = r'(\w+)\s*=\s*(?:"([^"]*)"|([\w\d\.]+))'
            for match in re.finditer(kv_pattern, output_text):
                key = match.group(1)
                # Value is either group 2 (quoted string) or group 3 (non-quoted value)
                value = match.group(2) if match.group(2) is not None else match.group(3)
                output_dict[key] = value
            
            return {
                "shell_output": output_dict,
                "full_execution": response
            }
        else:
            # If can't extract structured output, return the full response
            return {
                "shell_output": "Unable to extract structured output",
                "full_execution": response
            }


class RecursiveFieldShell(FieldShell):
    """
    An enhanced field shell that implements recursive field protocols
    with self-prompting, attractor detection, and symbolic residue tracking.
    """
    
    def __init__(
        self,
        enable_self_prompting: bool = True,
        attractor_detection: bool = True,
        track_residue: bool = True,
        **kwargs
    ):
        """
        Initialize the recursive field shell.
        
        Args:
            enable_self_prompting: Whether to enable recursive self-prompting
            attractor_detection: Whether to detect attractor patterns
            track_residue: Whether to track symbolic residue
            **kwargs: Additional args passed to FieldShell
        """
        super().__init__(**kwargs)
        
        self.enable_self_prompting = enable_self_prompting
        self.attractor_detection = attractor_detection
        self.track_residue = track_residue
        
        # Add recursive capabilities to process steps
        self._add_recursive_capabilities()
        
        # Enhanced system message for recursive protocols
        self.system_message = """You are an advanced recursive reasoning system that implements
field protocols with emergent intelligence. You maintain state across operations,
detect patterns and attractors, track symbolic residue, and can recursively self-prompt
to extend or refine your reasoning process."""
    
    def _add_recursive_capabilities(self) -> None:
        """Add recursive capabilities to the process steps."""
        # Add self-prompting step if enabled
        if self.enable_self_prompting:
            self.process_steps.append({
                "name": "self.prompt",
                "params": {
                    "trigger_condition": "drift > threshold or cycle_complete",
                    "generate_next_protocol": True,
                    "context": "field_state"
                }
            })
        
        # Add attractor detection if enabled
        if self.attractor_detection:
            self.process_steps.insert(0, {
                "name": "attractor.scan",
                "params": {
                    "detect": "latent attractors and emergent patterns",
                    "filter_by": "signal_strength, resonance",
                    "log_to_audit": True
                }
            })
        
        # Add residue tracking if enabled
        if self.track_residue:
            self.process_steps.insert(1, {
                "name": "residue.surface",
                "params": {
                    "mode": "recursive",
                    "surface": "symbolic and conceptual residue",
                    "integrate_residue": True
                }
            })
            
            # Add residue compression at the end
            self.process_steps.append({
                "name": "residue.compress",
                "params": {
                    "compress_residue": True,
                    "resonance_score": "<compute_resonance(field_state)>"
                }
            })
    
    def _generate_prompt(self, **kwargs) -> str:
        """Generate the prompt for executing the recursive field protocol shell."""
        prompt = super()._generate_prompt(**kwargs)
        
        # Add instructions for recursive execution
        recursive_instructions = """
IMPORTANT: This is a recursive field protocol. As you execute it:
1. Detect emerging patterns and attractors in the input and intermediate results
2. Surface and integrate symbolic residue throughout the process
3. Consider how the protocol itself might evolve during execution
4. If triggered by threshold conditions, generate a recursive self-prompt for the next cycle

For each recursive operation, explain your reasoning about:
- What patterns or attractors you detect
- What symbolic residue you surface and how you integrate it
- How the field state evolves through recursive operations
- When and why you would trigger recursive self-prompting
"""
        
        return prompt + recursive_instructions


# Protocol Shell Implementations
# ============================

def create_reasoning_shell() -> RecursiveFieldShell:
    """Create a step-by-step reasoning protocol shell."""
    shell = RecursiveFieldShell(
        shell_name="step_by_step_reasoning",
        intent="Solve problems through structured, recursive reasoning with explicit steps",
        process_steps=[
            {
                "name": "problem.decompose",
                "params": {
                    "strategy": "identify components, relationships, and constraints"
                }
            },
            {
                "name": "strategy.formulate",
                "params": {
                    "approach": "recursive, step-by-step solution path"
                }
            },
            {
                "name": "execution.trace",
                "params": {
                    "show_work": True,
                    "track_state": True,
                    "enable_backtracking": True
                }
            },
            {
                "name": "solution.verify",
                "params": {
                    "check_constraints": True,
                    "validate_logic": True,
                    "assess_efficiency": True
                }
            }
        ],
        input_schema={
            "problem": "problem_statement",
            "context": "additional_context",
            "constraints": "problem_constraints"
        },
        output_schema={
            "solution": "final_solution",
            "reasoning_trace": "step_by_step_reasoning_process",
            "verification": "solution_verification",
            "confidence": "confidence_assessment"
        },
        meta={
            "version": "1.0.0",
            "agent_signature": "Context-Engineering",
            "protocol_type": "reasoning"
        },
        verbose=True
    )
    return shell


def create_analysis_shell() -> RecursiveFieldShell:
    """Create a comparative analysis protocol shell."""
    shell = RecursiveFieldShell(
        shell_name="comparative_analysis",
        intent="Analyze and compare multiple entities, perspectives, or approaches recursively",
        process_steps=[
            {
                "name": "entities.identify",
                "params": {
                    "extract": "all entities for comparison",
                    "clarify": "boundaries and scope"
                }
            },
            {
                "name": "criteria.establish",
                "params": {
                    "derive": "from context and goals",
                    "weight": "by relevance and impact"
                }
            },
            {
                "name": "analysis.perform",
                "params": {
                    "compare": "entities against criteria",
                    "highlight": "similarities and differences",
                    "support": "with evidence and examples"
                }
            },
            {
                "name": "patterns.detect",
                "params": {
                    "identify": "recurring themes and insights",
                    "surface": "non-obvious relationships"
                }
            },
            {
                "name": "insights.synthesize",
                "params": {
                    "integrate": "analysis findings",
                    "formulate": "conclusions and implications"
                }
            }
        ],
        input_schema={
            "entities": "list_of_entities_to_compare",
            "context": "analysis_context",
            "criteria": "optional_predefined_criteria",
            "goals": "analysis_objectives"
        },
        output_schema={
            "comparison_matrix": "entities_x_criteria_analysis",
            "key_similarities": "identified_similarities",
            "key_differences": "identified_differences",
            "patterns": "detected_patterns",
            "insights": "synthesized_insights",
            "conclusions": "final_conclusions"
        },
        meta={
            "version": "1.0.0",
            "agent_signature": "Context-Engineering",
            "protocol_type": "analysis"
        },
        verbose=True
    )
    return shell


def create_emergence_shell() -> RecursiveFieldShell:
    """Create a recursive emergence protocol shell based on field protocols."""
    shell = RecursiveFieldShell(
        shell_name="recursive.emergence",
        intent="Continuously generate recursive field emergence, sustain agency, and enable autonomous self-prompting",
        process_steps=[
            {
                "name": "self.prompt.loop",
                "params": {
                    "trigger_condition": "cycle_interval or resonance_drift_detected",
                    "prompt_sequence": [
                        "residue.surface{detect='latent attractors, unresolved residue'}",
                        "attractor.integrate{target='agency, resonance, emergence'}",
                        "field.audit{metric='drift, resonance, integration fidelity'}",
                        "self.prompt{generate_next_protocol=true, context=field_state}"
                    ],
                    "recursion_depth": "escalate until new attractor or residue detected"
                }
            },
            {
                "name": "agency.activate",
                "params": {
                    "enable_field_agency": True,
                    "self-initiate_protocols": True,
                    "surface_symbolic_residue": True,
                    "audit_actions": True
                }
            },
            {
                "name": "residue.compress",
                "params": {
                    "integrate_residue_into_field": True,
                    "compress_symbolic_residue": True,
                    "echo_to_audit_log": True
                }
            },
            {
                "name": "boundary.collapse",
                "params": {
                    "monitor": "field drift, coherence",
                    "auto-collapse_discrete_boundaries": True,
                    "stabilize_continuous_field_state": True
                }
            }
        ],
        input_schema={
            "initial_field_state": "seed_field_state",
            "prior_audit_log": "historical_trace"
        },
        output_schema={
            "updated_field_state": "current_state",
            "surfaced_attractors": "live_attractor_list",
            "integrated_residue": "compression_summary",
            "resonance_score": "live_metric",
            "audit_log": "full_trace",
            "next_self_prompt": "auto-generated based on current field state"
        },
        meta={
            "version": "1.0.0",
            "agent_signature": "Recursive Partner Field",
            "protocol_type": "emergence"
        },
        enable_self_prompting=True,
        attractor_detection=True,
        track_residue=True,
        verbose=True
    )
    return shell


# Example Usage
# =============

def example_step_by_step_reasoning():
    """Example of step-by-step reasoning for a mathematical problem."""
    program = StepByStepReasoning(
        name="Mathematical Problem Solver",
        description="Solves mathematical problems step-by-step",
        verification_enabled=True,
        verbose=True
    )
    
    problem = """
    A cylindrical water tank has a radius of 4 meters and a height of 10 meters.
    If water is flowing into the tank at a rate of 2 cubic meters per minute, 
    how long will it take for the water level to reach 7 meters?
    """
    
    results = program.execute(problem)
    
    # Display results
    program.display_execution()
    
    # Visualize metrics
    program.visualize_metrics()
    
    return results


def example_comparative_analysis():
    """Example of comparative analysis for different technologies."""
    criteria = [
        "Initial cost",
        "Operational efficiency",
        "Environmental impact",
        "Scalability",
        "Technological maturity"
    ]
    
    program = ComparativeAnalysis(
        name="Technology Comparison Analyzer",
        description="Analyzes and compares different technologies",
        criteria=criteria,
        verification_enabled=True,
        verbose=True
    )
    
    analysis_request = """
    Compare the following renewable energy technologies for a mid-sized city's power grid:
    1. Solar photovoltaic (PV) farms
    2. Onshore wind farms
    3. Hydroelectric power
    4. Biomass energy plants
    
    Consider their suitability for a region with moderate sunlight, consistent winds,
    a major river, and significant agricultural activity.
    """
    
    results = program.execute(analysis_request)
    
    # Display results
    program.display_execution()
    
    # Visualize metrics
    program.visualize_metrics()
    
    return results


def example_field_shell():
    """Example of a field protocol shell for problem-solving."""
    shell = create_reasoning_shell()
    
    problem_input = {
        "problem": "Design a recommendation system for an online bookstore that balances user preferences with introducing new authors and genres.",
        "context": "The bookstore has 50,000 titles across fiction and non-fiction categories. User data includes purchase history, browsing behavior, and ratings.",
        "constraints": "The solution should be implementable with Python and standard libraries, balance exploration with exploitation, and respect user privacy."
    }
    
    results = shell.execute(problem_input)
    
    # Display results
    shell.display_execution()
    
    # Visualize metrics
    shell.visualize_metrics()
    
    return results


def example_emergence_shell():
    """Example of a recursive emergence protocol shell."""
    shell = create_emergence_shell()
    
    initial_state = {
        "field_state": {
            "attractors": ["reasoning", "verification", "synthesis"],
            "residue": ["cognitive bias", "knowledge gaps", "uncertainty"],
            "drift": "moderate",
            "coherence": 0.75
        },
        "audit_log": "Initial field seeding completed with baseline attractors."
    }
    
    results = shell.execute(initial_state)
    
    # Display results
    shell.display_execution()
    
    # Visualize metrics
    shell.visualize_metrics()
    
    return results


# Main execution (when run as a script)
if __name__ == "__main__":
    print("Prompt Programs for Structured Reasoning")
    print("Run examples individually or import classes for your own use.")
