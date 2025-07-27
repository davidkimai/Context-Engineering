"""
Field Resonance Measurement Tool
--------------------------------

This module provides tools for measuring resonance, coherence, and other properties
of neural fields in context engineering applications. It enables quantitative
assessment of field states to guide optimization and tuning.

Usage:
    # Initialize a resonance measurer
    measurer = FieldResonanceMeasurer()
    
    # Measure resonance between patterns
    score = measurer.measure_resonance(pattern1, pattern2)
    
    # Measure field coherence
    coherence = measurer.measure_coherence(field)
    
    # Get comprehensive field metrics
    metrics = measurer.get_field_metrics(field)
"""

import math
import time
import logging
from typing import Dict, List, Any, Optional, Callable, Union, Tuple, Set
from collections import defaultdict
import yaml
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("field_resonance")

# ------------------------------------------------------------------------------
# Resonance Measurement
# ------------------------------------------------------------------------------

class ResonanceMeasurer:
    """Measures resonance between patterns in a neural field."""
    
    def __init__(self, method: str = "cosine", threshold: float = 0.2, amplification: float = 1.2):
        """
        Initialize the resonance measurer.
        
        Args:
            method: Resonance calculation method ("cosine", "overlap", "embedding")
            threshold: Minimum threshold for resonance effects
            amplification: Amplification factor for resonance effects
        """
        self.method = method
        self.threshold = threshold
        self.amplification = amplification
        
        # Initialize embedding model if needed
        self.embedding_model = None
        if method == "embedding":
            try:
                self._initialize_embedding_model()
            except ImportError:
                logger.warning("Embedding model not available, falling back to cosine similarity")
                self.method = "cosine"
    
    def _initialize_embedding_model(self):
        """Initialize the embedding model for semantic similarity."""
        try:
            import numpy as np
            from sentence_transformers import SentenceTransformer
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
            self.np = np
        except ImportError:
            raise ImportError("Sentence-transformers not installed. Install with 'pip install sentence-transformers'")
    
    def measure(self, pattern1: str, pattern2: str) -> float:
        """
        Measure resonance between two patterns.
        
        Args:
            pattern1: First pattern
            pattern2: Second pattern
            
        Returns:
            Resonance score (0.0 to 1.0)
        """
        if not pattern1 or not pattern2:
            return 0.0
            
        if self.method == "cosine":
            return self._cosine_similarity(pattern1, pattern2)
        elif self.method == "overlap":
            return self._word_overlap(pattern1, pattern2)
        elif self.method == "embedding":
            return self._embedding_similarity(pattern1, pattern2)
        else:
            logger.warning(f"Unknown resonance method: {self.method}, falling back to cosine")
            return self._cosine_similarity(pattern1, pattern2)
    
    def _cosine_similarity(self, pattern1: str, pattern2: str) -> float:
        """Calculate cosine similarity based on word frequency."""
        # Get word frequency dictionaries
        words1 = self._get_word_freq(pattern1)
        words2 = self._get_word_freq(pattern2)
        
        # Find common words
        common_words = set(words1.keys()) & set(words2.keys())
        
        # Calculate dot product
        dot_product = sum(words1[word] * words2[word] for word in common_words)
        
        # Calculate magnitudes
        mag1 = math.sqrt(sum(value ** 2 for value in words1.values()))
        mag2 = math.sqrt(sum(value ** 2 for value in words2.values()))
        
        # Avoid division by zero
        if mag1 == 0 or mag2 == 0:
            return 0.0
            
        # Calculate cosine similarity
        similarity = dot_product / (mag1 * mag2)
        
        # Apply amplification and threshold
        if similarity < self.threshold:
            return 0.0
            
        return min(1.0, similarity * self.amplification)
    
    def _word_overlap(self, pattern1: str, pattern2: str) -> float:
        """Calculate similarity based on word overlap."""
        # Get word sets
        words1 = set(pattern1.lower().split())
        words2 = set(pattern2.lower().split())
        
        # Calculate overlap
        if not words1 or not words2:
            return 0.0
            
        overlap = len(words1 & words2)
        union = len(words1 | words2)
        
        # Calculate Jaccard similarity
        similarity = overlap / union
        
        # Apply amplification and threshold
        if similarity < self.threshold:
            return 0.0
            
        return min(1.0, similarity * self.amplification)
    
    def _embedding_similarity(self, pattern1: str, pattern2: str) -> float:
        """Calculate similarity based on embedding vectors."""
        if self.embedding_model is None:
            logger.warning("Embedding model not initialized, falling back to cosine similarity")
            return self._cosine_similarity(pattern1, pattern2)
            
        # Get embeddings
        embedding1 = self.embedding_model.encode([pattern1])[0]
        embedding2 = self.embedding_model.encode([pattern2])[0]
        
        # Calculate cosine similarity
        similarity = self.np.dot(embedding1, embedding2) / (
            self.np.linalg.norm(embedding1) * self.np.linalg.norm(embedding2)
        )
        
        # Apply amplification and threshold
        if similarity < self.threshold:
            return 0.0
            
        return min(1.0, float(similarity * self.amplification))
    
    def _get_word_freq(self, text: str) -> Dict[str, int]:
        """Get word frequency dictionary from text."""
        words = text.lower().split()
        freq = defaultdict(int)
        for word in words:
            freq[word] += 1
        return freq

# ------------------------------------------------------------------------------
# Coherence Measurement
# ------------------------------------------------------------------------------

class CoherenceMeasurer:
    """Measures coherence of a neural field."""
    
    def __init__(self, method: str = "attractor_alignment", sampling: str = "strength_weighted", sample_size: int = 100):
        """
        Initialize the coherence measurer.
        
        Args:
            method: Coherence calculation method ("pairwise", "attractor_alignment", "entropy")
            sampling: Sampling strategy for large fields ("full", "random", "strength_weighted")
            sample_size: Sample size for large fields
        """
        self.method = method
        self.sampling = sampling
        self.sample_size = sample_size
        self.resonance_measurer = ResonanceMeasurer()
    
    def measure(self, field: Any) -> float:
        """
        Measure coherence of a field.
        
        Args:
            field: Neural field to measure
            
        Returns:
            Coherence score (0.0 to 1.0)
        """
        if self.method == "pairwise":
            return self._pairwise_coherence(field)
        elif self.method == "attractor_alignment":
            return self._attractor_alignment(field)
        elif self.method == "entropy":
            return self._entropy_coherence(field)
        else:
            logger.warning(f"Unknown coherence method: {self.method}, falling back to attractor_alignment")
            return self._attractor_alignment(field)
    
    def _pairwise_coherence(self, field: Any) -> float:
        """Calculate coherence based on pairwise pattern resonance."""
        # Get patterns to evaluate
        patterns = self._sample_patterns(field)
        
        if len(patterns) < 2:
            return 1.0  # Perfect coherence for a single pattern
            
        # Calculate all pairwise resonances
        total_resonance = 0.0
        pair_count = 0
        
        for i, (pattern1, strength1) in enumerate(patterns):
            for j, (pattern2, strength2) in enumerate(patterns):
                if i < j:  # Only compare each pair once
                    resonance = self.resonance_measurer.measure(pattern1, pattern2)
                    weighted_resonance = resonance * strength1 * strength2
                    total_resonance += weighted_resonance
                    pair_count += 1
        
        if pair_count == 0:
            return 0.0
            
        # Calculate average resonance
        avg_resonance = total_resonance / pair_count
        
        return avg_resonance
    
    def _attractor_alignment(self, field: Any) -> float:
        """Calculate coherence based on alignment with attractors."""
        # Get attractors and patterns
        attractors = self._get_attractors(field)
        patterns = self._sample_patterns(field)
        
        if not attractors:
            return self._pairwise_coherence(field)  # Fall back to pairwise if no attractors
            
        # Calculate alignment with attractors
        total_alignment = 0.0
        total_weight = 0.0
        
        for pattern, pattern_strength in patterns:
            # Calculate alignment with each attractor
            best_alignment = 0.0
            for attractor, attractor_strength in attractors:
                alignment = self.resonance_measurer.measure(pattern, attractor)
                if alignment > best_alignment:
                    best_alignment = alignment
            
            # Weight by pattern strength
            total_alignment += best_alignment * pattern_strength
            total_weight += pattern_strength
        
        if total_weight == 0:
            return 0.0
            
        # Calculate average alignment
        avg_alignment = total_alignment / total_weight
        
        return avg_alignment
    
    def _entropy_coherence(self, field: Any) -> float:
        """Calculate coherence based on entropy reduction."""
        # This is a simplified approximation of entropy-based coherence
        # A full implementation would use proper information theory metrics
        
        # Get patterns and attractors
        patterns = self._sample_patterns(field)
        attractors = self._get_attractors(field)
        
        if not patterns:
            return 0.0
            
        # Calculate pattern organization
        organization = 0.0
        total_strength = sum(strength for _, strength in patterns)
        
        for pattern, pattern_strength in patterns:
            # Find most resonant attractor
            best_resonance = 0.0
            for attractor, _ in attractors:
                resonance = self.resonance_measurer.measure(pattern, attractor)
                if resonance > best_resonance:
                    best_resonance = resonance
            
            # More organized patterns contribute to lower entropy
            pattern_organization = best_resonance * (pattern_strength / total_strength)
            organization += pattern_organization
        
        # Convert to coherence score (higher organization = higher coherence)
        coherence = organization
        
        return coherence
    
    def _sample_patterns(self, field: Any) -> List[Tuple[str, float]]:
        """Sample patterns from the field based on sampling strategy."""
        # Extract patterns from field
        try:
            patterns = [(pattern, strength) for pattern, strength in field.state.items()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                patterns = field.get_patterns()
            except (AttributeError, TypeError):
                logger.warning("Could not extract patterns from field, using empty list")
                return []
        
        if not patterns:
            return []
            
        # Apply sampling strategy
        if self.sampling == "full" or len(patterns) <= self.sample_size:
            return patterns
            
        if self.sampling == "random":
            import random
            return random.sample(patterns, min(self.sample_size, len(patterns)))
            
        if self.sampling == "strength_weighted":
            # Sort by strength and take top patterns
            sorted_patterns = sorted(patterns, key=lambda x: x[1], reverse=True)
            return sorted_patterns[:self.sample_size]
            
        # Default to full sampling
        return patterns
    
    def _get_attractors(self, field: Any) -> List[Tuple[str, float]]:
        """Extract attractors from the field."""
        try:
            attractors = [(attractor['pattern'], attractor['strength']) 
                         for attractor in field.attractors.values()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                attractors = field.get_attractors()
            except (AttributeError, TypeError):
                logger.warning("Could not extract attractors from field, using empty list")
                return []
        
        return attractors

# ------------------------------------------------------------------------------
# Stability Measurement
# ------------------------------------------------------------------------------

class StabilityMeasurer:
    """Measures stability of a neural field."""
    
    def __init__(self, attractor_weight: float = 0.6, organization_weight: float = 0.4):
        """
        Initialize the stability measurer.
        
        Args:
            attractor_weight: Weight for attractor strength in stability calculation
            organization_weight: Weight for pattern organization in stability calculation
        """
        self.attractor_weight = attractor_weight
        self.organization_weight = organization_weight
        self.coherence_measurer = CoherenceMeasurer()
    
    def measure(self, field: Any) -> float:
        """
        Measure stability of a field.
        
        Args:
            field: Neural field to measure
            
        Returns:
            Stability score (0.0 to 1.0)
        """
        # Get attractors
        attractors = self._get_attractors(field)
        
        if not attractors:
            return 0.0  # No attractors = no stability
            
        # Calculate average attractor strength
        avg_attractor_strength = sum(strength for _, strength in attractors) / len(attractors)
        
        # Calculate pattern organization (using coherence as a proxy)
        organization = self.coherence_measurer.measure(field)
        
        # Combine metrics
        stability = (avg_attractor_strength * self.attractor_weight) + (organization * self.organization_weight)
        
        return min(1.0, stability)  # Cap at 1.0
    
    def _get_attractors(self, field: Any) -> List[Tuple[str, float]]:
        """Extract attractors from the field."""
        try:
            attractors = [(attractor['pattern'], attractor['strength']) 
                         for attractor in field.attractors.values()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                attractors = field.get_attractors()
            except (AttributeError, TypeError):
                logger.warning("Could not extract attractors from field, using empty list")
                return []
        
        return attractors

# ------------------------------------------------------------------------------
# Comprehensive Field Metrics
# ------------------------------------------------------------------------------

class FieldResonanceMeasurer:
    """
    Comprehensive tool for measuring neural field properties.
    Combines resonance, coherence, stability, and other metrics.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the field resonance measurer.
        
        Args:
            config_path: Path to configuration file (YAML)
        """
        self.config = self._load_config(config_path)
        
        # Initialize component measurers
        self.resonance_measurer = ResonanceMeasurer(
            method=self.config.get('resonance', {}).get('method', 'cosine'),
            threshold=self.config.get('resonance', {}).get('threshold', 0.2),
            amplification=self.config.get('resonance', {}).get('amplification', 1.2)
        )
        
        self.coherence_measurer = CoherenceMeasurer(
            method=self.config.get('coherence', {}).get('method', 'attractor_alignment'),
            sampling=self.config.get('coherence', {}).get('sampling', 'strength_weighted'),
            sample_size=self.config.get('coherence', {}).get('sample_size', 100)
        )
        
        self.stability_measurer = StabilityMeasurer(
            attractor_weight=self.config.get('stability', {}).get('attractor_weight', 0.6),
            organization_weight=self.config.get('stability', {}).get('organization_weight', 0.4)
        )
    
    def _load_config(self, config_path: Optional[str]) -> Dict[str, Any]:
        """Load configuration from file or use defaults."""
        if config_path:
            try:
                with open(config_path, 'r') as f:
                    return yaml.safe_load(f)
            except Exception as e:
                logger.warning(f"Failed to load config from {config_path}: {e}")
                logger.info("Using default configuration")
        
        # Default configuration
        return {
            'resonance': {
                'method': 'cosine',
                'threshold': 0.2,
                'amplification': 1.2
            },
            'coherence': {
                'method': 'attractor_alignment',
                'sampling': 'strength_weighted',
                'sample_size': 100
            },
            'stability': {
                'attractor_weight': 0.6,
                'organization_weight': 0.4
            }
        }
    
    def measure_resonance(self, pattern1: str, pattern2: str) -> float:
        """
        Measure resonance between two patterns.
        
        Args:
            pattern1: First pattern
            pattern2: Second pattern
            
        Returns:
            Resonance score (0.0 to 1.0)
        """
        return self.resonance_measurer.measure(pattern1, pattern2)
    
    def measure_coherence(self, field: Any) -> float:
        """
        Measure coherence of a field.
        
        Args:
            field: Neural field to measure
            
        Returns:
            Coherence score (0.0 to 1.0)
        """
        return self.coherence_measurer.measure(field)
    
    def measure_stability(self, field: Any) -> float:
        """
        Measure stability of a field.
        
        Args:
            field: Neural field to measure
            
        Returns:
            Stability score (0.0 to 1.0)
        """
        return self.stability_measurer.measure(field)
    
    def get_field_metrics(self, field: Any) -> Dict[str, float]:
        """
        Get comprehensive metrics for a field.
        
        Args:
            field: Neural field to measure
            
        Returns:
            Dictionary of metrics
        """
        # Basic metrics
        metrics = {
            'coherence': self.measure_coherence(field),
            'stability': self.measure_stability(field)
        }
        
        # Add attractor metrics
        attractors = self._get_attractors(field)
        if attractors:
            metrics['attractor_count'] = len(attractors)
            metrics['avg_attractor_strength'] = sum(strength for _, strength in attractors) / len(attractors)
            metrics['max_attractor_strength'] = max(strength for _, strength in attractors) if attractors else 0.0
        else:
            metrics['attractor_count'] = 0
            metrics['avg_attractor_strength'] = 0.0
            metrics['max_attractor_strength'] = 0.0
        
        # Add pattern metrics
        patterns = self._get_patterns(field)
        if patterns:
            metrics['pattern_count'] = len(patterns)
            metrics['avg_pattern_strength'] = sum(strength for _, strength in patterns) / len(patterns)
        else:
            metrics['pattern_count'] = 0
            metrics['avg_pattern_strength'] = 0.0
        
        # Calculate entropy (information disorder)
        entropy = self._calculate_entropy(field)
        metrics['entropy'] = entropy
        
        # Calculate information density
        if patterns:
            total_chars = sum(len(pattern) for pattern, _ in patterns)
            metrics['information_density'] = total_chars / max(1, len(patterns))
        else:
            metrics['information_density'] = 0.0
        
        return metrics
    
    def _get_attractors(self, field: Any) -> List[Tuple[str, float]]:
        """Extract attractors from the field."""
        try:
            attractors = [(attractor['pattern'], attractor['strength']) 
                         for attractor in field.attractors.values()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                attractors = field.get_attractors()
            except (AttributeError, TypeError):
                logger.warning("Could not extract attractors from field, using empty list")
                return []
        
        return attractors
    
    def _get_patterns(self, field: Any) -> List[Tuple[str, float]]:
        """Extract patterns from the field."""
        try:
            patterns = [(pattern, strength) for pattern, strength in field.state.items()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                patterns = field.get_patterns()
            except (AttributeError, TypeError):
                logger.warning("Could not extract patterns from field, using empty list")
                return []
        
        return patterns
    
    def _calculate_entropy(self, field: Any) -> float:
        """
        Calculate the entropy (disorder) of the field.
        Higher entropy = more disorder = less organization.
        
        Args:
            field: Neural field to measure
            
        Returns:
            Entropy score (0.0 to 1.0)
        """
        # Get patterns
        patterns = self._get_patterns(field)
        
        if not patterns:
            return 1.0  # Maximum entropy for empty field
            
        # Calculate total strength
        total_strength = sum(strength for _, strength in patterns)
        
        if total_strength == 0:
            return 1.0
            
        # Calculate probabilities
        probabilities = [strength / total_strength for _, strength in patterns]
        
        # Calculate Shannon entropy
        entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
        
        # Normalize to 0-1 range
        max_entropy = math.log2(len(patterns))
        if max_entropy == 0:
            normalized_entropy = 0.0
        else:
            normalized_entropy = entropy / max_entropy
        
        return normalized_entropy
    
    def visualize_field(self, field: Any, format: str = "ascii") -> str:
        """
        Generate a visualization of the field.
        
        Args:
            field: Neural field to visualize
            format: Visualization format ("ascii", "text", "json")
            
        Returns:
            Visualization string
        """
        if format == "json":
            return self._visualize_json(field)
        elif format == "text":
            return self._visualize_text(field)
        else:
            return self._visualize_ascii(field)
    
    def _visualize_ascii(self, field: Any) -> str:
        """Generate ASCII visualization of the field."""
        # Get field components
        attractors = self._get_attractors(field)
        patterns = self._get_patterns(field)
        metrics = self.get_field_metrics(field)
        
        # Sort by strength
        attractors = sorted(attractors, key=lambda x: x[1], reverse=True)
        patterns = sorted(patterns, key=lambda x: x[1], reverse=True)
        
        # Build visualization
        lines = []
        lines.append("=" * 80)
        lines.append("NEURAL FIELD VISUALIZATION")
        lines.append("=" * 80)
        
        # Add metrics
        lines.append("FIELD METRICS:")
        lines.append(f"Coherence:    {'*' * int(metrics['coherence'] * 20):<20} {metrics['coherence']:.2f}")
        lines.append(f"Stability:     {'*' * int(metrics['stability'] * 20):<20} {metrics['stability']:.2f}")
        lines.append(f"Entropy:       {'*' * int(metrics['entropy'] * 20):<20} {metrics['entropy']:.2f}")
        lines.append(f"Attractors:    {metrics['attractor_count']}")
        lines.append(f"Patterns:      {metrics['pattern_count']}")
        lines.append("-" * 80)
        
        # Add attractors
        lines.append("ATTRACTORS:")
        for i, (pattern, strength) in enumerate(attractors[:5]):  # Show top 5
            short_pattern = pattern[:50] + "..." if len(pattern) > 50 else pattern
            lines.append(f"A{i+1} ({strength:.2f}): {'#' * int(strength * 20):<20} {short_pattern}")
        lines.append("-" * 80)
        
        # Add active patterns
        lines.append("ACTIVE PATTERNS:")
        for i, (pattern, strength) in enumerate(patterns[:7]):  # Show top 7
            short_pattern = pattern[:40] + "..." if len(pattern) > 40 else pattern
            lines.append(f"P{i+1} ({strength:.2f}): {'*' * int(strength * 20):<20} {short_pattern}")
        lines.append("-" * 80)
        
        # Add resonance visualization
        if attractors and patterns:
            lines.append("RESONANCE MAP:")
            # Show resonance between top attractors and patterns
            for i, (pattern, p_strength) in enumerate(patterns[:3]):  # Top 3 patterns
                for j, (attractor, a_strength) in enumerate(attractors[:3]):  # Top 3 attractors
                    resonance = self.resonance_measurer.measure(pattern, attractor)
                    if resonance > 0.2:  # Only show significant resonance
                        lines.append(f"P{i+1} ↔ A{j+1}: {'-' * int(resonance * 20):<20} {resonance:.2f}")
            lines.append("-" * 80)
        
        return "\n".join(lines)
    
    def _visualize_text(self, field: Any) -> str:
        """Generate text visualization of the field."""
        # Get field components
        attractors = self._get_attractors(field)
        patterns = self._get_patterns(field)
        metrics = self.get_field_metrics(field)
        
        # Build visualization
        lines = []
        lines.append("NEURAL FIELD STATE")
        lines.append("")
        
        # Add metrics
        lines.append("Field Metrics:")
        lines.append(f"- Coherence: {metrics['coherence']:.2f}")
        lines.append(f"- Stability: {metrics['stability']:.2f}")
        lines.append(f"- Entropy: {metrics['entropy']:.2f}")
        lines.append(f"- Attractor count: {metrics['attractor_count']}")
        lines.append(f"- Pattern count: {metrics['pattern_count']}")
        lines.append("")
        
        # Add attractors
        lines.append("Key Attractors:")
        for i, (pattern, strength) in enumerate(sorted(attractors, key=lambda x: x[1], reverse=True)[:3]):
            short_pattern = pattern[:100] + "..." if len(pattern) > 100 else pattern
            lines.append(f"- Attractor {i+1} (Strength: {strength:.2f}): {short_pattern}")
        lines.append("")
        
        # Add patterns
        lines.append("Active Patterns:")
        for i, (pattern, strength) in enumerate(sorted(patterns, key=lambda x: x[1], reverse=True)[:5]):
            short_pattern = pattern[:80] + "..." if len(pattern) > 80 else pattern
            lines.append(f"- Pattern {i+1} (Strength: {strength:.2f}): {short_pattern}")
        
        return "\n".join(lines)
    
    def _visualize_json(self, field: Any) -> str:
        """Generate JSON visualization of the field."""
        # Get field components
        attractors = self._get_attractors(field)
        patterns = self._get_patterns(field)
        metrics = self.get_field_metrics(field)
        
        # Prepare data structure
        data = {
            "metrics": metrics,
            "attractors": [
                {
                    "id": f"A{i+1}",
                    "pattern": pattern[:100] + "..." if len(pattern) > 100 else pattern,
                    "strength": strength
                }
                for i, (pattern, strength) in enumerate(sorted(attractors, key=lambda x: x[1], reverse=True)[:5])
            ],
            "patterns": [
                {
                    "id": f"P{i+1}",
                    "pattern": pattern[:80] + "..." if len(pattern) > 80 else pattern,
                    "strength": strength
                }
                for i, (pattern, strength) in enumerate(sorted(patterns, key=lambda x: x[1], reverse=True)[:7])
            ],
            "resonance": []
        }
        
        # Add resonance data
        if attractors and patterns:
            top_attractors = sorted(attractors, key=lambda x: x[1], reverse=True)[:3]
            top_patterns = sorted(patterns, key=lambda x: x[1], reverse=True)[:3]
            
            for i, (pattern, _) in enumerate(top_patterns):
                for j, (attractor, _) in enumerate(top_attractors):
                    resonance = self.resonance_measurer.measure(pattern, attractor)
                    if resonance > 0.2:  # Only include significant resonance
                        data["resonance"].append({
                            "source": f"P{i+1}",
                            "target": f"A{j+1}",
                            "strength": resonance
                        })
        
        # Convert to JSON
        return json.dumps(data, indent=2)

# ------------------------------------------------------------------------------
# Field Analysis Tools
# ------------------------------------------------------------------------------

class FieldAnalyzer:
    """Tools for analyzing neural fields and providing insights."""
    
    def __init__(self, measurer: Optional[FieldResonanceMeasurer] = None):
        """
        Initialize the field analyzer.
        
        Args:
            measurer: FieldResonanceMeasurer instance or None to create a new one
        """
        self.measurer = measurer or FieldResonanceMeasurer()
    
    def analyze_field(self, field: Any) -> Dict[str, Any]:
        """
        Perform comprehensive analysis of a field.
        
        Args:
            field: Neural field to analyze
            
        Returns:
            Analysis results
        """
        # Get basic metrics
        metrics = self.measurer.get_field_metrics(field)
        
        # Get field components
        attractors = self._get_attractors(field)
        patterns = self._get_patterns(field)
        
        # Analyze attractor structure
        attractor_analysis = self._analyze_attractors(attractors)
        
        # Analyze pattern organization
        pattern_analysis = self._analyze_patterns(patterns, attractors)
        
        # Analyze field evolution potential
        evolution_analysis = self._analyze_evolution_potential(field, metrics)
        
        # Compile analysis
        analysis = {
            "metrics": metrics,
            "attractor_analysis": attractor_analysis,
            "pattern_analysis": pattern_analysis,
            "evolution_analysis": evolution_analysis,
            "recommendations": self._generate_recommendations(metrics, attractor_analysis, pattern_analysis)
        }
        
        return analysis
    
    def _get_attractors(self, field: Any) -> List[Tuple[str, float]]:
        """Extract attractors from the field."""
        try:
            attractors = [(attractor['pattern'], attractor['strength']) 
                         for attractor in field.attractors.values()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                attractors = field.get_attractors()
            except (AttributeError, TypeError):
                logger.warning("Could not extract attractors from field, using empty list")
                return []
        
        return attractors
    
    def _get_patterns(self, field: Any) -> List[Tuple[str, float]]:
        """Extract patterns from the field."""
        try:
            patterns = [(pattern, strength) for pattern, strength in field.state.items()]
        except AttributeError:
            # Handle case where field structure is different
            try:
                patterns = field.get_patterns()
            except (AttributeError, TypeError):
                logger.warning("Could not extract patterns from field, using empty list")
                return []
        
        return patterns
    
    def _analyze_attractors(self, attractors: List[Tuple[str, float]]) -> Dict[str, Any]:
        """
        Analyze attractor structure.
        
        Args:
            attractors: List of (pattern, strength) tuples
            
        Returns:
            Attractor analysis
        """
        if not attractors:
            return {
                "count": 0,
                "strength_distribution": "none",
                "diversity": 0.0,
                "dominant_theme": None
            }
        
        # Count attractors
        count = len(attractors)
        
        # Analyze strength distribution
        strengths = [strength for _, strength in attractors]
        max_strength = max(strengths)
        min_strength = min(strengths)
        avg_strength = sum(strengths) / count
        strength_range = max_strength - min_strength
        
        if strength_range < 0.2:
            strength_distribution = "uniform"
        elif max_strength > 0.8 and avg_strength < 0.5:
            strength_distribution = "dominant"
        else:
            strength_distribution = "balanced"
        
        # Analyze diversity
        # A simple approximation: check pairwise similarity
        total_similarity = 0.0
        pair_count = 0
        
        for i, (pattern1, _) in enumerate(attractors):
            for j, (pattern2, _) in enumerate(attractors):
                if i < j:  # Only compare each pair once
                    similarity = self.measurer.measure_resonance(pattern1, pattern2)
                    total_similarity += similarity
                    pair_count += 1
        
        diversity = 1.0 - (total_similarity / max(1, pair_count))
        
        # Identify dominant theme (simplified)
        strongest_attractor = max(attractors, key=lambda x: x[1])
        dominant_theme = strongest_attractor[0][:50] + "..." if len(strongest_attractor[0]) > 50 else strongest_attractor[0]
        
        return {
            "count": count,
            "strength_distribution": strength_distribution,
            "diversity": diversity,
            "dominant_theme": dominant_theme,
            "max_strength": max_strength,
            "min_strength": min_strength,
            "avg_strength": avg_strength
        }
    
    def _analyze_patterns(self, patterns: List[Tuple[str, float]], 
                         attractors: List[Tuple[str, float]]) -> Dict[str, Any]:
        """
        Analyze pattern organization.
        
        Args:
            patterns: List of (pattern, strength) tuples
            attractors: List of (pattern, strength) tuples
            
        Returns:
            Pattern analysis
        """
        if not patterns:
            return {
                "count": 0,
                "organization": "none",
                "attractor_alignment": 0.0,
                "fragmentation": 0.0
            }
        
        # Count patterns
        count = len(patterns)
        
        # Analyze pattern strength distribution
        strengths = [strength for _, strength in patterns]
        max_strength = max(strengths) if strengths else 0.0
        min_strength = min(strengths) if strengths else 0.0
        avg_strength = sum(strengths) / count if count > 0 else 0.0
        
        # Calculate attractor alignment
        if attractors:
            total_alignment = 0.0
            for pattern, pattern_strength in patterns:
                best_alignment = 0.0
                for attractor, _ in attractors:
                    alignment = self.measurer.measure_resonance(pattern, attractor)
                    if alignment > best_alignment:
                        best_alignment = alignment
                
                total_alignment += best_alignment * pattern_strength
            
            attractor_alignment = total_alignment / sum(strengths) if sum(strengths) > 0 else 0.0
        else:
            attractor_alignment = 0.0
        
        # Analyze fragmentation
        # Check how many disconnected pattern clusters exist
        if count > 1:
            # Simple approximation: count patterns with low similarity to any other
            isolated_patterns = 0
            for i, (pattern1, _) in enumerate(patterns):
                max_similarity = 0.0
                for j, (pattern2, _) in enumerate(patterns):
                    if i != j:
                        similarity = self.measurer.measure_resonance(pattern1, pattern2)
                        if similarity > max_similarity:
                            max_similarity = similarity
                
                if max_similarity < 0.3:  # Threshold for isolation
                    isolated_patterns += 1
            
            fragmentation = isolated_patterns / count
        else:
            fragmentation = 0.0
        
        # Determine organization type
        if attractor_alignment > 0.7:
            organization = "strongly_aligned"
        elif attractor_alignment > 0.4:
            organization = "moderately_aligned"
        elif fragmentation > 0.5:
            organization = "fragmented"
        else:
            organization = "loosely_connected"
        
        return {
            "count": count,
            "organization": organization,
            "attractor_alignment": attractor_alignment,
            "fragmentation": fragmentation,
            "max_strength": max_strength,
            "min_strength": min_strength,
            "avg_strength": avg_strength
        }
    
    def _analyze_evolution_potential(self, field: Any, metrics: Dict[str, float]) -> Dict[str, Any]:
        """
        Analyze field evolution potential.
        
        Args:
            field: Neural field to analyze
            metrics: Field metrics
            
        Returns:
            Evolution analysis
        """
        # Analyze stability vs. plasticity
        stability = metrics.get('stability', 0.0)
        entropy = metrics.get('entropy', 1.0)
        
        plasticity = 1.0 - stability
        
        # Determine evolution potential
        if stability > 0.8 and entropy < 0.3:
            # High stability, low entropy = rigid field
            evolution_potential = "limited"
            bottleneck = "field_rigidity"
        elif stability < 0.3 and entropy > 0.7:
            # Low stability, high entropy = chaotic field
            evolution_potential = "unstable"
            bottleneck = "field_instability"
        elif stability > 0.6 and entropy > 0.6:
            # High stability, high entropy = critical field
            evolution_potential = "optimal"
            bottleneck = None
        else:
            # Balanced field
            evolution_potential = "moderate"
            bottleneck = "needs_tuning"
        
        # Determine optimal operations
        if evolution_potential == "limited":
            recommended_operations = ["attenuate_attractors", "inject_novelty"]
        elif evolution_potential == "unstable":
            recommended_operations = ["strengthen_attractors", "prune_weak_patterns"]
        elif evolution_potential == "optimal":
            recommended_operations = ["maintain_balance", "selective_amplification"]
        else:
            recommended_operations = ["tune_parameters", "consolidate_patterns"]
        
        return {
            "evolution_potential": evolution_potential,
            "bottleneck": bottleneck,
            "stability": stability,
            "plasticity": plasticity,
            "recommended_operations": recommended_operations
        }
    
    def _generate_recommendations(self, metrics: Dict[str, float],
                                attractor_analysis: Dict[str, Any],
                                pattern_analysis: Dict[str, Any]) -> List[str]:
        """
        Generate recommendations for field improvement.
        
        Args:
            metrics: Field metrics
            attractor_analysis: Attractor analysis
            pattern_analysis: Pattern analysis
            
        Returns:
            List of recommendations
        """
        recommendations = []
        
        # Check attractor structure
        if attractor_analysis["count"] == 0:
            recommendations.append("Create initial attractors to provide field structure")
        elif attractor_analysis["count"] < 3:
            recommendations.append("Add more attractors to create a richer field structure")
        elif attractor_analysis["diversity"] < 0.3:
            recommendations.append("Increase attractor diversity to cover broader semantic space")
        
        if attractor_analysis.get("strength_distribution") == "dominant" and attractor_analysis.get("count") > 1:
            recommendations.append("Balance attractor strengths to avoid over-dominance")
        
        # Check pattern organization
        if pattern_analysis["organization"] == "fragmented":
            recommendations.append("Reduce fragmentation by strengthening relationships between patterns")
        
        if pattern_analysis["attractor_alignment"] < 0.3 and attractor_analysis["count"] > 0:
            recommendations.append("Improve alignment between patterns and attractors")
        
        # Check field metrics
        if metrics.get("coherence", 0.0) < 0.4:
            recommendations.append("Increase field coherence through pattern consolidation")
        
        if metrics.get("stability", 0.0) < 0.3:
            recommendations.append("Improve field stability by strengthening attractors")
        elif metrics.get("stability", 0.0) > 0.9:
            recommendations.append("Introduce controlled instability to enable field evolution")
        
        if metrics.get("entropy", 0.0) > 0.8:
            recommendations.append("Reduce entropy through pattern organization")
        elif metrics.get("entropy", 0.0) < 0.2:
            recommendations.append("Increase entropy to enable more diverse field states")
        
        # Ensure we have at least one recommendation
        if not recommendations:
            if metrics.get("coherence", 0.0) > 0.7 and metrics.get("stability", 0.0) > 0.7:
                recommendations.append("Maintain current field state with periodic reinforcement")
            else:
                recommendations.append("Tune field parameters based on application requirements")
        
        return recommendations

# ------------------------------------------------------------------------------
# Usage Examples
# ------------------------------------------------------------------------------

def measure_field_resonance_example():
    """Example usage of field resonance measurement."""
    # Create a simple mock field for demonstration
    class MockField:
        def __init__(self):
            self.state = {
                "Neural fields treat context as a continuous medium.": 0.9,
                "Information persists through resonance rather than explicit storage.": 0.8,
                "Patterns that align with existing field structures decay more slowly.": 0.7,
                "Field boundaries determine how information flows in and out.": 0.6,
                "New inputs interact with the entire field, not just recent tokens.": 0.5
            }
            self.attractors = {
                "attractor1": {
                    "pattern": "Neural fields represent context as a continuous semantic landscape.",
                    "strength": 0.9
                },
                "attractor2": {
                    "pattern": "Resonance is a key mechanism for information persistence.",
                    "strength": 0.8
                }
            }
    
    # Create a field
    field = MockField()
    
    # Create a measurer
    measurer = FieldResonanceMeasurer()
    
    # Measure resonance between two patterns
    pattern1 = "Neural fields enable persistent context."
    pattern2 = "Information persists in neural fields through resonance."
    resonance = measurer.measure_resonance(pattern1, pattern2)
    print(f"Resonance between patterns: {resonance:.2f}")
    
    # Measure field coherence
    coherence = measurer.measure_coherence(field)
    print(f"Field coherence: {coherence:.2f}")
    
    # Measure field stability
    stability = measurer.measure_stability(field)
    print(f"Field stability: {stability:.2f}")
    
    # Get comprehensive metrics
    metrics = measurer.get_field_metrics(field)
    print("Field metrics:")
    for key, value in metrics.items():
        print(f"- {key}: {value:.2f}")
    
    # Visualize the field
    visualization = measurer.visualize_field(field, format="ascii")
    print("\nField visualization:")
    print(visualization)
    
    # Analyze the field
    analyzer = FieldAnalyzer(measurer)
    analysis = analyzer.analyze_field(field)
    
    print("\nField analysis:")
    print(f"Evolution potential: {analysis['evolution_analysis']['evolution_potential']}")
    print("Recommendations:")
    for recommendation in analysis['recommendations']:
        print(f"- {recommendation}")

if __name__ == "__main__":
    # Example usage
    measure_field_resonance_example()
