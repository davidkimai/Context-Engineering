# Cognitive Tools: Extending the Context Engineering Framework  
认知工具：扩展上下文工程框架

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#cognitive-tools-extending-the-context-engineering-framework)

> "The mind is not a vessel to be filled, but a fire to be kindled." — Plutarch  
> “心灵不是一个需要填满的容器，而是一团需要点燃的火焰。”——普鲁塔克

## From Biology to Cognition  
从生物学到认知

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#from-biology-to-cognition)

Our journey through context engineering has followed a biological metaphor:  
我们的上下文工程之旅遵循了一个生物学隐喻：

```
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Atoms   │────►│ Molecules│────►│  Cells   │────►│  Organs  │
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
    │                │                │                │
    ▼                ▼                ▼                ▼
┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
│          │     │          │     │          │     │          │
│  Prompts │     │ Few-shot │     │  Memory  │     │Multi-agent│
│          │     │          │     │          │     │          │
└──────────┘     └──────────┘     └──────────┘     └──────────┘
```

Now, we'll extend this framework by drawing parallels to human cognition. Just as human minds use cognitive tools to process information efficiently, we can create similar structures for LLMs:  
现在，我们将通过与人类认知进行类比来扩展此框架。正如人类思维使用认知工具来有效地处理信息一样，我们可以为法学硕士 (LLM) 创建类似的结构：

```
┌──────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE TOOLS EXTENSION                       │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Heuristics        │ Mental shortcuts that simplify       │
│ COGNITION│                   │ complex problems                     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Prompt Programs   │ Structured prompt patterns that      │
│ PARALLEL │                   │ guide model reasoning                │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Schemas           │ Organized knowledge structures       │
│ COGNITION│                   │ that help categorize information     │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Context Schemas   │ Standardized formats that            │
│ PARALLEL │                   │ structure information for models     │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
├──────────┬───────────────────┬──────────────────────────────────────┤
│          │                   │                                      │
│ HUMAN    │ Priming           │ Activation of certain associations   │
│ COGNITION│                   │ that influence subsequent thinking   │
│          │                   │                                      │
├──────────┼───────────────────┼──────────────────────────────────────┤
│          │                   │                                      │
│ LLM      │ Recursive         │ Self-referential prompting that      │
│ PARALLEL │ Prompting         │ shapes model behavior patterns       │
│          │                   │                                      │
└──────────┴───────────────────┴──────────────────────────────────────┘
```

## Cognitive Tools?  认知工具？

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#cognitive-tools)

### **[Eliciting Reasoning in Language Models with Cognitive Tools - IBM Zurich June 2025  
利用认知工具在语言模型中引发推理 - IBM 苏黎世 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)**

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#eliciting-reasoning-in-language-models-with-cognitive-tools---ibm-zurich-june-2025)

### Prompts and Prompt Programs as Reasoning Tool Calls  
提示和提示程序作为推理工具调用

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#prompts-and-prompt-programs-as-reasoning-tool-calls)

> “Cognitive tools” encapsulate reasoning operations within the LLM itself — [IBM Zurich](https://www.arxiv.org/pdf/2506.12115)  
> “认知工具”将推理操作封装在法学硕士课程本身中 [——IBM 苏黎世](https://www.arxiv.org/pdf/2506.12115)

[![image](https://private-user-images.githubusercontent.com/208424706/461724761-cd06c3f5-5a0b-4ee7-bbba-2f9f243f70ae.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MDUzNzIsIm5iZiI6MTc1MTcwNTA3MiwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYxNzI0NzYxLWNkMDZjM2Y1LTVhMGItNGVlNy1iYmJhLTJmOWYyNDNmNzBhZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwODQ0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ZGYyOTI3ZDg1NTExNTRiZDNlMjBlYmI1NDQ2ZDllOTE2OTU4ZWQxNzRmZGUyZGY2YzlkNDZjZDljYWJmNTFiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.MHrTiBV_CSb-H-r9rYjmJtRRegwclEij0nVoJrcby3U)](https://private-user-images.githubusercontent.com/208424706/461724761-cd06c3f5-5a0b-4ee7-bbba-2f9f243f70ae.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MDUzNzIsIm5iZiI6MTc1MTcwNTA3MiwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYxNzI0NzYxLWNkMDZjM2Y1LTVhMGItNGVlNy1iYmJhLTJmOWYyNDNmNzBhZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwODQ0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04ZGYyOTI3ZDg1NTExNTRiZDNlMjBlYmI1NDQ2ZDllOTE2OTU4ZWQxNzRmZGUyZGY2YzlkNDZjZDljYWJmNTFiJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.MHrTiBV_CSb-H-r9rYjmJtRRegwclEij0nVoJrcby3U)

> **These cognitive tools (structured prompt templates as tool calls) break down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that might be helpful in solving the problem.  
> 这些认知工具（结构化提示模板作为工具调用）通过识别手头的主要概念、提取问题中的相关信息以及突出显示可能有助于解决问题的有意义的属性、定理和技术来分解问题。**

[![image](https://private-user-images.githubusercontent.com/208424706/461725384-f7ce8605-6fa3-494f-94cd-94e6b23032b6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MDUzNzIsIm5iZiI6MTc1MTcwNTA3MiwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYxNzI1Mzg0LWY3Y2U4NjA1LTZmYTMtNDk0Zi05NGNkLTk0ZTZiMjMwMzJiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwODQ0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MTYzZTQ3N2I1YjBlMDUxNDI1NThiZmRlMjM3ZTQ0MTcwZWVmZjdkN2Y2OWI3ODMyMDIzNjliNTYxNDM4ZWNkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-P7OpURPNnjnUV1g9uMOqtvqdjGHIJY4N8eJ9dJF6LY)](https://private-user-images.githubusercontent.com/208424706/461725384-f7ce8605-6fa3-494f-94cd-94e6b23032b6.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MDUzNzIsIm5iZiI6MTc1MTcwNTA3MiwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYxNzI1Mzg0LWY3Y2U4NjA1LTZmYTMtNDk0Zi05NGNkLTk0ZTZiMjMwMzJiNi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwODQ0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MTYzZTQ3N2I1YjBlMDUxNDI1NThiZmRlMjM3ZTQ0MTcwZWVmZjdkN2Y2OWI3ODMyMDIzNjliNTYxNDM4ZWNkJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-P7OpURPNnjnUV1g9uMOqtvqdjGHIJY4N8eJ9dJF6LY)

> **These templates scaffold reasoning layers similar to cognitive mental shortcuts, commonly studied as "heuristics".  
> 这些模板支撑类似于认知心理捷径的推理层，通常被称为“启发式”研究。**

## Prompt Programs: Algorithmic Thinking for LLMs (Reasoning Tool Calls)  
提示程序：法学硕士的算法思维（推理工具调用）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#prompt-programs-algorithmic-thinking-for-llms-reasoning-tool-calls)

A prompt program is a structured, reusable prompt pattern designed to guide an LLM's reasoning process—similar to how heuristics guide human thinking.  
提示程序是一种结构化的、可重复使用的提示模式，旨在指导 LLM 的推理过程——类似于启发式方法指导人类思维的方式。

### From Ad-hoc Prompts to Programmatic Patterns  
从临时提示到程序化模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#from-ad-hoc-prompts-to-programmatic-patterns)

Let's compare an ad-hoc prompt with a simple prompt program (reasoning tool calls):  
让我们将临时提示与简单提示程序（推理工具调用）进行比较：

```
┌───────────────────────────────────────────────────────────────┐
│ AD-HOC PROMPT                                                 │
├───────────────────────────────────────────────────────────────┤
│ "Summarize this article about climate change in 3 paragraphs. │
│  Make it easy to understand."                                 │
└───────────────────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────────────────┐
│ PROMPT PROGRAM                                                │
├───────────────────────────────────────────────────────────────┤
│ program Summarize(text, paragraphs=3, complexity="simple") {  │
│   // Define the task                                          │
│   task = `Summarize the following text in ${paragraphs}       │
│           paragraphs. Use ${complexity} language.`;           │
│                                                               │
│   // Define the process                                       │
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
│   format = "A ${paragraphs}-paragraph summary using           │
│             ${complexity} language.";                         │
│                                                               │
│   // Construct the complete prompt                            │
│   return `${task}\n\nProcess:\n${process}\n\n                │
│           Format:\n${format}\n\nText to summarize:\n${text}`; │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```

The prompt program approach offers several advantages:  
快速程序方法具有以下几个优点：

1. **Reusability**: The same pattern can be applied to different texts  
    **可重用性** ：相同的模式可以应用于不同的文本
2. **Parameterization**: Easily customize length, complexity, etc.  
    **参数化** ：轻松定制长度、复杂性等。
3. **Transparency**: Clear structure makes the prompt's intent explicit  
    **透明度** ：清晰的结构使提示的意图明确
4. **Consistency**: Produces more predictable results across runs  
    **一致性** ：在运行过程中产生更可预测的结果

### Simple Prompt Program Template  
简单提示程序模板

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#simple-prompt-program-template)

Here's a basic template for creating your own prompt programs:  
这是创建您自己的提示程序的基本模板：

```
program [Name]([parameters]) {
  // Define the task
  task = `[Clear instruction using parameters]`;
  
  // Define the process
  process = ```
    1. [First step]
    2. [Second step]
    3. [Additional steps as needed]
  ```;
  
  // Define the output format
  format = "[Expected response structure]";
  
  // Construct the complete prompt
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\n[Input]`;
}
```

In practice, this template can be implemented in various ways:  
在实践中，该模板可以通过多种方式实现：

- As pseudocode or protocol shells in your documentation  
    作为文档中的伪代码或协议外壳
- As actual JavaScript/Python functions that generate prompts  
    作为生成提示的实际 JavaScript/Python 函数
- As YAML templates with variable substitution  
    作为具有变量替换的 YAML 模板
- As JSON schemas for standardized prompt construction  
    作为标准化提示构造的 JSON 模式

## Reasoning Prompt Template (Tool Call)  
推理提示模板（工具调用）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#reasoning-prompt-template-tool-call)

### 1. Step-by-Step Reasoning  
1.逐步推理

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#1-step-by-step-reasoning)

The fundamental template for breaking down complex reasoning into manageable steps.  
将复杂推理分解为可管理步骤的基本模板。

```md
# Step-by-Step Reasoning Template

Task: Solve the following problem by breaking it down into clear, logical steps.

Problem: {{problem}}

Please follow this process:
1. **Understand**: Restate the problem and identify what you need to find.
2. **Plan**: Outline your approach to solving the problem.
3. **Execute**: Work through each step of your plan in detail.
   - Step 1: [Description of the first step]
   - Step 2: [Description of the second step]
   - Step 3: [Continue with additional steps as needed]
4. **Verify**: Check your solution against the original problem.
5. **Conclude**: State your final answer or conclusion clearly.

Show all your work and explain your reasoning at each step.
```

**Token Count**: ~130 tokens (template only)  
**令牌数量** ：~130 个令牌（仅模板）

## What Are Protocol Shells? (Reasoning Tool Calls)  
什么是协议外壳？（推理工具调用）

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#what-are-protocol-shells-reasoning-tool-calls)

Protocol shells are structured no code templates that organize communication with AI systems into clear, consistent patterns. Think of them as conversational blueprints that establish:  
协议外壳的结构并非代码模板，而是将与人工智能系统的通信组织成清晰一致的模式。可以将它们视为建立以下机制的对话蓝图：

1. **Intent**: What you're trying to accomplish  
    **意图** ：你想要实现的目标
2. **Input**: What information you're providing  
    **输入** ：您提供的信息
3. **Process**: How the information should be processed  
    **流程** ：如何处理信息
4. **Output**: What results you expect  
    **输出** ：你期望的结果

### Basic Protocol Shell Structure  
基本协议外壳结构

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#basic-protocol-shell-structure)

```
/protocol.name{
    intent="Clear statement of purpose",
    input={
        param1="value1",
        param2="value2"
    },
    process=[
        /step1{action="do something"},
        /step2{action="do something else"}
    ],
    output={
        result1="expected output 1",
        result2="expected output 2"
    }
}
```

This structure creates a clear, token-efficient framework that both you and the AI can follow.  
这种结构创建了一个清晰的、高效的令牌框架，您和 AI 都可以遵循。

**Reflective Exercise**: Look at your recent AI conversations. Can you identify implicit structures you've been using (ie. emotional context, underlying intent, long horizon goals, contradictory inputs, etc)? How might formalizing these into protocol shells and making data more explicit improve your interactions?  
**反思练习** ：回顾你最近的 AI 对话。你能识别出你一直在使用的隐性结构吗（例如情感语境、潜在意图、长远目标、矛盾的输入等等）？将这些内容形式化为协议框架，并使数据更加清晰，如何才能改善你的交互？

## Anatomy of a Protocol Shell  
协议 Shell 的剖析

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#anatomy-of-a-protocol-shell)

Let's dissect each component of a protocol shell to understand its purpose and power:  
让我们剖析协议外壳的每个组件，以了解其目的和功能：

```
┌─────────────────────────────────────────────────────────┐
│                    PROTOCOL ANATOMY                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  /protocol.name{                                        │
│    │       │                                            │
│    │       └── Subtype or specific variant              │
│    │                                                    │
│    └── Core protocol type                               │
│                                                         │
│    intent="Clear statement of purpose",                 │
│    │       │                                            │
│    │       └── Guides AI understanding of goals         │
│    │                                                    │
│    └── Declares objective                               │
│                                                         │
│    input={                                              │
│        param1="value1",   ◄── Structured input data     │
│        param2="value2"                                  │
│    },                                                   │
│                                                         │
│    process=[                                            │
│        /step1{action="do something"},     ◄── Ordered   │
│        /step2{action="do something else"} ◄── steps     │
│    ],                                                   │
│                                                         │
│    output={                                             │
│        result1="expected output 1",   ◄── Output        │
│        result2="expected output 2"    ◄── specification │
│    }                                                    │
│  }                                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Context Schemas: Structured Information Patterns  
上下文模式：结构化信息模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#context-schemas-structured-information-patterns)

Just as human minds use schemas to organize knowledge, we can create context schemas for LLMs—standardized ways of structuring information to improve model understanding.  
正如人类思维使用模式来组织知识一样，我们可以为 LLM 创建上下文模式——标准化的信息结构化方式，以提高模型理解。

### Basic Schema Structure  基本架构结构

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#basic-schema-structure)

```
┌───────────────────────────────────────────────────────────────┐
│ CONTEXT SCHEMA                                                │
├───────────────────────────────────────────────────────────────┤
│ {                                                             │
│   "$schema": "context-engineering/schemas/v1.json",           │
│   "title": "Analysis Request Schema",                         │
│   "description": "Standard format for requesting analysis",   │
│   "type": "object",                                           │
│   "properties": {                                             │
│     "task": {                                                 │
│       "type": "string",                                       │
│       "description": "The analysis task to perform"           │
│     },                                                        │
│     "context": {                                              │
│       "type": "object",                                       │
│       "properties": {                                         │
│         "background": { "type": "string" },                   │
│         "constraints": { "type": "array" },                   │
│         "examples": { "type": "array" }                       │
│       }                                                       │
│     },                                                        │
│     "data": {                                                 │
│       "type": "string",                                       │
│       "description": "The information to analyze"             │
│     },                                                        │
│     "output_format": {                                        │
│       "type": "string",                                       │
│       "enum": ["bullet_points", "paragraphs", "table"]        │
│     }                                                         │
│   },                                                          │
│   "required": ["task", "data"]                                │
│ }                                                             │
└───────────────────────────────────────────────────────────────┘
```

### **[MEM1: Learning to Synergize Memory and Reasoning for Efficient Long-Horizon Agents - Singapore-MIT June 2025  
MEM1：学习协同记忆与推理，打造高效的长远智能体 - 新加坡-麻省理工学院 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)**

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#mem1-learning-to-synergize-memory-and-reasoning-for-efficient-long-horizon-agents---singapore-mit-june-2025)

> “Our results demonstrate the promise of reasoning-driven memory consolidation as a scalable alternative to existing solutions for training long-horizon interactive agents, where both efficiency and performance are optimized." — [Singapore-MIT](https://arxiv.org/pdf/2506.15841)  
> “我们的研究结果表明，推理驱动的记忆整合有望成为现有训练长视界交互式代理的解决方案的一种可扩展替代方案，其效率和性能都得到了优化。”—— [新加坡-麻省理工学院](https://arxiv.org/pdf/2506.15841)

[![image](https://private-user-images.githubusercontent.com/208424706/462241893-16e3f241-5f44-4ed5-9622-f0b4acbb67b0.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MDUzNzIsIm5iZiI6MTc1MTcwNTA3MiwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYyMjQxODkzLTE2ZTNmMjQxLTVmNDQtNGVkNS05NjIyLWYwYjRhY2JiNjdiMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwODQ0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wM2NjODYyMjE0OGFlYjA4MzI1YjJhY2U4ODc0MTQwZGI1MzhjNWNjYmU4YTYzYjNjNjkxYTIwNjk2MTA1ZTFmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.bChpMpgKUv0kmrXbdYdx8NQeVCu_O8sJ2MdJFyr7Tpo)](https://private-user-images.githubusercontent.com/208424706/462241893-16e3f241-5f44-4ed5-9622-f0b4acbb67b0.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MDUzNzIsIm5iZiI6MTc1MTcwNTA3MiwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYyMjQxODkzLTE2ZTNmMjQxLTVmNDQtNGVkNS05NjIyLWYwYjRhY2JiNjdiMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQwODQ0MzJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wM2NjODYyMjE0OGFlYjA4MzI1YjJhY2U4ODc0MTQwZGI1MzhjNWNjYmU4YTYzYjNjNjkxYTIwNjk2MTA1ZTFmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.bChpMpgKUv0kmrXbdYdx8NQeVCu_O8sJ2MdJFyr7Tpo)

### From Schema to Prompt  从图式到提示

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#from-schema-to-prompt)

Schemas can be translated into actual prompts by filling in the structured template:  
通过填写结构化模板，可以将模式转换为实际提示：

```
# Analysis Request

## Task
Identify the main themes and supporting evidence in the provided text.

## Context
### Background
This is a speech given at a climate conference in 2023.

### Constraints
- Focus on scientific claims
- Ignore political statements
- Maintain neutrality

### Examples
- Theme: Rising Sea Levels
  Evidence: "Measurements show a 3.4mm annual rise since 2010"

## Data
[The full text of the speech would go here]

## Output Format
bullet_points
```

This structured approach helps the model understand exactly what information is being provided and what is expected in return.  
这种结构化方法有助于模型准确理解所提供的信息以及期望得到的回报。

## Recursive Prompting: Self-Referential Improvement  
递归提示：自我参照改进

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#recursive-prompting-self-referential-improvement)

Recursive prompting is similar to cognitive priming—it establishes patterns that influence subsequent model behavior. The key insight is having the model reflect on and improve its own outputs.  
递归提示类似于认知启动——它建立影响后续模型行为的模式。其关键在于让模型反思并改进自身的输出。

### Basic Recursive Pattern  基本递归模式

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#basic-recursive-pattern)

```
┌───────────────────────────────────────────────────────────────┐
│ RECURSIVE PROMPTING FLOW                                      │
│                                                               │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐    │
│  │             │      │             │      │             │    │
│  │  Initial    │─────►│  Self-      │─────►│  Improved   │    │
│  │  Response   │      │  Reflection │      │  Response   │    │
│  │             │      │             │      │             │    │
│  └─────────────┘      └─────────────┘      └─────────────┘    │
│        ▲                                          │           │
│        └──────────────────────────────────────────┘           │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Simple Implementation  简单实现

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#simple-implementation)

```python
def recursive_prompt(question, model, iterations=2):
    """Apply recursive prompting to improve responses."""
    
    # Initial response
    response = model.generate(f"Question: {question}\nAnswer:")
    
    for i in range(iterations):
        # Self-reflection prompt
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
        
        # Generate improved response
        response = model.generate(reflection_prompt)
    
    return response
```

This simple recursive pattern can dramatically improve response quality by encouraging the model to critique and refine its own thinking.  
这种简单的递归模式可以通过鼓励模型批判和改进自己的思维来显著提高响应质量。

## Putting It All Together: Cognitive Architecture  
整合：认知架构

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#putting-it-all-together-cognitive-architecture)

These cognitive tools can be combined into a complete architecture that mirrors human thinking processes:  
这些认知工具可以组合成一个反映人类思维过程的完整架构：

```
┌───────────────────────────────────────────────────────────────────────────┐
│                      COGNITIVE ARCHITECTURE                               │
│                                                                           │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Input Parser   │  Understands user intent using schema recognition    │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Prompt Program │  Selects and applies appropriate reasoning pattern   │
│  │  Selector       │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Working Memory │  Maintains state and context across steps            │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Recursive      │  Applies self-improvement through reflection         │
│  │  Processor      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│         │                                                                 │
│         ▼                                                                 │
│  ┌─────────────────┐                                                      │
│  │                 │                                                      │
│  │  Output         │  Formats final response according to schema          │
│  │  Formatter      │                                                      │
│  │                 │                                                      │
│  └─────────────────┘                                                      │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

This architecture can be implemented as a complete system using the tools and patterns we've discussed.  
可以使用我们讨论过的工具和模式将该架构实现为一个完整的系统。

## Key Takeaways  关键要点

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#key-takeaways)

1. **Prompt Programs/Protocols** structure reasoning like human heuristics  
    **提示程序/协议**结构推理类似于人类启发式推理
2. **Context Schemas** organize information like mental knowledge structures  
    **语境模式**像心理知识结构一样组织信息
3. **Recursive Prompting** creates self-improvement loops similar to cognitive reflection  
    **递归提示**创建了类似于认知反射的自我完善循环
4. **Cognitive Architecture** combines these tools into complete systems  
    **认知架构**将这些工具组合成完整的系统

These cognitive extensions to our context engineering framework allow us to create more sophisticated, yet understandable, approaches to working with LLMs.  
这些对我们的上下文工程框架的认知扩展使我们能够创建更复杂但更易于理解的方法来处理 LLM。

## Exercises for Practice  练习

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#exercises-for-practice)

1. Convert one of your frequently used prompts into a prompt program  
    将您常用的提示之一转换为提示程序
2. Create a simple schema for a common task you perform with LLMs  
    为使用 LLM 执行的常见任务创建一个简单的模式
3. Implement basic recursive prompting to improve response quality  
    实施基本的递归提示以提高响应质量
4. Combine these approaches into a mini cognitive architecture  
    将这些方法结合成一个微型认知架构

## Next Steps  后续步骤

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#next-steps)

In the next sections, we'll explore practical implementations of these cognitive tools:  
在接下来的部分中，我们将探讨这些认知工具的实际应用：

- Jupyter notebooks demonstrating prompt programs in action  
    Jupyter 笔记本演示了 Prompt 程序的运行
- Templates for creating your own schemas  
    用于创建您自己的模式的模板
- Examples of complete cognitive architectures  
    完整认知架构的示例

[Continue to Next Section →  
继续下一部分 →](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/06_advanced_applications.md)

---

## Deeper Dive: From Our Research to Your Applications  
深入探究：从我们的研究到您的应用

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/05_cognitive_tools.md#deeper-dive-from-our-research-to-your-applications)

The cognitive tools described above are simplified representations of more advanced research concepts. For those interested in exploring further:  
上述认知工具是更高级研究概念的简化表达。如果您有兴趣进一步探索，请参阅：

- **Prompt Programs** are practical implementations of what researchers call "programmatic prompting" or "structured prompting frameworks"  
    **提示程序**是研究人员所称的“程序化提示”或“结构化提示框架”的实际实现
- **Context Schemas** represent a simplified version of knowledge representation systems and ontological frameworks  
    **上下文模式**代表知识表示系统和本体框架的简化版本
- **Recursive Prompting** is related to self-reflection, metacognition, and recursive self-improvement in AI systems  
    **递归提示**与人工智能系统中的自我反思、元认知和递归自我改进相关

These simplified frameworks make advanced concepts accessible while preserving their practical utility.  
这些简化的框架使得先进的概念变得易于理解，同时保留了其实用性。