"""
Context-Engineering Control Loop Template
----------------------------------------

This template provides a flexible control loop implementation for orchestrating
context-based interactions with language models. It allows for:

1. Multi-step reasoning processes
2. State tracking across interactions
3. Dynamic context management
4. Outcome evaluation and refinement

Usage:
    control_loop = ControlLoop(
        model="gpt-4",
        initial_context={"goal": "Solve this math problem step by step"},
        max_iterations=5
    )
    result = control_loop.run(input_data="What is the square root of 144?")
"""

import time
import json
import logging
from typing import Dict, List, Any, Optional, Callable, Union, Tuple
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("control_loop")

# ------------------------------------------------------------------------------
# Model Interface
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
# Context Management
# ------------------------------------------------------------------------------

class ContextManager:
    """Manages the context for language model interactions."""
    
    def __init__(self, 
                 initial_context: Dict[str, Any] = None, 
                 max_tokens: int = 4000,
                 reserved_tokens: int = 1000):
        """
        Initialize the context manager.
        
        Args:
            initial_context: Initial context dictionary
            max_tokens: Maximum number of tokens in context
            reserved_tokens: Tokens reserved for model response
        """
        self.context = initial_context or {}
        self.max_tokens = max_tokens
        self.reserved_tokens = reserved_tokens
        self.history: List[Dict[str, Any]] = []
    
    def update(self, key: str, value: Any) -> None:
        """Update a specific context element."""
        self.context[key] = value
    
    def get_context_str(self, template: Optional[str] = None) -> str:
        """
        Get the formatted context string based on template or default format.
        
        Args:
            template: Optional template string with {placeholders}
            
        Returns:
            Formatted context string
        """
        if template:
            try:
                return template.format(**self.context)
            except KeyError as e:
                logger.warning(f"Template key error: {e}. Using default format.")
                # Fall back to default formatting
        
        # Default formatting
        parts = []
        
        # Add system instructions if present
        if "system" in self.context:
            parts.append(f"# Instructions\n{self.context['system']}\n\n")
        
        # Add goal if present
        if "goal" in self.context:
            parts.append(f"# Goal\n{self.context['goal']}\n\n")
        
        # Add context elements
        for key, value in self.context.items():
            if key not in ["system", "goal", "history", "current_input"]:
                parts.append(f"# {key.replace('_', ' ').title()}\n{value}\n\n")
        
        # Add history if present
        if "history" in self.context and self.context["history"]:
            parts.append("# Previous Steps\n")
            for i, entry in enumerate(self.context["history"]):
                parts.append(f"Step {i+1}: {entry}\n")
            parts.append("\n")
        
        # Add current input if present
        if "current_input" in self.context:
            parts.append(f"# Current Task\n{self.context['current_input']}\n\n")
        
        # Ensure the context isn't too long
        context_str = "".join(parts)
        self._prune_if_needed(context_str)
        
        return context_str
    
    def _prune_if_needed(self, context_str: str) -> str:
        """
        Prune context if it exceeds the maximum token limit.
        
        Args:
            context_str: The current context string
            
        Returns:
            Pruned context string
        """
        # Estimate token count (rough approximation)
        estimated_tokens = len(context_str.split())
        
        if estimated_tokens > (self.max_tokens - self.reserved_tokens):
            logger.warning(f"Context too long ({estimated_tokens} words). Pruning...")
            
            # Simple pruning strategy: remove oldest history entries
            if "history" in self.context and self.context["history"]:
                self.context["history"] = self.context["history"][1:]
                logger.info("Removed oldest history entry")
                
                # Recursively check if we need to prune more
                return self._prune_if_needed(self.get_context_str())
        
        return context_str
    
    def add_to_history(self, entry: Any) -> None:
        """Add an entry to the interaction history."""
        if "history" not in self.context:
            self.context["history"] = []
        
        self.context["history"].append(entry)
        self.history.append({"timestamp": time.time(), "entry": entry})
    
    def clear_history(self) -> None:
        """Clear the interaction history."""
        if "history" in self.context:
            self.context["history"] = []

# ------------------------------------------------------------------------------
# Evaluation Functions
# ------------------------------------------------------------------------------

class EvaluationFunction(ABC):
    """Base class for evaluation functions."""
    
    @abstractmethod
    def evaluate(self, response: str, context: Dict[str, Any]) -> Tuple[bool, float, str]:
        """
        Evaluate a model response.
        
        Args:
            response: The model's response
            context: The current context dictionary
            
        Returns:
            Tuple of (success_flag, score, feedback)
        """
        pass

class SimpleKeywordEvaluator(EvaluationFunction):
    """Evaluates responses based on keyword presence."""
    
    def __init__(self, required_keywords: List[str], forbidden_keywords: List[str] = None):
        """
        Initialize the keyword evaluator.
        
        Args:
            required_keywords: List of keywords that should be present
            forbidden_keywords: List of keywords that should not be present
        """
        self.required_keywords = required_keywords
        self.forbidden_keywords = forbidden_keywords or []
    
    def evaluate(self, response: str, context: Dict[str, Any]) -> Tuple[bool, float, str]:
        """
        Evaluate based on keyword presence.
        
        Returns:
            Tuple of (success_flag, score, feedback)
        """
        response_lower = response.lower()
        
        # Check required keywords
        missing_keywords = [kw for kw in self.required_keywords 
                           if kw.lower() not in response_lower]
        
        # Check forbidden keywords
        present_forbidden = [kw for kw in self.forbidden_keywords 
                            if kw.lower() in response_lower]
        
        # Calculate score (0.0 to 1.0)
        if self.required_keywords:
            required_score = (len(self.required_keywords) - len(missing_keywords)) / len(self.required_keywords)
        else:
            required_score = 1.0
            
        if self.forbidden_keywords:
            forbidden_score = (len(self.forbidden_keywords) - len(present_forbidden)) / len(self.forbidden_keywords)
        else:
            forbidden_score = 1.0
            
        score = (required_score + forbidden_score) / 2.0
        success = score > 0.8  # Consider successful if score > 80%
        
        # Generate feedback
        feedback = []
        if missing_keywords:
            feedback.append(f"Missing required keywords: {', '.join(missing_keywords)}")
        if present_forbidden:
            feedback.append(f"Contains forbidden keywords: {', '.join(present_forbidden)}")
        if not feedback:
            feedback.append("Response meets keyword criteria")
            
        return success, score, "; ".join(feedback)

class PatternMatchEvaluator(EvaluationFunction):
    """Evaluates responses based on regex pattern matching."""
    
    def __init__(self, required_patterns: List[str], forbidden_patterns: List[str] = None):
        """
        Initialize the pattern evaluator.
        
        Args:
            required_patterns: List of regex patterns that should match
            forbidden_patterns: List of regex patterns that should not match
        """
        import re
        self.re = re
        self.required_patterns = [re.compile(p, re.IGNORECASE) for p in required_patterns]
        self.forbidden_patterns = [re.compile(p, re.IGNORECASE) for p in (forbidden_patterns or [])]
    
    def evaluate(self, response: str, context: Dict[str, Any]) -> Tuple[bool, float, str]:
        """
        Evaluate based on pattern matching.
        
        Returns:
            Tuple of (success_flag, score, feedback)
        """
        # Check required patterns
        missing_patterns = [p.pattern for p in self.required_patterns 
                           if not p.search(response)]
        
        # Check forbidden patterns
        present_forbidden = [p.pattern for p in self.forbidden_patterns 
                            if p.search(response)]
        
        # Calculate score
        if self.required_patterns:
            required_score = (len(self.required_patterns) - len(missing_patterns)) / len(self.required_patterns)
        else:
            required_score = 1.0
            
        if self.forbidden_patterns:
            forbidden_score = (len(self.forbidden_patterns) - len(present_forbidden)) / len(self.forbidden_patterns)
        else:
            forbidden_score = 1.0
            
        score = (required_score + forbidden_score) / 2.0
        success = score > 0.8  # Consider successful if score > 80%
        
        # Generate feedback
        feedback = []
        if missing_patterns:
            feedback.append(f"Missing required patterns: {', '.join(missing_patterns)}")
        if present_forbidden:
            feedback.append(f"Contains forbidden patterns: {', '.join(present_forbidden)}")
        if not feedback:
            feedback.append("Response meets pattern criteria")
            
        return success, score, "; ".join(feedback)

class ModelEvaluator(EvaluationFunction):
    """Uses a model to evaluate another model's response."""
    
    def __init__(self, model_interface: ModelInterface, evaluation_prompt_template: str):
        """
        Initialize the model evaluator.
        
        Args:
            model_interface: ModelInterface instance for evaluation
            evaluation_prompt_template: Template for evaluation prompt
        """
        self.model = model_interface
        self.evaluation_prompt_template = evaluation_prompt_template
    
    def evaluate(self, response: str, context: Dict[str, Any]) -> Tuple[bool, float, str]:
        """
        Evaluate using another model.
        
        Returns:
            Tuple of (success_flag, score, feedback)
        """
        # Create evaluation prompt
        eval_prompt = self.evaluation_prompt_template.format(
            response=response,
            **context
        )
        
        # Get evaluation from model
        try:
            eval_response = self.model.generate(eval_prompt)
            
            # Try to parse structured response (JSON)
            try:
                result = json.loads(eval_response)
                success = result.get("success", False)
                score = result.get("score", 0.0)
                feedback = result.get("feedback", "No feedback provided")
            except json.JSONDecodeError:
                # If not JSON, try to extract score and feedback heuristically
                if "score" in eval_response.lower():
                    # Try to extract score (0-10 or 0-100 scale)
                    import re
                    score_match = re.search(r"score\s*(?::|=)\s*(\d+(?:\.\d+)?)", eval_response, re.IGNORECASE)
                    if score_match:
                        raw_score = float(score_match.group(1))
                        # Normalize to 0-1 scale
                        if raw_score > 10:
                            score = raw_score / 100.0
                        else:
                            score = raw_score / 10.0
                    else:
                        score = 0.5  # Default middle score
                else:
                    score = 0.5
                
                # Simple heuristic for success based on positive language
                positive_terms = ["good", "great", "excellent", "correct", "accurate", "yes", "pass"]
                negative_terms = ["bad", "poor", "incorrect", "inaccurate", "wrong", "no", "fail"]
                
                pos_count = sum(1 for term in positive_terms if term in eval_response.lower())
                neg_count = sum(1 for term in negative_terms if term in eval_response.lower())
                
                success = pos_count > neg_count
                feedback = eval_response.strip()
            
            return success, score, feedback
            
        except Exception as e:
            logger.error(f"Evaluation model error: {e}")
            return False, 0.0, f"Evaluation failed: {str(e)}"

# ------------------------------------------------------------------------------
# Control Loop
# ------------------------------------------------------------------------------

class ControlLoop:
    """
    Main control loop for context-based LLM interactions.
    Manages the flow of information, context updates, and evaluation.
    """
    
    def __init__(self, 
                 model: Union[str, ModelInterface],
                 initial_context: Dict[str, Any] = None,
                 context_template: Optional[str] = None,
                 max_iterations: int = 5,
                 evaluators: List[EvaluationFunction] = None,
                 stop_on_success: bool = True,
                 success_threshold: float = 0.8):
        """
        Initialize the control loop.
        
        Args:
            model: Model name or ModelInterface instance
            initial_context: Initial context dictionary
            context_template: Optional template for context formatting
            max_iterations: Maximum number of iterations
            evaluators: List of EvaluationFunction instances
            stop_on_success: Whether to stop iterating on first success
            success_threshold: Threshold for considering an iteration successful
        """
        # Set up model interface
        if isinstance(model, str):
            if "gpt" in model.lower():
                self.model = OpenAIInterface(model)
            elif "claude" in model.lower():
                self.model = AnthropicInterface(model)
            else:
                raise ValueError(f"Unknown model type: {model}")
        else:
            self.model = model
        
        # Set up context manager
        self.context_manager = ContextManager(initial_context)
        self.context_template = context_template
        
        # Set up control parameters
        self.max_iterations = max_iterations
        self.evaluators = evaluators or []
        self.stop_on_success = stop_on_success
        self.success_threshold = success_threshold
        
        # Set up tracking
        self.iterations = 0
        self.results = []
    
    def add_evaluator(self, evaluator: EvaluationFunction) -> None:
        """Add an evaluation function."""
        self.evaluators.append(evaluator)
    
    def run(self, input_data: Any = None) -> Dict[str, Any]:
        """
        Run the control loop with the given input.
        
        Args:
            input_data: Input data for the loop
            
        Returns:
            Result dictionary with final response and metadata
        """
        logger.info("Starting control loop")
        self.iterations = 0
        self.results = []
        
        # Add input to context
        if input_data:
            self.context_manager.update("current_input", input_data)
        
        final_response = None
        successful = False
        
        # Main control loop
        while self.iterations < self.max_iterations:
            self.iterations += 1
            logger.info(f"Iteration {self.iterations}/{self.max_iterations}")
            
            # Get formatted context
            context_str = self.context_manager.get_context_str(self.context_template)
            
            # Generate response from model
            try:
                response = self.model.generate(context_str)
                logger.info(f"Received response ({len(response)} chars)")
            except Exception as e:
                logger.error(f"Model generation failed: {e}")
                break
                
            # Store the response
            final_response = response
            
            # Evaluate the response
            evaluation_results = []
            overall_success = True
            overall_score = 1.0
            
            for evaluator in self.evaluators:
                success, score, feedback = evaluator.evaluate(
                    response, 
                    self.context_manager.context
                )
                evaluation_results.append({
                    "evaluator": evaluator.__class__.__name__,
                    "success": success,
                    "score": score,
                    "feedback": feedback
                })
                
                # Update overall results
                overall_success = overall_success and success
                overall_score *= score  # Multiply scores for a stricter measure
            
            # Store results
            iteration_result = {
                "iteration": self.iterations,
                "response": response,
                "evaluations": evaluation_results,
                "success": overall_success,
                "score": overall_score
            }
            self.results.append(iteration_result)
            
            # Add to history
            self.context_manager.add_to_history(
                f"Response: {response}\nEvaluation: {'Success' if overall_success else 'Failure'}"
            )
            
            # Check if we should stop
            if overall_success and self.stop_on_success:
                logger.info("Stopping on successful iteration")
                successful = True
                break
                
            # Check if we've reached the maximum iterations
            if self.iterations >= self.max_iterations:
                logger.info(f"Reached maximum iterations ({self.max_iterations})")
                break
        
        # Prepare final result
        result = {
            "successful": successful,
            "iterations": self.iterations,
            "final_response": final_response,
            "detailed_results": self.results,
            "context": self.context_manager.context
        }
        
        logger.info(f"Control loop completed: {'Success' if successful else 'Failure'}")
        return result
    
    def reset(self) -> None:
        """Reset the control loop to initial state."""
        self.iterations = 0
        self.results = []
        self.context_manager.clear_history()

# ------------------------------------------------------------------------------
# Neural Field Extensions
# ------------------------------------------------------------------------------

class NeuralField:
    """
    Neural field implementation for context engineering.
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

class NeuralFieldControlLoop(ControlLoop):
    """Control loop implementation using neural field for context management."""
    
    def __init__(self, 
                 model: Union[str, ModelInterface],
                 field_params: Dict[str, float] = None,
                 max_iterations: int = 5,
                 evaluators: List[EvaluationFunction] = None,
                 stop_on_success: bool = True,
                 success_threshold: float = 0.8):
        """
        Initialize the neural field control loop.
        
        Args:
            model: Model name or ModelInterface instance
            field_params: Parameters for the neural field
            max_iterations: Maximum number of iterations
            evaluators: List of EvaluationFunction instances
            stop_on_success: Whether to stop iterating on first success
            success_threshold: Threshold for considering an iteration successful
        """
        super().__init__(
            model=model,
            initial_context={},
            max_iterations=max_iterations,
            evaluators=evaluators,
            stop_on_success=stop_on_success,
            success_threshold=success_threshold
        )
        
        # Replace context manager with neural field
        field_params = field_params or {}
        self.field = NeuralField(
            decay_rate=field_params.get('decay_rate', 0.05),
            boundary_permeability=field_params.get('boundary_permeability', 0.8),
            resonance_bandwidth=field_params.get('resonance_bandwidth', 0.6),
            attractor_formation_threshold=field_params.get('attractor_threshold', 0.7)
        )
        
        # Initialize attractors if provided
        initial_attractors = field_params.get('initial_attractors', [])
        for attractor in initial_attractors:
            self.field.inject(attractor, strength=1.0)
    
    def run(self, input_data: Any = None) -> Dict[str, Any]:
        """
        Run the control loop with the given input using neural field dynamics.
        
        Args:
            input_data: Input data for the loop
            
        Returns:
            Result dictionary with final response and metadata
        """
        logger.info("Starting neural field control loop")
        self.iterations = 0
        self.results = []
        
        # Inject input to field
        if input_data:
            self.field.inject(f"Current task: {input_data}", strength=1.0)
        
        final_response = None
        successful = False
        
        # Main control loop
        while self.iterations < self.max_iterations:
            self.iterations += 1
            logger.info(f"Iteration {self.iterations}/{self.max_iterations}")
            
            # Apply field decay
            self.field.decay()
            
            # Get field representation
            context_str = self.field.get_context_representation()
            
            # Generate response from model
            try:
                response = self.model.generate(context_str)
                logger.info(f"Received response ({len(response)} chars)")
            except Exception as e:
                logger.error(f"Model generation failed: {e}")
                break
                
            # Store the response
            final_response = response
            
            # Inject response back into field
            self.field.inject(f"Response: {response}", strength=0.8)
            
            # Evaluate the response
            evaluation_results = []
            overall_success = True
            overall_score = 1.0
            
            # Create a mock context for evaluators
            mock_context = {
                "current_input": input_data,
                "history": self.field.history
            }
            
            for evaluator in self.evaluators:
                success, score, feedback = evaluator.evaluate(
                    response, 
                    mock_context
                )
                evaluation_results.append({
                    "evaluator": evaluator.__class__.__name__,
                    "success": success,
                    "score": score,
                    "feedback": feedback
                })
                
                # Inject evaluation feedback into field
                self.field.inject(f"Evaluation: {feedback}", strength=0.6)
                
                # Update overall results
                overall_success = overall_success and success
                overall_score *= score
            
            # Store results
            iteration_result = {
                "iteration": self.iterations,
                "response": response,
                "evaluations": evaluation_results,
                "success": overall_success,
                "score": overall_score,
                "field_stability": self.field.measure_field_stability()
            }
            self.results.append(iteration_result)
            
            # Check if we should stop
            if overall_success and self.stop_on_success:
                logger.info("Stopping on successful iteration")
                successful = True
                break
                
            # Check if we've reached the maximum iterations
            if self.iterations >= self.max_iterations:
                logger.info(f"Reached maximum iterations ({self.max_iterations})")
                break
        
        # Prepare final result
        result = {
            "successful": successful,
            "iterations": self.iterations,
            "final_response": final_response,
            "detailed_results": self.results,
            "field_state": {
                "stability": self.field.measure_field_stability(),
                "attractors": self.field.attractors,
                "active_patterns": len(self.field.state)
            }
        }
        
        logger.info(f"Neural field control loop completed: {'Success' if successful else 'Failure'}")
        return result
    
    def reset(self) -> None:
        """Reset the control loop to initial state."""
        self.iterations = 0
        self.results = []
        # Reset field state
        self.field = NeuralField(
            decay_rate=self.field.decay_rate,
            boundary_permeability=self.field.boundary_permeability,
            resonance_bandwidth=self.field.resonance_bandwidth,
            attractor_formation_threshold=self.field.attractor_threshold
        )

# ------------------------------------------------------------------------------
# Protocol Framework Integration
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
            step_name = step.get("name", "step")
            parts.append(f"        /{step_name}{{")
            
            for key, value in step.items():
                if key != "name":
                    if isinstance(value, str):
                        parts.append(f'            {key}="{value}",')
                    else:
                        parts.append(f"            {key}={value},")
            
            parts.append("        },")
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
                step_name = step.get("name", f"step_{i}")
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

class ProtocolShellControlLoop(ControlLoop):
    """Control loop implementation using protocol shells for context operations."""
    
    def __init__(self, 
                 model: Union[str, ModelInterface],
                 protocol_shell: Union[ProtocolShell, Dict[str, Any]],
                 max_iterations: int = 5,
                 evaluators: List[EvaluationFunction] = None,
                 stop_on_success: bool = True,
                 success_threshold: float = 0.8):
        """
        Initialize the protocol shell control loop.
        
        Args:
            model: Model name or ModelInterface instance
            protocol_shell: Protocol shell instance or definition dictionary
            max_iterations: Maximum number of iterations
            evaluators: List of EvaluationFunction instances
            stop_on_success: Whether to stop iterating on first success
            success_threshold: Threshold for considering an iteration successful
        """
        super().__init__(
            model=model,
            initial_context={},
            max_iterations=max_iterations,
            evaluators=evaluators,
            stop_on_success=stop_on_success,
            success_threshold=success_threshold
        )
        
        # Set up protocol shell
        if isinstance(protocol_shell, dict):
            self.protocol = ProtocolShell(
                intent=protocol_shell.get("intent", "Execute protocol"),
                input_params=protocol_shell.get("input", {}),
                process_steps=protocol_shell.get("process", []),
                output_schema=protocol_shell.get("output", {}),
                meta=protocol_shell.get("meta", {})
            )
        else:
            self.protocol = protocol_shell
        
        # Execution context
        self.context = {}
    
    def run(self, input_data: Any = None) -> Dict[str, Any]:
        """
        Run the control loop with the given input using protocol shell.
        
        Args:
            input_data: Input data for the loop
            
        Returns:
            Result dictionary with final response and metadata
        """
        logger.info("Starting protocol shell control loop")
        self.iterations = 0
        self.results = []
        
        # Add input to context
        if input_data:
            self.context["current_input"] = input_data
        
        final_response = None
        successful = False
        
        # Main control loop
        while self.iterations < self.max_iterations:
            self.iterations += 1
            logger.info(f"Iteration {self.iterations}/{self.max_iterations}")
            
            # Format protocol for model
            protocol_str = self.protocol.format()
            
            # Add instruction for model
            context_str = f"""
# Protocol Execution
Below is a protocol shell definition. Your task is to execute this protocol 
by following each step and providing the expected output.

{protocol_str}

# Current Context
Input: {input_data}
Iteration: {self.iterations}/{self.max_iterations}

# Instructions
1. Follow each step in the protocol's process section
2. Provide reasoning for each step
3. Return a final output that matches the expected output schema

Please execute the protocol now:
"""
            
            # Generate response from model
            try:
                response = self.model.generate(context_str)
                logger.info(f"Received response ({len(response)} chars)")
            except Exception as e:
                logger.error(f"Model generation failed: {e}")
                break
                
            # Store the response
            final_response = response
            
            # Update context with response
            self.context["latest_response"] = response
            
            # Try to extract structured output from response
            extracted_output = self._extract_output_from_response(response)
            if extracted_output:
                self.context.update(extracted_output)
            
            # Evaluate the response
            evaluation_results = []
            overall_success = True
            overall_score = 1.0
            
            for evaluator in self.evaluators:
                success, score, feedback = evaluator.evaluate(
                    response, 
                    self.context
                )
                evaluation_results.append({
                    "evaluator": evaluator.__class__.__name__,
                    "success": success,
                    "score": score,
                    "feedback": feedback
                })
                
                # Update context with evaluation
                if "evaluations" not in self.context:
                    self.context["evaluations"] = []
                self.context["evaluations"].append({
                    "iteration": self.iterations,
                    "feedback": feedback,
                    "score": score
                })
                
                # Update overall results
                overall_success = overall_success and success
                overall_score *= score
            
            # Store results
            iteration_result = {
                "iteration": self.iterations,
                "response": response,
                "extracted_output": extracted_output,
                "evaluations": evaluation_results,
                "success": overall_success,
                "score": overall_score
            }
            self.results.append(iteration_result)
            
            # Check if we should stop
            if overall_success and self.stop_on_success:
                logger.info("Stopping on successful iteration")
                successful = True
                break
                
            # Check if we've reached the maximum iterations
            if self.iterations >= self.max_iterations:
                logger.info(f"Reached maximum iterations ({self.max_iterations})")
                break
        
        # Prepare final result
        result = {
            "successful": successful,
            "iterations": self.iterations,
            "final_response": final_response,
            "detailed_results": self.results,
            "context": self.context,
            "protocol": {
                "intent": self.protocol.intent,
                "status": self.protocol.state["status"],
                "output": self.protocol.state["output"]
            }
        }
        
        logger.info(f"Protocol shell control loop completed: {'Success' if successful else 'Failure'}")
        return result
    
    def _extract_output_from_response(self, response: str) -> Dict[str, Any]:
        """
        Extract structured output from model response.
        
        Args:
            response: Model response text
            
        Returns:
            Extracted output dictionary
        """
        # Look for JSON output
        import re
        json_pattern = r'```(?:json)?\s*({[\s\S]*?})\s*```'
        json_matches = re.findall(json_pattern, response)
        
        if json_matches:
            try:
                return json.loads(json_matches[0])
            except json.JSONDecodeError:
                pass
        
        # Look for output section
        output_pattern = r'(?:Output|Result):\s*\n([\s\S]*?)(?:\n\n|\Z)'
        output_matches = re.findall(output_pattern, response)
        
        if output_matches:
            # Try to parse as key-value pairs
            output = {}
            lines = output_matches[0].strip().split('\n')
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    output[key.strip()] = value.strip()
            
            if output:
                return output
        
        # Return a simplified output if no structure found
        return {"raw_output": response}
    
    def reset(self) -> None:
        """Reset the control loop to initial state."""
        self.iterations = 0
        self.results = []
        self.context = {}
        
        # Reset protocol state
        self.protocol.state = {
            "status": "initialized",
            "step_index": 0,
            "error": None,
            "output": {},
            "log": []
        }

# ------------------------------------------------------------------------------
# Recursive Field Control Loop
# ------------------------------------------------------------------------------

class RecursiveFieldControlLoop:
    """
    Advanced control loop that combines neural fields and protocol shells
    with recursive self-improvement capabilities.
    """
    
    def __init__(self,
                 model: Union[str, ModelInterface],
                 field_params: Dict[str, float] = None,
                 protocol_template: Dict[str, Any] = None,
                 max_iterations: int = 10,
                 evaluators: List[EvaluationFunction] = None,
                 recursion_depth: int = 3):
        """
        Initialize the recursive field control loop.
        
        Args:
            model: Model name or ModelInterface instance
            field_params: Parameters for the neural field
            protocol_template: Template for protocol shells
            max_iterations: Maximum number of iterations
            evaluators: List of EvaluationFunction instances
            recursion_depth: Maximum depth of recursive self-improvement
        """
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
        
        # Set up default protocol template
        self.protocol_template = protocol_template or {
            "intent": "Process information and generate response",
            "input": {
                "current_input": "<current_input>",
                "field_state": "<field_state>",
                "iteration": "<iteration>"
            },
            "process": [
                {
                    "name": "analyze.input",
                    "target": "current_input"
                },
                {
                    "name": "process.field",
                    "measure": ["resonance", "coherence", "entropy"]
                },
                {
                    "name": "generate.response",
                    "style": "coherent and informative"
                }
            ],
            "output": {
                "response": "<generated_response>",
                "field_update": "<field_update_suggestions>",
                "metrics": "<quality_metrics>"
            },
            "meta": {
                "name": "recursive_field_protocol",
                "version": "1.0.0"
            }
        }
        
        # Set up execution parameters
        self.max_iterations = max_iterations
        self.evaluators = evaluators or []
        self.recursion_depth = recursion_depth
        
        # Execution state
        self.iterations = 0
        self.recursion_level = 0
        self.results = []
        self.context = {}
    
    def run(self, input_data: Any = None) -> Dict[str, Any]:
        """
        Run the recursive field control loop.
        
        Args:
            input_data: Input data for the loop
            
        Returns:
            Result dictionary with final response and metadata
        """
        logger.info("Starting recursive field control loop")
        self.iterations = 0
        self.recursion_level = 0
        self.results = []
        
        # Inject input to field
        if input_data:
            self.field.inject(f"Current task: {input_data}", strength=1.0)
            self.context["current_input"] = input_data
        
        final_response = None
        successful = False
        
        # Main control loop
        while self.iterations < self.max_iterations:
            self.iterations += 1
            logger.info(f"Iteration {self.iterations}/{self.max_iterations} (Recursion level {self.recursion_level})")
            
            # Apply field decay
            self.field.decay()
            
            # Generate protocol shell
            protocol = self._generate_protocol()
            
            # Format protocol for model
            protocol_str = protocol.format()
            field_str = self.field.get_context_representation()
            
            context_str = f"""
# Recursive Field Protocol
Below is a protocol shell definition and the current state of the neural field.
Your task is to execute this protocol, interact with the field, and generate a response.

## Neural Field State
{field_str}

## Protocol
{protocol_str}

## Current Context
Input: {input_data}
Iteration: {self.iterations}/{self.max_iterations}
Recursion Level: {self.recursion_level}/{self.recursion_depth}

## Instructions
1. Follow each step in the protocol's process section
2. Analyze the neural field state and identify key patterns
3. Generate a response that resonates with the field's attractors
4. Suggest field updates (new patterns to inject or strengthen)
5. Return output matching the protocol's output schema

Please execute the protocol now:
"""
            
            # Generate response from model
            try:
                response = self.model.generate(context_str)
                logger.info(f"Received response ({len(response)} chars)")
            except Exception as e:
                logger.error(f"Model generation failed: {e}")
                break
                
            # Store the response
            final_response = response
            
            # Update context and field
            self.context["latest_response"] = response
            self.field.inject(f"Response: {response}", strength=0.8)
            
            # Try to extract structured output
            extracted_output = self._extract_output_from_response(response)
            if extracted_output:
                # Process field update suggestions
                if "field_update" in extracted_output:
                    field_updates = extracted_output["field_update"]
                    if isinstance(field_updates, list):
                        for update in field_updates:
                            if isinstance(update, str):
                                self.field.inject(update, strength=0.7)
                    elif isinstance(field_updates, str):
                        self.field.inject(field_updates, strength=0.7)
                
                # Update context
                self.context.update(extracted_output)
            
            # Evaluate the response
            evaluation_results = self._evaluate_response(response)
            overall_success = all(result["success"] for result in evaluation_results)
            overall_score = 1.0
            for result in evaluation_results:
                overall_score *= result.get("score", 1.0)
            
            # Store results
            iteration_result = {
                "iteration": self.iterations,
                "recursion_level": self.recursion_level,
                "response": response,
                "extracted_output": extracted_output,
                "evaluations": evaluation_results,
                "success": overall_success,
                "score": overall_score,
                "field_stability": self.field.measure_field_stability()
            }
            self.results.append(iteration_result)
            
            # Check if we should recursively improve
            if not overall_success and self.recursion_level < self.recursion_depth:
                # Attempt recursive self-improvement
                logger.info(f"Initiating recursive self-improvement (level {self.recursion_level + 1})")
                improvement_result = self._recursive_improve(response, evaluation_results)
                
                if improvement_result:
                    # Inject improved response
                    self.field.inject(f"Improved response: {improvement_result}", strength=0.9)
                    final_response = improvement_result
                    
                    # Re-evaluate
                    new_evaluation = self._evaluate_response(improvement_result)
                    new_success = all(result["success"] for result in new_evaluation)
                    
                    if new_success:
                        logger.info("Recursive improvement successful")
                        successful = True
                        break
            
            # Check if we've reached the maximum iterations
            if self.iterations >= self.max_iterations:
                logger.info(f"Reached maximum iterations ({self.max_iterations})")
                break
        
        # Prepare final result
        result = {
            "successful": successful,
            "iterations": self.iterations,
            "recursion_level": self.recursion_level,
            "final_response": final_response,
            "detailed_results": self.results,
            "field_state": {
                "stability": self.field.measure_field_stability(),
                "attractors": self.field.attractors,
                "active_patterns": len(self.field.state)
            },
            "context": self.context
        }
        
        logger.info(f"Recursive field control loop completed: {'Success' if successful else 'Failure'}")
        return result
    
    def _generate_protocol(self) -> ProtocolShell:
        """
        Generate a protocol shell for the current iteration.
        
        Returns:
            Protocol shell instance
        """
        # Fill template with current values
        input_params = {}
        for key, value in self.protocol_template["input"].items():
            if isinstance(value, str) and value.startswith("<") and value.endswith(">"):
                var_name = value[1:-1]
                if var_name == "current_input":
                    input_params[key] = self.context.get("current_input", "")
                elif var_name == "field_state":
                    input_params[key] = "See Neural Field State section above"
                elif var_name == "iteration":
                    input_params[key] = self.iterations
                else:
                    input_params[key] = self.context.get(var_name, f"<{var_name}>")
            else:
                input_params[key] = value
        
        # Create protocol
        return ProtocolShell(
            intent=self.protocol_template["intent"],
            input_params=input_params,
            process_steps=self.protocol_template["process"],
            output_schema=self.protocol_template["output"],
            meta=self.protocol_template["meta"]
        )
    
    def _evaluate_response(self, response: str) -> List[Dict[str, Any]]:
        """
        Evaluate a response using all evaluators.
        
        Args:
            response: Model response to evaluate
            
        Returns:
            List of evaluation results
        """
        results = []
        
        for evaluator in self.evaluators:
            try:
                success, score, feedback = evaluator.evaluate(response, self.context)
                results.append({
                    "evaluator": evaluator.__class__.__name__,
                    "success": success,
                    "score": score,
                    "feedback": feedback
                })
                
                # Inject evaluation into field
                self.field.inject(f"Evaluation: {feedback}", strength=0.6)
                
            except Exception as e:
                logger.error(f"Evaluator {evaluator.__class__.__name__} failed: {e}")
                results.append({
                    "evaluator": evaluator.__class__.__name__,
                    "success": False,
                    "score": 0.0,
                    "feedback": f"Evaluation error: {str(e)}"
                })
        
        return results
    
    def _recursive_improve(self, response: str, evaluations: List[Dict[str, Any]]) -> Optional[str]:
        """
        Attempt to recursively improve a response based on evaluations.
        
        Args:
            response: Original response
            evaluations: Evaluation results
            
        Returns:
            Improved response or None if improvement failed
        """
        self.recursion_level += 1
        
        # Format evaluation feedback
        feedback_str = "\n".join([
            f"- {eval_result['evaluator']}: {eval_result['feedback']} (Score: {eval_result['score']:.2f})"
            for eval_result in evaluations
        ])
        
        # Create improvement prompt
        improvement_prompt = f"""
# Recursive Self-Improvement

## Original Response
```
{response}
```

## Evaluation Feedback
{feedback_str}

## Field State
{self.field.get_context_representation()}

## Task
Your task is to improve the original response by addressing the evaluation feedback.
Ensure your improved response:
1. Resonates with the field's strongest attractors
2. Addresses all issues raised in the evaluation feedback
3. Maintains coherence with the original intent
4. Incorporates field patterns that have high stability

Generate an improved response that will score higher on all evaluation metrics.
"""
        
        # Generate improved response
        try:
            improved_response = self.model.generate(improvement_prompt)
            logger.info(f"Generated recursive improvement at level {self.recursion_level}")
            
            # Extract improved response from model output (removing meta-commentary)
            import re
            
            # Look for response between code blocks
            code_block_pattern = r'```(?:.*?)\n([\s\S]*?)```'
            code_matches = re.findall(code_block_pattern, improved_response)
            
            if code_matches:
                return code_matches[0].strip()
            
            # Look for section headers indicating the response
            section_pattern = r'(?:Improved Response|New Response):\s*\n([\s\S]*?)(?:\n\n|$)'
            section_matches = re.findall(section_pattern, improved_response)
            
            if section_matches:
                return section_matches[0].strip()
            
            # If no clear demarcation, use the whole response
            return improved_response
            
        except Exception as e:
            logger.error(f"Recursive improvement failed: {e}")
            return None
        
    def _extract_output_from_response(self, response: str) -> Dict[str, Any]:
        """
        Extract structured output from model response.
        
        Args:
            response: Model response text
            
        Returns:
            Extracted output dictionary
        """
        # Look for JSON output
        import re
        json_pattern = r'```(?:json)?\s*({[\s\S]*?})\s*```'
        json_matches = re.findall(json_pattern, response)
        
        if json_matches:
            try:
                return json.loads(json_matches[0])
            except json.JSONDecodeError:
                pass
        
        # Look for output section
        output_pattern = r'(?:Output|Result):\s*\n([\s\S]*?)(?:\n\n|\Z)'
        output_matches = re.findall(output_pattern, response)
        
        if output_matches:
            # Try to parse as key-value pairs
            output = {}
            lines = output_matches[0].strip().split('\n')
            for line in lines:
                if ':' in line:
                    key, value = line.split(':', 1)
                    output[key.strip()] = value.strip()
            
            if output:
                return output
        
        # Return a simplified output if no structure found
        return {"raw_output": response}
    
    def reset(self) -> None:
        """Reset the control loop to initial state."""
        self.iterations = 0
        self.recursion_level = 0
        self.results = []
        self.context = {}
        
        # Reset field
        self.field = NeuralField(
            decay_rate=self.field.decay_rate,
            boundary_permeability=self.field.boundary_permeability,
            resonance_bandwidth=self.field.resonance_bandwidth,
            attractor_formation_threshold=self.field.attractor_threshold
        )

# ------------------------------------------------------------------------------
# Symbolic Residue Tracker Extension
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

class ResidueEnhancedNeuralField(NeuralField):
    """Neural field with explicit symbolic residue tracking."""
    
    def __init__(self, 
                 decay_rate: float = 0.05,
                 boundary_permeability: float = 0.8,
                 resonance_bandwidth: float = 0.6,
                 attractor_formation_threshold: float = 0.7):
        """Initialize the residue-enhanced neural field."""
        super().__init__(decay_rate, boundary_permeability, resonance_bandwidth, attractor_formation_threshold)
        self.residue_tracker = SymbolicResidueTracker()
    
    def inject(self, pattern: str, strength: float = 1.0, source: str = "manual") -> 'ResidueEnhancedNeuralField':
        """
        Inject a pattern with explicit residue tracking.
        
        Args:
            pattern: Pattern to inject
            strength: Strength of the pattern
            source: Source of the pattern
            
        Returns:
            Self for chaining
        """
        # Regular field injection
        super().inject(pattern, strength)
        
        # Surface residue
        residue_id = self.residue_tracker.surface(pattern, source, strength)
        
        # Check resonance with attractors
        for attractor_id, attractor in self.attractors.items():
            resonance = self._calculate_resonance(pattern, attractor['pattern'])
            if resonance > 0.3:
                # Integrate with attractor
                self.residue_tracker.integrate(residue_id, f"attractor:{attractor_id}", resonance * 0.5)
        
        return self
    
    def _form_attractor(self, pattern: str) -> str:
        """Form attractor with residue integration."""
        attractor_id = super()._form_attractor(pattern)
        
        # Find residues related to this pattern
        for residue in self.residue_tracker.get_active_residues():
            resonance = self._calculate_resonance(pattern, residue.content)
            if resonance > 0.3:
                self.residue_tracker.integrate(residue.id, f"attractor:{attractor_id}", resonance * 0.4)
        
        return attractor_id
    
    def decay(self) -> 'ResidueEnhancedNeuralField':
        """Apply decay with residue echoing."""
        # Standard decay
        super().decay()
        
        # Echo weak residues
        active_patterns = set(self.state.keys())
        for residue in self.residue_tracker.get_residues_by_state("surfaced"):
            if residue.content not in active_patterns and residue.strength < 0.5:
                # Create echo
                self.residue_tracker.echo(residue.id, "field", -0.1)
        
        return self
    
    def get_context_representation(self) -> str:
        """Get context representation with residue information."""
        # Get standard representation
        base_repr = super().get_context_representation()
        
        # Add residue information
        parts = [base_repr, "\n# Symbolic Residue"]
        
        # Add surfaced residues
        surfaced = self.residue_tracker.get_residues_by_state("surfaced")
        if surfaced:
            parts.append("## Surfaced Residue")
            for residue in sorted(surfaced, key=lambda r: r.strength, reverse=True)[:3]:
                parts.append(f"- ({residue.strength:.2f}) {residue.content[:100]}...")
        
        # Add integrated residues
        integrated = self.residue_tracker.get_residues_by_state("integrated")
        if integrated:
            parts.append("## Integrated Residue")
            for residue in sorted(integrated, key=lambda r: r.strength, reverse=True)[:3]:
                # Find most recent integration
                target = next((i["target"] for i in reversed(residue.interactions) 
                              if i["type"] == "integration"), "unknown")
                parts.append(f"- ({residue.strength:.2f}) {residue.content[:50]}... → {target}")
        
        # Add echo residues
        echo = self.residue_tracker.get_residues_by_state("echo")
        if echo:
            parts.append("## Echo Residue")
            for residue in sorted(echo, key=lambda r: r.strength, reverse=True)[:3]:
                parts.append(f"- ({residue.strength:.2f}) {residue.content[:50]}...")
        
        return "\n".join(parts)

# ------------------------------------------------------------------------------
# Usage Examples
# ------------------------------------------------------------------------------

def basic_control_loop_example():
    """Example of using the basic control loop."""
    # Initialize model
    model = OpenAIInterface("gpt-3.5-turbo")
    
    # Initialize context
    initial_context = {
        "system": "You are a helpful assistant that answers questions accurately and concisely.",
        "goal": "Provide accurate information about neural networks."
    }
    
    # Create evaluator
    evaluator = SimpleKeywordEvaluator(
        required_keywords=["neural network", "layers", "training"],
        forbidden_keywords=["I don't know", "I'm not sure"]
    )
    
    # Create control loop
    control_loop = ControlLoop(
        model=model,
        initial_context=initial_context,
        max_iterations=3,
        evaluators=[evaluator]
    )
    
    # Run control loop
    result = control_loop.run("Explain how neural networks work in simple terms.")
    
    # Print result
    print(f"Success: {result['successful']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Final response: {result['final_response'][:100]}...")

def neural_field_example():
    """Example of using the neural field control loop."""
    # Initialize model
    model = OpenAIInterface("gpt-3.5-turbo")
    
    # Create evaluator
    evaluator = PatternMatchEvaluator(
        required_patterns=[r"neural\s+field", r"resonance", r"attractor"],
        forbidden_patterns=[r"I don't know", r"I'm not sure"]
    )
    
    # Field parameters
    field_params = {
        "decay_rate": 0.1,
        "boundary_permeability": 0.9,
        "resonance_bandwidth": 0.7,
        "attractor_threshold": 0.6,
        "initial_attractors": [
            "Neural fields represent context as a continuous medium rather than discrete tokens.",
            "Resonance is a key property of neural fields that determines how information patterns interact.",
            "Attractors form stable centers of organization in the field's state space."
        ]
    }
    
    # Create control loop
    field_loop = NeuralFieldControlLoop(
        model=model,
        field_params=field_params,
        max_iterations=3,
        evaluators=[evaluator]
    )
    
    # Run control loop
    result = field_loop.run("Explain how neural fields maintain information persistence.")
    
    # Print result
    print(f"Success: {result['successful']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Field stability: {result['field_state']['stability']}")
    print(f"Final response: {result['final_response'][:100]}...")

def protocol_shell_example():
    """Example of using the protocol shell control loop."""
    # Initialize model
    model = OpenAIInterface("gpt-3.5-turbo")
    
    # Create evaluator
    evaluator = PatternMatchEvaluator(
        required_patterns=[r"step\s+by\s+step", r"analysis", r"conclusion"],
        forbidden_patterns=[r"I don't know", r"I'm not sure"]
    )
    
    # Create protocol shell
    protocol = {
        "intent": "Analyze a mathematical problem step by step",
        "input": {
            "problem": "<current_input>",
            "approach": "Break down into manageable steps"
        },
        "process": [
            {
                "name": "understand.problem",
                "goal": "Identify what is being asked"
            },
            {
                "name": "identify.knowns",
                "goal": "List all known information"
            },
            {
                "name": "identify.unknowns",
                "goal": "Identify what needs to be calculated"
            },
            {
                "name": "develop.strategy",
                "goal": "Choose appropriate mathematical technique"
            },
            {
                "name": "execute.solution",
                "goal": "Solve step by step"
            },
            {
                "name": "verify.answer",
                "goal": "Check if the solution makes sense"
            }
        ],
        "output": {
            "solution": "Complete step-by-step solution",
            "answer": "Final answer with units if applicable",
            "verification": "Explanation of why the answer makes sense"
        },
        "meta": {
            "name": "math_problem_solver",
            "version": "1.0.0"
        }
    }
    
    # Create control loop
    protocol_loop = ProtocolShellControlLoop(
        model=model,
        protocol_shell=protocol,
        max_iterations=2,
        evaluators=[evaluator]
    )
    
    # Run control loop
    result = protocol_loop.run("If a train travels at 60 mph for 2.5 hours, how far does it go?")
    
    # Print result
    print(f"Success: {result['successful']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Final response: {result['final_response'][:100]}...")

def recursive_field_example():
    """Example of using the recursive field control loop."""
    # Initialize model
    model = OpenAIInterface("gpt-4")
    
    # Create evaluator
    evaluator = PatternMatchEvaluator(
        required_patterns=[r"reasoning", r"analysis", r"conclusion"],
        forbidden_patterns=[r"I don't know", r"I'm not sure"]
    )
    
    # Field parameters
    field_params = {
        "decay_rate": 0.1,
        "boundary_permeability": 0.9,
        "resonance_bandwidth": 0.7,
        "attractor_threshold": 0.6,
        "initial_attractors": [
            "Break down complex problems into manageable steps.",
            "Consider multiple perspectives before reaching a conclusion.",
            "Evaluate evidence critically and identify assumptions."
        ]
    }
    
    # Protocol template
    protocol_template = {
        "intent": "Analyze a complex problem with recursive reasoning",
        "input": {
            "problem": "<current_input>",
            "field_state": "<field_state>",
            "iteration": "<iteration>"
        },
        "process": [
            {
                "name": "analyze.problem",
                "identify": "key components and relationships"
            },
            {
                "name": "generate.perspectives",
                "count": "at least 3 distinct viewpoints"
            },
            {
                "name": "evaluate.evidence",
                "criteria": ["relevance", "credibility", "significance"]
            },
            {
                "name": "synthesize.insights",
                "goal": "coherent understanding across perspectives"
            },
            {
                "name": "formulate.conclusion",
                "ensure": "balanced and well-supported"
            }
        ],
        "output": {
            "analysis": "Structured analysis with multiple perspectives",
            "conclusion": "Well-reasoned conclusion with supporting evidence",
            "field_update": "Suggestions for field pattern updates",
            "metrics": "Self-evaluation of reasoning quality"
        },
        "meta": {
            "name": "recursive_reasoning_protocol",
            "version": "1.0.0"
        }
    }
    
    # Create control loop
    recursive_loop = RecursiveFieldControlLoop(
        model=model,
        field_params=field_params,
        protocol_template=protocol_template,
        max_iterations=3,
        evaluators=[evaluator],
        recursion_depth=2
    )
    
    # Run control loop
    result = recursive_loop.run(
        "Analyze the potential long-term impacts of artificial general intelligence on society."
    )
    
    # Print result
    print(f"Success: {result['successful']}")
    print(f"Iterations: {result['iterations']}")
    print(f"Recursion level: {result['recursion_level']}")
    print(f"Field stability: {result['field_state']['stability']}")
    print(f"Final response: {result['final_response'][:100]}...")

if __name__ == "__main__":
    # Example usage
    print("Running basic control loop example...")
    basic_control_loop_example()
    
    print("\nRunning neural field example...")
    neural_field_example()
    
    print("\nRunning protocol shell example...")
    protocol_shell_example()
    
    print("\nRunning recursive field example...")
    recursive_field_example()
