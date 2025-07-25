# Atoms: The Fundamental Unit of Prompting  
原子：激发的基本单位

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#atoms-the-fundamental-unit-of-prompting)

> "If you wish to make an apple pie from scratch, you must first invent the universe." — Carl Sagan  
> “如果你想从零开始做一个苹果派，你必须先发明宇宙。”——卡尔·萨根

## The Atom: A Single Instruction  
原子：一条指令

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#the-atom-a-single-instruction)

In our journey through context engineering, we begin with the most fundamental unit: the **atom** — a single, standalone instruction to an LLM.  
在我们的上下文工程之旅中，我们从最基本的单位开始： **原子** ——对 LLM 来说是一个独立的指令。

```
┌───────────────────────────────────────────────┐
│                                               │
│  "Write a poem about the ocean in 4 lines."   │
│                                               │
└───────────────────────────────────────────────┘
```

This is prompt engineering in its purest form: one human, one instruction, one model response. Simple, direct, atomic.  
这是最纯粹的快速工程：一个人，一条指令，一个模型响应。简单、直接、原子化。

## The Anatomy of an Atomic Prompt  
原子提示的剖析

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#the-anatomy-of-an-atomic-prompt)

Let's break down what makes an effective atomic prompt:  
让我们分析一下什么是有效的原子提示：

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  ATOMIC PROMPT = [TASK] + [CONSTRAINTS] + [OUTPUT FORMAT]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

For example:  例如：

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

## The Limitations of Atoms  原子的局限性

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#the-limitations-of-atoms)

While atomic prompts are the building blocks of LLM interactions, they quickly reveal fundamental limitations:  
虽然原子提示是 LLM 交互的基石，但它们很快就暴露出其根本的局限性：

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

The problem? Even with the same atomic prompt, we get different responses each time. Models struggle with consistency when given minimal context.  
问题是什么？即使同一个原子提示，我们每次得到的响应也不同。当给定最少的上下文时，模型很难保持一致性。

## The Single-Atom Baseline: Useful But Limited  
单原子基线：有用但有限

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#the-single-atom-baseline-useful-but-limited)

Despite their limitations, atomic prompts establish our baseline. They help us:  
尽管原子提示有其局限性，但它确立了我们的基线。它们帮助我们：

1. Measure token efficiency (minimal overhead)  
    测量令牌效率（最小开销）
2. Benchmark response quality  
    基准响应质量
3. Establish a control for experiments  
    建立实验控制

```
                     [Response Quality]
                            ▲
                            │
                            │               ⭐ Context
                            │                 Engineering
                            │               
                            │           
                            │       ⭐ Advanced
                            │         Prompting
                            │
                            │   ⭐ Basic Prompting
                            │
                            │
                            └────────────────────────►
                                  [Complexity]
```

## The Unspoken Context: What Models Already "Know"  
未言明的背景：模型已经“知道”什么

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#the-unspoken-context-what-models-already-know)

Even with atomic prompts, LLMs leverage massive implicit context from their training:  
即使有原子提示，LLM 也会利用训练中大量的隐式上下文：

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
这些隐性知识为我们提供了基础，但它不可靠，并且因模型和版本而异。

## The Power Law: Token-Quality Curve  
幂律：代币质量曲线

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#the-power-law-token-quality-curve)

For many tasks, we observe a power law relationship between context tokens and output quality:  
对于许多任务，我们观察到上下文标记和输出质量之间存在幂律关系：

```
    Quality
      ▲
      │
      │    •
      │        •
      │            •
      │                •
      │                    •
      │                        •         •         •
      │                             
      └───────────────────────────────────────────► Tokens
                                      
          [Maximum ROI Zone]       [Diminishing Returns]
```

The critical insight: there's a "maximum ROI zone" where adding just a few tokens yields dramatic quality improvements.  
关键见解：存在一个“最大投资回报率区域”，在该区域中，仅添加几个标记即可显著提高质量。

## From Atoms to Molecules: The Need for More Context  
从原子到分子：需要更多背景信息

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#from-atoms-to-molecules-the-need-for-more-context)

The limitations of atoms lead us naturally to our next step: **molecules**, or multi-part prompts that combine instructions with examples, additional context, and structured formats.  
原子的局限性自然而然地引导我们进入下一步： **分子** ，或者将指令与示例、附加上下文和结构化格式相结合的多部分提示。

Here's the fundamental transition:  
以下是基本转变：

```
┌──────────────────────────┐         ┌──────────────────────────┐
│                          │         │ "Here's an example:      │
│ "Write a limerick about  │    →    │  There once was a...     │
│  a programmer."          │         │                          │
│                          │         │  Now write a limerick    │
└──────────────────────────┘         │  about a programmer."    │
                                     └──────────────────────────┘
    [Atomic Prompt]                       [Molecular Prompt]
```

By adding examples and structure, we begin to shape the context window deliberately—the first step toward context engineering.  
通过添加示例和结构，我们开始有意地塑造上下文窗口——这是迈向上下文工程的第一步。

## Measuring Atom Efficiency: Your First Task  
测量原子效率：您的首要任务

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#measuring-atom-efficiency-your-first-task)

Before moving on, try this simple exercise:  
在继续之前，请尝试这个简单的练习：

1. Take a basic task you'd give to an LLM  
    完成一项你交给法学硕士 (LLM) 的基本任务
2. Create three different atomic prompt versions  
    创建三个不同的原子提示版本
3. Measure tokens used and subjective quality  
    测量使用的令牌和主观质量
4. Plot the efficiency frontier  
    绘制效率前沿

```
┌─────────────────────────────────────────────────────────────┐
│ Task: Summarize a news article                              │
├─────────┬───────────────────────────────┬────────┬──────────┤
│ Version │ Prompt                        │ Tokens │ Quality  │
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

## Key Takeaways  关键要点

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#key-takeaways)

1. **Atomic prompts** are the fundamental unit of LLM interaction  
    **原子提示**是 LLM 交互的基本单位
2. They follow a basic structure: task + constraints + output format  
    它们遵循基本结构：任务+约束+输出格式
3. They have inherent limitations: no memory, examples, or reasoning scaffolds  
    它们有固有的局限性：没有记忆、例子或推理框架
4. Even simple atomic prompts leverage the model's implicit knowledge  
    即使是简单的原子提示也会利用模型的隐性知识
5. There's a power law relationship between context tokens and quality  
    上下文标记和质量之间存在幂律关系
6. Moving beyond atoms is the first step toward context engineering  
    超越原子是迈向上下文工程的第一步

## Next Steps  后续步骤

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#next-steps)

In the next section, we'll explore how to combine atoms into **molecules** — few-shot learning patterns that dramatically improve reliability and control.  
在下一节中，我们将探讨如何将原子组合成**分子** ——小样本学习模式可以显著提高可靠性和控制力。

[Continue to 02_molecules_context.md →  
继续 02_molecules_context.md →](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md)

---

## Deeper Dive: Prompt Templates  
深入了解：提示模板

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/01_atoms_prompting.md#deeper-dive-prompt-templates)

For those wanting to experiment more with atomic prompts, here are some templates to try:  
对于那些想要更多地尝试原子提示的人，这里有一些模板可以尝试：

```
# Basic instruction
{task}

# Persona-based
As a {persona}, {task}

# Format-specific
{task}
Format: {format_specification}

# Constraint-based
{task}
Constraints:
- {constraint_1}
- {constraint_2}
- {constraint_3}

# Step-by-step guided
{task}
Please follow these steps:
1. {step_1}
2. {step_2}
3. {step_3}
```

Try measuring the token count and quality for each template applied to the same task!  
尝试测量应用于同一任务的每个模板的令牌数量和质量！