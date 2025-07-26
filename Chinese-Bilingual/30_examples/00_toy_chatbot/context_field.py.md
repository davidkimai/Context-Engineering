# `context_field.py`: Context Field Management  
`context_field.py` ：上下文字段管理

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#context_fieldpy-context-field-management)

This module implements the context field, which serves as the continuous semantic substrate for our toy chatbot. The context field represents the transition from discrete token-based contexts to a continuous semantic medium with attractors, resonance, and emergent properties.  
该模块实现了上下文场，它作为我们玩具聊天机器人的连续语义基础。上下文场代表了从基于离散标记的上下文到具有吸引子、共振和涌现属性的连续语义介质的过渡。

## Conceptual Overview: From Tokens to Fields  
概念概述：从标记到字段

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#conceptual-overview-from-tokens-to-fields)

Traditional context management treats information as discrete tokens or chunks. Context engineering's field approach reimagines context as a continuous semantic landscape with:  
传统的上下文管理将信息视为离散的标记或块。上下文工程的场方法将上下文重新想象为一个连续的语义景观，其特点如下：

```python
┌─────────────────────────────────────────────────────────┐
│              CONTEXT FIELD VISUALIZATION                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│                        Z (Semantic Depth)               │
│                        ▲                                │
│                        │                                │
│                        │      Attractor B               │
│                        │      ╱╲                        │
│                        │     /  \                       │
│                        │    /    \                      │
│                        │   /      \        Attractor C  │
│                        │  /        \       ╱╲           │
│                        │ /          \     /  \          │
│  Attractor A           │/            \   /    \         │
│  ╱╲                    │              \ /      \        │
│ /  \                   │               /        \       │
│/    \                  │              /          \      │
│      \                 │             /            \     │
│       \                │            /              \    │
│        \               │           /                \   │
│         \              │          /                  \  │
│          \             │         /                    \ │
│           ╰─────────────────────┼──────────────────────┼─── X (Semantic Dimension 1)
│                                /                         │
│                               /                          │
│                              /                           │
│                             /                            │
│                            /                             │
│                           /                              │
│                          /                               │
│                         /                                │
│                        Y (Semantic Dimension 2)          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Field Concepts  关键字段概念

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#key-field-concepts)

1. **Attractors**: Stable semantic configurations that naturally form in the field, representing coherent concepts or meanings.  
    **吸引子** ：在场中自然形成的稳定语义配置，代表连贯的概念或含义。
    
2. **Resonance**: Mutual reinforcement between compatible patterns, creating coherent structures.  
    **共振** ：兼容模式之间的相互加强，创造出连贯的结构。
    
3. **Field Operations**: Actions that manipulate the field such as injection, decay, boundary manipulation, and attractor formation.  
    **场操作** ：操纵场的动作，例如注入、衰减、边界操纵和吸引子形成。
    
4. **Persistence**: The ability of field patterns to remain stable over time, forming semantic memory.  
    **持久性** ：场模式随时间保持稳定的能力，形成语义记忆。
    
5. **Emergence**: New properties and behaviors that arise from field dynamics, not explicitly programmed.  
    **涌现** ：由场动态产生的、未明确编程的新属性和行为。
    

## Implementation  执行

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#implementation)

Let's implement the context field for our toy chatbot:  
让我们为我们的玩具聊天机器人实现上下文字段：

```python
import time
import json
import uuid
import math
import random
import numpy as np
from typing import Dict, List, Any, Optional, Union, Tuple, Set

class ContextField:
    """
    A continuous semantic field with attractors, resonance, and persistence.
    
    The ContextField serves as the substrate for protocol shell operations,
    enabling sophisticated context management through field dynamics.
    """
    
    def __init__(
        self,
        dimensions: int = 2,
        decay_rate: float = 0.05,
        boundary_permeability: float = 0.8,
        resonance_bandwidth: float = 0.6,
        attractor_threshold: float = 0.7
    ):
        """
        Initialize the context field.
        
        Args:
            dimensions: Number of semantic dimensions in the field
            decay_rate: Base rate of pattern decay
            boundary_permeability: How easily new information enters the field
            resonance_bandwidth: How broadly patterns resonate with each other
            attractor_threshold: Threshold for attractor formation
        """
        self.dimensions = dimensions
        self.decay_rate = decay_rate
        self.boundary_permeability = boundary_permeability
        self.resonance_bandwidth = resonance_bandwidth
        self.attractor_threshold = attractor_threshold
        
        # Initialize field components
        self.content = {}  # Semantic content in the field
        self.patterns = {}  # Detected patterns in the field
        self.attractors = {}  # Stable attractors in the field
        self.pathways = {}  # Connections between field elements
        
        # Field state tracking
        self.state_history = []  # History of field states
        self.operation_log = []  # Log of operations performed on the field
        self.current_time = time.time()  # Current field time
        self.field_id = str(uuid.uuid4())  # Unique identifier for this field
        
        # Initialize field metrics
        self.metrics = {
            "coherence": 0.5,  # Initial field coherence
            "stability": 0.7,  # Initial field stability
            "boundary_integrity": 0.9,  # Initial boundary integrity
            "attractor_strength": 0.6,  # Initial attractor strength
            "overall_health": 0.0  # Will be calculated
        }
        self._update_overall_health()
        
        # Initialize empty field - in a real implementation, this would be a 
        # multidimensional semantic space representation
        self._initialize_empty_field()
    
    def _initialize_empty_field(self):
        """Initialize an empty semantic field."""
        # In a real implementation, this might use vector embeddings or 
        # another representation of semantic space
        # For this toy implementation, we'll use a simplified representation
        
        # Create a grid representation for visualization purposes
        grid_size = 10
        self.field_grid = np.zeros((grid_size, grid_size))
        
        # Initialize with a small amount of random noise
        self.field_grid += np.random.normal(0, 0.05, (grid_size, grid_size))
        
        # Log initialization
        self._log_operation("initialize_field", {"dimensions": self.dimensions})
    
    def _update_overall_health(self):
        """Update the overall health metric based on component metrics."""
        self.metrics["overall_health"] = (
            self.metrics["coherence"] * 0.3 +
            self.metrics["stability"] * 0.3 +
            self.metrics["boundary_integrity"] * 0.2 +
            self.metrics["attractor_strength"] * 0.2
        )
    
    def _log_operation(self, operation_type: str, parameters: Dict[str, Any]):
        """Log an operation performed on the field."""
        operation = {
            "type": operation_type,
            "timestamp": time.time(),
            "parameters": parameters
        }
        self.operation_log.append(operation)
    
    def _take_field_snapshot(self):
        """Take a snapshot of the current field state."""
        snapshot = {
            "timestamp": time.time(),
            "content_count": len(self.content),
            "pattern_count": len(self.patterns),
            "attractor_count": len(self.attractors),
            "pathway_count": len(self.pathways),
            "metrics": self.metrics.copy()
        }
        self.state_history.append(snapshot)
    
    def inject(self, content: str, strength: float = 1.0, position: Optional[Tuple[float, ...]] = None) -> str:
        """
        Inject new content into the field.
        
        Args:
            content: The semantic content to inject
            strength: The initial strength of the content
            position: Optional position in the field (if None, will be determined automatically)
            
        Returns:
            str: ID of the injected content
        """
        # Generate content ID
        content_id = str(uuid.uuid4())
        
        # Apply boundary filtering based on permeability
        effective_strength = strength * self.boundary_permeability
        
        # Determine position in semantic space
        if position is None:
            # In a real implementation, this would use embedding models
            # For this toy implementation, assign random position
            position = tuple(random.random() * 10 for _ in range(self.dimensions))
        
        # Check resonance with existing content
        resonances = {}
        for existing_id, existing_content in self.content.items():
            resonance = self._calculate_resonance(content, existing_content["content"])
            if resonance > 0.2:  # Minimum resonance threshold
                resonances[existing_id] = resonance
        
        # Create content entry
        content_entry = {
            "content": content,
            "strength": effective_strength,
            "position": position,
            "injection_time": time.time(),
            "last_update_time": time.time(),
            "resonances": resonances
        }
        
        # Add to field content
        self.content[content_id] = content_entry
        
        # Update field grid for visualization
        self._update_field_grid(content_entry)
        
        # Log operation
        self._log_operation("inject", {
            "content_id": content_id,
            "content_preview": content[:50] + "..." if len(content) > 50 else content,
            "strength": effective_strength,
            "resonances": len(resonances)
        })
        
        # Detect patterns after injection
        self._detect_patterns()
        
        # Check for attractor formation
        self._check_attractor_formation()
        
        # Take field snapshot
        self._take_field_snapshot()
        
        return content_id
    
    def _update_field_grid(self, content_entry: Dict[str, Any]):
        """Update the field grid with new content for visualization."""
        # Convert position to grid coordinates
        pos = content_entry["position"]
        strength = content_entry["strength"]
        
        # Ensure position is within grid bounds
        if len(pos) >= 2:
            x = min(int(pos[0]), self.field_grid.shape[0] - 1)
            y = min(int(pos[1]), self.field_grid.shape[1] - 1)
            
            # Create a small Gaussian bump centered at the position
            for i in range(max(0, x-2), min(self.field_grid.shape[0], x+3)):
                for j in range(max(0, y-2), min(self.field_grid.shape[1], y+3)):
                    # Calculate distance from center
                    dist = math.sqrt((i - x)**2 + (j - y)**2)
                    # Add Gaussian contribution
                    self.field_grid[i, j] += strength * math.exp(-dist**2)
    
    def _calculate_resonance(self, content1: str, content2: str) -> float:
        """
        Calculate resonance between two content items.
        
        Args:
            content1: First content item
            content2: Second content item
            
        Returns:
            float: Resonance score (0.0 to 1.0)
        """
        # In a real implementation, this would use semantic similarity
        # For this toy implementation, we'll use a simple word overlap measure
        
        # Tokenize to words (simple space splitting for demo)
        words1 = set(content1.lower().split())
        words2 = set(content2.lower().split())
        
        # Calculate overlap (Jaccard similarity)
        if not words1 or not words2:
            return 0.0
        
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        # Basic Jaccard similarity
        similarity = intersection / union if union > 0 else 0.0
        
        # Apply bandwidth modulation
        resonance = similarity * self.resonance_bandwidth
        
        return resonance
    
    def _detect_patterns(self):
        """Detect patterns in the field content."""
        # In a real implementation, this would use sophisticated pattern recognition
        # For this toy implementation, we'll use simple clustering by resonance
        
        # Reset patterns
        self.patterns = {}
        
        # Create a resonance matrix
        content_ids = list(self.content.keys())
        n = len(content_ids)
        resonance_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(i+1, n):  # Only upper triangle
                id1 = content_ids[i]
                id2 = content_ids[j]
                content1 = self.content[id1]["content"]
                content2 = self.content[id2]["content"]
                
                resonance = self._calculate_resonance(content1, content2)
                resonance_matrix[i, j] = resonance
                resonance_matrix[j, i] = resonance  # Symmetric
        
        # Simple clustering: find connected components with resonance > threshold
        pattern_clusters = []
        visited = set()
        resonance_threshold = 0.3
        
        for i in range(n):
            if i in visited:
                continue
            
            # Start a new cluster
            cluster = [i]
            visited.add(i)
            
            # BFS to find connected nodes
            queue = [i]
            while queue:
                node = queue.pop(0)
                for j in range(n):
                    if j not in visited and resonance_matrix[node, j] >= resonance_threshold:
                        cluster.append(j)
                        visited.add(j)
                        queue.append(j)
            
            # Add cluster if it has at least 2 elements
            if len(cluster) >= 2:
                pattern_clusters.append([content_ids[i] for i in cluster])
        
        # Create pattern entries
        for i, cluster in enumerate(pattern_clusters):
            pattern_id = f"pattern_{i}_{uuid.uuid4().hex[:8]}"
            
            # Calculate pattern center and strength
            contents = [self.content[cid]["content"] for cid in cluster]
            strengths = [self.content[cid]["strength"] for cid in cluster]
            
            # Pattern is characterized by most common words across contents
            all_words = []
            for content in contents:
                all_words.extend(content.lower().split())
            
            word_counts = {}
            for word in all_words:
                word_counts[word] = word_counts.get(word, 0) + 1
            
            # Get top words for pattern description
            top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            pattern_desc = " ".join([word for word, _ in top_words])
            
            # Calculate average strength
            avg_strength = sum(strengths) / len(strengths) if strengths else 0.0
            
            # Create pattern entry
            self.patterns[pattern_id] = {
                "description": pattern_desc,
                "content_ids": cluster,
                "strength": avg_strength,
                "detection_time": time.time()
            }
            
            # Log pattern detection
            self._log_operation("detect_pattern", {
                "pattern_id": pattern_id,
                "description": pattern_desc,
                "content_count": len(cluster),
                "strength": avg_strength
            })
    
    def _check_attractor_formation(self):
        """Check if any patterns have reached the threshold to form attractors."""
        for pattern_id, pattern in list(self.patterns.items()):
            if pattern["strength"] >= self.attractor_threshold:
                # Form a new attractor from this pattern
                attractor_id = f"attractor_{uuid.uuid4().hex[:8]}"
                
                attractor = {
                    "pattern": pattern["description"],
                    "strength": pattern["strength"],
                    "basin_width": 0.5 + (0.5 * pattern["strength"]),  # Stronger attractors have wider basins
                    "formation_time": time.time(),
                    "last_update_time": time.time(),
                    "source_pattern": pattern_id,
                    "content_ids": pattern["content_ids"].copy()
                }
                
                # Add to attractors
                self.attractors[attractor_id] = attractor
                
                # Log attractor formation
                self._log_operation("form_attractor", {
                    "attractor_id": attractor_id,
                    "pattern": attractor["pattern"],
                    "strength": attractor["strength"],
                    "basin_width": attractor["basin_width"]
                })
                
                # Update field metrics
                self._update_metrics_after_attractor_formation()
    
    def _update_metrics_after_attractor_formation(self):
        """Update field metrics after attractor formation."""
        # More attractors generally increase field coherence
        attractor_count = len(self.attractors)
        if attractor_count > 0:
            # Calculate average attractor strength
            avg_strength = sum(a["strength"] for a in self.attractors.values()) / attractor_count
            
            # Update metrics
            self.metrics["coherence"] = min(1.0, 0.5 + (0.1 * attractor_count))
            self.metrics["attractor_strength"] = avg_strength
            
            # Stability increases with attractor formation but decreases with too many attractors
            optimal_attractor_count = 5
            if attractor_count <= optimal_attractor_count:
                stability_factor = attractor_count / optimal_attractor_count
            else:
                stability_factor = optimal_attractor_count / attractor_count
            
            self.metrics["stability"] = 0.5 + (0.5 * stability_factor)
            
            # Update overall health
            self._update_overall_health()
    
    def decay(self):
        """Apply natural decay to all field elements."""
        # Apply decay to content
        for content_id, content_item in list(self.content.items()):
            # Calculate decay based on time since last update
            time_diff = time.time() - content_item["last_update_time"]
            time_factor = 1.0 - min(1.0, time_diff / 3600)  # Normalize to hours
            
            # Apply decay
            new_strength = content_item["strength"] * (1.0 - self.decay_rate) * time_factor
            
            # Update or remove if below threshold
            if new_strength > 0.1:  # Minimum strength threshold
                self.content[content_id]["strength"] = new_strength
                self.content[content_id]["last_update_time"] = time.time()
            else:
                # Content has decayed too much, remove it
                del self.content[content_id]
                # Log removal
                self._log_operation("decay_remove_content", {"content_id": content_id})
        
        # Apply decay to patterns
        for pattern_id, pattern in list(self.patterns.items()):
            # Recalculate pattern strength based on content
            content_ids = [cid for cid in pattern["content_ids"] if cid in self.content]
            if content_ids:
                avg_strength = sum(self.content[cid]["strength"] for cid in content_ids) / len(content_ids)
                pattern["strength"] = avg_strength
                pattern["content_ids"] = content_ids
            else:
                # No content left in this pattern, remove it
                del self.patterns[pattern_id]
                # Log removal
                self._log_operation("decay_remove_pattern", {"pattern_id": pattern_id})
        
        # Apply decay to attractors
        for attractor_id, attractor in list(self.attractors.items()):
            # Attractors decay more slowly
            time_diff = time.time() - attractor["last_update_time"]
            time_factor = 1.0 - min(1.0, time_diff / (3600 * 24))  # Normalize to days
            
            # Apply decay
            new_strength = attractor["strength"] * (1.0 - (self.decay_rate * 0.5)) * time_factor
            
            # Update or remove if below threshold
            if new_strength > 0.3:  # Higher threshold for attractors
                self.attractors[attractor_id]["strength"] = new_strength
                self.attractors[attractor_id]["last_update_time"] = time.time()
            else:
                # Attractor has decayed too much, remove it
                del self.attractors[attractor_id]
                # Log removal
                self._log_operation("decay_remove_attractor", {"attractor_id": attractor_id})
        
        # Update field metrics after decay
        self._update_metrics_after_decay()
        
        # Take field snapshot
        self._take_field_snapshot()
        
        # Log operation
        self._log_operation("decay", {"decay_rate": self.decay_rate})
    
    def _update_metrics_after_decay(self):
        """Update field metrics after decay."""
        # After decay, stability and coherence might decrease
        
        # Calculate attractor metrics
        attractor_count = len(self.attractors)
        if attractor_count > 0:
            avg_attractor_strength = sum(a["strength"] for a in self.attractors.values()) / attractor_count
        else:
            avg_attractor_strength = 0.0
        
        # Update metrics
        self.metrics["attractor_strength"] = avg_attractor_strength
        self.metrics["coherence"] = max(0.1, self.metrics["coherence"] * (0.9 + 0.1 * avg_attractor_strength))
        self.metrics["stability"] = max(0.1, self.metrics["stability"] * (0.9 + 0.1 * avg_attractor_strength))
        
        # Update overall health
        self._update_overall_health()
    
    def add_attractor(self, attractor: Dict[str, Any]) -> str:
        """
        Add a new attractor to the field.
        
        Args:
            attractor: The attractor to add
            
        Returns:
            str: ID of the added attractor
        """
        # Generate attractor ID
        attractor_id = f"attractor_{uuid.uuid4().hex[:8]}"
        
        # Ensure required fields are present
        if "pattern" not in attractor:
            attractor["pattern"] = f"Attractor-{attractor_id[-8:]}"
        
        if "strength" not in attractor:
            attractor["strength"] = 0.7
        
        if "formation_time" not in attractor:
            attractor["formation_time"] = time.time()
        
        if "last_update_time" not in attractor:
            attractor["last_update_time"] = time.time()
        
        if "basin_width" not in attractor:
            attractor["basin_width"] = 0.5 + (0.5 * attractor["strength"])
        
        # Add attractor to field
        self.attractors[attractor_id] = attractor
        
        # Log operation
        self._log_operation("add_attractor", {
            "attractor_id": attractor_id,
            "pattern": attractor["pattern"],
            "strength": attractor["strength"]
        })
        
        # Update field metrics
        self._update_metrics_after_attractor_formation()
        
        # Take field snapshot
        self._take_field_snapshot()
        
        return attractor_id
    
    def update_attractor(self, attractor: Dict[str, Any], updates: Dict[str, Any]) -> bool:
        """
        Update an existing attractor.
        
        Args:
            attractor: The attractor to update (or its ID)
            updates: The updates to apply
            
        Returns:
            bool: True if the update was successful
        """
        # Get attractor ID
        if isinstance(attractor, dict):
            # Find the attractor ID from the object
            attractor_id = None
            for aid, a in self.attractors.items():
                if a == attractor:
                    attractor_id = aid
                    break
            
            if attractor_id is None:
                return False  # Attractor not found
        else:
            # Attractor is already an ID
            attractor_id = attractor
            if attractor_id not in self.attractors:
                return False  # Attractor not found
        
        # Apply updates
        for key, value in updates.items():
            if key in self.attractors[attractor_id]:
                self.attractors[attractor_id][key] = value
        
        # Update last update time
        self.attractors[attractor_id]["last_update_time"] = time.time()
        
        # Log operation
        self._log_operation("update_attractor", {
            "attractor_id": attractor_id,
            "updates": list(updates.keys())
        })
        
        # Update field metrics
        self._update_metrics_after_attractor_update()
        
        return True
    
    def _update_metrics_after_attractor_update(self):
        """Update field metrics after attractor update."""
        # Recalculate attractor metrics
        attractor_count = len(self.attractors)
        if attractor_count > 0:
            avg_attractor_strength = sum(a["strength"] for a in self.attractors.values()) / attractor_count
        else:
            avg_attractor_strength = 0.0
        
        # Update metrics
        self.metrics["attractor_strength"] = avg_attractor_strength
        
        # Update overall health
        self._update_overall_health()
    
    def add_pathway(self, pathway: Dict[str, Any]) -> str:
        """
        Add a new pathway between field elements.
        
        Args:
            pathway: The pathway to add
            
        Returns:
            str: ID of the added pathway
        """
        # Generate pathway ID
        pathway_id = f"pathway_{uuid.uuid4().hex[:8]}"
        
        # Ensure required fields are present
        if "from" not in pathway or "to" not in pathway:
            raise ValueError("Pathway must have 'from' and 'to' fields")
        
        if "strength" not in pathway:
            pathway["strength"] = 0.5
        
        if "type" not in pathway:
            pathway["type"] = "generic"
        
        if "creation_time" not in pathway:
            pathway["creation_time"] = time.time()
        
        # Add pathway to field
        self.pathways[pathway_id] = pathway
        
        # Log operation
        self._log_operation("add_pathway", {
            "pathway_id": pathway_id,
            "from": str(pathway["from"]),
            "to": str(pathway["to"]),
            "type": pathway["type"],
            "strength": pathway["strength"]
        })
        
        # Take field snapshot
        self._take_field_snapshot()
        
        return pathway_id
    
    def detect_attractors(self) -> List[Dict[str, Any]]:
        """
        Detect attractors in the field.
        
        Returns:
            List[Dict[str, Any]]: List of attractors
        """
        return list(self.attractors.values())
    
    def detect_patterns(self) -> List[Dict[str, Any]]:
        """
        Detect patterns in the field.
        
        Returns:
            List[Dict[str, Any]]: List of patterns
        """
        return list(self.patterns.values())
    
    def calculate_resonance(self, pattern1: str, pattern2: str) -> float:
        """
        Calculate resonance between two patterns.
        
        Args:
            pattern1: First pattern
            pattern2: Second pattern
            
        Returns:
            float: Resonance score (0.0 to 1.0)
        """
        return self._calculate_resonance(pattern1, pattern2)
    
    def calculate_harmony(self) -> float:
        """
        Calculate overall field harmony.
        
        Returns:
            float: Harmony score (0.0 to 1.0)
        """
        # In a real implementation, this would be a more sophisticated analysis
        # For this toy implementation, use a combination of metrics
        
        harmony = (
            self.metrics["coherence"] * 0.4 +
            self.metrics["stability"] * 0.3 +
            self.metrics["attractor_strength"] * 0.3
        )
        
        return harmony
    
    def calculate_health_metrics(self) -> Dict[str, float]:
        """
        Calculate health metrics for the field.
        
        Returns:
            Dict[str, float]: Health metrics
        """
        return self.metrics.copy()
    
    def adjust_attractors_for_harmony(self, attractors: List[Dict[str, Any]]) -> None:
        """
        Adjust attractors to increase field harmony.
        
        Args:
            attractors: List of attractors to adjust
        """
        # In a real implementation, this would optimize attractor positions and strengths
        # For this toy implementation, just strengthen them slightly
        
        for attractor in attractors:
            if isinstance(attractor, dict) and "pattern" in attractor:
                pattern = attractor["pattern"]
                
                # Find matching attractors in the field
                for aid, field_attractor in self.attractors.items():
                    if self._calculate_resonance(field_attractor["pattern"], pattern) > 0.7:
                        # Strengthen the attractor slightly
                        self.attractors[aid]["strength"] = min(
                            1.0, 
                            self.attractors[aid]["strength"] * 1.1
                        )
                        self.attractors[aid]["last_update_time"] = time.time()
        
        # Update field metrics
        self._update_metrics_after_attractor_update()
        
        # Log operation
        self._log_operation("adjust_attractors_for_harmony", {"attractor_count": len(attractors)})
    
    def execute_repair(self, repair_type: str, target: str, operation: str, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a repair operation on the field.
        
        Args:
            repair_type: Type of repair
            target: Target of the repair
            operation: Operation to perform
            parameters: Parameters for the operation
            
        Returns:
            Dict[str, Any]: Result of the repair
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Execute repair based on type
        if repair_type == "coherence_amplification":
            result = self._execute_coherence_amplification(parameters)
        elif repair_type == "stability_reinforcement":
            result = self._execute_stability_reinforcement(parameters)
        elif repair_type == "boundary_reinforcement":
            result = self._execute_boundary_reinforcement(parameters)
        elif repair_type == "attractor_strengthening":
            result = self._execute_attractor_strengthening(parameters)
        elif repair_type == "attractor_harmonization":
            result = self._execute_attractor_harmonization(parameters)
        elif repair_type == "leak_repair":
            result = self._execute_leak_repair(parameters)
        elif repair_type == "resonance_tuning":
            result = self._execute_resonance_tuning(parameters)
        elif repair_type == "memory_integration":
            result = self._execute_memory_integration(parameters)
        else:
            result["details"]["error"] = f"Unknown repair type: {repair_type}"
        
        # Log operation
        self._log_operation("execute_repair", {
            "repair_type": repair_type,
            "target": target,
            "operation": operation,
            "success": result["success"],
            "improvement": result["improvement"]
        })
        
        # Take field snapshot
        self._take_field_snapshot()
        
        return result
    
    def _execute_coherence_amplification(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute coherence amplification repair.
        
        This repair strengthens coherence by amplifying resonance between compatible patterns.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        amplification_factor = parameters.get("amplification_factor", 1.5)
        target_coherence = parameters.get("target_coherence", 0.7)
        
        # Get current coherence
        initial_coherence = self.metrics["coherence"]
        
        # Find patterns with significant resonance
        pattern_pairs = []
        pattern_ids = list(self.patterns.keys())
        
        for i in range(len(pattern_ids)):
            for j in range(i+1, len(pattern_ids)):
                pattern1 = self.patterns[pattern_ids[i]]
                pattern2 = self.patterns[pattern_ids[j]]
                
                # Calculate resonance between patterns
                resonance = self._calculate_resonance(
                    pattern1["description"], 
                    pattern2["description"]
                )
                
                if resonance > 0.4:  # Threshold for significant resonance
                    pattern_pairs.append((pattern_ids[i], pattern_ids[j], resonance))
        
        # Amplify resonant patterns
        amplified_count = 0
        for id1, id2, resonance in pattern_pairs:
            # Strengthen both patterns
            new_strength1 = min(1.0, self.patterns[id1]["strength"] * amplification_factor)
            new_strength2 = min(1.0, self.patterns[id2]["strength"] * amplification_factor)
            
            self.patterns[id1]["strength"] = new_strength1
            self.patterns[id2]["strength"] = new_strength2
            
            # Check if either pattern can form an attractor
            for pattern_id, pattern in [(id1, self.patterns[id1]), (id2, self.patterns[id2])]:
                if pattern["strength"] >= self.attractor_threshold and pattern_id not in [a.get("source_pattern") for a in self.attractors.values()]:
                    # Form a new attractor from this pattern
                    self.add_attractor({
                        "pattern": pattern["description"],
                        "strength": pattern["strength"],
                        "source_pattern": pattern_id,
                        "content_ids": pattern["content_ids"].copy()
                    })
            
            amplified_count += 1
        
        # Update field metrics
        self.metrics["coherence"] = min(
            1.0, 
            initial_coherence + (0.1 * amplified_count)
        )
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate improvement
        improvement = self.metrics["coherence"] - initial_coherence
        
        # Update result
        result["success"] = improvement > 0
        result["improvement"] = improvement
        result["details"] = {
            "amplified_patterns": amplified_count,
            "initial_coherence": initial_coherence,
            "final_coherence": self.metrics["coherence"]
        }
        
        return result
    
    def _execute_stability_reinforcement(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute stability reinforcement repair.
        
        This repair increases field stability by strengthening attractors and reducing noise.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        strength_factor = parameters.get("strength_factor", 1.5)
        noise_reduction = parameters.get("noise_reduction", 0.5)
        
        # Get current stability
        initial_stability = self.metrics["stability"]
        
        # Strengthen attractors
        strengthened_count = 0
        for attractor_id, attractor in self.attractors.items():
            # Increase attractor strength
            new_strength = min(1.0, attractor["strength"] * strength_factor)
            self.attractors[attractor_id]["strength"] = new_strength
            self.attractors[attractor_id]["last_update_time"] = time.time()
            strengthened_count += 1
        
        # Reduce noise by weakening low-strength patterns
        noise_patterns = [
            pid for pid, pattern in self.patterns.items()
            if pattern["strength"] < 0.4  # Threshold for "noise"
        ]
        
        for pattern_id in noise_patterns:
            # Reduce pattern strength
            self.patterns[pattern_id]["strength"] *= (1.0 - noise_reduction)
        
        # Update field metrics
        stability_improvement = 0.1 * strengthened_count if strengthened_count > 0 else 0
        noise_improvement = 0.05 * len(noise_patterns) if len(noise_patterns) > 0 else 0
        
        self.metrics["stability"] = min(
            1.0, 
            initial_stability + stability_improvement + noise_improvement
        )
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate improvement
        improvement = self.metrics["stability"] - initial_stability
        
        # Update result
        result["success"] = improvement > 0
        result["improvement"] = improvement
        result["details"] = {
            "strengthened_attractors": strengthened_count,
            "noise_patterns_reduced": len(noise_patterns),
            "initial_stability": initial_stability,
            "final_stability": self.metrics["stability"]
        }
        
        return result
    
    def _execute_boundary_reinforcement(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute boundary reinforcement repair.
        
        This repair strengthens field boundaries to maintain integrity.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        reinforcement_factor = parameters.get("reinforcement_factor", 1.5)
        permeability_adjustment = parameters.get("permeability_adjustment", -0.2)
        
        # Get current boundary integrity
        initial_integrity = self.metrics["boundary_integrity"]
        
        # Adjust boundary permeability
        old_permeability = self.boundary_permeability
        new_permeability = max(0.1, min(1.0, old_permeability + permeability_adjustment))
        self.boundary_permeability = new_permeability
        
        # Calculate integrity improvement based on permeability change
        # Lower permeability generally means higher integrity
        integrity_improvement = 0.0
        if permeability_adjustment < 0:  # Reducing permeability
            integrity_improvement = abs(permeability_adjustment) * reinforcement_factor
        
        # Update field metrics
        self.metrics["boundary_integrity"] = min(
            1.0, 
            initial_integrity + integrity_improvement
        )
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate improvement
        improvement = self.metrics["boundary_integrity"] - initial_integrity
        
        # Update result
        result["success"] = improvement > 0
        result["improvement"] = improvement
        result["details"] = {
            "old_permeability": old_permeability,
            "new_permeability": new_permeability,
            "initial_integrity": initial_integrity,
            "final_integrity": self.metrics["boundary_integrity"]
        }
        
        return result
    
    def _execute_attractor_strengthening(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute attractor strengthening repair.
        
        This repair increases the strength of existing attractors.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        amplification_factor = parameters.get("amplification_factor", 1.5)
        min_strength = parameters.get("min_strength", 0.6)
        
        # Get current attractor strength
        initial_strength = self.metrics["attractor_strength"]
        
        # Strengthen attractors
        strengthened_count = 0
        for attractor_id, attractor in self.attractors.items():
            # Increase attractor strength
            new_strength = min(1.0, max(min_strength, attractor["strength"] * amplification_factor))
            
            if new_strength > attractor["strength"]:
                self.attractors[attractor_id]["strength"] = new_strength
                self.attractors[attractor_id]["last_update_time"] = time.time()
                strengthened_count += 1
        
        # Update field metrics
        if strengthened_count > 0:
            # Recalculate average attractor strength
            avg_strength = sum(a["strength"] for a in self.attractors.values()) / len(self.attractors)
            self.metrics["attractor_strength"] = avg_strength
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate improvement
        improvement = self.metrics["attractor_strength"] - initial_strength
        
        # Update result
        result["success"] = improvement > 0
        result["improvement"] = improvement
        result["details"] = {
            "strengthened_attractors": strengthened_count,
            "initial_strength": initial_strength,
            "final_strength": self.metrics["attractor_strength"]
        }
        
        return result
    
    def _execute_attractor_harmonization(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute attractor harmonization repair.
        
        This repair resolves conflicts between attractors by adjusting their relationships.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        separation_factor = parameters.get("separation_factor", 0.2)
        resonance_tuning = parameters.get("resonance_tuning", 0.5)
        
        # Find conflicting attractors
        conflicts = []
        attractor_ids = list(self.attractors.keys())
        
        for i in range(len(attractor_ids)):
            for j in range(i+1, len(attractor_ids)):
                id1 = attractor_ids[i]
                id2 = attractor_ids[j]
                attractor1 = self.attractors[id1]
                attractor2 = self.attractors[id2]
                
                # Check for conflict - similar patterns but different meaning
                # In a real implementation, this would use semantic analysis
                # For this toy implementation, use pattern similarity and strength
                pattern_similarity = self._calculate_resonance(
                    attractor1["pattern"], 
                    attractor2["pattern"]
                )
                
                # Conflicting attractors have medium similarity but compete for dominance
                if 0.3 < pattern_similarity < 0.7:
                    strength_difference = abs(attractor1["strength"] - attractor2["strength"])
                    
                    if strength_difference < 0.2:  # Close in strength - competing
                        conflicts.append((id1, id2, pattern_similarity))
        
        # Harmonize conflicting attractors
        harmonized_count = 0
        for id1, id2, similarity in conflicts:
            # Strategy 1: Increase separation by adjusting patterns
            # This is simulated in this toy implementation
            self.attractors[id1]["pattern"] += " [harmonized]"
            self.attractors[id2]["pattern"] += " [harmonized]"
            
            # Strategy 2: Balance strengths based on context
            # Strengthen the more relevant attractor
            # In this toy implementation, we'll just strengthen the stronger one
            if self.attractors[id1]["strength"] >= self.attractors[id2]["strength"]:
                self.attractors[id1]["strength"] = min(1.0, self.attractors[id1]["strength"] * (1 + resonance_tuning))
                self.attractors[id2]["strength"] = max(0.3, self.attractors[id2]["strength"] * (1 - separation_factor))
            else:
                self.attractors[id2]["strength"] = min(1.0, self.attractors[id2]["strength"] * (1 + resonance_tuning))
                self.attractors[id1]["strength"] = max(0.3, self.attractors[id1]["strength"] * (1 - separation_factor))
            
            # Update timestamps
            self.attractors[id1]["last_update_time"] = time.time()
            self.attractors[id2]["last_update_time"] = time.time()
            
            harmonized_count += 1
        
        # Calculate improvement
        # In a real implementation, this would measure actual field harmony
        # For this toy implementation, use a simple heuristic
        initial_coherence = self.metrics["coherence"]
        initial_stability = self.metrics["stability"]
        
        if harmonized_count > 0:
            # Harmonization improves both coherence and stability
            self.metrics["coherence"] = min(1.0, initial_coherence + (0.05 * harmonized_count))
            self.metrics["stability"] = min(1.0, initial_stability + (0.05 * harmonized_count))
            
            # Update overall health
            self._update_overall_health()
        
        # Calculate overall improvement
        coherence_improvement = self.metrics["coherence"] - initial_coherence
        stability_improvement = self.metrics["stability"] - initial_stability
        overall_improvement = (coherence_improvement + stability_improvement) / 2
        
        # Update result
        result["success"] = harmonized_count > 0
        result["improvement"] = overall_improvement
        result["details"] = {
            "conflicts_found": len(conflicts),
            "attractors_harmonized": harmonized_count,
            "coherence_improvement": coherence_improvement,
            "stability_improvement": stability_improvement
        }
        
        return result
    
    def _execute_leak_repair(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute leak repair operation.
        
        This repair fixes boundary leaks that allow unwanted information flow.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        seal_strength = parameters.get("seal_strength", 1.2)
        boundary_reset = parameters.get("boundary_reset", True)
        
        # Get current boundary integrity
        initial_integrity = self.metrics["boundary_integrity"]
        
        # Detect leaks (simulated in this toy implementation)
        # In a real implementation, this would analyze boundary crossing patterns
        # For simplicity, we'll assume leaks are present and repair them
        
        # Repair strategy 1: Strengthen boundaries
        integrity_improvement = (1.0 - initial_integrity) * 0.5 * seal_strength
        
        # Repair strategy 2: Reset boundary if specified
        if boundary_reset:
            # Reset permeability to a more restrictive value
            self.boundary_permeability = max(0.3, self.boundary_permeability * 0.8)
            integrity_improvement += 0.1  # Additional improvement from reset
        
        # Update field metrics
        self.metrics["boundary_integrity"] = min(
            1.0, 
            initial_integrity + integrity_improvement
        )
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate improvement
        improvement = self.metrics["boundary_integrity"] - initial_integrity
        
        # Update result
        result["success"] = improvement > 0
        result["improvement"] = improvement
        result["details"] = {
            "seal_strength_applied": seal_strength,
            "boundary_reset": boundary_reset,
            "new_permeability": self.boundary_permeability,
            "initial_integrity": initial_integrity,
            "final_integrity": self.metrics["boundary_integrity"]
        }
        
        return result
    
    def _execute_resonance_tuning(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute resonance tuning repair.
        
        This repair adjusts field resonance to improve pattern harmony.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        harmonic_factor = parameters.get("harmonic_factor", 1.2)
        interference_dampening = parameters.get("interference_dampening", 0.7)
        
        # Get current coherence and stability
        initial_coherence = self.metrics["coherence"]
        initial_stability = self.metrics["stability"]
        
        # Adjust resonance bandwidth
        old_bandwidth = self.resonance_bandwidth
        new_bandwidth = min(1.0, max(0.1, old_bandwidth * harmonic_factor))
        self.resonance_bandwidth = new_bandwidth
        
        # Apply interference dampening by reducing noise in the field
        # This is simulated in this toy implementation
        # In a real implementation, this would identify and dampen interference patterns
        
        # Identify weak patterns (considered "noise")
        noise_patterns = [
            pid for pid, pattern in self.patterns.items()
            if pattern["strength"] < 0.3  # Low-strength threshold
        ]
        
        # Dampen noise patterns
        for pattern_id in noise_patterns:
            self.patterns[pattern_id]["strength"] *= (1.0 - interference_dampening)
        
        # Calculate improvement
        # Resonance tuning primarily affects coherence
        coherence_improvement = 0.1 * (new_bandwidth / old_bandwidth - 1)
        
        # Noise reduction affects stability
        stability_improvement = 0.05 * len(noise_patterns) * interference_dampening
        
        # Update field metrics
        self.metrics["coherence"] = min(1.0, initial_coherence + coherence_improvement)
        self.metrics["stability"] = min(1.0, initial_stability + stability_improvement)
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate overall improvement
        overall_improvement = (
            (self.metrics["coherence"] - initial_coherence) + 
            (self.metrics["stability"] - initial_stability)
        ) / 2
        
        # Update result
        result["success"] = overall_improvement > 0
        result["improvement"] = overall_improvement
        result["details"] = {
            "old_resonance_bandwidth": old_bandwidth,
            "new_resonance_bandwidth": new_bandwidth,
            "noise_patterns_dampened": len(noise_patterns),
            "coherence_improvement": self.metrics["coherence"] - initial_coherence,
            "stability_improvement": self.metrics["stability"] - initial_stability
        }
        
        return result
    
    def _execute_memory_integration(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute memory integration repair.
        
        This repair integrates fragmented memory attractors to improve recall and coherence.
        """
        result = {
            "success": False,
            "improvement": 0.0,
            "details": {}
        }
        
        # Get parameters
        integration_strength = parameters.get("integration_strength", 1.2)
        connection_reinforcement = parameters.get("connection_reinforcement", 0.8)
        
        # Get current metrics
        initial_coherence = self.metrics["coherence"]
        initial_stability = self.metrics["stability"]
        
        # Identify memory attractors (in a real implementation, these would be tagged)
        # For this toy implementation, we'll assume all attractors are memory attractors
        memory_attractors = list(self.attractors.keys())
        
        # Identify fragmented memory (attractors that should be connected)
        fragments = []
        for i in range(len(memory_attractors)):
            for j in range(i+1, len(memory_attractors)):
                id1 = memory_attractors[i]
                id2 = memory_attractors[j]
                attractor1 = self.attractors[id1]
                attractor2 = self.attractors[id2]
                
                # Check for fragmentation - semantically related but not connected
                # In a real implementation, this would use sophisticated semantic analysis
                # For this toy implementation, use pattern similarity as a proxy
                pattern_similarity = self._calculate_resonance(
                    attractor1["pattern"], 
                    attractor2["pattern"]
                )
                
                # Check if they're already connected
                connected = False
                for pathway in self.pathways.values():
                    if ((pathway["from"] == id1 and pathway["to"] == id2) or
                        (pathway["from"] == id2 and pathway["to"] == id1)):
                        connected = True
                        break
                
                # If similar but not connected, they may be fragments
                if pattern_similarity > 0.4 and not connected:
                    fragments.append((id1, id2, pattern_similarity))
        
        # Integrate fragments
        integrated_count = 0
        for id1, id2, similarity in fragments:
            # Strategy 1: Create pathway between fragments
            pathway = {
                "from": id1,
                "to": id2,
                "strength": similarity * connection_reinforcement,
                "type": "memory_association"
            }
            self.add_pathway(pathway)
            
            # Strategy 2: Strengthen both attractors
            self.attractors[id1]["strength"] = min(1.0, self.attractors[id1]["strength"] * integration_strength)
            self.attractors[id2]["strength"] = min(1.0, self.attractors[id2]["strength"] * integration_strength)
            
            # Update timestamps
            self.attractors[id1]["last_update_time"] = time.time()
            self.attractors[id2]["last_update_time"] = time.time()
            
            integrated_count += 1
        
        # Calculate improvement
        # Memory integration improves both coherence and stability
        coherence_improvement = 0.05 * integrated_count
        stability_improvement = 0.05 * integrated_count
        
        # Update field metrics
        self.metrics["coherence"] = min(1.0, initial_coherence + coherence_improvement)
        self.metrics["stability"] = min(1.0, initial_stability + stability_improvement)
        
        # Recalculate attractor strength
        if integrated_count > 0:
            avg_strength = sum(a["strength"] for a in self.attractors.values()) / len(self.attractors)
            self.metrics["attractor_strength"] = avg_strength
        
        # Update overall health
        self._update_overall_health()
        
        # Calculate overall improvement
        overall_improvement = (
            (self.metrics["coherence"] - initial_coherence) + 
            (self.metrics["stability"] - initial_stability)
        ) / 2
        
        # Update result
        result["success"] = integrated_count > 0
        result["improvement"] = overall_improvement
        result["details"] = {
            "fragments_found": len(fragments),
            "fragments_integrated": integrated_count,
            "coherence_improvement": self.metrics["coherence"] - initial_coherence,
            "stability_improvement": self.metrics["stability"] - initial_stability
        }
        
        return result
    
    def visualize_field(self, display_mode: str = "attractors"):
        """
        Visualize the context field.
        
        Args:
            display_mode: What to visualize ('attractors', 'patterns', 'grid', 'metrics')
        
        Returns:
            Visualization data appropriate for the selected mode
        """
        if display_mode == "attractors":
            return self._visualize_attractors()
        elif display_mode == "patterns":
            return self._visualize_patterns()
        elif display_mode == "grid":
            return self._visualize_grid()
        elif display_mode == "metrics":
            return self._visualize_metrics()
        else:
            raise ValueError(f"Unknown display mode: {display_mode}")
    
    def _visualize_attractors(self):
        """Visualize attractors in the field."""
        # Create a dictionary of attractor information for visualization
        attractor_vis = {}
        
        for attractor_id, attractor in self.attractors.items():
            # Create visualization data
            vis_data = {
                "pattern": attractor["pattern"],
                "strength": attractor["strength"],
                "basin_width": attractor.get("basin_width", 0.5),
                "age": time.time() - attractor.get("formation_time", time.time()),
                "connections": []
            }
            
            # Find connections to other attractors
            for pathway_id, pathway in self.pathways.items():
                if pathway["from"] == attractor_id:
                    vis_data["connections"].append({
                        "to": pathway["to"],
                        "strength": pathway["strength"],
                        "type": pathway["type"]
                    })
                elif pathway["to"] == attractor_id:
                    vis_data["connections"].append({
                        "to": pathway["from"],
                        "strength": pathway["strength"],
                        "type": pathway["type"]
                    })
            
            attractor_vis[attractor_id] = vis_data
        
        return {
            "attractors": attractor_vis,
            "count": len(attractor_vis),
            "avg_strength": sum(a["strength"] for a in self.attractors.values()) / len(self.attractors) if self.attractors else 0,
            "field_coherence": self.metrics["coherence"]
        }
    
    def _visualize_patterns(self):
        """Visualize patterns in the field."""
        # Create a dictionary of pattern information for visualization
        pattern_vis = {}
        
        for pattern_id, pattern in self.patterns.items():
            # Create visualization data
            vis_data = {
                "description": pattern["description"],
                "strength": pattern["strength"],
                "content_count": len(pattern["content_ids"]),
                "age": time.time() - pattern.get("detection_time", time.time())
            }
            
            pattern_vis[pattern_id] = vis_data
        
        return {
            "patterns": pattern_vis,
            "count": len(pattern_vis),
            "avg_strength": sum(p["strength"] for p in self.patterns.values()) / len(self.patterns) if self.patterns else 0
        }
    
    def _visualize_grid(self):
        """Visualize the field grid."""
        # Return the grid data for visualization
        return {
            "grid": self.field_grid.tolist(),
            "dimensions": self.field_grid.shape,
            "min_value": float(self.field_grid.min()),
            "max_value": float(self.field_grid.max()),
            "avg_value": float(self.field_grid.mean())
        }
    
    def _visualize_metrics(self):
        """Visualize field metrics."""
        # Return metrics for visualization
        return {
            "current_metrics": self.metrics,
            "history": [
                {
                    "timestamp": snapshot["timestamp"],
                    "coherence": snapshot["metrics"]["coherence"],
                    "stability": snapshot["metrics"]["stability"],
                    "boundary_integrity": snapshot["metrics"]["boundary_integrity"],
                    "attractor_strength": snapshot["metrics"]["attractor_strength"],
                    "overall_health": snapshot["metrics"]["overall_health"]
                }
                for snapshot in self.state_history[-10:]  # Last 10 snapshots
            ]
        }
    
    def get_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the current field state.
        
        Returns:
            Dict[str, Any]: Summary of field state
        """
        return {
            "field_id": self.field_id,
            "age": time.time() - self.current_time,
            "content_count": len(self.content),
            "pattern_count": len(self.patterns),
            "attractor_count": len(self.attractors),
            "pathway_count": len(self.pathways),
            "operation_count": len(self.operation_log),
            "snapshot_count": len(self.state_history),
            "metrics": self.metrics,
            "parameters": {
                "dimensions": self.dimensions,
                "decay_rate": self.decay_rate,
                "boundary_permeability": self.boundary_permeability,
                "resonance_bandwidth": self.resonance_bandwidth,
                "attractor_threshold": self.attractor_threshold
            }
        }


# Usage demonstration
if __name__ == "__main__":
    # Initialize a context field
    field = ContextField(
        dimensions=2,
        decay_rate=0.05,
        boundary_permeability=0.8,
        resonance_bandwidth=0.6,
        attractor_threshold=0.7
    )
    
    # Inject some content
    field.inject("This is a demonstration of context field operations.", strength=0.8)
    field.inject("Context fields use attractors to represent stable meaning.", strength=0.9)
    field.inject("Attractors naturally form through resonance and pattern detection.", strength=0.7)
    field.inject("Field operations include injection, decay, and attractor formation.", strength=0.8)
    field.inject("Resonance occurs when compatible patterns reinforce each other.", strength=0.7)
    
    # Apply decay to simulate time passing
    field.decay()
    
    # Display field summary
    summary = field.get_summary()
    print("Field Summary:")
    for key, value in summary.items():
        if key != "metrics" and key != "parameters":
            print(f"  {key}: {value}")
    
    print("\nField Metrics:")
    for key, value in summary["metrics"].items():
        print(f"  {key}: {value:.2f}")
    
    # Visualize attractors
    attractor_vis = field.visualize_field("attractors")
    print(f"\nAttractors ({attractor_vis['count']}):")
    for attractor_id, attractor in attractor_vis.get("attractors", {}).items():
        print(f"  {attractor_id}: {attractor['pattern']} (strength: {attractor['strength']:.2f})")
```

# Field Visualization: Understanding Attractors and Resonance  
场可视化：理解吸引子和共振

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#field-visualization-understanding-attractors-and-resonance)

To truly understand how context fields work, it helps to visualize them. Let's explore how attractors and resonance function within a semantic space, using intuitive analogies and clear visuals.  
要真正理解上下文场的工​​作原理，将其可视化会有所帮助。让我们通过直观的类比和清晰的视觉效果，探索吸引子和共振如何在语义空间中发挥作用。

## Attractors in Semantic Space  
语义空间中的吸引子

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#attractors-in-semantic-space)

Imagine a landscape with valleys and hills. In a context field, concepts naturally settle into "valleys" (attractors) based on their meaning. Strong concepts form deeper valleys that pull in related ideas.  
想象一下一幅有山谷和丘陵的风景。在上下文场中，概念会根据其含义自然地落入“山谷”（吸引子）。强大的概念会形成更深的山谷，吸引相关的想法。

```python
┌─────────────────────────────────────────────────────────┐
│             FIELD VISUALIZATION: ATTRACTORS             │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     Semantic Space (2D Projection)                      │
│                                                         │
│     ╭─────────────────────────────────────────────╮     │
│     │                                             │     │
│     │                          Attractor B        │     │
│     │                          "Context Field"    │     │
│     │                               ╱╲            │     │
│     │                              /  \           │     │
│     │                             /    \          │     │
│     │                            /      \         │     │
│     │                     ─────╲        /─────    │     │
│     │                           ╲      /          │     │
│     │                            ╲    /           │     │
│     │                             ╲  /            │     │
│     │  Attractor A                 \/             │     │
│     │  "Prompt Engineering"         Resonance     │     │
│     │        ╱╲                     Pathway       │     │
│     │       /  \                                  │     │
│     │      /    \                                 │     │
│     │     /      \                      Attractor C     │
│     │    /        \                     "Memory"        │
│     │   /          \                        ╱╲          │
│     │  /            \                      /  \         │
│     │ /              \                    /    \        │
│     │/                \                  /      \       │
│     │                  \                /        \      │
│     │                   \              /          \     │
│     │                    \            /            \    │
│     │                     \          /              \   │
│     │                      \        /                \  │
│     │                                                   │
│     ╰─────────────────────────────────────────────╯     │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Concepts Visualized:  可视化的关键概念：

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#key-concepts-visualized)

1. **Attractors**: The valleys (A, B, C) represent stable concepts like "Prompt Engineering," "Context Field," and "Memory" that have formed in the field.  
    **吸引子** ：谷（A、B、C）代表在该领域中形成的稳定概念，例如“提示工程”、“上下文场”和“记忆”。
    
2. **Basin of Attraction**: The area around each valley shows how far the attractor's influence extends. Stronger attractors (deeper valleys) have wider basins.  
    **吸引盆地** ：每个谷周围的区域显示了吸引子的影响范围。吸引子越强（谷越深），盆地就越宽。
    
3. **Resonance Pathway**: The connection between attractors shows how related concepts reinforce each other. In this case, "Prompt Engineering" and "Context Field" share semantic overlap.  
    **共振路径** ：吸引子之间的连接体现了相关概念如何相互强化。在本例中，“提示工程”和“语境场”存在语义重叠。
    

## How Resonance Works  共振的工作原理

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#how-resonance-works)

Resonance occurs when patterns in the field vibrate at compatible frequencies, reinforcing each other. Think of it like tuning forks - when one vibrates, another with a similar frequency will start vibrating too.  
当场中的模式以兼容的频率振动并相互增强时，就会发生共振。可以把它想象成音叉——当一个音叉振动时，另一个频率相似的音叉也会开始振动。

```python
┌─────────────────────────────────────────────────────────┐
│                RESONANCE VISUALIZATION                  │
├─────────────────────────────────────────────────────────┤
│                                                         │
│     Before Resonance             After Resonance        │
│                                                         │
│     Pattern A    Pattern B       Pattern A    Pattern B │
│        ~~~~         ~~~~            ~~~~~~      ~~~~~~  │
│       ~    ~       ~    ~          ~~    ~~    ~~    ~~ │
│      ~      ~     ~      ~        ~~      ~~  ~~      ~~│
│     ~        ~   ~        ~      ~~        ~~~~        ~│
│                                                         │
│     • Separate oscillation      • Synchronized          │
│     • Independent strength      • Mutually amplified    │
│     • No information flow       • Shared information    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Real-World Example:  真实世界的例子：

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#real-world-example)

When you hear "context engineering," it naturally activates related concepts like "prompt design," "field operations," and "attractor dynamics." This is resonance in action - one concept triggers related ones.  
当你听到“上下文工程”这个词时，它自然会激活相关的概念，例如“即时设计”、“现场操作”和“吸引子动力学”。这就是共振——一个概念会触发相关的概念。

## Field Evolution Over Time  
领域随时间演变

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#field-evolution-over-time)

Fields aren't static - they evolve as new information is added and old information decays. This animation shows how a field might evolve over time:  
场并非静态的——它们会随着新信息的添加和旧信息的衰减而演变。以下动画展示了场如何随时间演变：

```python
┌─────────────────────────────────────────────────────────┐
│               FIELD EVOLUTION OVER TIME                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Time 1: Initial Field      Time 2: After New Input     │
│  ──────────────────────    ────────────────────────     │
│                                                         │
│     A       B                   A       B               │
│    ╱╲      ╱╲                  ╱╲      ╱╲               │
│   /  \    /  \                /  \    /  ╲              │
│  /    \  /    \              /    \  /    ╲             │
│ /      \/      \            /      \/      ╲            │
│                              resonance       ╲           │
│                                               ╲          │
│                                                ╲         │
│                                          C     ╲        │
│                                         ╱╲     ╲       │
│                                        /  \     ╲      │
│                                       /    \     ╲     │
│                                      /      \     ╲    │
│                                                         │
│  Time 3: After Decay        Time 4: Field Repair        │
│  ──────────────────────    ────────────────────────     │
│                                                         │
│     A                           A                       │
│    ╱╲                          ╱╲                       │
│   /  \                        /  \                      │
│  /    \     B                /    \     B'              │
│ /      \   ╱╲               /      \   ╱╲               │
│           /  ╲             /        \ /  \              │
│          /    ╲           /          /    \             │
│         /      ╲         /                \             │
│                 ╲       /                  \            │
│          C       ╲     /                    \           │
│         ╱╱        ╲   /                      \          │
│        /  \        ╲ /                        \         │
│       /    \                                             │
│      /      \                                            │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Field Evolution Process:  场演化过程：

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#field-evolution-process)

1. **Time 1**: Initial field with two stable attractors A and B.  
    **时间 1** ：具有两个稳定吸引子 A 和 B 的初始场。
2. **Time 2**: New information creates attractor C, which starts resonating with B.  
    **时间 2** ：新信息创建吸引子 C，它开始与 B 产生共振。
3. **Time 3**: After decay, attractor B weakens and C shifts position.  
    **时间 3** ：衰减后，吸引子 B 减弱并且 C 改变位置。
4. **Time 4**: Field repair strengthens and restores attractor B (now B').  
    **时间 4** ：场修复增强并恢复吸引子 B（现为 B'）。

## How Protocol Shells Operate on Fields  
协议 Shell 如何操作字段

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#how-protocol-shells-operate-on-fields)

Protocol shells provide structured operations for manipulating the field. Here's a visualization of the different protocols in action:  
协议外壳提供了用于操作该字段的结构化操作。以下是不同协议的实际运行可视化：

```python
┌─────────────────────────────────────────────────────────┐
│               PROTOCOL SHELL OPERATIONS                 │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  /attractor.co.emerge        /field.resonance.scaffold  │
│  ────────────────────        ──────────────────────     │
│                                                         │
│      A     B                      A     B               │
│     ╱╲    ╱╲                     ╱╲    ╱╲               │
│    /  \  /  \                   /  \  /  \              │
│   /    \/    \                 /    \/    \             │
│                     ──►       /              \          │
│        C   D                 /   Amplified    \         │
│       ╱╲  ╱╲                /                  \        │
│      /  \/  \              /        C   D      \        │
│     /        \            /        ╱╲  ╱╲       \       │
│                          /        /  \/  \       \      │
│                                  /        \              │
│                                                         │
│  Co-emergence creates new        Resonance amplifies     │
│  attractor from A+B+C+D          coherent patterns       │
│                                                         │
│  /recursive.memory.attractor    /field.self.repair      │
│  ────────────────────────       ────────────────────    │
│                                                         │
│      A                             A                    │
│     ╱╲                            ╱╲                    │
│    /  \    Memory                /  \                   │
│   /    \   Pathway              /    \                  │
│  /      \ - - - - - - ►        /      \                 │
│ /        \  B                 /        \                │
│/          \/╲                /          \               │
│            /  \             /     Fixed   \             │
│           /    \           /       B       \            │
│          /      \         /       ╱╲        \           │
│         /        \       /       /  \        \          │
│                                /    \                   │
│                               /      \                  │
│                                                         │
│  Memory creates persistent    Self-repair fixes         │
│  pathways between attractors  damaged attractors        │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Field Health and Coherence  
现场健康与一致性

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#field-health-and-coherence)

Just like a physical system, context fields have measurable health metrics. Think of coherence as the field's "immune system" - when coherence is high, the field maintains its structure even when faced with noise or damage.  
就像物理系统一样，上下文场具有可测量的健康指标。将相干性视为场的“免疫系统”——当相干性较高时，即使面临噪声或损坏，场也能保持其结构。

```python
┌─────────────────────────────────────────────────────────┐
│               FIELD HEALTH VISUALIZATION                │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Healthy Field (High Coherence)                         │
│  ────────────────────────                               │
│                                                         │
│    Strong, stable attractors    Clear pathways          │
│         ╱╲      ╱╲              between related         │
│        /  \    /  \             concepts                │
│       /    \──/    \                                    │
│      /                \         Minimal noise           │
│     /                  \                                │
│    /                    \       Resilient to            │
│   /                      \      perturbations           │
│                                                         │
│  Unhealthy Field (Low Coherence)                        │
│  ──────────────────────────                             │
│                                                         │
│    Weak, unstable attractors    Fragmented              │
│         ╱╲      ╱╲              connections             │
│        /· ·    /  \                                     │
│       /    ·   ·   \            High noise              │
│      /     ·   ·    \           levels                  │
│     /      ·····     \                                  │
│    /                  \         Vulnerable to           │
│   /                    \        collapse                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Practical Applications: From Theory to Implementation  
实际应用：从理论到实施

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#practical-applications-from-theory-to-implementation)

Now that we understand the visual concepts, let's look at how these principles translate to code. Here's a simplified code snippet demonstrating how we might implement attractor formation:  
现在我们理解了视觉概念，让我们看看如何将这些原理转化为代码。以下是一段简化的代码片段，演示了如何实现吸引子的形成：

```python
def form_attractor(field, pattern, strength=0.7):
    """Form a new attractor in the field."""
    # Check if pattern is strong enough
    if strength >= field.attractor_threshold:
        # Create attractor
        attractor = {
            "pattern": pattern,
            "strength": strength,
            "basin_width": 0.5 + (0.5 * strength),  # Stronger = wider basin
            "formation_time": time.time()
        }
        
        # Add to field
        attractor_id = field.add_attractor(attractor)
        
        # Log formation
        field._log_operation("form_attractor", {
            "attractor_id": attractor_id,
            "pattern": pattern,
            "strength": strength
        })
        
        # Update field metrics
        field._update_metrics_after_attractor_formation()
        
        return attractor_id
    
    return None
```

This simple function captures the essence of attractor formation in our context field implementation.  
这个简单的函数捕捉到了我们上下文场实现中吸引子形成的本质。

## Understanding Through Analogy  
通过类比来理解

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#understanding-through-analogy)

For those new to field theory, here are some helpful analogies:  
对于场论的新手来说，这里有一些有用的类比：

1. **Gravitational Analogy**: Attractors are like planets with gravity wells, pulling in related concepts.  
    **引力类比** ：吸引子就像具有引力井的行星，吸引相关概念。
    
2. **Social Network Analogy**: Think of attractors as popular topics in a conversation that naturally draw attention and connect to other topics.  
    **社交网络类比** ：将吸引子视为对话中的热门话题，它自然会引起人们的注意并与其他话题联系起来。
    
3. **Musical Analogy**: Resonance is like harmony between musical notes - when the frequencies match, they amplify each other.  
    **音乐类比** ：共振就像音符之间的和谐——当频率匹配时，它们会相互放大。
    
4. **Ecosystem Analogy**: The field is like a balanced ecosystem where different species (concepts) find their natural niches and form relationships.  
    **生态系统类比** ：该领域就像一个平衡的生态系统，其中不同物种（概念）找到自己的自然位置并形成关系。
    

## Visualizing Your Own Fields  
可视化你自己的字段

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/30_examples/00_toy_chatbot/context_field.py.md#visualizing-your-own-fields)

When working with context fields, it can be helpful to visualize them. Here's a simple approach:  
使用上下文字段时，将其可视化会很有帮助。以下是一个简单的方法：

1. **Map key concepts** as potential attractors  
    **将关键概念映射**为潜在吸引子
2. **Draw connections** between related concepts  
    **建立相关概念之间的联系**
3. **Identify strong attractors** that should persist  
    **确定应该持续存在的强吸引子**
4. **Simulate field operations** to see how the field might evolve  
    **模拟现场操作，** 了解现场可能如何发展

By making these abstract concepts visual and tangible, we can better understand how context fields operate and how to use them effectively in our applications.  
通过使这些抽象概念变得直观和有形，我们可以更好地理解上下文字段如何运作以及如何在我们的应用程序中有效地使用它们。