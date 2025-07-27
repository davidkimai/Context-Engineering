# Atoms: The Fundamental Unit of Prompting （原子：提示的基本单位）

> "If you wish to make an apple pie from scratch, you must first invent the universe." — Carl Sagan

> “如果你想从零开始制作一个苹果派，你必须首先创造宇宙。”——卡尔·萨根

## The Atom: A Single Instruction （原子：单个指令）

In our journey through context engineering, we begin with the most fundamental unit: the **atom** — a single, standalone instruction to an LLM.

在我们的上下文工程之旅中，我们从最基本的单元开始：**原子**——一个对大型语言模型（LLM）的单一、独立的指令。

```
┌───────────────────────────────────────────────┐
│                                               │
│  "Write a poem about the ocean in 4 lines."   │
│                                               │
└───────────────────────────────────────────────┘
```

This is prompt engineering in its purest form: one human, one instruction, one model response. Simple, direct, atomic.

这是提示工程最纯粹的形式：一个人，一个指令，一个模型响应。简单、直接、原子化。

## The Anatomy of an Atomic Prompt （原子提示的剖析）

Let's break down what makes an effective atomic prompt:

让我们分解一下构成有效原子提示的要素：

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ATOMIC PROMPT = [TASK] + [CONSTRAINTS] + [OUTPUT FORMAT]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

For example:

例如：

```
┌─────────────────────┬────────────────────────┬────────────────────┐
│        TASK         │      CONSTRAINTS       │   OUTPUT FORMAT    │
├─────────────────────┼────────────────────────┼────────────────────┤
│ "Write a poem       │ "about the ocean       │ "in 4 lines."      │
│  about space."      │  using only words      │                    │
│                     │  with 5 letters        │                    │
│                     │  or less."             │                    │
└─────────────────────┴────────────────────────┴────────────────────┘
```

## The Limitations of Atoms （原子的局限性）

While atomic prompts are the building blocks of LLM interactions, they quickly reveal fundamental limitations:

虽然原子提示是大型语言模型（LLM）交互的基石，但它们很快就暴露出根本性的局限性：

```
┌──────────────────────────────────────┐
│ LIMITATIONS OF ATOMIC PROMPTS        │
├──────────────────────────────────────┤
│ ✗ No memory across interactions      │
│ ✗ Limited demonstration capability   │
│ ✗ No complex reasoning scaffolds     │
│ ✗ Prone to ambiguity                 │
│ ✗ High variance in outputs           │
└──────────────────────────────────────┘
```

Let's measure this empirically with a simple experiment:

让我们通过一个简单的实验来实证测量这一点：

```python
# A basic atomic prompt
atomic_prompt = "List 5 symptoms of diabetes."

# Send to LLM multiple times
responses = [llm.generate(atomic_prompt) for _ in range(5)]

# Measure variability
unique_symptoms = set()
for response in responses:
    symptoms = extract_symptoms(response)
    unique_symptoms.update(symptoms)

print(f"Found {len(unique_symptoms)} unique symptoms across 5 identical prompts")
# Typically outputs far more than just 5 unique symptoms
```

The problem? Models struggle with consistency when given minimal context.

问题是什么？模型在给定最少上下文时难以保持一致性。

## The Single-Atom Baseline: Useful But Limited （单原子基线：有用但有限）

Despite their limitations, atomic prompts establish our baseline. They help us:

尽管原子提示有其局限性，但它们确立了我们的基线。它们帮助我们：

1. Measure token efficiency (minimal overhead)
2. Benchmark response quality
3. Establish a control for experiments

1. 衡量令牌效率（最小开销）
2. 评估响应质量
3. 建立实验对照组

```
                     [Response Quality] （响应质量）
                            ▲
                            │
                            │               ⭐ Context （上下文）
                            │                 Engineering （工程）
                            │               
                            │           
                            │       ⭐ Advanced （高级）
                            │         Prompting （提示）
                            │
                            │   ⭐ Basic Prompting （基本提示）
                            │
                            │
                            └────────────────────────►
                                  [Complexity] （复杂性）
```

## The Unspoken Context: What Models Already "Know" （不言而喻的上下文：模型已经“知道”什么）

Even with atomic prompts, LLMs leverage massive implicit context from their training:

即使使用原子提示，大型语言模型（LLM）也会利用其训练中大量的隐式上下文：

```
┌───────────────────────────────────────────────────────────────┐
│ IMPLICIT CONTEXT IN MODELS                                    │
├───────────────────────────────────────────────────────────────┤
│ ✓ Language rules and grammar                                  │
│ ✓ Common knowledge facts                                      │
│ ✓ Format conventions (lists, paragraphs, etc.)                │
│ ✓ Domain-specific knowledge (varies by model)                 │
│ ✓ Learned interaction patterns                                │
└───────────────────────────────────────────────────────────────┘
```

This implicit knowledge gives us a foundation, but it's unreliable and varies between models and versions.

这种隐性知识为我们提供了基础，但它不可靠，并且在不同模型和版本之间存在差异。

## The Power Law: Token-Quality Curve （幂律：令牌-质量曲线）

For many tasks, we observe a power law relationship between context tokens and output quality:

对于许多任务，我们观察到上下文令牌和输出质量之间存在幂律关系：

```
    Quality （质量）
      ▲
      │
      │    •
      │        •
      │            •
      │                •
      │                    •
      │                        •         •         •
      │                             
      └───────────────────────────────────────────► Tokens （令牌）
                                      
          [Maximum ROI Zone] （最大投资回报区）       [Diminishing Returns] （收益递减）
```

The critical insight: there's a "maximum ROI zone" where adding just a few tokens yields dramatic quality improvements.

关键的见解是：“最大投资回报区”的存在，在这个区域内，只需添加少量令牌就能显著提高质量。

## From Atoms to Molecules: The Need for More Context （从原子到分子：对更多上下文的需求）

The limitations of atoms lead us naturally to our next step: **molecules**, or multi-part prompts that combine instructions with examples, additional context, and structured formats.

原子的局限性自然地引导我们走向下一步：**分子**，即结合指令、示例、额外上下文和结构化格式的多部分提示。

Here's the fundamental transition:

这是根本性的转变：

```
┌──────────────────────────┐         ┌──────────────────────────┐
│                          │         │ "Here's an example:      │
│ "Write a limerick about  │    →    │  There once was a...     │
│  a programmer."          │         │                          │
│                          │         │  Now write a limerick    │
└──────────────────────────┘         │  about a programmer."    │
                                     └──────────────────────────┘
    [Atomic Prompt] （原子提示）                       [Molecular Prompt] （分子提示）
```

By adding examples and structure, we begin to shape the context window deliberately—the first step toward context engineering.

通过添加示例和结构，我们开始有意识地塑造上下文窗口——这是迈向上下文工程的第一步。

## Measuring Atom Efficiency: Your First Task （衡量原子效率：你的第一个任务）

Before moving on, try this simple exercise:

在继续之前，请尝试这个简单的练习：

1. Take a basic task you'd give to an LLM
2. Create three different atomic prompt versions
3. Measure tokens used and subjective quality
4. Plot the efficiency frontier

1. 选择一个你会交给大型语言模型（LLM）的基本任务
2. 创建三个不同的原子提示版本
3. 测量使用的令牌和主观质量
4. 绘制效率前沿

```
┌─────────────────────────────────────────────────────────────┐
│ Task: Summarize a news article （任务：总结一篇新闻文章）                              │
├─────────┬───────────────────────────────┬────────┬──────────┤
│ Version │ Prompt                        │ Tokens │ Quality  │
│ （版本）  │ （提示）                        │ （令牌） │ （质量）   │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ A       │ "Summarize this article."     │ 4      │ 2/10     │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ B       │ "Provide a concise summary    │ 14     │ 6/10     │
│         │  of this article in 3         │        │          │
│         │  sentences."                  │        │          │
├─────────┼───────────────────────────────┼────────┼──────────┤
│ C       │ "Write a summary of the key   │ 27     │ 8/10     │
│         │  points in this article,      │        │          │
│         │  highlighting the main        │        │          │
│         │  people and events."          │        │          │
└─────────┴───────────────────────────────┴────────┴──────────┘
```

## Key Takeaways （主要收获）

1. **Atomic prompts** are the fundamental unit of LLM interaction
2. They follow a basic structure: task + constraints + output format
3. They have inherent limitations: no memory, examples, or reasoning scaffolds
4. Even simple atomic prompts leverage the model's implicit knowledge
5. There's a power law relationship between context tokens and quality
6. Moving beyond atoms is the first step toward context engineering

1. **原子提示**是大型语言模型（LLM）交互的基本单位
2. 它们遵循基本结构：任务 + 约束 + 输出格式
3. 它们具有固有的局限性：没有记忆、示例或推理支架
4. 即使是简单的原子提示也利用了模型的隐性知识
5. 上下文令牌和质量之间存在幂律关系
6. 超越原子是迈向上下文工程的第一步

## Next Steps （下一步）

In the next section, we'll explore how to combine atoms into **molecules** — few-shot learning patterns that dramatically improve reliability and control.

在下一节中，我们将探讨如何将原子组合成**分子**——一种能够显著提高可靠性和控制力的少样本学习模式。

[Continue to 02_molecules_context.md →](02_molecules_context.md)

---

## Deeper Dive: Prompt Templates （深入探讨：提示模板）

For those wanting to experiment more with atomic prompts, here are some templates to try:

对于那些希望更多地尝试原子提示的人，这里有一些可以尝试的模板：

```
# Basic instruction （基本指令）
{task}

# Persona-based （基于角色的）
As a {persona}, {task} （作为一名{角色}，{任务}）

# Format-specific （格式特定）
{task}
Format: {format_specification} （格式：{格式规范}）

# Constraint-based （基于约束的）
{task}
Constraints: （约束：）
- {constraint_1}
- {constraint_2}
- {constraint_3}

# Step-by-step guided （分步指导）
{task}
Please follow these steps: （请遵循以下步骤：）
1. {step_1}
2. {step_2}
3. {step_3}
```

Try measuring the token count and quality for each template applied to the same task!

尝试测量应用于相同任务的每个模板的令牌计数和质量！