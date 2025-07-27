# Cognitive Tools: Extending the Context Engineering Framework （认知工具：扩展上下文工程框架）

> "The mind is not a vessel to be filled, but a fire to be kindled." — Plutarch

> “思想不是一个需要被填满的容器，而是一团需要被点燃的火焰。”——普鲁塔克

## From Biology to Cognition （从生物学到认知）

Our journey through context engineering has followed a biological metaphor:

我们对上下文工程的探索遵循了生物学隐喻：

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Atoms   │────►│ Molecules│────►│  Cells   │────►│  Organs  │
│  （原子）  │     │ （分子）   │     │ （细胞）   │     │ （器官）   │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
    │                │                │                │
    ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Prompts │     │ Few-shot │     │  Memory  │     │Multi-agent│
│  （提示）  │     │ （少样本） │     │  （记忆）  │     │（多智能体）│
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```

Now, we'll extend this framework by drawing parallels to human cognition. Just as human minds use cognitive tools to process information efficiently, we can create similar structures for LLMs:

现在，我们将通过与人类认知的类比来扩展这个框架。正如人类大脑使用认知工具高效处理信息一样，我们也可以为大型语言模型（LLM）创建类似的结构：

```
┌──────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE TOOLS EXTENSION                       │
│                      （认知工具扩展）                                  │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Heuristics        │ Mental shortcuts that simplify       │
│ COGNITION│ （启发式）          │ complex problems                     │
│ （人类认知）│                   │ （简化复杂问题的思维捷径）             │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Prompt Programs   │ Structured prompt patterns that      │
│ PARALLEL │ （提示程序）        │ guide model reasoning                │
│ （大型语言模型并行）│                   │ （引导模型推理的结构化提示模式） │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Schemas           │ Organized knowledge structures       │
│ COGNITION│ （图式）            │ that help categorize information     │
│ （人类认知）│                   │ （帮助分类信息的有组织知识结构）       │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Context Schemas   │ Standardized formats that            │
│ PARALLEL │ （上下文图式）      │ structure information for models     │
│ （大型语言模型并行）│                   │ （为模型结构化信息的标准化格式） │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Priming           │ Activation of certain associations   │
│ COGNITION│ （启动）            │ that influence subsequent thinking   │
│ （人类认知）│                   │ （影响后续思维的某些联想的激活）       │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Recursive         │ Self-referential prompting that      │
│ PARALLEL │ Prompting         │ shapes model behavior patterns       │
│ （大型语言模型并行）│ （递归提示）        │ （塑造模型行为模式的自指提示）   │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘
```


## Cognitive Tools? （认知工具？）

### **[Eliciting Reasoning in Language Models with Cognitive Tools - IBM Zurich June 2025](https://www.arxiv.org/pdf/2506.12115)**

### Prompts and Prompt Programs as Reasoning Tool Calls （提示和提示程序作为推理工具调用）
> “Cognitive tools” encapsulate reasoning operations within the LLM itself — [IBM Zurich](https://www.arxiv.org/pdf/2506.12115)

> “认知工具”将推理操作封装在大型语言模型（LLM）本身中——[IBM 苏黎世](https://www.arxiv.org/pdf/2506.12115)

![image](https://github.com/user-attachments/assets/cd06c3f5-5a0b-4ee7-bbba-2f9f243f70ae)

> **These cognitive tools (structured prompt templates as tool calls) break down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that
might be helpful in solving the problem.**

> **这些认知工具（作为工具调用的结构化提示模板）通过识别手头的主要概念、提取问题中的相关信息以及突出可能有助于解决问题的有意义的属性、定理和技术来分解问题。**

![image](https://github.com/user-attachments/assets/f7ce8605-6fa3-494f-94cd-94e6b23032b6)


> **These templates scaffold reasoning layers similar to cognitive mental shortcuts, commonly studied as "heuristics".**

> **这些模板构建的推理层类似于认知思维捷径，通常被研究为“启发式”。**

## Prompt Programs: Algorithmic Thinking for LLMs (Reasoning Tool Calls) （提示程序：大型语言模型的算法思维（推理工具调用））

A prompt program is a structured, reusable prompt pattern designed to guide an LLM's reasoning process—similar to how heuristics guide human thinking.

提示程序是一种结构化、可重用的提示模式，旨在引导大型语言模型（LLM）的推理过程——类似于启发式引导人类思维的方式。

### From Ad-hoc Prompts to Programmatic Patterns （从临时提示到程序化模式）

Let's compare an ad-hoc prompt with a simple prompt program (reasoning tool calls):

让我们将临时提示与简单的提示程序（推理工具调用）进行比较：

```
┌───────────────────────────────────────────────────────────────┐
│ AD-HOC PROMPT                                                 │
│ （临时提示）                                                    │
├───────────────────────────────────────────────────────────────┤
│ "Summarize this article about climate change in 3 paragraphs. │
│  Make it easy to understand."                                 │
│ （“用 3 段话总结这篇关于气候变化的文章。使其易于理解。”）         │
└───────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│ PROMPT PROGRAM                                                │
│ （提示程序）                                                    │
├───────────────────────────────────────────────────────────────┤
│ program Summarize(text, paragraphs=3, complexity="simple") {  │
│   // Define the task                                          │
│   // 定义任务                                                   │
│   task = `Summarize the following text in ${paragraphs}       │
│           paragraphs. Use ${complexity} language.`;           │
│                                                               │
│   // Define the process                                       │
│   // 定义过程                                                   │
│   process = ```                                               │
│     1. Identify the main topic and key points                 │
│     2. Organize points by importance                          │
│     3. Create a coherent summary with:                        │
│        - First paragraph: Main topic and context              │
│        - Middle paragraph(s): Key supporting details          │
│        - Final paragraph: Conclusions or implications         │
│   ```;                                                        │
│                                                               │
│   // Define the output format                                 │
│   // 定义输出格式                                               │
│   format = "A ${paragraphs}-paragraph summary using           │
│             ${complexity} language.";                         │
│                                                               │
│   // Construct the complete prompt                            │
│   // 构建完整提示                                               │
│   return `${task}\n\nProcess:\n${process}\n\n                │
│           Format:\n${format}\n\nText to summarize:\n${text}`; │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```

The prompt program approach offers several advantages:
1. **Reusability**: The same pattern can be applied to different texts
2. **Parameterization**: Easily customize length, complexity, etc.
3. **Transparency**: Clear structure makes the prompt's intent explicit
4. **Consistency**: Produces more predictable results across runs

提示程序方法具有以下几个优点：
1. **可重用性**：相同的模式可以应用于不同的文本
2. **参数化**：轻松自定义长度、复杂性等
3. **透明性**：清晰的结构使提示的意图明确
4. **一致性**：在多次运行中产生更可预测的结果

### Simple Prompt Program Template （简单提示程序模板）

Here's a basic template for creating your own prompt programs:

这是一个创建自己的提示程序的基本模板：

```
program [Name]([parameters]) {
  // Define the task （定义任务）
  task = `[Clear instruction using parameters]`; // （使用参数的清晰指令）
  
  // Define the process （定义过程）
  process = ```
    1. [First step] （第一步）
    2. [Second step] （第二步）
    3. [Additional steps as needed] （根据需要添加额外步骤）
  ```;
  
  // Define the output format （定义输出格式）
  format = "[Expected response structure]"; // （预期响应结构）
  
  // Construct the complete prompt （构建完整提示）
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\n[Input]`;
}
```

In practice, this template can be implemented in various ways:
- As pseudocode or protocol shells in your documentation
- As actual JavaScript/Python functions that generate prompts
- As YAML templates with variable substitution
- As JSON schemas for standardized prompt construction

在实践中，这个模板可以通过多种方式实现：
- 作为文档中的伪代码或协议外壳
- 作为生成提示的实际 JavaScript/Python 函数
- 作为带有变量替换的 YAML 模板
- 作为标准化提示构建的 JSON 模式

## Reasoning Prompt Template (Tool Call) （推理提示模板（工具调用））

### 1. Step-by-Step Reasoning （1. 逐步推理）

The fundamental template for breaking down complex reasoning into manageable steps.

将复杂推理分解为可管理步骤的基本模板。

```markdown
# Step-by-Step Reasoning Template （逐步推理模板）

Task: Solve the following problem by breaking it down into clear, logical steps.

任务：通过将其分解为清晰、逻辑的步骤来解决以下问题。

Problem: {{problem}} （问题：{{问题}}）

Please follow this process: （请遵循以下过程：）
1. **Understand**: Restate the problem and identify what you need to find.
   **理解**：重新陈述问题并确定你需要找到什么。
2. **Plan**: Outline your approach to solving the problem.
   **计划**：概述你解决问题的方法。
3. **Execute**: Work through each step of your plan in detail.
   **执行**：详细完成计划的每个步骤。
   - Step 1: [Description of the first step] （步骤 1：[第一步的描述]）
   - Step 2: [Description of the second step] （步骤 2：[第二步的描述]）
   - Step 3: [Continue with additional steps as needed] （步骤 3：[根据需要继续添加步骤]）
4. **Verify**: Check your solution against the original problem.
   **验证**：根据原始问题检查你的解决方案。
5. **Conclude**: State your final answer or conclusion clearly.
   **结论**：清晰地陈述你的最终答案或结论。

Show all your work and explain your reasoning at each step.

展示你的所有工作并在每个步骤中解释你的推理。
```

**Token Count**: ~130 tokens (template only)

**令牌计数**：约 130 个令牌（仅模板）

## What Are Protocol Shells? (Reasoning Tool Calls) （什么是协议外壳？（推理工具调用））

Protocol shells are structured no code templates that organize communication with AI systems into clear, consistent patterns. Think of them as conversational blueprints that establish:

协议外壳是结构化的无代码模板，它将与人工智能系统的通信组织成清晰、一致的模式。将它们视为对话蓝图，用于建立：

1. **Intent**: What you're trying to accomplish
2. **Input**: What information you're providing
3. **Process**: How the information should be processed
4. **Output**: What results you expect

1. **意图**：你想要完成什么
2. **输入**：你提供什么信息
3. **过程**：信息应该如何处理
4. **输出**：你期望得到什么结果

### Basic Protocol Shell Structure （基本协议外壳结构）

```
/protocol.name{
    intent="Clear statement of purpose", // （明确的意图声明）
    input={
        param1="value1",
        param2="value2"
    },
    process=[
        /step1{action="do something"}, // （执行某事）
        /step2{action="do something else"} // （执行其他事）
    ],
    output={
        result1="expected output 1", // （预期输出 1）
        result2="expected output 2" // （预期输出 2）
    }
}
```

This structure creates a clear, token-efficient framework that both you and the AI can follow.

这种结构创建了一个清晰、令牌高效的框架，你和人工智能都可以遵循。

**Reflective Exercise**: Look at your recent AI conversations. Can you identify implicit structures you've been using (ie. emotional context, underlying intent, long horizon goals, contradictory inputs, etc)? How might formalizing these into protocol shells and making data more explicit improve your interactions?

**反思练习**：回顾你最近的人工智能对话。你能识别出你一直在使用的隐式结构吗（例如，情感上下文、潜在意图、长期目标、矛盾输入等）？将这些形式化为协议外壳并使数据更明确，如何能改善你的交互？

## Anatomy of a Protocol Shell （协议外壳的剖析）

Let's dissect each component of a protocol shell to understand its purpose and power:

让我们剖析协议外壳的每个组成部分，以了解其目的和力量：

```
┌─────────────────────────────────────────────────────────┐
│                    PROTOCOL ANATOMY                     │
│                    （协议剖析）                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  /protocol.name{                                        │
│    │       │                                            │
│    │       └── Subtype or specific variant              │
│    │           （子类型或特定变体）                       │
│    │                                                    │
│    └── Core protocol type                               │
│        （核心协议类型）                                   │
│                                                         │
│    intent="Clear statement of purpose",                 │
│    │       │                                            │
│    │       └── Guides AI understanding of goals         │
│    │           （引导人工智能理解目标）                   │
│    │                                                    │
│    └── Declares objective                               │
│        （声明目标）                                       │
│                                                         │
│    input={                                              │
│        param1="value1",   ◄── Structured input data     │
│        param2="value2"        （结构化输入数据）          │
│    },
│                                                         │
│    process=[
│        /step1{action="do something"},     ◄── Ordered   │
│        /step2{action="do something else"} ◄── steps     │
│        （执行某事）                           （有序步骤）  │
│    ],
│                                                         │
│    output={
│        result1="expected output 1",   ◄── Output        │
│        result2="expected output 2"    ◄── specification │
│        （预期输出 1）                     （输出规范）      │
│    }
│  }
│                                                         │
└─────────────────────────────────────────────────────────┘
```


## Context Schemas: Structured Information Patterns （上下文图式：结构化信息模式）


Just as human minds use schemas to organize knowledge, we can create context schemas for LLMs—standardized ways of structuring information to improve model understanding.

正如人类大脑使用图式来组织知识一样，我们可以为大型语言模型（LLM）创建上下文图式——一种标准化信息结构的方式，以提高模型理解能力。

### Basic Schema Structure （基本图式结构）

```
┌───────────────────────────────────────────────────────────────┐
│ CONTEXT SCHEMA                                                │
│ （上下文图式）                                                  │
├───────────────────────────────────────────────────────────────┤
│ {
│   "$schema": "context-engineering/schemas/v1.json",           │
│   "title": "Analysis Request Schema",                         │
│   "description": "Standard format for requesting analysis",   │
│   "type": "object",                                           │
│   "properties": {
│     "task": {
│       "type": "string",                                       │
│       "description": "The analysis task to perform"           │
│     },
│     "context": {
│       "type": "object",                                       │
│       "properties": {
│         "background": { "type": "string" },                   │
│         "constraints": { "type": "array" },                   │
│         "examples": { "type": "array" }                       │
│       }
│     },
│     "data": {
│       "type": "string",                                       │
│       "description": "The information to analyze"             │
│     },
│     "output_format": {
│       "type": "string",                                       │
│       "enum": ["bullet_points", "paragraphs", "table"]        │
│     }
│   },
│   "required": ["task", "data"]
│ }
└───────────────────────────────────────────────────────────────┘
```


### **[MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents - Singapore-MIT June 2025](https://www.arxiv.org/pdf/2506.12115)**

> “Our results demonstrate the promise of reasoning-driven memory consolidation as a scalable alternative to existing solutions for training long-horizon interactive agents, where both efficiency and performance are optimized." — [Singapore-MIT](https://arxiv.org/pdf/2506.15841)

> “我们的结果表明，推理驱动的记忆整合作为训练长周期交互式代理的现有解决方案的可扩展替代方案，具有广阔前景，其中效率和性能都得到了优化。”——[新加坡-麻省理工学院](https://arxiv.org/pdf/2506.15841)

![image](https://github.com/user-attachments/assets/16e3f241-5f44-4ed5-9622-f0b4acbb67b0)


### From Schema to Prompt （从图式到提示）

Schemas can be translated into actual prompts by filling in the structured template:

通过填充结构化模板，图式可以转换为实际的提示：

```
# Analysis Request （分析请求）

## Task （任务）
Identify the main themes and supporting evidence in the provided text.

识别所提供文本中的主要主题和支持证据。

## Context （上下文）
### Background （背景）
This is a speech given at a climate conference in 2023.

这是 2023 年气候大会上发表的演讲。

### Constraints （约束）
- Focus on scientific claims （关注科学主张）
- Ignore political statements （忽略政治言论）
- Maintain neutrality （保持中立）

### Examples （示例）
- Theme: Rising Sea Levels （主题：海平面上升）
  Evidence: "Measurements show a 3.4mm annual rise since 2010" （证据：“测量显示自 2010 年以来每年上升 3.4 毫米”）

## Data （数据）
[The full text of the speech would go here] （[演讲的全文将在此处]）

## Output Format （输出格式）
bullet_points （要点）
```

This structured approach helps the model understand exactly what information is being provided and what is expected in return.

这种结构化方法有助于模型准确理解所提供的信息以及预期返回的内容。

## Recursive Prompting: Self-Referential Improvement （递归提示：自指改进）

Recursive prompting is similar to cognitive priming—it establishes patterns that influence subsequent model behavior. The key insight is having the model reflect on and improve its own outputs.

递归提示类似于认知启动——它建立影响后续模型行为的模式。关键的见解是让模型反思并改进自己的输出。

### Basic Recursive Pattern （基本递归模式）

```
┌───────────────────────────────────────────────────────────────┐
│ RECURSIVE PROMPTING FLOW                                      │
│ （递归提示流程）                                                │
│                                                               │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐    │
│  │             │      │             │      │             │    │
│  │  Initial    │─────►│  Self-      │─────►│  Improved   │    │
│  │  Response   │      │  Reflection │      │  Response   │    │
│  │  （初始响应）  │      │  （自我反思） │      │  （改进响应） │    │
│  └─────────────┘      └─────────────┘      └─────────────┘    │
│        ▲                                          │           │
│        └──────────────────────────────────────────┘           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Simple Implementation （简单实现）

```python
def recursive_prompt(question, model, iterations=2):
    """Apply recursive prompting to improve responses."""
    
    # Initial response （初始响应）
    response = model.generate(f"Question: {question}\nAnswer:")
    
    for i in range(iterations):
        # Self-reflection prompt （自我反思提示）
        reflection_prompt = f"""
        Question: {question}
        
        Your previous answer: 
        {response}
        
        Please reflect on your answer:
        1. What information might be missing?
        2. Are there any assumptions that should be questioned?
        3. How could the explanation be clearer or more accurate?
        
        Now, provide an improved answer:
        """
        
        # Generate improved response （生成改进响应）
        response = model.generate(reflection_prompt)
    
    return response
```

This simple recursive pattern can dramatically improve response quality by encouraging the model to critique and refine its own thinking.

这种简单的递归模式可以通过鼓励模型批判和完善自己的思维来显著提高响应质量。

## Putting It All Together: Cognitive Architecture （整合：认知架构）

These cognitive tools can be combined into a complete architecture that mirrors human thinking processes:

这些认知工具可以组合成一个完整的架构，模仿人类的思维过程：

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE ARCHITECTURE                               │
│                      （认知架构）                                           │
│                                                                           │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Input Parser   │  Understands user intent using schema recognition    │
│  │  （输入解析器）   │  （使用图式识别理解用户意图）                        │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Prompt Program │  Selects and applies appropriate reasoning pattern   │
│  │  Selector       │  （选择并应用适当的推理模式）                        │
│  │  （提示程序选择器）│                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Working Memory │  Maintains state and context across steps            │
│  │  （工作记忆）     │  （在步骤之间维护状态和上下文）                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Recursive      │  Applies self-improvement through reflection         │
│  │  Processor      │  （通过反思实现自我改进）                            │
│  │  （递归处理器）   │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Output         │  Formats final response according to schema          │
│  │  Formatter      │  （根据图式格式化最终响应）                          │
│  │  （输出格式化器） │                                                      │
│  └─────────────────┘                                                      │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

This architecture can be implemented as a complete system using the tools and patterns we've discussed.

这个架构可以使用我们讨论过的工具和模式实现为一个完整的系统。

## Key Takeaways （主要收获）

1. **Prompt Programs/Protocols** structure reasoning like human heuristics
2. **Context Schemas** organize information like mental knowledge structures
3. **Recursive Prompting** creates self-improvement loops similar to cognitive reflection
4. **Cognitive Architecture** combines these tools into complete systems

1. **提示程序/协议**像人类启发式一样构建推理
2. **上下文图式**像心理知识结构一样组织信息
3. **递归提示**创建类似于认知反思的自我改进循环
4. **认知架构**将这些工具组合成完整的系统

These cognitive extensions to our context engineering framework allow us to create more sophisticated, yet understandable, approaches to working with LLMs.

这些对我们上下文工程框架的认知扩展使我们能够创建更复杂但易于理解的与大型语言模型（LLM）协作的方法。

## Exercises for Practice （练习）

1. Convert one of your frequently used prompts into a prompt program
2. Create a simple schema for a common task you perform with LLMs
3. Implement basic recursive prompting to improve response quality
4. Combine these approaches into a mini cognitive architecture

1. 将你常用的一个提示转换为提示程序
2. 为你使用大型语言模型（LLM）执行的常见任务创建一个简单的图式
3. 实现基本的递归提示以提高响应质量
4. 将这些方法组合成一个迷你认知架构

## Next Steps （下一步）

In the next sections, we'll explore practical implementations of these cognitive tools:
- Jupyter notebooks demonstrating prompt programs in action
- Templates for creating your own schemas
- Examples of complete cognitive architectures

在接下来的章节中，我们将探讨这些认知工具的实际实现：
- 演示提示程序实际应用的 Jupyter Notebook
- 创建自己的图式的模板
- 完整认知架构的示例

[Continue to Next Section →](06_advanced_applications.md)

---

## Deeper Dive: From Our Research to Your Applications （深入探讨：从我们的研究到你的应用）

The cognitive tools described above are simplified representations of more advanced research concepts. For those interested in exploring further:

上面描述的认知工具是更高级研究概念的简化表示。对于那些有兴趣进一步探索的人：

- **Prompt Programs** are practical implementations of what researchers call "programmatic prompting" or "structured prompting frameworks"
- **Context Schemas** represent a simplified version of knowledge representation systems and ontological frameworks
- **Recursive Prompting** is related to self-reflection, metacognition, and recursive self-improvement in AI systems

- **提示程序**是研究人员所称的“程序化提示”或“结构化提示框架”的实际实现
- **上下文图式**代表了知识表示系统和本体论框架的简化版本
- **递归提示**与人工智能系统中的自我反思、元认知和递归自我改进有关

These simplified frameworks make advanced concepts accessible while preserving their practical utility.

这些简化的框架使高级概念易于理解，同时保留了其实用性。