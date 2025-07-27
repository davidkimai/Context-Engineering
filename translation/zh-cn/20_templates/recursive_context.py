"""
Recursive Context Framework for Context Engineering
------------------------------------------

This module provides a framework for implementing recursive contexts that can
extend, refine, and evolve themselves. It combines neural field concepts with
protocol shells and self-improvement mechanisms to create contexts that become
more effective through recursive iterations.

Key capabilities:
1. Self-reflection and introspection
2. Recursive self-improvement
3. Neural field integration
4. Protocol shell orchestration
5. Symbolic residue tracking
6. Attribution and interpretability

Usage:
    # Create a basic recursive framework
    framework = RecursiveFramework(
        description="Mathematical problem solver",
        model="gpt-4"
    )
    
    # Add self-improvement loop
    framework.add_self_improvement_loop(
        evaluation_metric="solution_correctness",
        improvement_strategy="step_refinement"
    )
    
    # Execute with recursive improvement
    result = framework.execute_recursive(
        "Solve for x: 3x + 7 = 22",
        max_iterations=3
    )
"""

import time
import json
import logging
import re
import math
import copy
from typing import Dict, List, Any, Optional, Union, Callable, Tuple, Set
from enum import Enum
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("recursive_framework")

# ------------------------------------------------------------------------------
# Base Model Interface
# ------------------------------------------------------------------------------

class ModelInterface(ABC):
    """Abstract base class for language model interfaces."""
    
    @abstractmethod
    def generate(self, context: str, max_tokens: int = 1000) -> str:
        """Generate a response from the model given a context."""
        pass

class OpenAIInterface(ModelInterface):
    """OpenAI API interface for language models."""
    
    def __init__(self, model_name: str, api_key: Optional[str] = None):
        """
        Initialize the OpenAI interface.
        
        Args:
            model_name: Name of the OpenAI model to use
            api_key: OpenAI API key (optional if set in environment)
        """
        try:
            import openai
            self.openai = openai
            if api_key:
                openai.api_key = api_key
            self.model_name = model_name
        except ImportError:
            raise ImportError("OpenAI package not installed. Install with 'pip install openai'")
    
    def generate(self, context: str, max_tokens: int = 1000) -> str:
        """Generate a response using the OpenAI API."""
        try:
            response = self.openai.ChatCompletion.create(
                model=self.model_name,
                messages=[{"role": "user", "content": context}],
                max_tokens=max_tokens,
                n=1,
                temperature=0.7,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise

class AnthropicInterface(ModelInterface):
    """Anthropic API interface for Claude models."""
    
    def __init__(self, model_name: str, api_key: Optional[str] = None):
        """
        Initialize the Anthropic interface.
        
        Args:
            model_name: Name of the Anthropic model to use
            api_key: Anthropic API key (optional if set in environment)
        """
        try:
            import anthropic
            self.anthropic = anthropic
            self.client = anthropic.Anthropic(api_key=api_key)
            self.model_name = model_name
        except ImportError:
            raise ImportError("Anthropic package not installed. Install with 'pip install anthropic'")
    
    def generate(self, context: str, max_tokens: int = 1000) -> str:
        """Generate a response using the Anthropic API."""
        try:
            response = self.client.completion(
                model=self.model_name,
                prompt=f"\n\nHuman: {context}\n\nAssistant:",
                max_tokens_to_sample=max_tokens,
                temperature=0.7,
            )
            return response.completion
        except Exception as e:
            logger.error(f"Anthropic API error: {e}")
            raise

# ------------------------------------------------------------------------------
# Neural Field Components
# ------------------------------------------------------------------------------

class NeuralField:
    """
    Neural field implementation for recursive context engineering.
    Treats context as a continuous field rather than discrete tokens.
    """
    
    def __init__(self, 
                 decay_rate: float = 0.05,
                 boundary_permeability: float = 0.8,
                 resonance_bandwidth: float = 0.6,
                 attractor_formation_threshold: float = 0.7):
        """
        Initialize the neural field.
        
        Args:
            decay_rate: Base rate of pattern decay
            boundary_permeability: How easily new information enters
            resonance_bandwidth: How broadly patterns resonate
            attractor_formation_threshold: Threshold for attractor formation
        """
        self.state = {}  # Field state
        self.attractors = {}  # Stable attractors
        self.history = []  # Field evolution history
        
        # Field properties
        self.decay_rate = decay_rate
        self.boundary_permeability = boundary_permeability
        self.resonance_bandwidth = resonance_bandwidth
        self.attractor_threshold = attractor_formation_threshold
    
    def inject(self, pattern: str, strength: float = 1.0) -> 'NeuralField':
        """
        Introduce a new pattern into the field.
        
        Args:
            pattern: The information pattern to inject
            strength: The strength of the pattern
            
        Returns:
            Self for chaining
        """
        # Apply boundary filtering
        effective_strength = strength * self.boundary_permeability
        
        # Check resonance with existing attractors
        for attractor_id, attractor in self.attractors.items():
            resonance = self._calculate_resonance(pattern, attractor['pattern'])
            if resonance > 0.2:
                # Attractor pulls pattern toward it
                pattern = self._blend_patterns(
                    pattern, 
                    attractor['pattern'],
                    blend_ratio=resonance * 0.3
                )
                # Strengthen attractor
                self.attractors[attractor_id]['strength'] += resonance * 0.1
        
        # Update field state with new pattern
        if pattern in self.state:
            self.state[pattern] += effective_strength
        else:
            self.state[pattern] = effective_strength
            
        # Record history
        self.history.append(("inject", pattern, effective_strength))
        
        # Check for attractor formation
        if pattern in self.state and self.state[pattern] > self.attractor_threshold:
            self._form_attractor(pattern)
        
        # Process resonance effects
        self._process_resonance(pattern)
        
        return self
    
    def _form_attractor(self, pattern: str) -> str:
        """
        Form a new attractor around a strong pattern.
        
        Args:
            pattern: The pattern to form an attractor around
            
        Returns:
            ID of the formed attractor
        """
        attractor_id = f"attractor_{len(self.attractors)}"
        self.attractors[attractor_id] = {
            'pattern': pattern,
            'strength': self.state[pattern],
            'formation_time': len(self.history),
            'basin_width': self.resonance_bandwidth
        }
        return attractor_id
    
    def _process_resonance(self, trigger_pattern: str) -> 'NeuralField':
        """
        Process resonance effects from a trigger pattern.
        
        Args:
            trigger_pattern: The pattern triggering resonance
            
        Returns:
            Self for chaining
        """
        # For each existing pattern, calculate resonance with trigger
        resonance_effects = {}
        for pattern, strength in self.state.items():
            if pattern != trigger_pattern:
                resonance = self._calculate_resonance(pattern, trigger_pattern)
                effect = resonance * strength * 0.2
                resonance_effects[pattern] = effect
        
        # Apply resonance effects
        for pattern, effect in resonance_effects.items():
            self.state[pattern] += effect
        
        return self
    
    def decay(self) -> 'NeuralField':
        """
        Apply natural decay to all patterns.
        
        Returns:
            Self for chaining
        """
        # Apply decay to field state
        for pattern in list(self.state.keys()):
            # Patterns that resonate with attractors decay more slowly
            attractor_protection = 0
            for attractor in self.attractors.values():
                resonance = self._calculate_resonance(pattern, attractor['pattern'])
                attractor_protection += resonance * 0.5
            
            effective_decay = self.decay_rate * (1 - min(attractor_protection, 0.9))
            self.state[pattern] *= (1 - effective_decay)
            
        # Apply minimal decay to attractors
        for attractor_id in list(self.attractors.keys()):
            self.attractors[attractor_id]['strength'] *= (1 - self.decay_rate * 0.2)
            
        # Remove patterns that have decayed below threshold
        self.state = {k: v for k, v in self.state.items() if v > 0.01}
        self.attractors = {k: v for k, v in self.attractors.items() if v['strength'] > 0.1}
        
        return self
    
    def _calculate_resonance(self, pattern1: str, pattern2: str) -> float:
        """
        Calculate resonance between two patterns.
        
        Args:
            pattern1: First pattern
            pattern2: Second pattern
            
        Returns:
            Resonance score (0.0 to 1.0)
        """
        # Simple word overlap similarity
        words1 = set(pattern1.lower().split())
        words2 = set(pattern2.lower().split())
        
        if not words1 or not words2:
            return 0.0
            
        overlap = len(words1.intersection(words2))
        similarity = overlap / max(len(words1), len(words2))
        
        # Apply bandwidth modulation
        resonance = similarity * self.resonance_bandwidth
        
        return resonance
    
    def _blend_patterns(self, pattern1: str, pattern2: str, blend_ratio: float) -> str:
        """
        Blend two patterns based on ratio.
        
        Args:
            pattern1: First pattern
            pattern2: Second pattern
            blend_ratio: Ratio of blending (0.0 to 1.0)
            
        Returns:
            Blended pattern
        """
        # Simple concatenation with weighting indication
        return f"{pattern1} {blend_ratio:.2f}↔️ {pattern2}"
    
    def measure_field_stability(self) -> float:
        """
        Measure how stable the field is.
        
        Returns:
            Stability score (0.0 to 1.0)
        """
        if not self.attractors:
            return 0.0
        
        # Measure average attractor strength
        avg_strength = sum(a['strength'] for a in self.attractors.values()) / len(self.attractors)
        
        # Measure pattern organization around attractors
        organization = 0
        for pattern, strength in self.state.items():
            best_resonance = max(
                self._calculate_resonance(pattern, a['pattern']) 
                for a in self.attractors.values()
            ) if self.attractors else 0
            
            organization += best_resonance * strength
            
        if self.state:
            organization /= sum(self.state.values())
        else:
            organization = 0
        
        # Combine metrics
        stability = (avg_strength * 0.6) + (organization * 0.4)
        return min(1.0, stability)  # Cap at 1.0
    
    def get_context_representation(self) -> str:
        """
        Get a string representation of the current field state.
        
        Returns:
            String representation of the field
        """
        parts = []
        
        # Add attractors
        if self.attractors:
            parts.append("# Field Attractors")
            for attractor_id, attractor in self.attractors.items():
                parts.append(f"- {attractor_id} (Strength: {attractor['strength']:.2f}): {attractor['pattern'][:100]}...")
            parts.append("")
        
        # Add most active patterns
        parts.append("# Active Patterns")
        active_patterns = sorted(self.state.items(), key=lambda x: x[1], reverse=True)[:5]
        for pattern, strength in active_patterns:
            parts.append(f"- ({strength:.2f}): {pattern[:100]}...")
        
        # Add field metrics
        parts.append("")
        parts.append(f"Field Stability: {self.measure_field_stability():.2f}")
        parts.append(f"Active Patterns: {len(self.state)}")
        parts.append(f"Attractor Count: {len(self.attractors)}")
        
        return "\n".join(parts)

# ------------------------------------------------------------------------------
# Symbolic Residue Components
# ------------------------------------------------------------------------------

class SymbolicResidue:
    """Represents a symbolic residue fragment in the neural field."""
    
    def __init__(self, 
                 content: str,
                 source: str,
                 strength: float = 1.0,
                 state: str = "surfaced"):
        """
        Initialize a symbolic residue.
        
        Args:
            content: The content/pattern of the residue
            source: Where the residue originated from
            strength: Initial strength of the residue
            state: Current state of the residue (surfaced, integrated, echo)
        """
        self.content = content
        self.source = source
        self.strength = strength
        self.state = state
        self.timestamp = time.time()
        self.id = f"residue_{hash(content)}_{int(self.timestamp)}"
        self.interactions = []
    
    def interact(self, target: str, interaction_type: str, strength_delta: float) -> None:
        """Record an interaction with another element."""
        self.interactions.append({
            "target": target,
            "type": interaction_type,
            "strength_delta": strength_delta,
            "timestamp": time.time()
        })
        
        # Update strength
        self.strength += strength_delta
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "id": self.id,
            "content": self.content,
            "source": self.source,
            "strength": self.strength,
            "state": self.state,
            "timestamp": self.timestamp,
            "interactions": self.interactions
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SymbolicResidue':
        """Create from dictionary representation."""
        residue = cls(
            content=data["content"],
            source=data["source"],
            strength=data["strength"],
            state=data["state"]
        )
        residue.id = data["id"]
        residue.timestamp = data["timestamp"]
        residue.interactions = data.get("interactions", [])
        return residue

class SymbolicResidueTracker:
    """Tracks and manages symbolic residue in neural fields."""
    
    def __init__(self):
        """Initialize the residue tracker."""
        self.residues: Dict[str, SymbolicResidue] = {}
        self.history: List[Dict[str, Any]] = []
    
    def surface(self, content: str, source: str, strength: float = 1.0) -> str:
        """
        Surface a new symbolic residue.
        
        Args:
            content: The content/pattern of the residue
            source: Where the residue originated from
            strength: Initial strength of the residue
            
        Returns:
            ID of the surfaced residue
        """
        residue = SymbolicResidue(content, source, strength)
        self.residues[residue.id] = residue
        
        self.history.append({
            "action": "surface",
            "residue_id": residue.id,
            "timestamp": time.time()
        })
        
        return residue.id
    
    def integrate(self, residue_id: str, target: str, strength_delta: float = 0.5) -> None:
        """
        Integrate a residue into a target.
        
        Args:
            residue_id: ID of the residue to integrate
            target: Target to integrate with
            strength_delta: Change in strength from integration
        """
        if residue_id not in self.residues:
            raise ValueError(f"Residue {residue_id} not found")
        
        residue = self.residues[residue_id]
        residue.state = "integrated"
        residue.interact(target, "integration", strength_delta)
        
        self.history.append({
            "action": "integrate",
            "residue_id": residue_id,
            "target": target,
            "timestamp": time.time()
        })
    
    def echo(self, residue_id: str, target: str, strength_delta: float = -0.2) -> None:
        """
        Create an echo of a residue.
        
        Args:
            residue_id: ID of the residue to echo
            target: Target of the echo
            strength_delta: Change in strength from echo
        """
        if residue_id not in self.residues:
            raise ValueError(f"Residue {residue_id} not found")
        
        residue = self.residues[residue_id]
        residue.state = "echo"
        residue.interact(target, "echo", strength_delta)
        
        self.history.append({
            "action": "echo",
            "residue_id": residue_id,
            "target": target,
            "timestamp": time.time()
        })
    
    def get_active_residues(self, min_strength: float = 0.5) -> List[SymbolicResidue]:
        """Get active residues above the specified strength threshold."""
        return [r for r in self.residues.values() if r.strength >= min_strength]
    
    def get_residues_by_state(self, state: str) -> List[SymbolicResidue]:
        """Get residues in the specified state."""
        return [r for r in self.residues.values() if r.state == state]
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        return {
            "residues": {rid: r.to_dict() for rid, r in self.residues.items()},
            "history": self.history
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SymbolicResidueTracker':
        """Create from dictionary representation."""
        tracker = cls()
        
        for rid, rdata in data.get("residues", {}).items():
            tracker.residues[rid] = SymbolicResidue.from_dict(rdata)
        
        tracker.history = data.get("history", [])
        return tracker

# ------------------------------------------------------------------------------
# Protocol Shell Components
# ------------------------------------------------------------------------------

class ProtocolShell:
    """
    Protocol shell for defining structured context operations.
    Based on the pareto-lang format from the Context-Engineering project.
    """
    
    def __init__(self, 
                 intent: str,
                 input_params: Dict[str, Any] = None,
                 process_steps: List[Dict[str, Any]] = None,
                 output_schema: Dict[str, Any] = None,
                 meta: Dict[str, Any] = None):
        """
        Initialize the protocol shell.
        
        Args:
            intent: Goal or purpose of the protocol
            input_params: Input parameters and structure
            process_steps: List of process steps to execute
            output_schema: Expected output structure
            meta: Metadata about the protocol
        """
        self.intent = intent
        self.input_params = input_params or {}
        self.process_steps = process_steps or []
        self.output_schema = output_schema or {}
        self.meta = meta or {
            "name": "protocol",
            "version": "1.0.0",
            "timestamp": time.time()
        }
        
        # Execution state
        self.state = {
            "status": "initialized",
            "step_index": 0,
            "error": None,
            "output": {},
            "log": []
        }
    
    def format(self) -> str:
        """
        Format the protocol shell as a string in pareto-lang format.
        
        Returns:
            Formatted protocol string
        """
        parts = []
        
        # Protocol name (derived from meta if available)
        protocol_name = self.meta.get("name", "protocol")
        parts.append(f"/{protocol_name}{{")
        
        # Intent
        parts.append(f'    intent="{self.intent}",')
        
        # Input parameters
        parts.append("    input={")
        for key, value in self.input_params.items():
            if isinstance(value, str):
                parts.append(f'        {key}="{value}",')
            else:
                parts.append(f"        {key}={value},")
        parts.append("    },")
        
        # Process steps
        parts.append("    process=[")
        for step in self.process_steps:
            step_name = next(iter(step)) if isinstance(step, dict) else step
            
            if isinstance(step, dict):
                parts.append(f"        /{step_name}{{")
                
                step_content = step[step_name]
                if isinstance(step_content, dict):
                    for k, v in step_content.items():
                        if isinstance(v, str):
                            parts.append(f'            {k}="{v}",')
                        else:
                            parts.append(f"            {k}={v},")
                elif isinstance(step_content, list):
                    content_str = ", ".join(f'"{item}"' if isinstance(item, str) else str(item) for item in step_content)
                    parts.append(f"            {content_str}")
                else:
                    if isinstance(step_content, str):
                        parts.append(f'            "{step_content}"')
                    else:
                        parts.append(f"            {step_content}")
                
                parts.append("        },")
            else:
                parts.append(f"        {step},")
        parts.append("    ],")
        
        # Output schema
        parts.append("    output={")
        for key, value in self.output_schema.items():
            if isinstance(value, str):
                parts.append(f'        {key}="{value}",')
            else:
                parts.append(f"        {key}={value},")
        parts.append("    },")
        
        # Meta
        parts.append("    meta={")
        for key, value in self.meta.items():
            if isinstance(value, str):
                parts.append(f'        {key}="{value}",')
            else:
                parts.append(f"        {key}={value},")
        parts.append("    }")
        
        # Close protocol
        parts.append("}")
        
        return "\n".join(parts)
    
    def execute(self, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Execute the protocol steps.
        This is a simplified execution that uses the context to resolve variables.
        
        Args:
            context: Execution context
            
        Returns:
            Output dictionary
        """
        context = context or {}
        self.state["status"] = "running"
        self.state["log"].append(f"Starting execution of protocol '{self.meta.get('name', 'protocol')}'")
        
        try:
            # Process input parameters
            processed_inputs = {}
            for key, value in self.input_params.items():
                if isinstance(value, str) and value.startswith("<") and value.endswith(">"):
                    # This is a variable reference
                    var_name = value[1:-1]
                    if var_name in context:
                        processed_inputs[key] = context[var_name]
                    else:
                        self.state["log"].append(f"Warning: Variable {var_name} not found in context")
                        processed_inputs[key] = None
                else:
                    processed_inputs[key] = value
            
            # Execute process steps
            step_results = []
            for i, step in enumerate(self.process_steps):
                self.state["step_index"] = i
                step_name = next(iter(step)) if isinstance(step, dict) else step
                self.state["log"].append(f"Executing step {i+1}/{len(self.process_steps)}: {step_name}")
                
                # Execute the step (simplified simulation)
                # In a full implementation, this would interpret and execute each step
                result = {
                    "step": step_name,
                    "status": "completed",
                    "output": f"Simulated execution of {step_name}"
                }
                
                step_results.append(result)
            
            # Prepare output
            output = {}
            for key in self.output_schema:
                if key in context:
                    output[key] = context[key]
                else:
                    output[key] = f"<simulated_{key}>"
            
            self.state["output"] = output
            self.state["status"] = "completed"
            
        except Exception as e:
            self.state["status"] = "error"
            self.state["error"] = str(e)
            self.state["log"].append(f"Error: {str(e)}")
        
        return {
            "status": self.state["status"],
            "output": self.state["output"],
            "log": self.state["log"],
            "error": self.state["error"]
        }

# ------------------------------------------------------------------------------
# Recursive Framework Core
# ------------------------------------------------------------------------------

class RecursiveFramework:
    """
    Framework for implementing recursive contexts with self-improvement.
    Combines neural fields, protocol shells, and symbolic residue tracking.
    """
    
    def __init__(self, 
                 description: str,
                 model: Union[str, ModelInterface],
                 field_params: Dict[str, Any] = None,
                 protocol_template: Dict[str, Any] = None,
                 recursion_depth: int = 3,
                 verbose: bool = False):
        """
        Initialize the recursive framework.
        
        Args:
            description: Description of the framework's purpose
            model: Model name or ModelInterface instance
            field_params: Parameters for the neural field
            protocol_template: Template for protocol shells
            recursion_depth: Maximum recursion depth
            verbose: Whether to log detailed information
        """
        self.description = description
        self.recursion_depth = recursion_depth
        self.verbose = verbose
        
        # Set up model
        if isinstance(model, str):
            if "gpt" in model.lower():
                self.model = OpenAIInterface(model)
            elif "claude" in model.lower():
                self.model = AnthropicInterface(model)
            else:
                raise ValueError(f"Unknown model type: {model}")
        else:
            self.model = model
        
        # Set up neural field
        field_params = field_params or {}
        self.field = NeuralField(
            decay_rate=field_params.get('decay_rate', 0.05),
            boundary_permeability=field_params.get('boundary_permeability', 0.8),
            resonance_bandwidth=field_params.get('resonance_bandwidth', 0.6),
            attractor_formation_threshold=field_params.get('attractor_threshold', 0.7)
        )
        
        # Set up residue tracker
        self.residue_tracker = SymbolicResidueTracker()
        
        # Set up protocol template
        self.protocol_template = protocol_template or {
            "intent": "Process information recursively",
            "input": {
                "current_input": "<current_input>",
                "field_state": "<field_state>",
                "recursion_level": "<recursion_level>"
            },
            "process": [
                {
                    "analyze.input": {
                        "understand": "core request"
                    }
                },
                {
                    "process.field": {
                        "measure": ["resonance", "coherence", "stability"]
                    }
                },
                {
                    "generate.response": {
                        "style": "clear and helpful"
                    }
                },
                {
                    "self.improve": {
                        "target": "response quality"
                    }
                }
            ],
            "output": {
                "response": "<generated_response>",
                "field_update": "<field_update_suggestions>",
                "improvement": "<improvement_suggestions>"
            },
            "meta": {
                "name": "recursive_framework",
                "version": "1.0.0"
            }
        }
        
        # Execution state
        self.current_recursion_level = 0
        self.execution_trace = []
        self.improvement_history = []
        
        # Initialize field with core concepts
        self._initialize_field()
    
    def _initialize_field(self) -> None:
        """Initialize the neural field with core concepts."""
        # Add core attractors
        core_attractors = [
            (f"The purpose of this framework is to {self.description}", 0.9),
            ("Recursive improvement leads to better outcomes", 0.8),
            ("Context should evolve based on feedback", 0.8),
            ("Neural fields enable continuous context representation", 0.7),
            ("Symbolic residue captures subtle meaning fragments", 0.7)
        ]
        
        for pattern, strength in core_attractors:
            self.field.inject(pattern, strength)
            # Explicitly form attractor
            self.field._form_attractor(pattern)
            
            # Surface as symbolic residue
            self.residue_tracker.surface(pattern, "initialization", strength)
    
    def add_attractor(self, pattern: str, strength: float = 1.0) -> None:
        """
        Add an attractor to the neural field.
        
        Args:
            pattern: The attractor pattern
            strength: The attractor strength
        """
        # Inject with high strength to form attractor
        self.field.inject(pattern, strength)
        
        # Explicitly form attractor
        self.field._form_attractor(pattern)
        
        # Surface as symbolic residue
        self.residue_tracker.surface(pattern, "manual_addition", strength)
    
    def add_self_improvement_strategy(self, 
                                     strategy_name: str,
                                     strategy_description: str,
                                     strategy_prompt: str) -> None:
        """
        Add a self-improvement strategy.
        
        Args:
            strategy_name: Name of the strategy
            strategy_description: Description of the strategy
            strategy_prompt: Prompt template for the strategy
        """
        # Add as attractor
        pattern = f"Self-improvement strategy: {strategy_name} - {strategy_
