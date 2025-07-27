"""
Prompt Program Template
----------------------

This template provides a structured framework for creating prompt programs -
code-like structures for guiding LLM reasoning through explicit, step-by-step
instructions. Prompt programs combine the flexibility of natural language
with the rigor of programming constructs.

Key features:
1. Modular prompt components that can be composed
2. Control flow constructs (if/else, loops)
3. Variable management for context tracking
4. Explicit reasoning steps
5. Error handling and fallback logic
6. Integration with neural fields for persistence

Usage:
    # Create a basic prompt program
    program = PromptProgram("Solve mathematical word problems step by step")
    
    # Add reasoning steps
    program.add_step("Parse the problem to identify variables and relationships")
    program.add_step("Set up the appropriate equations")
    program.add_step("Solve for the unknown variables")
    program.add_step("Verify the solution makes sense in the original context")
    
    # Execute the program
    result = program.execute("If a train travels at 60 mph for 2.5 hours, how far does it go?")
"""

import re
import json
import time
import logging
from typing import Dict, List, Any, Optional, Union, Callable, Tuple
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("prompt_program")

# ------------------------------------------------------------------------------
# Prompt Program Components
# ------------------------------------------------------------------------------

class StepType(Enum):
    """Types of steps in a prompt program."""
    INSTRUCTION = "instruction"  # Basic instruction step
    CONDITION = "condition"      # Conditional branch
    LOOP = "loop"                # Iteration
    VARIABLE = "variable"        # Variable assignment
    FUNCTION = "function"        # Function call
    ERROR = "error"              # Error handling

class ProgramStep:
    """A single step in a prompt program."""
    
    def __init__(self, 
                 content: str, 
                 step_type: StepType = StepType.INSTRUCTION,
                 metadata: Optional[Dict[str, Any]] = None):
        """
        Initialize a program step.
        
        Args:
            content: The content of the step
            step_type: The type of step
            metadata: Additional metadata for the step
        """
        self.content = content
        self.step_type = step_type
        self.metadata = metadata or {}
        self.substeps: List[ProgramStep] = []
    
    def add_substep(self, substep: 'ProgramStep') -> None:
        """Add a substep to this step."""
        self.substeps.append(substep)
    
    def format(self, index: Optional[int] = None, indent: int = 0) -> str:
        """Format the step as a string."""
        # Base indentation
        indent_str = "  " * indent
        
        # Step header
        if index is not None:
            header = f"{indent_str}{index}. "
        else:
            header = f"{indent_str}- "
        
        # Format based on step type
        if self.step_type == StepType.INSTRUCTION:
            formatted = f"{header}{self.content}"
        elif self.step_type == StepType.CONDITION:
            condition = self.metadata.get("condition", "IF condition")
            formatted = f"{header}IF {condition}:"
        elif self.step_type == StepType.LOOP:
            loop_var = self.metadata.get("variable", "item")
            loop_iterable = self.metadata.get("iterable", "items")
            formatted = f"{header}FOR EACH {loop_var} IN {loop_iterable}:"
        elif self.step_type == StepType.VARIABLE:
            var_name = self.metadata.get("name", "variable")
            formatted = f"{header}SET {var_name} = {self.content}"
        elif self.step_type == StepType.FUNCTION:
            func_name = self.metadata.get("name", "function")
            formatted = f"{header}CALL {func_name}({self.content})"
        elif self.step_type == StepType.ERROR:
            formatted = f"{header}ON ERROR: {self.content}"
        else:
            formatted = f"{header}{self.content}"
        
        # Add substeps
        if self.substeps:
            substep_str = "\n".join(
                substep.format(i+1, indent+1) 
                for i, substep in enumerate(self.substeps)
            )
            formatted = f"{formatted}\n{substep_str}"
        
        return formatted

class PromptProgram:
    """
    A structured program for guiding LLM reasoning.
    Combines natural language with programming constructs.
    """
    
    def __init__(self, 
                 description: str,
                 model: Optional[Any] = None,
                 variables: Optional[Dict[str, Any]] = None,
                 neural_field: Optional[Any] = None):
        """
        Initialize a prompt program.
        
        Args:
            description: Description of the program's purpose
            model: Language model interface (optional)
            variables: Initial variables (optional)
            neural_field: Neural field for context persistence (optional)
        """
        self.description = description
        self.model = model
        self.variables = variables or {}
        self.neural_field = neural_field
        
        self.steps: List[ProgramStep] = []
        self.error_handlers: List[ProgramStep] = []
        
        # Execution state
        self.current_step: int = 0
        self.execution_trace: List[Dict[str, Any]] = []
    
    def add_step(self, content: str, step_type: StepType = StepType.INSTRUCTION, 
                metadata: Optional[Dict[str, Any]] = None) -> ProgramStep:
        """
        Add a step to the program.
        
        Args:
            content: The content of the step
            step_type: The type of step
            metadata: Additional metadata for the step
            
        Returns:
            The created step
        """
        step = ProgramStep(content, step_type, metadata)
        self.steps.append(step)
        return step
    
    def add_condition(self, condition: str, true_step: str, 
                     false_step: Optional[str] = None) -> Tuple[ProgramStep, ProgramStep, Optional[ProgramStep]]:
        """
        Add a conditional branch to the program.
        
        Args:
            condition: The condition to evaluate
            true_step: The step to execute if condition is true
            false_step: The step to execute if condition is false (optional)
            
        Returns:
            Tuple of (condition_step, true_step, false_step)
        """
        # Create condition step
        condition_step = self.add_step(condition, StepType.CONDITION, {"condition": condition})
        
        # Create true branch
        true_branch = ProgramStep(true_step, StepType.INSTRUCTION)
        condition_step.add_substep(true_branch)
        
        # Create false branch if provided
        false_branch = None
        if false_step:
            false_branch = ProgramStep(false_step, StepType.INSTRUCTION)
            condition_step.add_substep(false_branch)
        
        return condition_step, true_branch, false_branch
    
    def add_loop(self, variable: str, iterable: str, 
                body: str) -> Tuple[ProgramStep, ProgramStep]:
        """
        Add a loop to the program.
        
        Args:
            variable: The loop variable name
            iterable: The iterable to loop over
            body: The loop body content
            
        Returns:
            Tuple of (loop_step, body_step)
        """
        # Create loop step
        loop_step = self.add_step(f"Loop over {iterable}", StepType.LOOP, 
                                 {"variable": variable, "iterable": iterable})
        
        # Create loop body
        body_step = ProgramStep(body, StepType.INSTRUCTION)
        loop_step.add_substep(body_step)
        
        return loop_step, body_step
    
    def add_variable(self, name: str, value: str) -> ProgramStep:
        """
        Add a variable assignment to the program.
        
        Args:
            name: The variable name
            value: The variable value or expression
            
        Returns:
            The created step
        """
        return self.add_step(value, StepType.VARIABLE, {"name": name})
    
    def add_function(self, name: str, params: str) -> ProgramStep:
        """
        Add a function call to the program.
        
        Args:
            name: The function name
            params: The function parameters
            
        Returns:
            The created step
        """
        return self.add_step(params, StepType.FUNCTION, {"name": name})
    
    def add_error_handler(self, handler: str) -> ProgramStep:
        """
        Add an error handler to the program.
        
        Args:
            handler: The error handling instruction
            
        Returns:
            The created step
        """
        step = ProgramStep(handler, StepType.ERROR)
        self.error_handlers.append(step)
        return step
    
    def format(self) -> str:
        """Format the program as a string for use in prompts."""
        # Program header
        parts = [
            f"# {self.description}",
            ""
        ]
        
        # Format steps
        if self.steps:
            parts.append("## Steps:")
            for i, step in enumerate(self.steps):
                parts.append(step.format(i+1))
        
        # Format error handlers
        if self.error_handlers:
            parts.append("")
            parts.append("## Error Handling:")
            for handler in self.error_handlers:
                parts.append(handler.format())
        
        # Format variables
        if self.variables:
            parts.append("")
            parts.append("## Initial Context:")
            for name, value in self.variables.items():
                if isinstance(value, str):
                    parts.append(f"- {name} = \"{value}\"")
                else:
                    parts.append(f"- {name} = {value}")
        
        return "\n".join(parts)
    
    def execute(self, input_data: str, max_tokens: int = 1000) -> str:
        """
        Execute the prompt program with the given input.
        
        Args:
            input_data: The input data for the program
            max_tokens: Maximum tokens for generation
            
        Returns:
            The execution result
        """
        if not self.model:
            raise ValueError("No model provided for execution")
        
        # Reset execution state
        self.current_step = 0
        self.execution_trace = []
        
        # Format program
        program_str = self.format()
        
        # Inject into neural field if available
        if self.neural_field:
            try:
                self.neural_field.inject(f"Prompt Program: {self.description}", strength=0.9)
                self.neural_field.inject(program_str, strength=0.8)
                
                # Inject input
                self.neural_field.inject(f"Input: {input_data}", strength=1.0)
                
                # Get field representation for context
                field_context = self.neural_field.get_context_representation()
                
                # Create execution prompt with field context
                prompt = f"""
{field_context}

# Input
{input_data}

# Program
{program_str}

# Execution
Please execute the above program step by step using the provided input.
For each step:
1. Show your reasoning
2. Show the result
3. Update any variables

After executing all steps, provide your final answer.
"""
            except (AttributeError, TypeError):
                logger.warning("Failed to use neural field, falling back to standard prompt")
                # Fall back to standard prompt
                prompt = self._create_standard_prompt(program_str, input_data)
        else:
            # Standard prompt without neural field
            prompt = self._create_standard_prompt(program_str, input_data)
        
        # Execute the program
        try:
            response = self.model.generate(prompt, max_tokens=max_tokens)
            
            # Record execution
            self.execution_trace.append({
                "timestamp": time.time(),
                "prompt": prompt,
                "response": response
            })
            
            # Update neural field if available
            if self.neural_field:
                try:
                    self.neural_field.inject(f"Execution Result: {response}", strength=0.7)
                except (AttributeError, TypeError):
                    pass
            
            return response
        except Exception as e:
            logger.error(f"Execution failed: {e}")
            
            # Try error handlers if available
            if self.error_handlers and hasattr(self.model, 'generate'):
                error_prompt = f"""
The program execution encountered an error: {str(e)}

Please apply the following error handling:
"""
                for handler in self.error_handlers:
                    error_prompt += f"\n- {handler.content}"
                
                error_prompt += f"\n\nInput: {input_data}"
                
                try:
                    return self.model.generate(error_prompt, max_tokens=max_tokens)
                except Exception as e2:
                    logger.error(f"Error handler failed: {e2}")
            
            return f"Execution failed: {str(e)}"
    
    def _create_standard_prompt(self, program_str: str, input_data: str) -> str:
        """Create a standard execution prompt."""
        return f"""
# Input
{input_data}

# Program
{program_str}

# Execution
Please execute the above program step by step using the provided input.
For each step:
1. Show your reasoning
2. Show the result
3. Update any variables

After executing all steps, provide your final answer.
"""
    
    def execute_with_trace(self, input_data: str, max_tokens: int = 1000) -> Dict[str, Any]:
        """
        Execute the program and return detailed execution trace.
        
        Args:
            input_data: Input data for the program
            max_tokens: Maximum tokens for generation
            
        Returns:
            Dictionary with execution results and trace
        """
        result = self.execute(input_data, max_tokens)
        
        # Parse execution trace from result
        steps_trace = self._parse_execution_trace(result)
        
        return {
            "input": input_data,
            "result": result,
            "steps_trace": steps_trace,
            "execution_trace": self.execution_trace
        }
    
    def _parse_execution_trace(self, result: str) -> List[Dict[str, Any]]:
        """Parse step-by-step execution trace from result."""
        steps = []
        
        # Look for numbered steps
        step_pattern = r'(?:Step|step) (\d+)[\s\.:]+(.+?)(?=(?:Step|step) \d+[\s\.:]+|$)'
        step_matches = re.findall(step_pattern, result, re.DOTALL)
        
        if step_matches:
            for step_num, step_content in step_matches:
                # Try to separate reasoning and result
                parts = re.split(r'(?:Result|result|Output|output)[\s\.:]+', step_content, 1)
                
                if len(parts) == 2:
                    reasoning, result_text = parts
                else:
                    reasoning = step_content
                    result_text = ""
                
                steps.append({
                    "step": int(step_num),
                    "reasoning": reasoning.strip(),
                    "result": result_text.strip()
                })
        else:
            # No clear step structure, just return the whole result
            steps.append({
                "step": 1,
                "reasoning": "Full execution",
                "result": result
            })
        
        return steps

# ------------------------------------------------------------------------------
# Neural Field Integration
# ------------------------------------------------------------------------------

class NeuralFieldProgram(PromptProgram):
    """Prompt program with enhanced neural field integration."""
    
    def __init__(self, 
                 description: str,
                 model: Optional[Any] = None,
                 variables: Optional[Dict[str, Any]] = None,
                 neural_field: Optional[Any] = None,
                 field_params: Optional[Dict[str, Any]] = None):
        """
        Initialize a neural field prompt program.
        
        Args:
            description: Description of the program's purpose
            model: Language model interface
            variables: Initial variables
            neural_field: Neural field for context persistence
            field_params: Neural field parameters
        """
        super().__init__(description, model, variables)
        
        # Set up neural field
        if neural_field:
            self.neural_field = neural_field
        elif field_params:
            # Import here to avoid circular import
            try:
                # Try to import from local module
                from .field_resonance_measure import ResidueEnhancedNeuralField
                self.neural_field = ResidueEnhancedNeuralField(**field_params)
            except (ImportError, AttributeError):
                try:
                    # Try as separate module
                    from field_resonance_measure import ResidueEnhancedNeuralField
                    self.neural_field = ResidueEnhancedNeuralField(**field_params)
                except (ImportError, AttributeError):
                    logger.warning("Could not import ResidueEnhancedNeuralField, using basic NeuralField")
                    self.neural_field = self._create_basic_neural_field(field_params)
        else:
            self.neural_field = None
    
    def _create_basic_neural_field(self, params: Dict[str, Any]) -> Any:
        """Create a basic neural field from parameters."""
        # Simple neural field implementation
        class BasicNeuralField:
            def __init__(self, decay_rate=0.05, boundary_permeability=0.8):
                self.state = {}
                self.attractors = {}
                self.decay_rate = decay_rate
                self.boundary_permeability = boundary_permeability
                self.history = []
            
            def inject(self, pattern, strength=1.0):
                # Apply boundary filtering
                effective_strength = strength * self.boundary_permeability
                
                # Update field state
                if pattern in self.state:
                    self.state[pattern] += effective_strength
                else:
                    self.state[pattern] = effective_strength
                
                # Record history
                self.history.append(("inject", pattern, effective_strength))
                
                return self
            
            def decay(self):
                # Apply decay to all patterns
                for pattern in list(self.state.keys()):
                    self.state[pattern] *= (1 - self.decay_rate)
                
                # Remove patterns that have decayed below threshold
                self.state = {k: v for k, v in self.state.items() if v > 0.01}
                
                return self
            
            def get_context_representation(self):
                parts = ["# Neural Field State"]
                
                # Add active patterns
                parts.append("## Active Patterns")
                for pattern, strength in sorted(self.state.items(), key=lambda x: x[1], reverse=True)[:5]:
                    short_pattern = (pattern[:50] + "...") if len(pattern) > 50 else pattern
                    parts.append(f"- ({strength:.2f}) {short_pattern}")
                
                return "\n".join(parts)
        
        return BasicNeuralField(
            decay_rate=params.get("decay_rate", 0.05),
            boundary_permeability=params.get("boundary_permeability", 0.8)
        )
    
    def add_resonance_step(self, description: str, patterns: List[str]) -> ProgramStep:
        """
        Add a step that resonates with specific patterns in the field.
        
        Args:
            description: Step description
            patterns: Patterns to resonate with
            
        Returns:
            The created step
        """
        step = self.add_step(description, StepType.INSTRUCTION)
        
        # Inject patterns into field
        if self.neural_field:
            for pattern in patterns:
                try:
                    self.neural_field.inject(pattern, strength=0.7)
                except (AttributeError, TypeError):
                    pass
        
        return step
    
    def add_attractor(self, pattern: str, strength: float = 1.0) -> None:
        """
        Add an attractor to the neural field.
        
        Args:
            pattern: The attractor pattern
            strength: The attractor strength
        """
        if not self.neural_field:
            return
            
        try:
            # Inject with high strength to form attractor
            self.neural_field.inject(pattern, strength=strength)
            
            # Explicitly form attractor if method exists
            if hasattr(self.neural_field, "_form_attractor"):
                self.neural_field._form_attractor(pattern)
            elif hasattr(self.neural_field, "attractors"):
                attractor_id = f"attractor_{len(self.neural_field.attractors)}"
                self.neural_field.attractors[attractor_id] = {
                    "pattern": pattern,
                    "strength": strength
                }
        except (AttributeError, TypeError) as e:
            logger.warning(f"Failed to add attractor: {e}")
    
    def execute(self, input_data: str, max_tokens: int = 1000) -> str:
        """
        Execute the neural field program with the given input.
        
        Args:
            input_data: The input data for the program
            max_tokens: Maximum tokens for generation
            
        Returns:
            The execution result
        """
        # Apply field decay before execution
        if self.neural_field:
            try:
                self.neural_field.decay()
            except (AttributeError, TypeError):
                pass
        
        # Execute program
        result = super().execute(input_data, max_tokens)
        
        # Measure field properties after execution
        if self.neural_field:
            try:
                # Try to get field metrics
                field_metrics = self._measure_field_metrics()
                
                # Log metrics
                logger.info(f"Field metrics after execution: {field_metrics}")
                
                # Save metrics in execution trace
                if self.execution_trace:
                    self.execution_trace[-1]["field_metrics"] = field_metrics
            except (AttributeError, TypeError) as e:
                logger.warning(f"Failed to measure field metrics: {e}")
        
        return result
    
    def _measure_field_metrics(self) -> Dict[str, float]:
        """Measure neural field metrics."""
        metrics = {}
        
        # Try different field measurement approaches
        try:
            # Try to use field's built-in measurement
            if hasattr(self.neural_field, "measure_field_stability"):
                metrics["stability"] = self.neural_field.measure_field_stability()
            
            # Count attractors
            if hasattr(self.neural_field, "attractors"):
                metrics["attractor_count"] = len(self.neural_field.attractors)
            
            # Count patterns
            if hasattr(self.neural_field, "state"):
                metrics["pattern_count"] = len(self.neural_field.state)
            
            # Try to import resonance measurer
            try:
                from field_resonance_measure import FieldResonanceMeasurer
                measurer = FieldResonanceMeasurer()
                
                # Get comprehensive metrics
                field_metrics = measurer.get_field_metrics(self.neural_field)
                metrics.update(field_metrics)
            except (ImportError, AttributeError):
                pass
                
        except Exception as e:
            logger.warning(f"Error measuring field metrics: {e}")
        
        return metrics

# ------------------------------------------------------------------------------
# Protocol Shell Integration
# ------------------------------------------------------------------------------

class ProtocolShellProgram(PromptProgram):
    """Prompt program with protocol shell integration."""
    
    def __init__(self, 
                 description: str,
                 protocol: Dict[str, Any],
                 model: Optional[Any] = None,
                 variables: Optional[Dict[str, Any]] = None,
                 neural_field: Optional[Any] = None):
        """
        Initialize a protocol shell prompt program.
        
        Args:
            description: Description of the program's purpose
            protocol: Protocol shell definition
            model: Language model interface
            variables: Initial variables
            neural_field: Neural field for context persistence
        """
        super().__init__(description, model, variables, neural_field)
        
        # Set up protocol
        self.protocol = protocol
        
        # Generate steps from protocol
        self._generate_steps_from_protocol()
    
    def _generate_steps_from_protocol(self) -> None:
        """Generate program steps from protocol definition."""
        # Extract process steps
        process_steps = self.protocol.get("process", [])
        
        if not process_steps:
            return
            
        # Generate step for each process item
        for step in process_steps:
            if isinstance(step, dict):
                # Get step name
                step_name = next(iter(step))
                
                # Create step content
                if isinstance(step[step_name], dict):
                    # Format dictionary as step
                    content = f"{step_name}: " + ", ".join(
                        f"{k}=\"{v}\"" if isinstance(v, str) else f"{k}={v}"
                        for k, v in step[step_name].items()
                    )
                elif isinstance(step[step_name], list):
                    # Format list as step
                    content = f"{step_name}: " + ", ".join(
                        f"\"{item}\"" if isinstance(item, str) else f"{item}"
                        for item in step[step_name]
                    )
                else:
                    # Simple step
                    content = f"{step_name}: {step[step_name]}"
                
                # Add step
                self.add_step(content)
            elif isinstance(step, str):
                # Simple step
                self.add_step(step)
    
    def format(self) -> str:
        """Format the program with protocol shell."""
        # Format protocol
        protocol_str = self._format_protocol()
        
        # Format program steps
        steps_str = super().format()
        
        return f"{protocol_str}\n\n{steps_str}"
    
    def _format_protocol(self) -> str:
        """Format the protocol shell as a string."""
        parts = []
        
        # Protocol name
        protocol_name = self.protocol.get("name", "protocol")
        parts.append(f"/{protocol_name}{{")
        
        # Intent
        intent = self.protocol.get("intent", self.description)
        parts.append(f'    intent="{intent}",')
        
        # Input parameters
        input_params = self.protocol.get("input", {})
        if input_params:
            parts.append("    input={")
            for key, value in input_params.items():
                if isinstance(value, str):
                    parts.append(f'        {key}="{value}",')
                else:
                    parts.append(f"        {key}={value},")
            parts.append("    },")
        
        # Process steps
        process_steps = self.protocol.get("process", [])
        if process_steps:
            parts.append("    process=[")
            for step in process_steps:
                if isinstance(step, dict):
                    step_name = next(iter(step))
                    parts.append(f"        /{step_name}{{")
                    
                    if isinstance(step[step_name], dict):
                        for k, v in step[step_name].items():
                            if isinstance(v, str):
                                parts.append(f'            {k}="{v}",')
                            else:
                                parts.append(f"            {k}={v},")
                    elif isinstance(step[step_name], list):
                        parts.append(f"            {', '.join(step[step_name])}")
                    else:
                        if isinstance(step[step_name], str):
                            parts.append(f'            "{step[step_name]}"')
                        else:
                            parts.append(f"            {step[step_name]}")
                    
                    parts.append("        },")
                elif isinstance(step, str):
                    parts.append(f"        {step},")
            parts.append("    ],")
        
        # Output schema
        output_schema = self.protocol.get("output", {})
        if output_schema:
            parts.append("    output={")
            for key, value in output_schema.items():
                if isinstance(value, str):
                    parts.append(f'        {key}="{value}",')
                else:
                    parts.append(f"        {key}={value},")
            parts.append("    },")
        
        # Meta
        meta = self.protocol.get("meta", {})
        if meta:
            parts.append("    meta={")
            for key, value in meta.items():
                if isinstance(value, str):
                    parts.append(f'        {key}="{value}",')
                else:
                    parts.append(f"        {key}={value},")
            parts.append("    }")
        
        # Close protocol
        parts.append("}")
        
        return "\n".join(parts)
    
    def execute(self, input_data: str, max_tokens: int = 1000) -> str:
        """
        Execute the protocol program with the given input.
        
        Args:
            input_data: The input data for the program
            max_tokens: Maximum tokens for generation
            
        Returns:
            The execution result
        """
        # Update input parameter in protocol
        if "input" in self.protocol:
            input_key = next((k for k, v in self.protocol["input"].items() 
                            if v == "<current_input>" or v == "<input>"), None)
            if input_key:
                self.protocol["input"][input_key] = input_data
        
        # Execute program
        return super().execute(input_data, max_tokens)
    
    def extract_output(self, response: str) -> Dict[str, Any]:
        """
        Extract structured output from response based on protocol schema.
        
        Args:
            response: The execution response
            
        Returns:
            Extracted output dictionary
        """
        # Get output schema
        output_schema = self.protocol.get("output", {})
        if not output_schema:
            return {"raw_output": response}
        
        # Try to extract JSON output
        json_pattern = r'```(?:json)?\s*({[\s\S]*?})\s*```'
        json_matches = re.findall(json_pattern, response)
        
        if json_matches:
            try:
                extracted = json.loads(json_matches[0])
                
                # Filter to match schema
                output = {}
                for key in output_schema:
                    if key in extracted:
                        output[key] = extracted[key]
                
                # Add any missing keys
                for key in output_schema:
                    if key not in output:
                        output[key] = f"<missing_{key}>"
                
                return output
            except json.JSONDecodeError:
                pass
        
        # Try to extract output section
        output_section_pattern = r'(?:Output|Result):\s*\n([\s\S]*?)(?:\n\n|\Z)'
        section_matches = re.findall(output_section_pattern, response)
        
        if section_matches:
            section = section_matches[0]
            
            # Extract key-value pairs
            output = {}
            for line in section.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    key = key.strip()
                    if key in output_schema:
                        output[key] = value.strip()
            
            # Add any missing keys
            for key in output_schema:
                if key not in output:
                    output[key] = f"<missing_{key}>"
            
            return output
        
        # Fallback: just return raw output
        return {"raw_output": response}

# ------------------------------------------------------------------------------
# Usage Examples
# ------------------------------------------------------------------------------

def basic_program_example():
    """Example of a basic prompt program."""
    # Mock model for demonstration
    class MockModel:
        def generate(self, prompt, max_tokens=1000):
            return f"""
Step 1: Parse the problem to identify variables and relationships
Reasoning: I need to understand what variables are involved and their relationships.
Result: The problem involves a train traveling at 60 mph for 2.5 hours, and I need to find the distance.

Step 2: Set up the appropriate equations
Reasoning: I'll use the distance = speed × time formula.
Result: distance = 60 mph × 2.5 hours

Step 3: Solve for the unknown variables
Reasoning: I'll substitute the values and calculate.
Result: distance = 60 × 2.5 = 150 miles

Step 4: Verify the solution makes sense in the original context
Reasoning: I need to check if the answer is reasonable for a train traveling for 2.5 hours.
Result: 150 miles is a reasonable distance for a train traveling at 60 mph for 2.5 hours.

Final Answer: The train travels 150 miles.
"""
    
    # Create program
    model = MockModel()
    program = PromptProgram("Solve mathematical word problems step by step", model)
    
    # Add reasoning steps
    program.add_step("Parse the problem to identify variables and relationships")
    program.add_step("Set up the appropriate equations")
    program.add_step("Solve for the unknown variables")
    program.add_step("Verify the solution makes sense in the original context")
    
    # Print formatted program
    print("Program:")
    print(program.format())
    print()
    
    # Execute the program
    result = program.execute("If a train travels at 60 mph for 2.5 hours, how far does it go?")
    print("Execution Result:")
    print(result)
    
    # Execute with trace
    trace_result = program.execute_with_trace("If a train travels at 60 mph for 2.5 hours, how far does it go?")
    print("\nExecution Trace:")
    for step in trace_result["steps_trace"]:
        print(f"Step {step['step']}:")
        print(f"  Reasoning: {step['reasoning']}")
        print(f"  Result: {step['result']}")

def neural_field_program_example():
    """Example of a neural field prompt program."""
    # Mock model for demonstration
    class MockModel:
        def generate(self, prompt, max_tokens=1000):
            return f"""
Step 1: Understand the research area of interest
Reasoning: I need to identify the main research area the user is interested in.
Result: The user is interested in climate change research.

Step 2: Identify key subtopics in this research area
Reasoning: Climate change research spans multiple domains, I'll identify the main subtopics.
Result: Key subtopics include: atmospheric science, oceanography, ecology, renewable energy, policy analysis, and climate modeling.

Step 3: Determine most active research questions
Reasoning: Within these subtopics, I need to identify currently active research questions.
Result: Active research questions include: 
- How will climate change impact biodiversity in marine ecosystems?
- What are effective carbon capture technologies?
- How can climate models better predict extreme weather events?
- What policy frameworks best incentivize carbon reduction?

Step 4: Suggest specific research focus areas
Reasoning: Based on the active questions, I'll suggest specific focus areas with potential for impact.
Result: Recommended research focus areas:
1. Marine ecosystem resilience to ocean acidification
2. Machine learning applications in climate prediction
3. Economic models for carbon pricing mechanisms
4. Nature-based solutions for carbon sequestration

Final Answer: Based on current trends in climate change research, I recommend focusing on these promising areas:
1. Marine ecosystem resilience to ocean acidification - This combines ecology and oceanography with urgent practical applications
2. Machine learning applications in climate prediction - This leverages AI advances to improve climate modeling accuracy
3. Economic models for carbon pricing mechanisms - This addresses the policy implementation gap
4. Nature-based solutions for carbon sequestration - This offers scalable approaches to carbon capture

Each of these areas has active funding opportunities, growing research communities, and significant potential for impact.
"""
    
    # Create program with neural field
    model = MockModel()
    field_params = {
        "decay_rate": 0.1,
        "boundary_permeability": 0.9
    }
    program = NeuralFieldProgram(
        "Identify promising research directions in a field",
        model=model,
        field_params=field_params
    )
    
    # Add attractors to field
    program.add_attractor("Research should focus on areas with significant impact potential")
    program.add_attractor("Interdisciplinary approaches often yield novel insights")
    program.add_attractor("Consider both theoretical advances and practical applications")
    
    # Add reasoning steps
    program.add_step("Understand the research area of interest")
    program.add_step("Identify key subtopics in this research area")
    program.add_step("Determine most active research questions")
    program.add_resonance_step("Suggest specific research focus areas", [
        "Prioritize areas with growing funding opportunities",
        "Consider interdisciplinary connections",
        "Balance theoretical and applied research"
    ])
    
    # Print formatted program
    print("Neural Field Program:")
    print(program.format())
    print()
    
    # Execute the program
    result = program.execute("What are promising research directions in climate change?")
    print("Execution Result:")
    print(result)

def protocol_shell_program_example():
    """Example of a protocol shell prompt program."""
    # Mock model for demonstration
    class MockModel:
        def generate(self, prompt, max_tokens=1000):
            return f"""
I'll execute this protocol step by step.

Step 1: Analyze the document structure
Reasoning: I need to identify the main sections and organization of the document.
Result: The document has 5 main sections: Introduction, Methods, Results, Discussion, and Conclusion.

Step 2: Identify key information in each section
Reasoning: I need to extract the most important information from each section.
Result: 
- Introduction: Study purpose is to evaluate effect of diet on cholesterol levels
- Methods: Randomized controlled trial with 200 participants over 6 months
- Results: Plant-based diet group showed 15% reduction in LDL cholesterol
- Discussion: Results align with previous studies showing similar benefits
- Conclusion: Plant-based diets can significantly reduce cholesterol levels

Step 3: Generate a concise summary
Reasoning: I need to create a summary that captures the essential information.
Result: This 6-month randomized controlled trial with 200 participants found that a plant-based diet resulted in a 15% reduction in LDL cholesterol levels, supporting previous research on diet-based interventions for cardiovascular health.

Output:
summary="This 6-month randomized controlled trial with 200 participants found that a plant-based diet resulted in a 15% reduction in LDL cholesterol levels, supporting previous research on diet-based interventions for cardiovascular health."
key_finding="15% reduction in LDL cholesterol with plant-based diet"
study_design="Randomized controlled trial, 200 participants, 6 months"
recommendation="Plant-based diets can significantly reduce cholesterol levels"
"""
    
    # Create protocol shell
    protocol = {
        "intent": "Summarize a research paper concisely",
        "input": {
            "document": "<current_input>",
            "focus_area": "key findings and methodology"
        },
        "process": [
            {
                "analyze.document": {
                    "target": "structure"
                }
            },
            {
                "identify": {
                    "information": "key points per section"
                }
            },
            {
                "generate.summary": {
                    "style": "concise",
                    "length": "1-2 sentences"
                }
            }
        ],
        "output": {
            "summary": "<generated_summary>",
            "key_finding": "<main_result>",
            "study_design": "<methodology_summary>",
            "recommendation": "<primary_conclusion>"
        },
        "meta": {
            "name": "research.summarize",
            "version": "1.0.0",
            "timestamp": time.time()
        }
    }
    
    # Create program
    model = MockModel()
    program = ProtocolShellProgram(
        "Research Paper Summarizer",
        protocol=protocol,
        model=model
    )
    
    # Print formatted program
    print("Protocol Shell Program:")
    print(program.format())
    print()
    
    # Execute the program
    result = program.execute("A comprehensive study on the effects of plant-based diets on cholesterol levels...")
    print("Execution Result:")
    print(result)
    
    # Extract structured output
    output = program.extract_output(result)
    print("\nExtracted Output:")
    for key, value in output.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    # Example usage
    print("Basic Program Example:")
    basic_program_example()
    
    print("\n\nNeural Field Program Example:")
    neural_field_program_example()
    
    print("\n\nProtocol Shell Program Example:")
    protocol_shell_program_example()
