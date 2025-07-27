# Information Theory: Quantifying Context Quality and Relevance (信息论：量化上下文质量和相关性)
## From Intuitive Relevance to Mathematical Precision (从直觉相关性到数学精度)

> **Module 00.3** | *Context Engineering Course: From Foundations to Frontier Systems*
> **模块 00.3** | *上下文工程课程：从基础到前沿系统*
> 
> "Information is the resolution of uncertainty" — Claude Shannon*
> *“信息是消除不确定性的方法”——克劳德·香农*

---

## From Guesswork to Information Science (从猜测到信息科学)

You've learned to formalize context and optimize assembly functions. Now comes a fundamental question: **How do we measure the information value of context components?**
您已经学会了形式化上下文和优化组合函数。现在出现了一个基本问题：**我们如何衡量上下文组件的信息价值？**

### The Universal Information Challenge (普遍的信息挑战)

Consider these familiar information scenarios:
考虑一下这些熟悉的信息场景：

**Signal vs. Noise in Communication**:
**通信中的信号与噪声**:
```
Clear Phone Call: High information content, low noise
Staticky Call: Same information, but harder to extract (low signal-to-noise ratio)
```

**Relevant vs. Irrelevant Search Results**:
**相关与不相关的搜索结果**:
```
Targeted Search: Results directly answer your question (high relevance)
Broad Search: Many results, but few actually help (low information density)
```

**Context Engineering Information Problem**:
**上下文工程信息问题**:
```
High-Quality Context: Maximum relevant information within token constraints
Poor Context: Mixture of relevant and irrelevant information (inefficient)
```

**The Pattern**: In each case, we want to maximize useful information while minimizing noise, irrelevance, or redundancy.
**模式**: 在每种情况下，我们都希望在最小化噪声、不相关性或冗余的同时最大化有用信息。

---

## Mathematical Foundations of Information Theory (信息论的数学基础)

### Core Information Concepts (核心信息概念)

#### Information Content (Surprise) (信息内容（惊奇度）)
```
I(x) = -log₂(P(x))

Where:
I(x) = Information content of event x (measured in bits)
P(x) = Probability of event x occurring

Intuition: Rare events contain more information than common events
```

**Visual Understanding**:
**可视化理解**:
```
    Information Content (信息内容)
         ↑
    10   │ ████ "AI system became sentient" (very rare, high information) ("人工智能系统产生了意识"（非常罕见，信息量大）)
         │
     5   │ ██ "It's raining today" (somewhat rare, medium information) ("今天下雨"（有点罕见，中等信息量）)  
         │
     1   │ ▌ "The sun rose this morning" (very common, low information) ("今天早上太阳升起来了"（很常见，信息量低）)
         │
     0   │________________________→
         0    0.5    1.0    Probability of Event (事件概率)
```

#### Entropy (Average Information) (熵（平均信息）)
```
H(X) = -Σ P(x) × log₂(P(x))

Where:
H(X) = Entropy of random variable X (average information content)
P(x) = Probability of each possible outcome x

Intuition: Entropy measures uncertainty - how much information we expect on average
```

#### Mutual Information (Shared Information) (互信息（共享信息）)
```
I(X;Y) = H(X) + H(Y) - H(X,Y)

Where:
I(X;Y) = Mutual information between X and Y
H(X,Y) = Joint entropy of X and Y

Intuition: How much knowing Y tells us about X (and vice versa)
```

**Ground-up Explanation**: Information theory provides mathematical tools for measuring information content, just like physics provides tools for measuring energy. Entropy measures how much information something contains on average, while mutual information measures how much two pieces of information overlap or relate to each other.
**从头解释**: 信息论提供了测量信息内容的数学工具，就像物理学提供了测量能量的工具一样。熵衡量某事物平均包含多少信息，而互信息衡量两段信息重叠或相互关联的程度。

---

## Software 3.0 Paradigm 1: Prompts (Information Assessment Templates) (软件 3.0 范式 1：提示（信息评估模板）)

Prompts provide systematic frameworks for analyzing and optimizing information content in context components.
提示为分析和优化上下文组件中的信息内容提供了系统化的框架。

### Information Relevance Assessment Template (信息相关性评估模板)

```markdown
# Information Relevance Analysis Framework

## Relevance Quantification Strategy
**Goal**: Systematically measure how relevant each piece of information is to the user's query
**Approach**: Multi-dimensional relevance scoring with mathematical precision

## Semantic Relevance Analysis

### 1. Direct Relevance (Primary Dimension)
**Definition**: How directly does this information address the core query?
**Measurement Framework**:

Direct_Relevance(info, query) = Semantic_Similarity(info_embedding, query_embedding)

Where:
- Semantic_Similarity uses cosine similarity between embeddings
- Range: [0, 1] where 1 = perfect semantic match
- Threshold for inclusion: typically ≥ 0.6


**Assessment Questions**:
- Does this information directly answer the user's question?
- Would removing this information make the response incomplete?
- How central is this information to the query's core intent?

**Scoring Rubric**:
- **0.9-1.0**: Information directly answers the query
- **0.7-0.9**: Information strongly supports answering the query  
- **0.5-0.7**: Information provides useful context for the query
- **0.3-0.5**: Information is tangentially related to the query
- **0.0-0.3**: Information is not relevant to the query

### 2. Contextual Relevance (Secondary Dimension)
**Definition**: How does this information relate to the broader context and background needed?
**Measurement Framework**:

Contextual_Relevance(info, context) = 
    α × Background_Importance(info) + 
    β × Dependency_Strength(info, other_components) +
    γ × Completeness_Contribution(info)

Where α + β + γ = 1 (weighted combination)


**Assessment Criteria**:
- **Background Importance**: Essential for understanding vs. nice-to-know
- **Dependency Strength**: How much other information depends on this
- **Completeness Contribution**: How much this adds to overall completeness

### 3. Information Efficiency Analysis
**Definition**: How much valuable information per token does this component provide?
**Measurement Framework**:

Information_Efficiency(component) = 
    Information_Value(component) / Token_Count(component)

Where Information_Value combines:
- Relevance_Score × Importance_Weight
- Uniqueness_Factor (penalty for redundant information)  
- Credibility_Multiplier (boost for authoritative sources)


**Efficiency Optimization Questions**:
- Can this information be expressed more concisely without losing value?
- Is there redundancy with other components that can be eliminated?
- What is the minimum token count needed to convey this information effectively?

## Information Value Calculation

### Composite Information Score

Total_Information_Value(component) = 
    w₁ × Direct_Relevance(component) +
    w₂ × Contextual_Relevance(component) +  
    w₃ × Information_Efficiency(component) +
    w₄ × Source_Credibility(component) +
    w₅ × Information_Freshness(component)

Where: w₁ + w₂ + w₃ + w₄ + w₅ = 1


## Redundancy Detection Framework

### Information Overlap Analysis

Redundancy_Score(component_A, component_B) = 
    Mutual_Information(A, B) / min(H(A), H(B))

Where:
- High redundancy (>0.8): Consider consolidating or removing one component
- Medium redundancy (0.4-0.8): Look for complementary aspects to preserve
- Low redundancy (<0.4): Both components provide unique value


### Diversity Optimization Strategy

Target: Maximize information coverage while minimizing redundancy

Optimal_Component_Set = arg max[Σ Information_Value(cᵢ) - λ × Σᵢⱼ Redundancy(cᵢ, cⱼ)]

Where λ controls the penalty for redundant information
```

**Ground-up Explanation**: This template provides a systematic approach to measuring information value, like having a precise scale for weighing the usefulness of different pieces of information. It helps you identify what adds real value versus what just takes up space.
**从头解释**: 此模板提供了一种系统化的方法来衡量信息价值，就像有一个精确的标尺来衡量不同信息的有用性一样。它可以帮助您识别哪些信息增加了真正的价值，哪些只是占用了空间。

### Mutual Information Optimization Template (互信息优化模板)

```xml
<mutual_information_optimization>
  <objective>Maximize mutual information between context components and user query</objective>
  
  <mutual_information_framework>
    <definition>
      I(Context; Query) = H(Query) - H(Query|Context)
      
      Interpretation:
      - H(Query): Uncertainty about query without context
      - H(Query|Context): Uncertainty about query given context
      - I(Context; Query): Information that context provides about query
    </definition>
    
    <optimization_target>
      Maximize: I(Context; Query) = Σᵢ I(component_i; Query) - Redundancy_Penalty
      
      Subject to: Token_Budget_Constraint
    </optimization_target>
  </mutual_information_framework>
  
  <component_selection_strategy>
    <greedy_approach>
      <step_1>Calculate I(component; Query) for all available components</step_1>
      <step_2>Select component with highest mutual information</step_2>
      <step_3>For remaining components, calculate conditional mutual information:
        I(component; Query | already_selected_components)</step_3>
      <step_4>Repeat until token budget exhausted</step_4>
    </greedy_approach>
    
    <optimal_approach>
      <description>Find globally optimal subset of components</description>
      <formulation>
        max Σᵢ∈S I(componentᵢ; Query) - λ × Σᵢ,ⱼ∈S I(componentᵢ; componentⱼ)
        
        Subject to: Σᵢ∈S tokens(componentᵢ) ≤ Budget
      </formulation>
      <solution_method>Dynamic programming or integer linear programming</solution_method>
    </optimal_approach>
  </component_selection_strategy>
  
  <practical_implementation>
    <embedding_based_approximation>
      <mutual_information_estimate>
        I(component; query) ≈ 1 - JS_Divergence(P_component, P_query)
        
        Where JS_Divergence is Jensen-Shannon divergence between probability distributions
        derived from embeddings
      </mutual_information_estimate>
      
      <conditional_mutual_information>
        I(component; query | context) ≈ 
          I(component; query) - α × max_j I(component; context_component_j)
        
        Where α controls redundancy penalty strength
      </conditional_mutual_information>
    </embedding_based_approximation>
    
    <frequency_based_approximation>
      <term_overlap_method>
        I(component; query) ≈ 
          |Unique_Terms(component) ∩ Terms(query)| / |Terms(query)|
      </term_overlap_method>
      
      <semantic_term_expansion>
        Expand query terms with synonyms and related concepts
        Calculate overlap with expanded term set
      </semantic_term_expansion>
    </frequency_based_approximation>
  </practical_implementation>
  
  <quality_validation>
    <information_coverage_check>
      Ensure selected components cover all major aspects of the query:
      Coverage(components, query) = |Query_Aspects_Covered| / |Total_Query_Aspects|
    </information_coverage_check>
    
    <diminishing_returns_analysis>
      Monitor marginal information gain as components are added:
      If Marginal_I(new_component) < threshold, consider stopping selection
    </diminishing_returns_analysis>
    
    <coherence_validation>
      Ensure selected components form coherent information set:
      Coherence = Average_Mutual_Information(component_pairs) - Conflict_Penalty
    </coherence_validation>
  </quality_validation>
</mutual_information_optimization>
```

**Ground-up Explanation**: This XML template provides a systematic approach to selecting information components that maximize mutual information with the user's query, like choosing the most relevant books from a library to answer a specific research question.
**从头解释**: 此 XML 模板提供了一种系统化的方法来选择与用户查询具有最大互信息的信息组件，就像从图书馆中选择最相关的书籍来回答特定的研究问题一样。

### Information Compression Strategy Template (信息压缩策略模板)

```yaml
# Information Compression Strategy Template
compression_optimization:
  
  objective: "Maximize information density while preserving essential content"
  
  compression_dimensions:
    semantic_compression:
      description: "Reduce redundancy while preserving meaning"
      techniques:
        - synonym_replacement: "Replace verbose phrases with concise equivalents"
        - redundancy_elimination: "Remove repetitive information"
        - concept_consolidation: "Merge related concepts into unified descriptions"
      
      measurement:
        compression_ratio: "original_tokens / compressed_tokens"
        information_preservation: "semantic_similarity(original, compressed)"
        target_preservation: ">= 0.95"
    
    syntactic_compression:
      description: "Optimize sentence structure and word choice"
      techniques:
        - passive_to_active_voice: "Convert passive constructions to active"
        - unnecessary_qualifier_removal: "Remove hedge words and filler phrases"
        - sentence_combination: "Merge related sentences for conciseness"
      
      measurement:
        readability_preservation: "reading_ease_score comparison"
        clarity_maintenance: "information_accessibility assessment"
    
    structural_compression:
      description: "Optimize information organization and presentation"
      techniques:
        - hierarchical_organization: "Group related information together"
        - bullet_point_conversion: "Convert prose to structured lists when appropriate"
        - example_consolidation: "Reduce multiple examples to most illustrative ones"
  
  compression_strategies:
    lossy_compression:
      description: "Remove information deemed less important"
      decision_criteria:
        - relevance_threshold: "Remove components below relevance threshold"
        - importance_ranking: "Preserve highest-value information first"
        - user_priority_alignment: "Maintain information user explicitly prioritized"
      
      quality_control:
        - essential_information_preservation: "Never compress critical facts"
        - accuracy_maintenance: "Ensure compression doesn't introduce errors"
        - completeness_thresholds: "Maintain minimum completeness levels"
    
    lossless_compression:
      description: "Reduce tokens without losing information content"
      techniques:
        - format_optimization: "Use more compact representation formats"
        - reference_consolidation: "Use pronouns and references effectively"
        - abbreviation_standardization: "Use accepted abbreviations consistently"
      
      validation:
        - information_equivalence: "Verify compressed version contains same information"
        - reconstructability: "Ensure original meaning can be recovered"
        - error_detection: "Check for compression-induced ambiguities"
  
  adaptive_compression:
    context_aware_compression:
      high_relevance_preservation: "Apply minimal compression to highly relevant content"
      background_information_compression: "More aggressive compression for supporting details"
      user_expertise_adjustment: "Compress basic concepts more for expert users"
    
    token_budget_adaptation:
      emergency_compression: "Aggressive compression when severely over token budget"
      optimal_compression: "Balanced compression for normal token pressure"
      minimal_compression: "Light compression when well within budget"
    
    quality_feedback_integration:
      user_satisfaction_monitoring: "Track user satisfaction with compressed content"
      compression_strategy_adjustment: "Modify compression based on feedback"
      iterative_improvement: "Refine compression algorithms over time"
  
  implementation_guidelines:
    compression_pipeline:
      step_1: "Identify compression opportunities through information analysis"
      step_2: "Apply appropriate compression techniques based on content type"
      step_3: "Validate compression quality and information preservation"
      step_4: "Adjust compression level based on token budget and quality requirements"
    
    quality_assurance:
      - pre_compression_analysis: "Assess information value before compression"
      - compression_impact_measurement: "Quantify effects of compression decisions"
      - post_compression_validation: "Verify compressed content meets quality standards"
      - user_feedback_integration: "Incorporate user preferences into compression strategies"
    
    compression_monitoring:
      - compression_effectiveness_tracking: "Monitor compression ratio vs. quality trade-offs"
      - user_satisfaction_correlation: "Track relationship between compression and user satisfaction"
      - continuous_improvement: "Refine compression strategies based on empirical data"
```

**Ground-up Explanation**: This YAML template provides systematic approaches to information compression, like having professional editing techniques that preserve meaning while reducing length. It balances efficiency with quality preservation.
**从头解释**: 这个 YAML 模板提供了系统化的信息压缩方法，就像拥有专业的编辑技术，在保留意义的同时缩短长度。它在效率和质量保留之间取得了平衡。

---

## Software 3.0 Paradigm 2: Programming (Information Algorithms) (软件 3.0 范式 2：编程（信息算法）)

Programming provides computational methods for measuring, optimizing, and managing information content in context components.
编程为测量、优化和管理上下文组件中的信息内容提供了计算方法。

### Information Theory Implementation (信息论实现)

```python
import numpy as np
import math
from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

@dataclass
class InformationMetrics:
    """Container for information-theoretic measurements"""
    entropy: float
    mutual_information: float
    conditional_entropy: float
    information_gain: float
    redundancy_score: float
    efficiency_ratio: float

class InformationAnalyzer:
    """Comprehensive information theory analysis for context components"""
    
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=10000)
        self.vocabulary_stats = {}
        
    def calculate_entropy(self, text: str) -> float:
        """
        Calculate Shannon entropy of text based on character/word frequencies
        
        Args:
            text: Input text to analyze
            
        Returns:
            Entropy value in bits
        """
        
        if not text or len(text.strip()) == 0:
            return 0.0
        
        # Calculate character-level entropy
        char_counts = Counter(text.lower())
        total_chars = len(text)
        
        entropy = 0.0
        for count in char_counts.values():
            probability = count / total_chars
            if probability > 0:
                entropy += -probability * math.log2(probability)
        
        return entropy
    
    def calculate_word_entropy(self, text: str) -> float:
        """Calculate entropy based on word frequencies"""
        
        words = text.lower().split()
        if not words:
            return 0.0
        
        word_counts = Counter(words)
        total_words = len(words)
        
        entropy = 0.0
        for count in word_counts.values():
            probability = count / total_words
            entropy += -probability * math.log2(probability)
        
        return entropy
    
    def calculate_mutual_information(self, text1: str, text2: str) -> float:
        """
        Calculate mutual information between two text components
        
        Uses TF-IDF vectors and entropy calculations to estimate mutual information
        """
        
        try:
            # Create TF-IDF vectors
            texts = [text1, text2]
            tfidf_matrix = self.vectorizer.fit_transform(texts)
            
            # Calculate joint distribution approximation
            vec1 = tfidf_matrix[0].toarray().flatten()
            vec2 = tfidf_matrix[1].toarray().flatten()
            
            # Normalize to create probability distributions
            vec1_norm = vec1 / (np.sum(vec1) + 1e-10)
            vec2_norm = vec2 / (np.sum(vec2) + 1e-10)
            
            # Calculate mutual information approximation
            joint_prob = np.outer(vec1_norm, vec2_norm)
            
            # Calculate marginal entropies
            h1 = -np.sum(vec1_norm * np.log2(vec1_norm + 1e-10))
            h2 = -np.sum(vec2_norm * np.log2(vec2_norm + 1e-10))
            
            # Calculate joint entropy
            joint_prob_flat = joint_prob.flatten()
            h_joint = -np.sum(joint_prob_flat * np.log2(joint_prob_flat + 1e-10))
            
            # Mutual information = H(X) + H(Y) - H(X,Y)
            mutual_info = h1 + h2 - h_joint
            
            return max(0.0, mutual_info)
            
        except Exception as e:
            # Fallback to simpler overlap-based measure
            return self._calculate_overlap_based_mi(text1, text2)
    
    def _calculate_overlap_based_mi(self, text1: str, text2: str) -> float:
        """Fallback mutual information calculation based on word overlap"""
        
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0.0
        
        overlap = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        if union == 0:
            return 0.0
        
        # Jaccard similarity as MI approximation
        jaccard = overlap / union
        
        # Convert to mutual information scale (rough approximation)
        return -math.log2(1 - jaccard + 1e-10)
    
    def calculate_conditional_entropy(self, text_y: str, text_x: str) -> float:
        """
        Calculate H(Y|X) - entropy of Y given X
        
        Approximated as H(Y) - I(X;Y)
        """
        
        h_y = self.calculate_word_entropy(text_y)
        mi_xy = self.calculate_mutual_information(text_x, text_y)
        
        return max(0.0, h_y - mi_xy)
    
    def calculate_information_gain(self, text_before: str, additional_text: str) -> float:
        """
        Calculate information gain from adding additional text
        
        IG = H(before) - H(before|additional)
        """
        
        h_before = self.calculate_word_entropy(text_before)
        h_conditional = self.calculate_conditional_entropy(text_before, additional_text)
        
        return h_before - h_conditional
    
    def analyze_component_information(self, component_text: str, 
                                    query_text: str) -> InformationMetrics:
        """
        Comprehensive information analysis of a context component
        
        Args:
            component_text: Text content of the component
            query_text: User query for relevance assessment
            
        Returns:
            InformationMetrics with all calculated measures
        """
        
        # Calculate basic information measures
        entropy = self.calculate_word_entropy(component_text)
        mutual_info = self.calculate_mutual_information(component_text, query_text)
        conditional_entropy = self.calculate_conditional_entropy(query_text, component_text)
        information_gain = self.calculate_information_gain(query_text, component_text)
        
        # Calculate redundancy (self-similarity measure)
        sentences = component_text.split('.')
        if len(sentences) > 1:
            redundancy_scores = []
            for i in range(len(sentences)):
                for j in range(i + 1, len(sentences)):
                    if sentences[i].strip() and sentences[j].strip():
                        redundancy = self.calculate_mutual_information(
                            sentences[i], sentences[j]
                        )
                        redundancy_scores.append(redundancy)
            
            redundancy_score = np.mean(redundancy_scores) if redundancy_scores else 0.0
        else:
            redundancy_score = 0.0
        
        # Calculate efficiency (information per token)
        token_count = len(component_text.split())
        efficiency_ratio = mutual_info / (token_count + 1) if token_count > 0 else 0.0
        
        return InformationMetrics(
            entropy=entropy,
            mutual_information=mutual_info,
            conditional_entropy=conditional_entropy,
            information_gain=information_gain,
            redundancy_score=redundancy_score,
            efficiency_ratio=efficiency_ratio
        )

class InformationOptimizer:
    """Optimize context components based on information-theoretic principles"""
    
    def __init__(self):
        self.analyzer = InformationAnalyzer()
        self.optimization_history = []
        
    def optimize_component_selection(self, candidate_components: List[str],
                                   query: str, token_budget: int) -> List[str]:
        """
        Select optimal subset of components to maximize mutual information with query
        
        Args:
            candidate_components: List of candidate text components
            query: User query
            token_budget: Maximum allowed tokens
            
        Returns:
            Optimally selected components
        """
        
        # Calculate information metrics for all components
        component_metrics = []
        for i, component in enumerate(candidate_components):
            metrics = self.analyzer.analyze_component_information(component, query)
            token_count = len(component.split())
            
            component_metrics.append({
                'index': i,
                'component': component,
                'metrics': metrics,
                'token_count': token_count,
                'efficiency': metrics.mutual_information / (token_count + 1)
            })
        
        # Sort by efficiency (mutual information per token)
        component_metrics.sort(key=lambda x: x['efficiency'], reverse=True)
        
        # Greedy selection with redundancy penalty
        selected_components = []
        selected_indices = set()
        total_tokens = 0
        
        for comp_data in component_metrics:
            if comp_data['token_count'] + total_tokens <= token_budget:
                # Check redundancy with already selected components
                redundancy_penalty = 0.0
                
                for selected_comp in selected_components:
                    redundancy = self.analyzer.calculate_mutual_information(
                        comp_data['component'], selected_comp
                    )
                    redundancy_penalty += redundancy
                
                # Adjusted score accounting for redundancy
                adjusted_score = (comp_data['metrics'].mutual_information - 
                                0.5 * redundancy_penalty)
                
                if adjusted_score > 0.1:  # Minimum threshold
                    selected_components.append(comp_data['component'])
                    selected_indices.add(comp_data['index'])
                    total_tokens += comp_data['token_count']
        
        return selected_components
    
    def optimize_component_order(self, components: List[str], query: str) -> List[str]:
        """
        Optimize the order of components to maximize information flow
        
        Place components with highest mutual information with query first,
        followed by components that provide complementary information
        """
        
        if len(components) <= 1:
            return components
        
        # Calculate mutual information with query for each component
        mi_scores = []
        for comp in components:
            mi = self.analyzer.calculate_mutual_information(comp, query)
            mi_scores.append(mi)
        
        # Sort by mutual information with query (descending)
        component_mi_pairs = list(zip(components, mi_scores))
        component_mi_pairs.sort(key=lambda x: x[1], reverse=True)
        
        return [comp for comp, _ in component_mi_pairs]
    
    def compress_component(self, component: str, target_compression: float = 0.8) -> str:
        """
        Compress component while preserving maximum information content
        
        Args:
            component: Original component text
            target_compression: Target length as fraction of original (0.8 = 80% of original)
            
        Returns:
            Compressed component text
        """
        
        sentences = [s.strip() for s in component.split('.') if s.strip()]
        
        if len(sentences) <= 1:
            return component  # Cannot compress single sentence meaningfully
        
        # Calculate information value of each sentence
        sentence_scores = []
        
        for sentence in sentences:
            # Score based on entropy and uniqueness
            entropy = self.analyzer.calculate_word_entropy(sentence)
            
            # Penalty for redundancy with other sentences
            redundancy_penalty = 0.0
            for other_sentence in sentences:
                if sentence != other_sentence:
                    redundancy = self.analyzer.calculate_mutual_information(
                        sentence, other_sentence
                    )
                    redundancy_penalty += redundancy
            
            score = entropy - 0.3 * redundancy_penalty
            sentence_scores.append((sentence, score))
        
        # Sort by score and select top sentences to meet compression target
        sentence_scores.sort(key=lambda x: x[1], reverse=True)
        
        target_length = int(len(sentences) * target_compression)
        target_length = max(1, target_length)  # Keep at least one sentence
        
        selected_sentences = [s for s, _ in sentence_scores[:target_length]]
        
        # Reconstruct component maintaining logical order
        compressed_component = '. '.join(selected_sentences)
        
        return compressed_component

class MutualInformationMaximizer:
    """Specialized optimizer for maximizing mutual information in context assembly"""
    
    def __init__(self, token_budget: int):
        self.token_budget = token_budget
        self.analyzer = InformationAnalyzer()
        
    def maximize_mutual_information(self, knowledge_base: List[str], 
                                  query: str) -> Dict:
        """
        Find optimal combination of knowledge components to maximize I(Context; Query)
        
        Uses greedy algorithm with look-ahead to approximate optimal solution
        """
        
        # Phase 1: Calculate individual mutual information scores
        component_scores = []
        for i, component in enumerate(knowledge_base):
            mi_score = self.analyzer.calculate_mutual_information(component, query)
            token_count = len(component.split())
            
            component_scores.append({
                'index': i,
                'component': component,
                'mi_score': mi_score,
                'token_count': token_count,
                'efficiency': mi_score / (token_count + 1)
            })
        
        # Phase 2: Greedy selection with redundancy consideration
        selected = []
        remaining = component_scores.copy()
        total_tokens = 0
        total_mi = 0.0
        
        while remaining and total_tokens < self.token_budget:
            best_addition = None
            best_marginal_mi = 0.0
            
            for candidate in remaining:
                # Check if it fits in budget
                if total_tokens + candidate['token_count'] > self.token_budget:
                    continue
                
                # Calculate marginal mutual information
                marginal_mi = candidate['mi_score']
                
                # Subtract redundancy with already selected components
                for selected_comp in selected:
                    redundancy = self.analyzer.calculate_mutual_information(
                        candidate['component'], selected_comp['component']
                    )
                    marginal_mi -= 0.5 * redundancy  # Redundancy penalty
                
                if marginal_mi > 0.01:  # Minimum gain threshold
                    best_marginal_mi = marginal_mi
                    best_addition = candidate
            
            if best_addition and best_marginal_mi > 0.01:  # Minimum gain threshold
                selected.append(best_addition)
                remaining.remove(best_addition)
                total_tokens += best_addition['token_count']
                total_mi += best_marginal_mi
            else:
                break  # No more beneficial additions
        
        return {
            'selected_components': [comp['component'] for comp in selected],
            'total_mutual_information': total_mi,
            'token_utilization': total_tokens / self.token_budget,
            'selection_metadata': {
                'num_selected': len(selected),
                'efficiency_score': total_mi / (total_tokens + 1),
                'coverage_score': len(selected) / len(knowledge_base)
            }
        }

# Example usage and demonstration
def demonstrate_information_theory():
    """Demonstrate information theory applications in context engineering"""
    
    # Sample components and query
    query = "How can machine learning improve business decision making?"
    
    candidate_components = [
        "Machine learning algorithms can analyze large datasets to identify patterns and trends that humans might miss, enabling more data-driven business decisions.",
        "Predictive analytics using ML can forecast market trends, customer behavior, and operational needs, allowing businesses to make proactive decisions.",
        "Automated decision-making systems can process information faster than humans, enabling real-time responses to changing business conditions.",
        "Machine learning can reduce human bias in decision-making by relying on objective data analysis rather than subjective judgments.",
        "The weather today is sunny with a high of 75 degrees, perfect for outdoor activities and beach visits.",
        "ML models require careful validation and testing to ensure they provide reliable insights for business decision-making processes.",
        "Integration of machine learning with existing business intelligence tools can enhance decision-making capabilities across organizations."
    ]
    
    # Initialize analyzers
    analyzer = InformationAnalyzer()
    optimizer = InformationOptimizer()
    mi_maximizer = MutualInformationMaximizer(token_budget=150)
    
    print("=== INFORMATION THEORY DEMONSTRATION ===")
    print(f"Query: {query}")
    print(f"Candidate Components: {len(candidate_components)}")
    
    # Analyze each component
    print("\n=== COMPONENT ANALYSIS ===")
    for i, component in enumerate(candidate_components):
        metrics = analyzer.analyze_component_information(component, query)
        print(f"\nComponent {i+1}:")
        print(f"  Mutual Information: {metrics.mutual_information:.3f}")
        print(f"  Entropy: {metrics.entropy:.3f}")
        print(f"  Efficiency Ratio: {metrics.efficiency_ratio:.3f}")
        print(f"  Redundancy Score: {metrics.redundancy_score:.3f}")
    
    # Optimize component selection
    print("\n=== OPTIMIZATION RESULTS ===")
    selected_components = optimizer.optimize_component_selection(
        candidate_components, query, token_budget=150
    )
    
    print(f"Selected {len(selected_components)} components:")
    for i, component in enumerate(selected_components):
        print(f"  {i+1}. {component[:80]}...")
    
    # Maximize mutual information
    mi_results = mi_maximizer.maximize_mutual_information(candidate_components, query)
    
    print(f"\nMutual Information Optimization:")
    print(f"  Total MI: {mi_results['total_mutual_information']:.3f}")
    print(f"  Token Utilization: {mi_results['token_utilization']:.1%}")
    print(f"  Efficiency Score: {mi_results['selection_metadata']['efficiency_score']:.3f}")
    
    return {
        'selected_components': selected_components,
        'mi_results': mi_results,
        'component_analysis': [
            analyzer.analyze_component_information(comp, query) 
            for comp in candidate_components
        ]
    }

# Run demonstration
if __name__ == "__main__":
    results = demonstrate_information_theory()
```

**Ground-up Explanation**: This programming framework implements information theory concepts as working algorithms. Like having scientific instruments that can precisely measure information content, it quantifies how much value each piece of information contributes to answering the user's question.
**从头解释**: 这个编程框架将信息论概念实现为可行的算法。就像拥有可以精确测量信息内容的科学仪器一样，它量化了每条信息对回答用户问题的贡献价值。

---

## Software 3.0 Paradigm 3: Protocols (Adaptive Information Evolution) (软件 3.0 范式 3：协议（自适应信息演化）)

Protocols provide self-improving information systems that learn optimal information selection and organization strategies based on effectiveness feedback.
协议提供了自我完善的信息系统，该系统可以根据有效性反馈学习最佳的信息选择和组织策略。

### Adaptive Information Optimization Protocol (自适应信息优化协议)

```
/information.optimize.adaptive{
    intent="Continuously improve information selection and organization through information-theoretic learning",
    
    input={
        information_landscape={
            available_knowledge=<comprehensive_knowledge_sources>,
            query_context=<user_query_and_intent_analysis>,
            information_constraints=<token_budget_quality_requirements>,
            user_preferences=<information_density_style_preferences>
        },
        
        information_theory_context={
            historical_mi_performance=<mutual_information_optimization_results>,
            entropy_patterns=<information_content_distribution_analysis>,
            redundancy_detection_history=<past_redundancy_identification_success>,
            compression_effectiveness=<information_compression_quality_metrics>
        },
        
        adaptation_parameters={
            information_learning_rate=<speed_of_information_strategy_adaptation>,
            exploration_vs_exploitation=<balance_new_vs_proven_information_sources>,
            quality_vs_efficiency_preference=<trade_off_between_completeness_and_conciseness>,
            user_feedback_sensitivity=<responsiveness_to_user_information_preferences>
        }
    },
    
    process=[
        /analyze.information.landscape{
            action="Systematically analyze available information using information-theoretic principles",
            method="Multi-dimensional information analysis with entropy and mutual information assessment",
            analysis_dimensions=[
                {entropy_assessment="Calculate information content and uncertainty reduction potential"},
                {mutual_information_calculation="Measure relevance and overlap between information sources"},
                {redundancy_detection="Identify duplicate or highly similar information content"},
                {information_efficiency_evaluation="Assess information value per token or processing cost"}
            ],
            pattern_recognition=[
                {high_value_information_characteristics="Identify patterns in most effective information"},
                {redundancy_sources="Recognize common sources of information duplication"},
                {information_gaps="Detect missing information that would increase mutual information"},
                {optimal_information_density="Learn ideal balance of detail vs. conciseness"}
            ],
            output="Comprehensive information landscape analysis with optimization opportunities"
        },
        
        /optimize.information.selection{
            action="Select optimal information subset to maximize mutual information with query",
            method="Greedy optimization with redundancy penalties and look-ahead heuristics",
            selection_algorithms=[
                {greedy_mutual_information="Select components with highest I(component; query)"},
                {redundancy_penalized_selection="Apply penalties for I(component_i; component_j)"},
                {marginal_information_gain="Choose components with highest marginal information"},
                {diversity_maximization="Ensure information covers different aspects of query"}
            ],
            optimization_strategies=[
                {token_budget_optimization="Maximize information per token within constraints"},
                {quality_threshold_maintenance="Ensure minimum information quality standards"},
                {user_preference_integration="Weight information types based on user preferences"},
                {dynamic_threshold_adjustment="Adapt selection criteria based on available information"}
            ],
            output="Optimally selected information components with maximum mutual information"
        },
        
        /compress.information.intelligently{
            action="Apply information-theoretic compression to maximize information density",
            method="Entropy-preserving compression with semantic coherence maintenance",
            compression_techniques=[
                {entropy_based_sentence_selection="Keep sentences with highest information content"},
                {redundancy_elimination="Remove duplicate or highly overlapping information"},
                {semantic_compression="Use more compact representations while preserving meaning"},
                {hierarchical_information_organization="Structure information for maximum clarity"}
            ],
            quality_preservation=[
                {semantic_similarity_maintenance="Ensure compressed content preserves original meaning"},
                {mutual_information_preservation="Maintain relevance to query through compression"},
                {readability_optimization="Keep compressed content easily understandable"},
                {critical_information_protection="Never compress essential facts or key insights"}
            ],
            output="Information-dense compressed content with preserved semantic value"
        },
        
        /validate.information.quality{
            action="Assess information quality using multiple information-theoretic measures",
            method="Comprehensive quality evaluation with user feedback integration",
            quality_dimensions=[
                {relevance_assessment="Measure I(selected_information; query)"},
                {completeness_evaluation="Assess coverage of query aspects"},
                {efficiency_measurement="Calculate information value per token used"},
                {coherence_analysis="Evaluate logical flow and consistency of information"}
            ],
            validation_metrics=[
                {mutual_information_achievement="Compare achieved vs. theoretical maximum MI"},
                {redundancy_minimization="Verify successful elimination of duplicate content"},
                {user_satisfaction_correlation="Track relationship between MI scores and user feedback"},
                {compression_fidelity="Measure information preservation through compression"}
            ],
            output="Comprehensive information quality assessment with improvement recommendations"
        },
        
        /learn.information.patterns{
            action="Extract patterns and insights from information optimization experience",
            method="Meta-learning about information selection and organization effectiveness",
            learning_mechanisms=[
                {information_type_effectiveness="Learn which types of information work best for different queries"},
                {compression_strategy_optimization="Identify most effective compression techniques"},
                {redundancy_pattern_recognition="Understand common sources of information duplication"},
                {user_preference_modeling="Build models of user information preferences and needs"}
            ],
            knowledge_integration=[
                {selection_strategy_refinement="Improve information selection algorithms"},
                {compression_algorithm_tuning="Optimize compression techniques for better results"},
                {mutual_information_prediction="Build models to predict information value"},
                {adaptive_threshold_learning="Learn optimal quality and selection thresholds"}
            ],
            output="Updated information optimization knowledge with improved strategies"
        }
    ],
    
    output={
        optimized_information={
            selected_components=<information_components_maximizing_mutual_information>,
            information_organization=<optimal_structure_for_information_presentation>,
            compression_results=<intelligently_compressed_high_density_information>,
            quality_metrics=<information_theoretic_quality_measurements>
        },
        
        optimization_insights={
            mutual_information_achieved=<total_I_context_query_accomplished>,
            redundancy_eliminated=<amount_of_duplicate_information_removed>,
            compression_efficiency=<information_density_improvement_ratio>,
            selection_effectiveness=<quality_of_information_component_choices>
        },
        
        learning_outcomes={
            information_strategy_improvements=<enhancements_to_selection_algorithms>,
            pattern_discoveries=<new_insights_about_effective_information_organization>,
            user_preference_updates=<refined_understanding_of_user_information_needs>,
            predictive_model_improvements=<better_models_for_information_value_prediction>
        }
    },
    
    meta={
        information_optimization_approach=<specific_algorithms_and_techniques_used>,
        learning_integration_level=<degree_of_adaptive_improvement_achieved>,
        theoretical_grounding=<connection_to_information_theory_principles>,
        practical_effectiveness=<real_world_performance_and_user_satisfaction>
    },
    
    // Self-evolution mechanisms for information optimization improvement
    information_evolution=[
        {trigger="low_mutual_information_achieved", 
         action="experiment_with_alternative_information_selection_strategies"},
        {trigger="high_redundancy_detected_post_selection", 
         action="improve_redundancy_detection_and_elimination_algorithms"},
        {trigger="user_feedback_indicates_information_gaps", 
         action="enhance_completeness_assessment_and_gap_detection"},
        {trigger="compression_causing_information_loss", 
         action="refine_compression_techniques_for_better_preservation"}
    ]
}
```

**Ground-up Explanation**: This protocol creates an information optimization system that continuously learns how to select and organize information more effectively, like a librarian who gets better at finding exactly the right resources by learning from what has worked well in the past.
**从头解释**: 该协议创建了一个信息优化系统，该系统可以不断学习如何更有效地选择和组织信息，就像一个图书馆员通过从过去的成功经验中学习，从而更擅长找到恰当的资源一样。

---

## Research Connections and Future Directions (研究联系和未来方向)

### Connection to Context Engineering Survey (与上下文工程调查的联系)

This information theory module directly implements and extends foundational concepts from the [Context Engineering Survey](https://arxiv.org/pdf/2507.13334):
该信息论模块直接实现并扩展了[上下文工程调查](https://arxiv.org/pdf/2507.13334)中的基础概念:

**Information-Theoretic Context Optimization (§4.1 & §4.2)**:
- Implements systematic approaches to context generation through mutual information maximization
- Extends dynamic assembly concepts through entropy-based component selection
- Addresses information redundancy challenges through mathematical redundancy detection

**信息论上下文优化 (§4.1 & §4.2)**:
- 通过互信息最大化实现上下文生成的系统方法
- 通过基于熵的组件选择扩展动态组合概念
- 通过数学冗余检测解决信息冗余挑战

**Context Processing and Management (§4.2 & §4.3)**:
- Tackles context compression through information-theoretic compression strategies
- Addresses context quality assessment through entropy and mutual information metrics
- Implements intelligent context filtering based on information value quantification

**上下文处理和管理 (§4.2 & §4.3)**:
- 通过信息论压缩策略解决上下文压缩问题
- 通过熵和互信息指标解决上下文质量评估问题
- 基于信息价值量化实现智能上下文过滤

**Foundational Research Applications (§7.1)**:
- Demonstrates information-theoretic foundations for context optimization
- Implements compositional understanding frameworks through information component analysis
- Provides mathematical basis for context quality measurement and optimization

**基础研究应用 (§7.1)**:
- 展示了上下文优化的信息论基础
- 通过信息组件分析实现组合理解框架
- 为上下文质量测量和优化提供数学基础

### Novel Contributions Beyond Current Research (超越当前研究的新颖贡献)

**Mathematical Information Framework for Context Engineering**: While the survey covers context engineering techniques, our systematic application of Shannon information theory (entropy, mutual information, conditional entropy) to context component selection represents novel research into rigorous information-theoretic foundations for context quality measurement.
**上下文工程的数学信息框架**: 虽然调查涵盖了上下文工程技术，但我们将香农信息论（熵、互信息、条件熵）系统地应用于上下文组件选择，代表了对上下文质量测量的严格信息论基础的新颖研究。

**Redundancy-Aware Optimization**: Our integration of redundancy detection and elimination through mutual information calculations extends beyond current approaches by providing mathematical frameworks for identifying and removing duplicate information while preserving unique value.
**冗余感知优化**: 我们通过互信息计算整合冗余检测和消除，超越了当前的方法，为识别和删除重复信息同时保留独特价值提供了数学框架。

**Information Compression with Semantic Preservation**: The development of compression techniques that maintain semantic coherence while maximizing information density represents advancement beyond simple token reduction toward intelligent information distillation.
**具有语义保留的信息压缩**: 开发在保持语义连贯性的同时最大化信息密度的压缩技术，代表了从简单的令牌缩减向智能信息提炼的进步。

**Adaptive Information Learning**: Our self-improving information selection systems that learn optimal information patterns through experience represent frontier research into meta-information optimization.
**自适应信息学习**: 我们的自我完善信息选择系统通过经验学习最佳信息模式，代表了元信息优化的前沿研究。

### Future Research Directions (未来研究方向)

**Quantum Information Theory Applications**: Exploring quantum information concepts like quantum entropy and quantum mutual information for context engineering, potentially enabling more sophisticated information relationships and superposition states of information relevance.
**量子信息论应用**: 探索量子熵和量子互信息等量子信息概念在上下文工程中的应用，可能实现更复杂的信息关系和信息相关性的叠加态。

**Multimodal Information Integration**: Research into unified information-theoretic frameworks for text, visual, audio, and temporal information, developing mathematical approaches for measuring mutual information across different modalities.
**多模态信息集成**: 研究用于文本、视觉、音频和时间信息的统一信息论框架，开发用于测量不同模态之间互信息的数学方法。

**Causal Information Theory**: Investigation of causal relationships between information components using directed information and transfer entropy, enabling context systems that understand not just correlation but causation in information flow.
**因果信息论**: 使用有向信息和传递熵研究信息组件之间的因果关系，使上下文系统不仅能理解信息流中的相关性，还能理解因果关系。

**Information-Theoretic Context Security**: Development of information theory applications to context privacy and security, using concepts like differential privacy and information-theoretic security to protect sensitive information while maintaining context utility.
**信息论上下文安全**: 开发信息论在上下文隐私和安全方面的应用，使用差分隐私和信息论安全等概念来保护敏感信息，同时保持上下文的效用。

**Temporal Information Dynamics**: Research into time-dependent information theory where information value, entropy, and mutual information evolve over time, requiring dynamic mathematical frameworks for temporal context optimization.
**时间信息动力学**: 研究时间相关的信息论，其中信息价值、熵和互信息随时间演变，需要动态的数学框架来进行时间上下文优化。

**Distributed Information Optimization**: Investigation of information theory applications to distributed context engineering where information components are distributed across multiple systems while maintaining global information optimization.
**分布式信息优化**: 研究信息论在分布式上下文工程中的应用，其中信息组件分布在多个系统中，同时保持全局信息优化。

**Meta-Information Theory**: Research into information about information - developing mathematical frameworks for reasoning about the information content of information selection strategies themselves.
**元信息论**: 研究关于信息的信息——开发用于推理信息选择策略本身的信息内容的数学框架。

**Human-Information Theory Integration**: Development of information-theoretic models that account for human cognitive processing, attention limits, and information comprehension patterns in context optimization.
**人-信息论整合**: 开发在上下文优化中考虑人类认知处理、注意力限制和信息理解模式的信息论模型。

---

## Practical Exercises and Projects (实践练习和项目)

### Exercise 1: Mutual Information Calculator (练习 1：互信息计算器)
**Goal**: Implement mutual information calculation for text components
**目标**: 实现文本组件的互信息计算

```python
# Your implementation template
class MutualInformationCalculator:
    def __init__(self):
        # TODO: Initialize text processing components
        pass
    
    def calculate_mi(self, text1: str, text2: str) -> float:
        # TODO: Implement mutual information calculation
        # Consider both word-level and character-level approaches
        pass
    
    def calculate_conditional_entropy(self, text_y: str, text_x: str) -> float:
        # TODO: Calculate H(Y|X) = H(Y) - I(X;Y)
        pass

# Test your implementation
calculator = MutualInformationCalculator()
# Add test cases here
```

### Exercise 2: Information-Theoretic Component Selector (练习 2：信息论组件选择器)
**Goal**: Build system that selects optimal components using information theory
**目标**: 构建使用信息论选择最优组件的系统

```python
class InformationBasedSelector:
    def __init__(self, token_budget: int):
        self.token_budget = token_budget
        
    def select_components(self, candidates: List[str], 
                         query: str) -> List[str]:
        # TODO: Implement greedy selection maximizing mutual information
        # TODO: Include redundancy penalties
        # TODO: Respect token budget constraints
        pass
    
    def calculate_selection_quality(self, selected: List[str], 
                                   query: str) -> Dict[str, float]:
        # TODO: Return comprehensive quality metrics
        pass

# Test your selector
selector = InformationBasedSelector(token_budget=200)
```

### Exercise 3: Adaptive Information Compression (练习 3：自适应信息压缩)
**Goal**: Create compression system that preserves maximum information
**目标**: 创建保留最大信息量的压缩系统

```python
class InformationPreservingCompressor:
    def __init__(self):
        # TODO: Initialize compression algorithms
        pass
    
    def compress_with_entropy_preservation(self, text: str, 
                                         compression_ratio: float) -> str:
        # TODO: Compress while preserving highest entropy content
        pass
    
    def measure_compression_quality(self, original: str, 
                                   compressed: str) -> Dict[str, float]:
        # TODO: Calculate information preservation metrics
        pass

# Test compression system
compressor = InformationPreservingCompressor()
```

---

## Summary and Next Steps (总结和后续步骤)

### Key Concepts Mastered (掌握的关键概念)

**Information Theory Foundations**:
- Shannon entropy: H(X) = -Σ P(x) × log₂(P(x))
- Mutual information: I(X;Y) = H(X) + H(Y) - H(X,Y)
- Conditional entropy and information gain calculations
- Redundancy detection and elimination strategies

**信息论基础**:
- 香农熵：H(X) = -Σ P(x) × log₂(P(x))
- 互信息：I(X;Y) = H(X) + H(Y) - H(X,Y)
- 条件熵和信息增益计算
- 冗余检测和消除策略

**Three Paradigm Integration**:
- **Prompts**: Strategic templates for information assessment and optimization
- **Programming**: Computational algorithms for information-theoretic calculations
- **Protocols**: Adaptive systems that learn optimal information selection patterns

**三个范式的整合**:
- **提示**: 用于信息评估和优化的战略模板
- **编程**: 用于信息论计算的计算算法
- **协议**: 学习最优信息选择模式的自适应系统

**Advanced Information Applications**:
- Component selection based on mutual information maximization
- Intelligent compression preserving semantic and information content
- Redundancy elimination with mathematical precision
- Information quality assessment using multiple metrics

**高级信息应用**:
- 基于互信息最大化的组件选择
- 保留语义和信息内容的智能压缩
- 具有数学精度的冗余消除
- 使用多个指标进行信息质量评估

### Practical Mastery Achieved (实现的实际掌握)

You can now:
1. **Quantify information value** using mathematical information theory
2. **Optimize component selection** to maximize mutual information with queries
3. **Eliminate redundancy** while preserving unique information content
4. **Compress information intelligently** maintaining semantic coherence
5. **Build adaptive systems** that learn optimal information patterns

您现在可以:
1. **使用数学信息论量化信息价值**
2. **优化组件选择**以最大化与查询的互信息
3. **消除冗余**同时保留独特的信息内容
4. **智能压缩信息**保持语义连贯性
5. **构建学习最优信息模式的自适应系统**

### Connection to Course Progression (与课程进展的联系)

This information theory foundation enables:
- **Bayesian Inference** (Module 04): Probabilistic reasoning about information uncertainty
- **Advanced Context Systems**: Information-theoretic optimization in real applications
- **Research Applications**: Contributing to information-theoretic context engineering research

这个信息论基础使得:
- **贝叶斯推断**（模块 04）：关于信息不确定性的概率推理
- **高级上下文系统**：在实际应用中的信息论优化
- **研究应用**：为信息论上下文工程研究做出贡献

The mathematical precision in information measurement you've mastered here provides the quantitative foundation for making optimal decisions about what information to include, exclude, and how to organize it most effectively.
您在这里掌握的信息测量的数学精度，为做出关于包含、排除哪些信息以及如何最有效地组织信息的最佳决策提供了定量基础。

**Next Module**: [04_bayesian_inference.md](04_bayesian_inference.md) - Where we'll learn to reason about uncertainty in context selection and adapt context strategies based on probabilistic feedback.
**下一个模块**: [04_bayesian_inference.md](04_bayesian_inference.md) - 在这里，我们将学习如何在上下文选择中对不确定性进行推理，并根据概率反馈调整上下文策略。

---

## Quick Reference: Information Theory Formulas (快速参考：信息论公式)

| Concept | Formula | Application |
|---------|---------|-------------|
| **Entropy** | H(X) = -Σ P(x)log₂(P(x)) | Measure information content |
| **Mutual Information** | I(X;Y) = H(X) + H(Y) - H(X,Y) | Measure relevance/overlap |
| **Conditional Entropy** | H(Y\|X) = H(Y) - I(X;Y) | Remaining uncertainty |
| **Information Gain** | IG = H(before) - H(after) | Value of additional info |
| **Redundancy** | R = I(X;Y) / min(H(X),H(Y)) | Duplicate information |

| 概念 | 公式 | 应用 |
|---|---|---|
| **熵** | H(X) = -Σ P(x)log₂(P(x)) | 测量信息内容 |
| **互信息** | I(X;Y) = H(X) + H(Y) - H(X,Y) | 测量相关性/重叠 |
| **条件熵** | H(Y\|X) = H(Y) - I(X;Y) | 剩余不确定性 |
| **信息增益** | IG = H(before) - H(after) | 附加信息的价值 |
| **冗余** | R = I(X;Y) / min(H(X),H(Y)) | 重复信息 |

This information theory mastery transforms context engineering from intuitive relevance assessment to mathematically precise information optimization based on fundamental principles of information science.
这种信息论的掌握将上下文工程从直观的相关性评估转变为基于信息科学基本原理的数学精确的信息优化。