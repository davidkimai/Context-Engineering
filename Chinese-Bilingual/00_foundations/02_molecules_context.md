# Molecules: Combining Prompts with Examples  
分子：结合提示和例子

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#molecules-combining-prompts-with-examples)

> "The whole is greater than the sum of its parts." — Aristotle  
> “整体大于部分之和。”——亚里士多德

## From Atoms to Molecules  从原子到分子

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#from-atoms-to-molecules)

In the previous section, we explored **atomic prompts** — single instructions that form the basic unit of LLM interaction. Now we'll combine these atoms into **molecules**: structured contexts that include examples and patterns for the model to follow.  
在上一节中，我们探讨了**原子提示** ——构成 LLM 交互基本单元的单个指令。现在，我们将这些原子组合成**分子** ：包含模型要遵循的示例和模式的结构化上下文。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

This molecular approach leverages a powerful capability of LLMs: **few-shot learning**.  
这种分子方法利用了 LLM 的强大功能： **小样本学习** 。

## Few-Shot Learning: Teaching by Example  
少量学习：通过示例教学

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#few-shot-learning-teaching-by-example)

Few-shot learning is when we provide examples of the desired input-output pattern, allowing the model to recognize and continue the pattern.  
少量学习是指我们提供所需输入输出模式的示例，让模型识别并延续该模式。

```
┌───────────────────────────────────────────────────────────────────────┐
│ Input: "Paris"                                                         │
│ Output: "Paris is the capital of France."                              │
│                                                                        │
│ Input: "Tokyo"                                                         │
│ Output: "Tokyo is the capital of Japan."                               │
│                                                                        │
│ Input: "Ottawa"                                                        │
│ Output: ?                                                              │
└───────────────────────────────────────────────────────────────────────┘
```

The model recognizes the pattern and completes it: "Ottawa is the capital of Canada."  
模型识别了该模式并完成它：“渥太华是加拿大的首都。”

## The Molecular Advantage: Measurable Improvements  
分子优势：可衡量的改进

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#the-molecular-advantage-measurable-improvements)

Let's compare atomic vs. molecular approaches to the same task:  
让我们比较一下原子方法和分子方法对同一任务的处理方式：

```
┌───────────────────────────────────────┬─────────────────────────────────────┐
│ ATOMIC APPROACH                       │ MOLECULAR APPROACH                   │
├───────────────────────────────────────┼─────────────────────────────────────┤
│ "Classify this review as positive     │ "Classify the sentiment of reviews.  │
│  or negative:                         │                                      │
│                                       │ Review: 'The food was amazing!'      │
│  'The service was terrible and        │ Sentiment: Positive                  │
│   the food was cold.'"                │                                      │
│                                       │ Review: 'Waited 30 minutes and       │
│                                       │  the food was cold.'                 │
│                                       │ Sentiment: Negative                  │
│                                       │                                      │
│                                       │ Review: 'The service was terrible    │
│                                       │  and the food was cold.'"            │
│                                       │ Sentiment:                           │
└───────────────────────────────────────┴─────────────────────────────────────┘
```

The molecular approach typically achieves:  
分子方法通常可以实现：

- Higher accuracy (10-30% improvement on many tasks)  
    更高的准确率（许多任务的准确率提高了 10-30%）
- Greater consistency (lower variance in outputs)  
    更高的一致性（输出的差异更低）
- Better format adherence  更好地遵守格式
- Clearer handling of edge cases  
    更清晰地处理边缘情况

## Designing Effective Molecular Templates  
设计有效的分子模板

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#designing-effective-molecular-templates)

The structure of your molecular context matters greatly. Here are common patterns:  
分子结构非常重要。以下是一些常见的模式：

```
┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│ PREFIX-SUFFIX     │  │ INPUT-OUTPUT PAIRS │  │ CHAIN-OF-THOUGHT  │
├───────────────────┤  ├───────────────────┤  ├───────────────────┤
│ <instruction>     │  │ <instruction>     │  │ <instruction>     │
│                   │  │                   │  │                   │
│ Input: <example1> │  │ Input: <example1> │  │ Input: <example1> │
│ Output: <result1> │  │ Output: <result1> │  │ Thinking: <step1> │
│                   │  │                   │  │         <step2>   │
│ Input: <example2> │  │ Input: <example2> │  │ Output: <result1> │
│ Output: <result2> │  │ Output: <result2> │  │                   │
│                   │  │                   │  │ Input: <example2> │
│ Input: <new_input>│  │ Input: <new_input>│  │ Thinking: <step1> │
│ Output:           │  │ Output:           │  │         <step2>   │
└───────────────────┘  └───────────────────┘  │ Output: <result2> │
                                              │                   │
                                              │ Input: <new_input>│
                                              │ Thinking:         │
                                              └───────────────────┘
```

Each template has strengths for different tasks:  
每个模板针对不同的任务都有其优势：

- **Prefix-Suffix**: Simplest, works well for straightforward tasks  
    **前缀-后缀** ：最简单，适用于简单的任务
- **Input-Output Pairs**: Clear demarcation, good for structured data  
    **输入输出对** ：界限清晰，适合结构化数据
- **Chain-of-Thought**: Exposes reasoning steps, best for complex tasks  
    **思路链** ：揭示推理步骤，最适合复杂任务

## The Science of Example Selection  
示例选择的科学

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#the-science-of-example-selection)

Not all examples are created equal. When choosing examples for your molecular context:  
并非所有示例都生而平等。在为你的分子上下文选择示例时：

```
┌──────────────────────────────────────────────────────────────┐
│ EXAMPLE SELECTION STRATEGIES                                 │
├──────────────────────────────────────────────────────────────┤
│ ✓ Cover diverse cases to show range                          │
│ ✓ Include edge cases that clarify boundaries                 │
│ ✓ Order from simple to complex when possible                 │
│ ✓ Use recent or common examples (recency and frequency bias) │
│ ✓ Include near-misses to establish precise boundaries        │
└──────────────────────────────────────────────────────────────┘
```

## Measuring Molecular Efficiency  
测量分子效率

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#measuring-molecular-efficiency)

As context size grows, so does token count. Let's empirically measure the trade-off:  
随着上下文规模的增长，token 数量也会随之增加。让我们通过实证分析来衡量一下其中的利弊：

```
                   [Accuracy]
                       ▲
                       │
                       │                  ● 4-shot
                       │
                       │              ● 3-shot
                       │
                       │          ● 2-shot
                       │
                       │      ● 1-shot
                       │
                       │  ● 0-shot
                       │
                       └────────────────────────►
                                [Tokens]
```

The key insight: **diminishing returns**. Each additional example costs tokens but yields less improvement than the previous one.  
关键洞察： **收益递减** 。每个额外的示例都会花费代币，但产生的改进却比前一个更少。

## Finding the Molecular Sweet Spot  
寻找分子最佳点

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#finding-the-molecular-sweet-spot)

For most tasks, there's an optimal number of examples that balances quality and token efficiency:  
对于大多数任务来说，存在一个可以平衡质量和标记效率的最佳示例数量：

```
┌─────────────────────────────────────────────────────────────────┐
│ EXAMPLE COUNT HEURISTICS BY TASK TYPE                           │
├───────────────────────────┬─────────────────────────────────────┤
│ Classification            │ 1-3 examples per class              │
├───────────────────────────┼─────────────────────────────────────┤
│ Generation                │ 2-5 examples                        │
├───────────────────────────┼─────────────────────────────────────┤
│ Structured Extraction     │ 2-4 examples covering all fields    │
├───────────────────────────┼─────────────────────────────────────┤
│ Reasoning                 │ 2-3 examples with thinking steps    │
├───────────────────────────┼─────────────────────────────────────┤
│ Translation               │ 3-5 examples with varying complexity│
└───────────────────────────┴─────────────────────────────────────┘
```

## Dynamic Molecule Construction  
动态分子构建

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#dynamic-molecule-construction)

Advanced context engineering involves dynamically selecting the most relevant examples for each input:  
高级上下文工程涉及为每个输入动态选择最相关的示例：

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   User Query                                                      │
│       │                                                           │
│       ▼                                                           │
│  ┌─────────────┐      ┌─────────────────┐                         │
│  │ Query       │      │                 │                         │
│  │ Analysis    │─────▶│ Example         │                         │
│  │             │      │ Database        │                         │
│  └─────────────┘      │                 │                         │
│                       └─────────────────┘                         │
│                              │                                    │
│                              │ Retrieve most                      │
│                              │ similar examples                   │
│                              ▼                                    │
│                       ┌─────────────────┐                         │
│                       │ Dynamic         │                         │
│                       │ Molecular       │                         │
│                       │ Context         │                         │
│                       └─────────────────┘                         │
│                              │                                    │
│                              │                                    │
│                              ▼                                    │
│                       ┌─────────────────┐                         │
│                       │                 │                         │
│                       │ LLM             │                         │
│                       │                 │                         │
│                       └─────────────────┘                         │
│                                                                   │
└───────────────────────────────────────────────────────────────────┘
```

This approach:  这种方法：

1. Analyzes the user query  
    分析用户查询
2. Retrieves the most relevant examples  
    检索最相关的示例
3. Constructs a tailored molecular context  
    构建定制的分子环境
4. Sends the optimized context to the LLM  
    将优化的上下文发送到 LLM

## Putting It Into Practice: A Simple Implementation  
付诸实践：一个简单的实现

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#putting-it-into-practice-a-simple-implementation)

Here's a Python function that constructs a molecular context from examples:  
下面是一个根据示例构建分子背景的 Python 函数：

```python
def create_molecular_context(instruction, examples, new_input, 
                            format_type="input-output"):
    """
    Construct a molecular context from examples.
    
    Args:
        instruction (str): The task instruction
        examples (List[Dict]): List of example input/output pairs
        new_input (str): The new input to process
        format_type (str): Template type (input-output, chain-of-thought)
    
    Returns:
        str: The complete molecular context
    """
    context = f"{instruction}\n\n"
    
    # Add examples based on format type
    if format_type == "input-output":
        for example in examples:
            context += f"Input: {example['input']}\n"
            context += f"Output: {example['output']}\n\n"
    elif format_type == "chain-of-thought":
        for example in examples:
            context += f"Input: {example['input']}\n"
            context += f"Thinking: {example['thinking']}\n"
            context += f"Output: {example['output']}\n\n"
    
    # Add the new input
    context += f"Input: {new_input}\nOutput:"
    
    return context
```

## Key Takeaways  关键要点

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#key-takeaways)

1. **Molecular contexts** combine instructions with examples to improve LLM performance  
    **分子背景**将说明与示例相结合，以提高 LLM 的表现
2. **Few-shot learning** lets models recognize and continue patterns  
    **少量学习**让模型识别并延续模式
3. **Template structure** matters; different formats work better for different tasks  
    **模板结构**很重要；不同的格式更适合不同的任务
4. **Example selection** is a science; diversity, edge cases, and ordering all matter  
    **示例选择**是一门科学；多样性、边缘情况和排序都很重要
5. **Diminishing returns** exist; each additional example costs tokens with decreasing benefit  
    **收益递减**存在；每个额外的示例都会花费代币，收益也会递减
6. **Dynamic construction** can optimize the context for each specific input  
    **动态构造**可以针对每个特定输入优化上下文

## Exercises for Practice  练习

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#exercises-for-practice)

1. Take a simple classification task and measure performance with 0, 1, 3, and 5 examples  
    进行简单的分类任务，并用 0、1、3 和 5 个示例衡量性能
2. Compare different template structures on the same task  
    比较同一任务上不同的模板结构
3. Implement dynamic example selection based on similarity to the new input  
    根据与新输入的相似性实现动态示例选择
4. Find the "minimum viable molecule" for a task you care about  
    找到你关心的任务的“最小可行分子”

## Next Steps  后续步骤

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#next-steps)

In the next section, we'll explore **cells** — context structures that maintain memory and state across multiple interactions.  
在下一节中，我们将探索**单元格** ——在多个交互中维持记忆和状态的上下文结构。

[Continue to 03_cells_memory.md →  
继续 03_cells_memory.md →](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md)

---

## Deeper Dive: Prompt Engineering vs. Context Engineering  
深入探讨：即时工程与上下文工程

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/02_molecules_context.md#deeper-dive-prompt-engineering-vs-context-engineering)

Prompt engineering focuses on crafting the perfect instruction. Context engineering encompasses that and more:  
即时工程专注于制定完美的教学方案。上下文工程则涵盖了这一点，甚至更多：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT ENGINEERING LAYERS                                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────┐                                               │
│   │ State & Memory  │  Conversation history, persistent variables   │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Retrieved Data  │  RAG, tool outputs, external knowledge        │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Examples        │  Few-shot learning, demonstrations            │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Instructions    │  Prompts, system messages, constraints        │
│   └─────────────────┘                                               │
│           ▲                                                         │
│           │                                                         │
│   ┌─────────────────┐                                               │
│   │ Model Behavior  │  Training data, alignments, capabilities      │
│   └─────────────────┘                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

Context engineering gives you control over more of these layers, leading to more powerful applications.  
上下文工程使您可以控制更多这些层，从而实现更强大的应用程序。