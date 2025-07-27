# Understanding Templates （理解模板）

> "The beginning of wisdom is the definition of terms." — Socrates
> “智慧的开端是给事物下定义。” — 苏格拉底

## Overview （概述）

Understanding templates help language models comprehend and analyze information before attempting to solve a problem or generate content. These templates serve as the foundation for effective reasoning by ensuring the model has properly interpreted the task, context, and requirements.
理解模板可帮助语言模型在尝试解决问题或生成内容之前，理解和分析信息。这些模板通过确保模型正确解读任务、背景和要求，为有效推理奠定基础。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  UNDERSTANDING PROCESS                                       │
│  （理解流程）                                                │
│                                                              │
│  Input → Analyze → Structure → Clarify → Ready for Reasoning │
│  （输入 → 分析 → 结构化 → 澄清 → 准备推理）                  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Basic Templates （基础模板）

### 1. Question Analysis （问题分析）

The most fundamental understanding template helps break down a question or problem into its core components.
最基本的理解模板有助于将问题或难题分解为其核心组成部分。

```markdown
# Question Analysis Template （问题分析模板）

Task: Analyze and break down the following question before attempting to answer it.
任务：在尝试回答以下问题之前，对其进行分析和分解。

Question: {{question}}
问题：{{question}}

Please provide:
请提供：
1. **Question Type**: What kind of question is this? (e.g., factual, conceptual, analytical)
   **问题类型**：这是什么类型的问题？（例如，事实型、概念型、分析型）
2. **Core Task**: What specific action or thinking is required?
   **核心任务**：需要采取什么具体行动或进行何种思考？
3. **Key Components**: What are the main elements that need to be addressed?
   **关键组成部分**：需要解决的主要元素是什么？
4. **Implicit Assumptions**: What unstated assumptions might be relevant?
   **隐含假设**：哪些未言明的假设可能相关？
5. **Knowledge Domains**: What fields of knowledge are relevant?
   **知识领域**：哪些知识领域是相关的？
6. **Constraints**: Are there any explicit or implicit constraints?
   **约束条件**：是否存在任何明确或隐含的约束？
7. **Restatement**: Restate the question in your own words for clarity.
   **重述**：为了清晰起见，用你自己的话重述问题。

Once you've completed this analysis, you'll be better prepared to address the question effectively.
完成此分析后，你将能更有效地解决问题。
```

**Token Count**: ~120 tokens (template only)
**令牌数**：约 120 个令牌（仅模板）

**Usage Example**:
- For complex questions where understanding the requirements is crucial
- When precision in interpretation matters
- Before tackling multi-step problems

**使用示例**：
- 用于理解要求至关重要的复杂问题
- 当解释的精确性很重要时
- 在处理多步骤问题之前

### 2. Information Extraction （信息提取）

For extracting structured information from text.
用于从文本中提取结构化信息。

```markdown
# Information Extraction Template （信息提取模板）

Task: Extract and organize the key information from the following text.
任务：从以下文本中提取并组织关键信息。

Text: {{text}}
文本：{{text}}

Please extract:
请提取：
1. **Main Topic**: What is the central subject?
   **主要主题**：中心主题是什么？
2. **Key Facts**: List the most important factual statements.
   **关键事实**：列出最重要的事实陈述。
3. **Entities**: Identify people, organizations, locations, dates, etc.
   **实体**：识别人、组织、地点、日期等。
4. **Relationships**: How are these entities related to each other?
   **关系**：这些实体之间有何关联？
5. **Numerical Data**: Extract any numbers, statistics, or measurements.
   **数值数据**：提取任何数字、统计数据或测量值。
6. **Claims**: What assertions or arguments are made?
   **主张**：提出了哪些断言或论点？
7. **Evidence**: What support is provided for these claims?
   **证据**：为这些主张提供了哪些支持？

Organize this information in a clear, structured format.
以清晰、结构化的格式组织这些信息。
```

**Token Count**: ~110 tokens (template only)
**令牌数**：约 110 个令牌（仅模板）

**Usage Example**:
- For processing research papers or articles
- When summarizing complex documents
- Before synthesizing information from multiple sources

**使用示例**：
- 用于处理研究论文或文章
- 在总结复杂文档时
- 在综合来自多个来源的信息之前

### 3. Problem Decomposition （问题分解）

For breaking down complex problems into solvable parts.
用于将复杂问题分解为可解决的部分。

```markdown
# Problem Decomposition Template （问题分解模板）

Task: Decompose the following problem into smaller, manageable components.
任务：将以下问题分解为更小、可管理的部分。

Problem: {{problem}}
问题：{{problem}}

Please provide:
请提供：
1. **Problem Type**: What category of problem is this?
   **问题类型**：这是哪一类问题？
2. **Goal State**: What does a successful solution look like?
   **目标状态**：一个成功的解决方案是什么样的？
3. **Given Information**: What information is explicitly provided?
   **给定信息**：明确提供了哪些信息？
4. **Unknown Variables**: What needs to be determined?
   **未知变量**：需要确定什么？
5. **Constraints**: What limitations or conditions must be satisfied?
   **约束条件**：必须满足哪些限制或条件？
6. **Sub-Problems**: Break down the main problem into smaller parts.
   **子问题**：将主问题分解为更小的部分。
7. **Dependencies**: How do these sub-problems relate to each other?
   **依赖关系**：这些子问题之间有何关联？
8. **Solution Approach**: Suggest a high-level strategy for solving the problem.
   **解决方法**：提出一个解决问题的高层次策略。

This decomposition will provide a structured approach to solving the problem.
这种分解将为解决问题提供一个结构化的方法。
```

**Token Count**: ~120 tokens (template only)
**令牌数**：约 120 个令牌（仅模板）

**Usage Example**:
- For mathematical or logical problems
- When faced with multi-step reasoning tasks
- Before attempting complex analyses

**使用示例**：
- 用于数学或逻辑问题
- 面对多步推理任务时
- 在尝试复杂分析之前

## Advanced Templates （高级模板）

### 4. Conceptual Mapping （概念映射）

For understanding relationships between concepts within a domain.
用于理解一个领域内概念之间的关系。

```markdown
# Conceptual Mapping Template （概念映射模板）

Task: Create a conceptual map of the ideas and relationships in the following text.
任务：为以下文本中的思想和关系创建一个概念图。

Text: {{text}}
文本：{{text}}

Please provide:
请提供：
1. **Core Concepts**: Identify the central ideas or concepts.
   **核心概念**：识别中心思想或概念。
2. **Concept Definitions**: Briefly define each concept.
   **概念定义**：简要定义每个概念。
3. **Hierarchical Relationships**: Which concepts are subcategories of others?
   **层级关系**：哪些概念是其他概念的子类别？
4. **Causal Relationships**: Which concepts influence or cause others?
   **因果关系**：哪些概念影响或导致其他概念？
5. **Contrasting Concepts**: Which concepts stand in opposition to each other?
   **对比概念**：哪些概念相互对立？
6. **Complementary Concepts**: Which concepts support or enhance each other?
   **互补概念**：哪些概念相互支持或增强？
7. **Missing Concepts**: Are there any implied but unstated concepts?
   **缺失概念**：是否存在任何隐含但未言明的概念？

Represent these relationships in a structured format that shows how the concepts interconnect.
以结构化的格式表示这些关系，展示概念之间如何相互关联。
```

**Token Count**: ~120 tokens (template only)
**令牌数**：约 120 个令牌（仅模板）

**Usage Example**:
- For theoretical or abstract content
- When analyzing complex systems
- Before synthesizing disparate information

**使用示例**：
- 用于理论或抽象内容
- 在分析复杂系统时
- 在综合不同信息之前

### 5. Multi-Perspective Analysis （多视角分析）

For understanding different viewpoints on a topic.
用于理解一个主题的不同观点。

```markdown
# Multi-Perspective Analysis Template （多视角分析模板）

Task: Analyze the following topic from multiple perspectives.
任务：从多个视角分析以下主题。

Topic: {{topic}}
主题：{{topic}}

Please provide:
请提供：
1. **Perspective Identification**: What major viewpoints exist on this topic?
   **视角识别**：关于这个主题存在哪些主要观点？
2. **Core Arguments**: What are the main arguments from each perspective?
   **核心论点**：每个视角的主要论点是什么？
3. **Evidence Base**: What evidence supports each perspective?
   **证据基础**：哪些证据支持每个视角？
4. **Underlying Values**: What values or assumptions underlie each perspective?
   **潜在价值观**：每个视角背后是何种价值观或假设？
5. **Areas of Agreement**: Where do the perspectives converge?
   **共识领域**：这些视角在哪些方面达成一致？
6. **Key Disagreements**: What are the fundamental points of contention?
   **主要分歧**：根本的争议点是什么？
7. **Synthesis Possibilities**: How might these perspectives be integrated?
   **综合可能性**：如何整合这些视角？

This analysis will provide a balanced understanding of the different ways to view this topic.
此分析将提供对看待此主题的不同方式的平衡理解。
```

**Token Count**: ~120 tokens (template only)
**令牌数**：约 120 个令牌（仅模板）

**Usage Example**:
- For controversial or complex topics
- When balanced understanding is crucial
- Before forming a nuanced position

**使用示例**：
- 用于有争议或复杂的主题
- 当平衡的理解至关重要时
- 在形成一个细致入微的立场之前

### 6. Requirement Analysis （需求分析）

For clearly understanding task requirements.
用于清晰地理解任务要求。

```markdown
# Requirement Analysis Template （需求分析模板）

Task: Analyze the requirements for the following task or project.
任务：分析以下任务或项目的要求。

Task Description: {{task_description}}
任务描述：{{task_description}}

Please provide:
请提供：
1. **Primary Objective**: What is the main goal?
   **主要目标**：主要目标是什么？
2. **Deliverables**: What specific outputs are required?
   **可交付成果**：需要哪些具体产出？
3. **Quality Criteria**: How will success be measured?
   **质量标准**：如何衡量成功？
4. **Constraints**: What limitations must be worked within?
   **约束条件**：必须在哪些限制内工作？
5. **Dependencies**: What external factors impact this task?
   **依赖关系**：哪些外部因素影响此任务？
6. **Stakeholders**: Who is involved or affected?
   **利益相关者**：谁参与其中或受其影响？
7. **Priorities**: Which aspects are most important?
   **优先级**：哪些方面最重要？
8. **Ambiguities**: What aspects need clarification?
   **模糊之处**：哪些方面需要澄清？

This analysis will ensure all requirements are properly understood before proceeding.
此分析将确保在继续之前所有要求都得到正确理解。
```

**Token Count**: ~120 tokens (template only)
**令牌数**：约 120 个令牌（仅模板）

**Usage Example**:
- For project planning
- When tasked with creating specific outputs
- Before beginning any complex task

**使用示例**：
- 用于项目规划
- 当被要求创建特定产出时
- 在开始任何复杂任务之前

## Implementation Patterns （实施模式）

Here's a simple Python function to implement the Question Analysis template:
这是一个实现问题分析模板的简单 Python 函数：

```python
def understand_question(question):
    """
    Create a prompt that analyzes and breaks down a question.
    （创建一个分析和分解问题的提示。）
    
    Args:
        question (str): The question to analyze
        （question (str): 待分析的问题）
        
    Returns:
        str: A formatted prompt for question analysis
        （str: 用于问题分析的格式化提示）
    """
    return f"""
Task: Analyze and break down the following question before attempting to answer it.
（任务：在尝试回答以下问题之前，对其进行分析和分解。）

Question: {question}
（问题：{question}）

Please provide:
（请提供：）
1. **Question Type**: What kind of question is this? (e.g., factual, conceptual, analytical)
   （**问题类型**：这是什么类型的问题？（例如，事实型、概念型、分析型））
2. **Core Task**: What specific action or thinking is required?
   （**核心任务**：需要采取什么具体行动或进行何种思考？）
3. **Key Components**: What are the main elements that need to be addressed?
   （**关键组成部分**：需要解决的主要元素是什么？）
4. **Implicit Assumptions**: What unstated assumptions might be relevant?
   （**隐含假设**：哪些未言明的假设可能相关？）
5. **Knowledge Domains**: What fields of knowledge are relevant?
   （**知识领域**：哪些知识领域是相关的？）
6. **Constraints**: Are there any explicit or implicit constraints?
   （**约束条件**：是否存在任何明确或隐含的约束？）
7. **Restatement**: Restate the question in your own words for clarity.
   （**重述**：为了清晰起见，用你自己的话重述问题。）

Once you've completed this analysis, you'll be better prepared to address the question effectively.
（完成此分析后，你将能更有效地解决问题。）
"""
```

## Measurement and Optimization （测量与优化）

When using understanding templates, measure their effectiveness by:
在使用理解模板时，通过以下方式衡量其有效性：

1. **Accuracy**: Does the understanding correctly identify all key elements?
   **准确性**：理解是否正确识别了所有关键元素？
2. **Comprehensiveness**: Are all important aspects of the input covered?
   **全面性**：是否涵盖了输入的所有重要方面？
3. **Clarity**: Is the structured understanding clear and unambiguous?
   **清晰度**：结构化的理解是否清晰明确？
4. **Utility**: Does the understanding improve subsequent reasoning?
   **实用性**：这种理解是否有助于后续的推理？

Optimize your templates by:
通过以下方式优化您的模板：
- Removing unnecessary components that don't improve understanding
  - 移除不能增进理解的不必要组件
- Adding specific components needed for your particular domain
  - 添加您特定领域所需的特定组件
- Adjusting the level of detail based on the complexity of your inputs
  - 根据输入的复杂性调整细节级别

## Combining with Other Tools （与其他工具结合）

Understanding templates work best when combined with other cognitive tools:
理解模板与其他认知工具结合使用时效果最佳：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│ （理解模板）        │     │ （推理模板）      │     │ （验证模板）      │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```

For example, use the Question Analysis template first, then pass the structured understanding to a problem-solving template, and finally verify the solution with a verification template.
例如，首先使用问题分析模板，然后将结构化的理解传递给问题解决模板，最后用验证模板验证解决方案。

## Next Steps （后续步骤）

- Explore [reasoning.md](./reasoning.md) for templates that build on understanding
- See [composition.md](./composition.md) for ways to combine multiple templates
- Check out [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md) for programmatic approaches that use these templates

- 探索 [reasoning.md](./reasoning.md) 以了解基于理解构建的模板
- 查看 [composition.md](./composition.md) 以了解组合多个模板的方法
- 查看 [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md) 以了解使用这些模板的程序化方法