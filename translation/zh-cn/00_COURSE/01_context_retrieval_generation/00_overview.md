# Context Retrieval and Generation (上下文检索与生成)
## From Static Prompts to Dynamic Knowledge Orchestration (从静态提示到动态知识编排)

> **Module 01** | *Context Engineering Course: From Foundations to Frontier Systems*
> **模块 01** | *上下文工程课程：从基础到前沿系统*
> 
> Building on [Context Engineering Survey](https://arxiv.org/pdf/2507.13334) | Advancing Software 3.0 Paradigms
> 基于 [上下文工程调查](https://arxiv.org/pdf/2507.13334) | 推进软件 3.0 范式

---

## Learning Objectives (学习目标)

By the end of this module, you will understand and implement:
在本模块结束时，您将理解并实现：

- **Advanced Prompt Engineering**: From basic prompts to sophisticated reasoning templates
- **External Knowledge Integration**: RAG foundations and dynamic knowledge retrieval
- **Dynamic Context Assembly**: Real-time composition of multi-source information
- **Strategic Context Orchestration**: Optimization of information payload for maximum model effectiveness

- **高级提示工程**：从基本提示到复杂的推理模板
- **外部知识整合**：RAG 基础和动态知识检索
- **动态上下文组合**：多源信息的实时组合
- **战略性上下文编排**：优化信息有效载荷以实现最大模型效能

---

## Conceptual Progression: Static Text to Intelligent Knowledge Orchestration (概念演进：从静态文本到智能知识编排)

Think of context generation like the evolution of how we provide information to someone solving a problem - from handing them a single document, to organizing a research library, to having an intelligent research assistant who knows exactly what information to gather and how to present it.
将上下文生成想象成我们向解决问题的人提供信息方式的演变——从递给他们一份文件，到组织一个研究图书馆，再到拥有一个知道确切需要收集哪些信息以及如何呈现这些信息的智能研究助理。

### Stage 1: Static Prompt Engineering (第一阶段：静态提示工程)
```
"Solve this problem: [problem description]"
```
**Context**: Like giving someone a single instruction sheet. Simple and direct, but limited by what you can fit in one document.
**上下文**：就像给某人一张单独的说明书。简单直接，但受限于一份文件所能容纳的内容。

### Stage 2: Enhanced Prompt Patterns (第二阶段：增强提示模式)
```
"Let's think step by step:
1. First, understand the problem...
2. Then consider approaches...
3. Finally implement the solution..."
```
**Context**: Like providing a structured methodology. More effective because it guides thinking process, but still constrained by static content.
**上下文**：就像提供一个结构化的方法论。更有效，因为它指导了思维过程，但仍然受到静态内容的限制。

### Stage 3: External Knowledge Integration (第三阶段：外部知识整合)
```
[Retrieved relevant information from knowledge base]
"Given the following context: [external knowledge]
Now solve: [problem]"
```
**Context**: Like having access to a research library. Much more powerful because it can include specialized, current information beyond what fits in working memory.
**上下文**：就像可以访问研究图书馆一样。功能强大得多，因为它可以包含超出工作记忆容量的专门、最新的信息。

### Stage 4: Dynamic Context Assembly (第四阶段：动态上下文组合)
```
Context = Assemble(
    task_instructions + 
    relevant_retrieved_knowledge + 
    user_history + 
    domain_expertise + 
    real_time_data
)
```
**Context**: Like having a research assistant who gathers exactly the right information from multiple sources and organizes it optimally for your specific task.
**上下文**：就像有一个研究助理，他能从多个来源收集恰到好处的信息，并为您的特定任务进行最佳组织。

### Stage 5: Intelligent Context Orchestration (第五阶段：智能上下文编排)
```
Adaptive Context System:
- Understands your goals and constraints
- Monitors your progress and adapts information flow
- Learns from outcomes to improve future context assembly
- Balances relevance, completeness, and cognitive load
```
**Context**: Like having an AI research partner who understands not just what you need to know, but how you think and learn, continuously optimizing the information environment for maximum effectiveness.
**上下文**：就像拥有一个人工智能研究伙伴，他不仅了解您需要知道什么，还了解您的思维和学习方式，并不断优化信息环境以实现最大效率。

---

## Mathematical Foundations (数学基础)

### Context Formalization Framework (上下文形式化框架)
From our core mathematical foundation:
从我们的核心数学基础：
```
C = A(cinstr, cknow, ctools, cmem, cstate, cquery)
```

In this module, we focus primarily on **cknow** (external knowledge) and the assembly function **A**, specifically:
在本模块中，我们主要关注 **cknow**（外部知识）和组合函数 **A**，具体来说：

```
cknow = R(cquery, K)
```

Where:
- **R** is the retrieval function
- **cquery** is the user's immediate request  
- **K** is the external knowledge base

其中：
- **R** 是检索函数
- **cquery** 是用户的即时请求
- **K** 是外部知识库

### Information-Theoretic Optimization (信息论优化)
The optimal retrieval function maximizes relevant information:
最优检索函数最大化相关信息：
```
R* = arg max_R I(Y*; cknow | cquery)
```

Where **I(Y*; cknow | cquery)** is the mutual information between the target response **Y*** and the retrieved knowledge **cknow**, given the query **cquery**.
其中 **I(Y*; cknow | cquery)** 是在给定查询 **cquery** 的情况下，目标响应 **Y*** 和检索到的知识 **cknow** 之间的互信息。

**Intuitive Explanation**: We want to retrieve information that tells us the most about what the correct answer should be. This is like a skilled librarian who doesn't just find books on your topic, but finds the specific books that contain the exact insights you need.
**直观解释**：我们希望检索能够最大程度地告诉我们正确答案应该是什么的信息。这就像一个熟练的图书管理员，他不仅能找到关于你主题的书籍，还能找到包含你所需确切见解的特定书籍。

### Dynamic Assembly Optimization (动态组合优化)
```
A*(cinstr, cknow, cmem, cquery) = arg max_A P(Y* | A(...)) × Efficiency(A)
```

Subject to constraints:
- `|A(...)| ≤ Lmax` (context window limit)
- `Quality(cknow) ≥ threshold` (information quality threshold)
- `Relevance(cknow, cquery) ≥ min_relevance` (relevance threshold)

受约束于：
- `|A(...)| ≤ Lmax`（上下文窗口限制）
- `Quality(cknow) ≥ threshold`（信息质量阈值）
- `Relevance(cknow, cquery) ≥ min_relevance`（相关性阈值）

**Intuitive Explanation**: The assembly function is like a master editor who knows how to combine different pieces of information into a coherent, effective brief that maximizes the chance of getting a great response while staying within practical limits.
**直观解释**：组合函数就像一位大师级的编辑，他知道如何将不同的信息片段组合成一份连贯、有效的简报，从而在实际限制内最大化获得出色响应的机会。

---

## Visual Architecture: The Context Engineering Stack (可视化架构：上下文工程栈)

```
┌─────────────────────────────────────────────────────────────┐
│                    CONTEXT ASSEMBLY LAYER (上下文组合层)                  │
│  ┌─────────────────┬────────────────┬─────────────────────┐ │
│  │   INSTRUCTIONS (指令)  │    KNOWLEDGE (知识)   │      ORCHESTRATION (编排)  │ │
│  │                 │                │                     │ │
│  │  • Task specs (任务规范)   │  • Retrieved (检索到的)   │  • Assembly logic (组合逻辑)  │ │
│  │  • Constraints (约束)  │    documents (文档)   │  • Prioritization (优先级)  │ │
│  │  • Examples (示例)     │  • Real-time (实时)   │  • Formatting (格式化)      │ │
│  │  • Format rules (格式规则) │    data (数据)        │  • Length mgmt (长度管理)     │ │
│  └─────────────────┴────────────────┴─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ▲
┌─────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE RETRIEVAL LAYER (知识检索层)                │
│  ┌─────────────────┬────────────────┬─────────────────────┐ │
│  │   QUERY PROC (查询处理)    │   RETRIEVAL (检索)    │    KNOWLEDGE BASES (知识库)  │ │
│  │                 │                │                     │ │
│  │  • Query anal (查询分析)   │  • Vector (向量)      │  • Documents (文档)       │ │
│  │  • Intent extr (意图提取)  │    search (搜索)      │  • Databases (数据库)       │ │
│  │  • Expansion (扩展)    │  • Semantic (语义)    │  • APIs (应用程序接口)            │ │
│  │  • Filtering (过滤)    │    matching (匹配)    │  • Real-time (实时)       │ │
│  └─────────────────┴────────────────┴─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
                              ▲
┌─────────────────────────────────────────────────────────────┐
│                    PROMPT ENGINEERING LAYER (提示工程层)                │
│  ┌─────────────────┬────────────────┬─────────────────────┐ │
│  │  BASIC PROMPTS (基本提示)  │   TEMPLATES (模板)    │   REASONING CHAINS (推理链)  │ │
│  │                 │                │                     │ │
│  │  • Direct inst (直接指令) │  • Reusable (可重用)    │  • Chain-of-thought (思维链) │ │
│  │  • Few-shot (少样本)     │    patterns (模式)    │  • Tree-of-thought (思维树)  │ │
│  │  • Zero-shot (零样本)    │  • Domain (领域)      │  • Self-consistency (自我一致性) │ │
│  │  • Role-based (基于角色)   │    specific (特定)    │  • Reflection (反思)       │ │
│  └─────────────────┴────────────────┴─────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

**Ground-up Explanation**: This stack shows how context engineering builds up from basic prompts to sophisticated information orchestration. Each layer adds capability:
- **Bottom Layer**: Core prompt engineering - how to communicate effectively with LLMs
- **Middle Layer**: Knowledge retrieval - how to find and access relevant external information  
- **Top Layer**: Context assembly - how to combine everything optimally

**从头解释**：这个堆栈展示了上下文工程如何从基本的提示发展到复杂的信息编排。每一层都增加了能力：
- **底层**：核心提示工程——如何与大型语言模型有效沟通
- **中层**：知识检索——如何查找和访问相关的外部信息
- **顶层**：上下文组合——如何最佳地组合所有内容

---

## Software 3.0 Paradigm 1: Prompts (Strategic Templates) (软件 3.0 范式 1：提示（战略模板）)

Prompts in context engineering go beyond simple instructions to become strategic templates for information gathering and reasoning.
在上下文工程中，提示超越了简单的指令，成为信息收集和推理的战略模板。

### Advanced Reasoning Template (高级推理模板)
```markdown
# Chain-of-Thought Reasoning Framework

## Context Assessment
You are tasked with [specific_task] requiring deep analysis and step-by-step reasoning.
Consider the complexity, available information, and reasoning requirements.

## Information Inventory
**Available Context**: {context_summary}
**Missing Information**: {information_gaps}
**Assumptions Required**: {necessary_assumptions}
**Reasoning Type**: {deductive|inductive|abductive|analogical}

## Structured Reasoning Process

### Step 1: Problem Decomposition
Break down the main question into sub-questions:
1. {subquestion_1}
2. {subquestion_2}  
3. {subquestion_3}

### Step 2: Evidence Analysis
For each sub-question, analyze available evidence:
- **Supporting Evidence**: [list relevant supporting information]
- **Contradicting Evidence**: [list conflicting information]
- **Evidence Quality**: [assess reliability and relevance]
- **Evidence Gaps**: [identify missing crucial information]

### Step 3: Reasoning Chain Construction
Build logical connections between evidence and conclusions:

Premise 1: [statement with evidence]
    ├─ Supporting detail A
    ├─ Supporting detail B
    └─ Confidence level: [high/medium/low]

Premise 2: [statement with evidence] 
    ├─ Supporting detail C
    ├─ Supporting detail D
    └─ Confidence level: [high/medium/low]

Intermediate Conclusion: [logical inference from premises]
    └─ Reasoning: [explain the logical connection]


### Step 4: Alternative Hypothesis Consideration
What other explanations or solutions are possible?
- **Alternative 1**: [different interpretation/approach]
  - Strengths: [what supports this alternative]
  - Weaknesses: [what argues against it]
- **Alternative 2**: [another interpretation/approach]
  - Strengths: [supporting factors]
  - Weaknesses: [limiting factors]

### Step 5: Synthesis and Conclusion
**Primary Conclusion**: [main answer/solution]
**Confidence Level**: [percentage or qualitative assessment]
**Key Reasoning**: [the most critical logical steps that led to this conclusion]
**Limitations**: [what could make this conclusion wrong]
**Next Steps**: [what additional information would strengthen the conclusion]

## Quality Assurance
- [ ] Have I addressed all sub-questions?
- [ ] Are my logical connections explicit and valid?
- [ ] Have I considered major alternative explanations?
- [ ] Is my confidence assessment realistic?
- [ ] Can someone else follow my reasoning chain?
```

**Ground-up Explanation**: This template transforms the simple "let's think step by step" approach into a comprehensive reasoning methodology. It's like having a master logician guide your thinking process, ensuring you consider all angles, make explicit connections, and assess your own reasoning quality.
**从头解释**：此模板将简单的“让我们一步一步思考”的方法转变为全面的推理方法论。这就像有一位逻辑大师指导您的思维过程，确保您考虑所有角度，建立明确的联系，并评估您自己的推理质量。

### Dynamic Knowledge Integration Template (动态知识集成模板)
```xml
<knowledge_integration_template>
  <intent>Systematically integrate external knowledge with user query for optimal response</intent>
  
  <context_analysis>
    <user_query>
      <main_intent>{primary_user_goal}</main_intent>
      <sub_intents>
        <intent priority="high">{critical_sub_goal}</intent>
        <intent priority="medium">{important_sub_goal}</intent>
        <intent priority="low">{optional_sub_goal}</intent>
      </sub_intents>
      <complexity_level>{simple|moderate|complex|expert}</complexity_level>
      <domain_context>{specific_field_or_general}</domain_context>
    </user_query>
    
    <information_needs>
      <critical_info>Information absolutely required for accurate response</critical_info>
      <supporting_info>Information that would improve response quality</supporting_info>
      <contextual_info>Information that provides helpful background</contextual_info>
    </information_needs>
  </context_analysis>
  
  <knowledge_retrieval_strategy>
    <search_approach>
      <primary_search>{most_likely_to_find_critical_info}</primary_search>
      <secondary_search>{backup_approach_for_comprehensive_coverage}</secondary_search>
      <tertiary_search>{specialized_or_edge_case_coverage}</tertiary_search>
    </search_approach>
    
    <quality_filters>
      <relevance_threshold>How closely information must match query intent</relevance_threshold>
      <credibility_threshold>Minimum source reliability standard</credibility_threshold>
      <recency_weight>How much to prioritize recent vs authoritative information</recency_weight>
    </quality_filters>
  </knowledge_retrieval_strategy>
  
  <context_assembly>
    <information_hierarchy>
      <tier_1>Core facts directly answering main question</tier_1>
      <tier_2>Supporting evidence and explanations</tier_2>
      <tier_3>Background context and related information</tier_3>
    </information_hierarchy>
    
    <assembly_constraints>
      <max_context_length>{token_limit_consideration}</max_context_length>
      <cognitive_load_limit>Maximum information complexity for user comprehension</cognitive_load_limit>
      <coherence_requirement>How information should connect logically</coherence_requirement>
    </assembly_constraints>
    
    <assembly_process>
      <step name="prioritize">Rank retrieved information by relevance and importance</step>
      <step name="filter">Remove redundant, outdated, or low-quality information</step>
      <step name="structure">Organize information for logical flow and comprehension</step>
      <step name="integrate">Weave information into coherent narrative addressing user query</step>
      <step name="validate">Ensure assembled context supports accurate, helpful response</step>
    </assembly_process>
  </context_assembly>
  
  <response_optimization>
    <tailoring>
      <user_expertise_level>Adjust technical depth appropriately</user_expertise_level>
      <communication_style>Match user's preferred interaction mode</communication_style>
      <information_density>Balance comprehensiveness with clarity</information_density>
    </tailoring>
    
    <quality_assurance>
      <accuracy_check>Verify information correctness and context alignment</accuracy_check>
      <completeness_check>Ensure all critical user needs are addressed</completeness_check>
      <coherence_check>Confirm logical flow and clear communication</coherence_check>
    </quality_assurance>
  </response_optimization>
</knowledge_integration_template>
```

**Ground-up Explanation**: This XML template structures the complex process of finding and integrating external knowledge. It's like having a research methodology that ensures you not only find relevant information, but organize and present it in the most effective way for the specific user and task.
**从头解释**：此 XML 模板构建了查找和整合外部知识的复杂过程。这就像拥有一种研究方法，不仅能确保您找到相关信息，还能以最有效的方式为特定用户和任务组织和呈现这些信息。

---

## Software 3.0 Paradigm 2: Programming (Retrieval Algorithms) (软件 3.0 范式 2：编程（检索算法）)

Programming provides the computational mechanisms for intelligent context retrieval and assembly.
编程为智能上下文检索和组合提供了计算机制。

### Semantic Retrieval Engine (语义检索引擎)

```python
import numpy as np
from typing import Dict, List, Optional, Tuple, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod
import sqlite3
import json
from datetime import datetime, timedelta

@dataclass
class RetrievalCandidate:
    """A piece of information that could be relevant to the query"""
    content: str
    source: str
    relevance_score: float
    credibility_score: float
    recency_score: float
    content_type: str  # 'fact', 'procedure', 'example', 'definition'
    metadata: Dict
    
class KnowledgeRetriever(ABC):
    """Abstract base for different knowledge retrieval strategies"""
    
    @abstractmethod
    def retrieve(self, query: str, max_results: int = 10) -> List[RetrievalCandidate]:
        """Retrieve relevant knowledge for the given query"""
        pass
    
    @abstractmethod
    def update_relevance_feedback(self, query: str, candidate: RetrievalCandidate, 
                                 helpful: bool):
        """Learn from user feedback about retrieval quality"""
        pass

class SemanticVectorRetriever(KnowledgeRetriever):
    """Retrieval using semantic similarity via embeddings"""
    
    def __init__(self, embedding_model, vector_database):
        self.embedding_model = embedding_model
        self.vector_db = vector_database
        self.feedback_history = []
        
    def retrieve(self, query: str, max_results: int = 10) -> List[RetrievalCandidate]:
        """Retrieve semantically similar content"""
        
        # Generate query embedding
        query_embedding = self.embedding_model.encode(query)
        
        # Search vector database
        raw_results = self.vector_db.similarity_search(
            query_embedding, 
            top_k=max_results * 2  # Get more candidates for filtering
        )
        
        # Convert to RetrievalCandidates with scoring
        candidates = []
        for result in raw_results:
            candidate = RetrievalCandidate(
                content=result.content,
                source=result.source,
                relevance_score=self._calculate_relevance_score(query, result),
                credibility_score=self._calculate_credibility_score(result),
                recency_score=self._calculate_recency_score(result),
                content_type=self._classify_content_type(result.content),
                metadata=result.metadata
            )
            candidates.append(candidate)
        
        # Apply learning from feedback history
        candidates = self._apply_feedback_learning(query, candidates)
        
        # Rank and filter
        ranked_candidates = self._rank_candidates(candidates)
        
        return ranked_candidates[:max_results]
    
    def _calculate_relevance_score(self, query: str, result) -> float:
        """Calculate how relevant the content is to the query"""
        
        # Base semantic similarity
        base_score = result.similarity_score
        
        # Adjust based on content type match
        content_type_bonus = self._get_content_type_bonus(query, result.content)
        
        # Adjust based on query specificity
        specificity_factor = self._calculate_query_specificity_factor(query, result)
        
        # Combine factors
        relevance_score = base_score * (1 + content_type_bonus) * specificity_factor
        
        return min(1.0, max(0.0, relevance_score))
    
    def _calculate_credibility_score(self, result) -> float:
        """Assess source credibility and information quality"""
        
        # Source authority (academic, government, established organization)
        source_authority = self._get_source_authority_score(result.source)
        
        # Content quality indicators (length, structure, citations)
        content_quality = self._assess_content_quality(result.content)
        
        # Cross-reference validation (how well it aligns with other sources)
        cross_reference_score = self._calculate_cross_reference_score(result)
        
        # Combine factors
        credibility = (source_authority * 0.4 + 
                      content_quality * 0.3 + 
                      cross_reference_score * 0.3)
        
        return credibility
    
    def _calculate_recency_score(self, result) -> float:
        """Score based on information recency (more recent = higher score)"""
        if 'date' not in result.metadata:
            return 0.5  # Neutral score for undated content
            
        content_date = datetime.fromisoformat(result.metadata['date'])
        days_old = (datetime.now() - content_date).days
        
        # Exponential decay: score decreases as content gets older
        # Half-life of 365 days (information relevance decreases by half each year)
        half_life = 365
        recency_score = 0.5 ** (days_old / half_life)
        
        return recency_score
    
    def _classify_content_type(self, content: str) -> str:
        """Classify content as fact, procedure, example, or definition"""
        
        # Simple heuristic classification (in practice, use ML classifier)
        content_lower = content.lower()
        
        if any(phrase in content_lower for phrase in ['step', 'first', 'then', 'finally', 'procedure']):
            return 'procedure'
        elif any(phrase in content_lower for phrase in ['for example', 'such as', 'instance']):
            return 'example'
        elif any(phrase in content_lower for phrase in ['is defined as', 'refers to', 'means']):
            return 'definition'
        else:
            return 'fact'
    
    def _rank_candidates(self, candidates: List[RetrievalCandidate]) -> List[RetrievalCandidate]:
        """Rank candidates using composite scoring"""
        
        for candidate in candidates:
            # Composite score balancing multiple factors
            candidate.composite_score = (
                candidate.relevance_score * 0.5 +      # Relevance is most important
                candidate.credibility_score * 0.3 +    # Credibility is very important  
                candidate.recency_score * 0.2          # Recency matters but less
            )
        
        # Sort by composite score
        ranked = sorted(candidates, key=lambda c: c.composite_score, reverse=True)
        
        return ranked
    
    def update_relevance_feedback(self, query: str, candidate: RetrievalCandidate, 
                                 helpful: bool):
        """Learn from feedback to improve future retrieval"""
        
        feedback_entry = {
            'query': query,
            'candidate_source': candidate.source,
            'candidate_type': candidate.content_type,
            'helpful': helpful,
            'timestamp': datetime.now().isoformat()
        }
        
        self.feedback_history.append(feedback_entry)
        
        # Update retrieval parameters based on feedback patterns
        self._update_retrieval_parameters()
    
    def _apply_feedback_learning(self, query: str, candidates: List[RetrievalCandidate]) -> List[RetrievalCandidate]:
        """Adjust candidate scores based on learned feedback patterns"""
        
        if not self.feedback_history:
            return candidates
        
        # Analyze feedback patterns
        feedback_patterns = self._analyze_feedback_patterns(query)
        
        # Adjust scores based on patterns
        for candidate in candidates:
            adjustment = self._calculate_feedback_adjustment(candidate, feedback_patterns)
            candidate.relevance_score = min(1.0, max(0.0, candidate.relevance_score + adjustment))
        
        return candidates
    
    def _analyze_feedback_patterns(self, query: str) -> Dict:
        """Analyze historical feedback to identify useful patterns"""
        
        patterns = {
            'helpful_sources': [],
            'helpful_content_types': [],
            'unhelpful_sources': [],
            'unhelpful_content_types': []
        }
        
        # Group feedback by helpfulness
        for feedback in self.feedback_history[-100:]:  # Recent feedback
            if self._is_similar_query(query, feedback['query']):
                if feedback['helpful']:
                    patterns['helpful_sources'].append(feedback['candidate_source'])
                    patterns['helpful_content_types'].append(feedback['candidate_type'])
                else:
                    patterns['unhelpful_sources'].append(feedback['candidate_source'])
                    patterns['unhelpful_content_types'].append(feedback['candidate_type'])
        
        return patterns

class HybridKnowledgeRetriever(KnowledgeRetriever):
    """Combines multiple retrieval strategies for comprehensive results"""
    
    def __init__(self, retrievers: List[KnowledgeRetriever], weights: List[float] = None):
        self.retrievers = retrievers
        self.weights = weights or [1.0] * len(retrievers)
        self.performance_history = {i: [] for i in range(len(retrievers))}
        
    def retrieve(self, query: str, max_results: int = 10) -> List[RetrievalCandidate]:
        """Retrieve from multiple sources and intelligently combine results"""
        
        all_candidates = []
        
        # Retrieve from each strategy
        for i, retriever in enumerate(self.retrievers):
            try:
                candidates = retriever.retrieve(query, max_results)
                
                # Weight candidates based on retriever performance
                weight = self.weights[i] * self._get_dynamic_weight(i, query)
                
                for candidate in candidates:
                    candidate.composite_score *= weight
                    candidate.metadata['retriever_id'] = i
                
                all_candidates.extend(candidates)
                
            except Exception as e:
                print(f"Retriever {i} failed: {e}")
                continue
        
        # Remove duplicates and merge similar content
        unique_candidates = self._deduplicate_candidates(all_candidates)
        
        # Rank final candidates
        final_candidates = self._rank_hybrid_candidates(unique_candidates)
        
        return final_candidates[:max_results]
    
    def _get_dynamic_weight(self, retriever_id: int, query: str) -> float:
        """Calculate dynamic weight based on retriever performance for similar queries"""
        
        if not self.performance_history[retriever_id]:
            return 1.0  # Default weight for new retrievers
        
        # Calculate recent performance average
        recent_performance = self.performance_history[retriever_id][-10:]  # Last 10 queries
        avg_performance = sum(recent_performance) / len(recent_performance)
        
        # Dynamic weight based on performance (better performers get higher weight)
        return max(0.1, min(2.0, avg_performance))
    
    def _deduplicate_candidates(self, candidates: List[RetrievalCandidate]) -> List[RetrievalCandidate]:
        """Remove duplicate and very similar candidates"""
        
        unique_candidates = []
        content_hashes = set()
        
        for candidate in sorted(candidates, key=lambda c: c.composite_score, reverse=True):
            # Simple deduplication based on content similarity
            content_hash = hash(candidate.content[:200])  # Hash first 200 chars
            
            if content_hash not in content_hashes:
                content_hashes.add(content_hash)
                unique_candidates.append(candidate)
        
        return unique_candidates
    
    def update_relevance_feedback(self, query: str, candidate: RetrievalCandidate, helpful: bool):
        """Update feedback for the specific retriever that provided this candidate"""
        
        retriever_id = candidate.metadata.get('retriever_id')
        if retriever_id is not None:
            # Update performance history
            performance_score = 1.0 if helpful else 0.0
            self.performance_history[retriever_id].append(performance_score)
            
            # Forward feedback to specific retriever
            self.retrievers[retriever_id].update_relevance_feedback(query, candidate, helpful)

class DynamicContextAssembler:
    """Assembles optimal context from retrieved knowledge and other sources"""
    
    def __init__(self, max_context_length: int = 4000):
        self.max_context_length = max_context_length
        self.assembly_history = []
        
    def assemble_context(self, query: str, retrieved_candidates: List[RetrievalCandidate],
                        instructions: str = "", user_context: str = "",
                        task_type: str = "general") -> str:
        """Dynamically assemble optimal context from available information"""
        
        # Analyze query to understand information needs
        info_needs = self._analyze_information_needs(query, task_type)
        
        # Select optimal subset of candidates
        selected_candidates = self._select_optimal_candidates(
            retrieved_candidates, info_needs, self.max_context_length
        )
        
        # Structure and format context
        assembled_context = self._structure_context(
            instructions, selected_candidates, user_context, query, info_needs
        )
        
        # Validate and optimize final context
        optimized_context = self._optimize_context(assembled_context, query)
        
        return optimized_context
    
    def _analyze_information_needs(self, query: str, task_type: str) -> Dict:
        """Analyze what types of information are needed for this query"""
        
        needs = {
            'definitions': 0.0,
            'facts': 0.0,
            'procedures': 0.0,
            'examples': 0.0,
            'background': 0.0
        }
        
        query_lower = query.lower()
        
        # Heuristic analysis of information needs
        if any(word in query_lower for word in ['what is', 'define', 'meaning', 'definition']):
            needs['definitions'] = 1.0
            needs['examples'] = 0.7
            
        elif any(word in query_lower for word in ['how to', 'steps', 'procedure', 'process']):
            needs['procedures'] = 1.0
            needs['examples'] = 0.8
            
        elif any(word in query_lower for word in ['why', 'explain', 'reason', 'cause']):
            needs['facts'] = 1.0
            needs['background'] = 0.8
            
        elif 'example' in query_lower:
            needs['examples'] = 1.0
            needs['procedures'] = 0.5
            
        else:
            # General query - balanced information needs
            for key in needs:
                needs[key] = 0.6
        
        # Adjust based on task type
        if task_type == "analytical":
            needs['facts'] *= 1.3
            needs['background'] *= 1.2
        elif task_type == "practical":
            needs['procedures'] *= 1.3
            needs['examples'] *= 1.2
        elif task_type == "creative":
            needs['examples'] *= 1.2
            needs['background'] *= 1.1
        
        return needs
    
    def _select_optimal_candidates(self, candidates: List[RetrievalCandidate],
                                  info_needs: Dict, max_length: int) -> List[RetrievalCandidate]:
        """Select optimal subset of candidates based on information needs and length constraints"""
        
        # Score candidates based on information needs alignment
        for candidate in candidates:
            content_type_score = info_needs.get(candidate.content_type, 0.5)
            candidate.need_alignment_score = (
                candidate.composite_score * 0.7 + 
                content_type_score * 0.3
            )
        
        # Use greedy knapsack-style selection
        selected = []
        total_length = 0
        remaining_candidates = sorted(candidates, key=lambda c: c.need_alignment_score, reverse=True)
        
        for candidate in remaining_candidates:
            candidate_length = len(candidate.content)
            
            if total_length + candidate_length <= max_length * 0.8:  # Reserve 20% for formatting
                selected.append(candidate)
                total_length += candidate_length
            elif len(selected) < 2:  # Ensure we have at least 2 candidates
                # Truncate content to fit
                available_space = max_length * 0.8 - total_length
                if available_space > 100:  # Only if we can fit meaningful content
                    truncated_candidate = RetrievalCandidate(
                        content=candidate.content[:int(available_space)],
                        source=candidate.source,
                        relevance_score=candidate.relevance_score,
                        credibility_score=candidate.credibility_score,
                        recency_score=candidate.recency_score,
                        content_type=candidate.content_type,
                        metadata=candidate.metadata
                    )
                    selected.append(truncated_candidate)
                    break
        
        return selected
    
    def _structure_context(self, instructions: str, candidates: List[RetrievalCandidate],
                          user_context: str, query: str, info_needs: Dict) -> str:
        """Structure the context for optimal comprehension and utility"""
        
        context_parts = []
        
        # Add instructions if provided
        if instructions.strip():
            context_parts.append(f"## Instructions\n{instructions}\n")
        
        # Add user context if provided
        if user_context.strip():
            context_parts.append(f"## Context\n{user_context}\n")
        
        # Group candidates by type for better organization
        candidates_by_type = {}
        for candidate in candidates:
            if candidate.content_type not in candidates_by_type:
                candidates_by_type[candidate.content_type] = []
            candidates_by_type[candidate.content_type].append(candidate)
        
        # Add retrieved information in logical order
        type_order = ['definitions', 'facts', 'procedures', 'examples']
        type_labels = {
            'definition': 'Key Definitions',
            'fact': 'Relevant Information', 
            'procedure': 'Procedures and Methods',
            'example': 'Examples and Case Studies'
        }
        
        context_parts.append("## Retrieved Knowledge\n")
        
        for content_type in type_order:
            if content_type in candidates_by_type:
                candidates_of_type = candidates_by_type[content_type]
                section_label = type_labels.get(content_type, content_type.title())
                
                context_parts.append(f"### {section_label}\n")
                
                for i, candidate in enumerate(candidates_of_type, 1):
                    source_note = f" (Source: {candidate.source})" if candidate.source else ""
                    context_parts.append(f"{i}. {candidate.content.strip()}{source_note}\n")
                
                context_parts.append("")  # Add spacing
        
        # Add the user's specific query
        context_parts.append(f"## Current Query\n{query}\n")
        
        return "\n".join(context_parts)
    
    def _optimize_context(self, context: str, query: str) -> str:
        """Final optimization of assembled context"""
        
        # Remove excessive whitespace
        optimized = "\n".join(line.strip() for line in context.split("\n"))
        
        # Remove duplicate information (simple approach)
        lines = optimized.split("\n")
        unique_lines = []
        seen_content = set()
        
        for line in lines:
            if line.strip():
                # Check for substantial duplicates (not just headers)
                line_content = line.lower().strip()
                if len(line_content) > 20:  # Only check substantial lines
                    if line_content not in seen_content:
                        seen_content.add(line_content)
                        unique_lines.append(line)
                else:
                    unique_lines.append(line)
            else:
                unique_lines.append(line)
        
        return "\n".join(unique_lines)

# Example usage demonstrating the complete retrieval and assembly pipeline
class ContextGenerationDemo:
    """Demonstration of complete context generation pipeline"""
    
    def __init__(self):
        # Initialize retrievers (mock implementations for demo)
        self.semantic_retriever = SemanticVectorRetriever(
            embedding_model=MockEmbeddingModel(),
            vector_database=MockVectorDatabase()
        )
        
        self.hybrid_retriever = HybridKnowledgeRetriever([
            self.semantic_retriever,
            # Add other retrievers as needed
        ])
        
        self.context_assembler = DynamicContextAssembler(max_context_length=4000)
    
    def generate_context(self, query: str, instructions: str = "", 
                        user_context: str = "", task_type: str = "general") -> str:
        """Complete context generation pipeline"""
        
        print(f"Generating context for query: '{query}'")
        
        # Step 1: Retrieve relevant knowledge
        print("Step 1: Retrieving knowledge...")
        candidates = self.hybrid_retriever.retrieve(query, max_results=10)
        print(f"Retrieved {len(candidates)} candidates")
        
        # Step 2: Assemble optimal context
        print("Step 2: Assembling context...")
        context = self.context_assembler.assemble_context(
            query, candidates, instructions, user_context, task_type
        )
        
        print(f"Step 3: Generated context ({len(context)} characters)")
        
        return context

# Mock classes for demonstration
class MockEmbeddingModel:
    def encode(self, text: str) -> np.ndarray:
        # Simplified mock embedding
        return np.random.rand(384)

class MockVectorDatabase:
    def __init__(self):
        self.mock_results = [
            MockResult("Machine learning is a subset of artificial intelligence...", "wikipedia.org", 0.85),
            MockResult("To implement a neural network: 1. Define architecture...", "tutorial.com", 0.78),
            MockResult("For example, a simple classification model...", "examples.org", 0.72)
        ]
    
    def similarity_search(self, query_embedding: np.ndarray, top_k: int = 10):
        return self.mock_results[:top_k]

@dataclass 
class MockResult:
    content: str
    source: str
    similarity_score: float
    metadata: Dict = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {"date": "2024-01-01"}
```

**Ground-up Explanation**: This retrieval system works like having multiple research assistants with different specialties, plus a master editor who knows how to combine their findings into the perfect briefing document. The `HybridKnowledgeRetriever` gets input from multiple sources, the `DynamicContextAssembler` organizes everything optimally, and the system learns from feedback to get better over time.
**从头解释**：这个检索系统就像拥有多个不同专业的助理研究员，外加一位知道如何将他们的发现整合成完美简报的大师级编辑。`HybridKnowledgeRetriever` 从多个来源获取输入，`DynamicContextAssembler` 对所有内容进行优化组织，并且系统会从反馈中学习，以便随着时间的推移不断改进。

---

## Software 3.0 Paradigm 3: Protocols (Adaptive Assembly Shells) (软件 3.0 范式 3：协议（自适应组合外壳）)

Protocols provide self-modifying context generation patterns that evolve based on effectiveness.
协议提供了可自我修改的上下文生成模式，这些模式会根据有效性进行演变。

### Adaptive Context Generation Protocol (自适应上下文生成协议)

```
/context.generate.adaptive{
    intent="Dynamically generate optimal context by learning from usage patterns and adapting assembly strategies",
    
    input={
        user_query=<immediate_user_request>,
        task_context={
            domain=<subject_area_or_field>,
            complexity_level=<simple|moderate|complex|expert>,
            user_expertise=<novice|intermediate|advanced|expert>,
            time_constraints=<available_processing_time>,
            quality_requirements=<accuracy_completeness_specificity_needs>
        },
        available_sources={
            knowledge_bases=<accessible_information_repositories>,
            real_time_data=<current_information_streams>,
            user_history=<relevant_past_interactions>,
            domain_expertise=<specialized_knowledge_sources>
        }
    },
    
    process=[
        /analyze.information_needs{
            action="Deep analysis of what information is required for optimal response",
            method="Multi-dimensional need assessment with learning integration",
            analysis_dimensions=[
                {factual_requirements="What facts, data, or evidence are needed?"},
                {conceptual_requirements="What concepts, definitions, or frameworks are needed?"},
                {procedural_requirements="What processes, methods, or steps are needed?"},
                {contextual_requirements="What background or situational information is needed?"},
                {example_requirements="What illustrations, cases, or demonstrations are needed?"}
            ],
            learning_integration="Apply patterns learned from similar successful query contexts",
            output="Comprehensive information need specification with priority weighting"
        },
        
        /orchestrate.multi_source_retrieval{
            action="Intelligently coordinate retrieval from multiple information sources",
            method="Parallel retrieval with strategic source selection and result fusion",
            retrieval_strategies=[
                {semantic_search="Vector similarity matching against knowledge embeddings"},
                {keyword_expansion="Query expansion with domain-specific terminology"},
                {contextual_filtering="Filter by relevance to user context and expertise level"},
                {temporal_prioritization="Weight recent vs authoritative information appropriately"},
                {cross_reference_validation="Verify consistency across multiple sources"}
            ],
            fusion_algorithm="Intelligent combination of results with deduplication and relevance ranking",
            output="Ranked collection of high-quality information candidates"
        },
        
        /optimize.context_assembly{
            action="Assemble retrieved information into optimal context structure",
            method="Dynamic assembly optimization with cognitive load management",
            assembly_strategies=[
                {information_hierarchy="Structure information from most to least critical"},
                {cognitive_chunking="Group related information to reduce cognitive load"},
                {logical_flow="Organize information in natural reasoning progression"},
                {length_optimization="Maximize information value within context window constraints"},
                {user_customization="Adapt presentation style to user expertise and preferences"}
            ],
            optimization_criteria=[
                {relevance_maximization="Ensure every piece of information serves the user's goal"},
                {coherence_enhancement="Create logical connections between information pieces"},
                {clarity_optimization="Present information at appropriate complexity level"},
                {actionability_focus="Emphasize information that enables user action"}
            ],
            output="Optimally structured context ready for model consumption"
        },
        
        /monitor.effectiveness{
            action="Track context generation effectiveness and identify improvement opportunities",
            method="Multi-metric effectiveness assessment with learning integration",
            effectiveness_metrics=[
                {response_quality="How well does the generated context enable high-quality responses?"},
                {user_satisfaction="How satisfied are users with responses generated from this context?"},
                {task_completion="How effectively does the context enable task completion?"},
                {efficiency_measures="Context generation speed and resource utilization"},
                {learning_indicators="Evidence of improved performance over time"}
            ],
            feedback_integration=[
                {explicit_feedback="Direct user ratings and comments on response quality"},
                {implicit_feedback="User behavior patterns indicating satisfaction/dissatisfaction"},
                {outcome_tracking="Long-term success metrics for tasks involving generated contexts"},
                {comparative_analysis="Performance comparison with alternative context generation approaches"}
            ],
            output="Comprehensive effectiveness assessment with specific improvement recommendations"
        }
    ],
    
    output={
        generated_context={
            assembled_information=<optimally_structured_context_ready_for_model>,
            information_sources=<attribution_and_credibility_information>,
            assembly_rationale=<explanation_of_context_construction_decisions>,
            quality_indicators=<confidence_scores_and_completeness_measures>
        },
        
        optimization_metadata={
            retrieval_performance=<metrics_on_information_gathering_effectiveness>,
            assembly_efficiency=<metrics_on_context_construction_performance>,
            predicted_effectiveness=<estimated_quality_of_generated_context>,
            alternative_approaches=<other_context_generation_strategies_considered>
        },
        
        learning_updates={
            pattern_discoveries=<new_effective_patterns_identified>,
            strategy_refinements=<improvements_to_existing_approaches>,
            feedback_integration=<how_user_feedback_influenced_context_generation>,
            knowledge_base_updates=<improvements_to_underlying_information_sources>
        }
    },
    
    // Self-improvement mechanisms
    adaptation_triggers=[
        {condition="user_satisfaction < 0.7", action="analyze_context_assembly_weaknesses"},
        {condition="response_quality_decline_detected", action="audit_information_source_quality"},
        {condition="new_domain_patterns_identified", action="integrate_domain_specific_optimizations"},
        {condition="efficiency_below_threshold", action="optimize_retrieval_and_assembly_performance"}
    ],
    
    meta={
        context_generation_version="adaptive_v2.1",
        learning_integration_level="advanced",
        adaptation_frequency="continuous_with_batch_updates",
        quality_assurance="multi_dimensional_effectiveness_monitoring"
    }
}
```

**Ground-up Explanation**: This protocol creates a self-improving context generation system. Like having a research team that gets better at finding and organizing information each time they work on a project, learning what kinds of information are most valuable for different types of questions and users.
**从头解释**：该协议创建了一个自我完善的上下文生成系统。就像拥有一支研究团队，每次开展项目时，他们都会在查找和组织信息方面做得更好，从而了解哪种信息对不同类型的问题和用户最有价值。

---

## Integration and Real-World Applications (集成和实际应用)

### Case Study: Medical Diagnosis Support Context Generation (案例研究：医疗诊断支持上下文生成)

```python
def medical_diagnosis_context_example():
    """Demonstrate context generation for medical diagnosis support"""
    
    # Simulated medical query
    query = "Patient presents with chest pain, shortness of breath, and elevated troponin levels. What are the differential diagnoses and recommended diagnostic workup?"
    
    # Medical-specific context generation
    medical_context_generator = ContextGenerationDemo()
    
    # Generate specialized medical context
    context = medical_context_generator.generate_context(
        query=query,
        instructions="""
        You are providing medical decision support. Focus on:
        1. Evidence-based differential diagnoses
        2. Appropriate diagnostic workup recommendations  
        3. Risk stratification considerations
        4. Latest clinical guidelines and protocols
        
        Always emphasize the need for clinical judgment and direct patient evaluation.
        """,
        user_context="Emergency department setting, adult patient, no known allergies",
        task_type="analytical"
    )
    
    print("Medical Diagnosis Support Context:")
    print("=" * 50)
    print(context)
    
    return context
```

### Performance Evaluation Framework (性能评估框架)

```python
class ContextGenerationEvaluator:
    """Comprehensive evaluation of context generation effectiveness"""
    
    def __init__(self):
        self.evaluation_metrics = {
            'relevance': self._evaluate_relevance,
            'completeness': self._evaluate_completeness,
            'clarity': self._evaluate_clarity,
            'efficiency': self._evaluate_efficiency,
            'adaptability': self._evaluate_adaptability
        }
    
    def evaluate_context_generation(self, query: str, generated_context: str, 
                                   response_quality: float, user_feedback: Dict) -> Dict:
        """Comprehensive evaluation of context generation performance"""
        
        results = {}
        for metric_name, metric_function in self.evaluation_metrics.items():
            score = metric_function(query, generated_context, response_quality, user_feedback)
            results[metric_name] = score
        
        # Calculate overall effectiveness
        results['overall_effectiveness'] = self._calculate_overall_effectiveness(results)
        
        # Generate improvement recommendations
        results['improvement_recommendations'] = self._generate_improvement_recommendations(results)
        
        return results
    
    def _evaluate_relevance(self, query: str, context: str, response_quality: float, feedback: Dict) -> float:
        """Evaluate how relevant the generated context is to the query"""
        
        # Analyze semantic alignment between query and context
        query_terms = set(query.lower().split())
        context_terms = set(context.lower().split())
        
        term_overlap = len(query_terms.intersection(context_terms)) / len(query_terms.union(context_terms))
        
        # Factor in response quality as indicator of context relevance
        relevance_score = (term_overlap * 0.3 + response_quality * 0.7)
        
        return min(1.0, max(0.0, relevance_score))
    
    def _evaluate_completeness(self, query: str, context: str, response_quality: float, feedback: Dict) -> float:
        """Evaluate whether context contains all necessary information"""
        
        # Simple heuristic: longer contexts are generally more complete
        # But also consider user feedback about missing information
        
        context_length_score = min(1.0, len(context) / 2000)  # Normalize to reasonable length
        
        # Check feedback for missing information indicators
        missing_info_penalty = 0.0
        if feedback.get('missing_information', False):
            missing_info_penalty = 0.3
        
        completeness_score = max(0.0, context_length_score - missing_info_penalty)
        
        return completeness_score
    
    def _calculate_overall_effectiveness(self, metric_scores: Dict) -> float:
        """Calculate weighted overall effectiveness score"""
        
        weights = {
            'relevance': 0.30,
            'completeness': 0.25,
            'clarity': 0.20,
            'efficiency': 0.15,
            'adaptability': 0.10
        }
        
        overall = sum(metric_scores[metric] * weight 
                     for metric, weight in weights.items() 
                     if metric in metric_scores)
        
        return overall
```

**Ground-up Explanation**: This evaluation framework works like having a comprehensive quality control system that looks at context generation from multiple angles - not just whether it worked, but how well it worked and how it could be improved.
**从头解释**：这个评估框架就像一个全面的质量控制系统，从多个角度审视上下文的生成——不仅看它是否有效，还看它效果如何以及如何改进。

---

## Practical Exercises and Next Steps (实践练习和后续步骤)

### Exercise 1: Build Your Own Retrieval System (练习 1：构建您自己的检索系统)
**Goal**: Implement a basic semantic retrieval system
**目标**：实现一个基本的语义检索系统

```python
# Your implementation template
class BasicRetriever:
    def __init__(self):
        # TODO: Initialize your retrieval system
        self.knowledge_base = {}
        self.embedding_cache = {}
    
    def add_document(self, doc_id: str, content: str):
        # TODO: Add document to knowledge base
        pass
    
    def retrieve(self, query: str, max_results: int = 5) -> List[str]:
        # TODO: Implement retrieval logic
        pass

# Test your retriever
retriever = BasicRetriever()
# Add some test documents
# Test retrieval with different queries
```

### Exercise 2: Context Assembly Optimization (练习 2：上下文组合优化)
**Goal**: Create a context assembler that optimizes information organization
**目标**：创建一个优化信息组织的上下文组合器

```python
class ContextOptimizer:
    def __init__(self, max_length: int = 2000):
        # TODO: Initialize context optimizer
        self.max_length = max_length
    
    def optimize_context(self, information_pieces: List[str], query: str) -> str:
        # TODO: Implement optimal context assembly
        pass
```

---

## Summary and Next Steps (总结和后续步骤)

**Core Concepts Mastered**:
- Evolution from static prompts to dynamic context orchestration
- Information-theoretic optimization of knowledge retrieval
- Multi-source retrieval strategies and result fusion
- Adaptive context assembly with learning integration
- Comprehensive evaluation of context generation effectiveness

**掌握的核心概念**：
- 从静态提示到动态上下文编排的演变
- 知识检索的信息论优化
- 多源检索策略和结果融合
- 具有学习集成的自适应上下文组合
- 上下文生成有效性的综合评估

**Software 3.0 Integration**:
- **Prompts**: Strategic templates for reasoning and knowledge integration
- **Programming**: Sophisticated retrieval and assembly algorithms
- **Protocols**: Self-improving context generation systems

**软件 3.0 集成**：
- **提示**：用于推理和知识集成的战略模板
- **编程**：复杂的检索和组合算法
- **协议**：自我完善的上下文生成系统

**Implementation Skills**:
- Semantic retrieval using embeddings and vector databases
- Dynamic context assembly with cognitive load optimization
- Multi-source information fusion and deduplication
- Effectiveness evaluation and continuous improvement systems

**实施技能**：
- 使用嵌入和向量数据库进行语义检索
- 具有认知负荷优化的动态上下文组合
- 多源信息融合和去重
- 有效性评估和持续改进系统

**Research Grounding**: Direct implementation of context generation research (§4.1) with novel extensions into adaptive assembly, multi-source fusion, and self-improving context orchestration.
**研究基础**：直接实现上下文生成研究（§4.1），并将其新颖地扩展到自适应组合、多源融合和自我完善的上下文编排。

**Next Module**: [01_prompt_engineering.md](01_prompt_engineering.md) - Deep dive into advanced prompting techniques, building on context generation foundations to master the art and science of LLM communication.
**下一个模块**：[01_prompt_engineering.md](01_prompt_engineering.md) - 深入探讨高级提示技术，在上下文生成的基础上掌握大型语言模型沟通的艺术和科学。

---

*This module establishes the foundation for intelligent context engineering, transforming the simple concept of "prompt" into a sophisticated system for dynamic knowledge orchestration and optimal information assembly.*
*本模块为智能上下文工程奠定了基础，将简单的“提示”概念转变为用于动态知识编排和优化信息组合的复杂系统。*