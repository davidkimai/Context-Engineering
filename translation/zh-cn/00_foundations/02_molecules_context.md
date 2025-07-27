# Molecules: Combining Prompts with Examples （分子：将提示与示例结合）

> "The whole is greater than the sum of its parts." — Aristotle

> “整体大于部分之和。”——亚里士多德

## From Atoms to Molecules （从原子到分子）

In the previous section, we explored **atomic prompts** — single instructions that form the basic unit of LLM interaction. Now we'll combine these atoms into **molecules**: structured contexts that include examples and patterns for the model to follow.

在上一节中，我们探讨了**原子提示**——构成大型语言模型（LLM）交互基本单位的单一指令。现在，我们将这些原子组合成**分子**：包含示例和模式的结构化上下文，供模型遵循。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

This molecular approach leverages a powerful capability of LLMs: **few-shot learning**.

这种分子方法利用了大型语言模型（LLM）的一个强大能力：**少样本学习**。

## Few-Shot Learning: Teaching by Example （少样本学习：通过示例教学）

Few-shot learning is when we provide examples of the desired input-output pattern, allowing the model to recognize and continue the pattern.

少样本学习是指我们提供所需输入-输出模式的示例，让模型识别并继续该模式。

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

模型识别出模式并完成它：“渥太华是加拿大的首都。”

## The Molecular Advantage: Measurable Improvements （分子优势：可衡量的改进）

Let's compare atomic vs. molecular approaches to the same task:

让我们比较一下原子方法和分子方法在同一任务上的表现：

```
┌───────────────────────────────────────┬─────────────────────────────────────┐
│ ATOMIC APPROACH                       │ MOLECULAR APPROACH                   │
│ （原子方法）                            │ （分子方法）                         │
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
- Higher accuracy (10-30% improvement on many tasks)
- Greater consistency (lower variance in outputs)
- Better format adherence
- Clearer handling of edge cases

分子方法通常能实现：
- 更高的准确性（在许多任务上提高10-30%）
- 更大的一致性（输出方差更低）
- 更好的格式依从性
- 更清晰的边缘情况处理

## Designing Effective Molecular Templates （设计有效的分子模板）

The structure of your molecular context matters greatly. Here are common patterns:

分子上下文的结构至关重要。以下是常见的模式：

```
┌─────────────────────────┐  ┌───────────────────┐  ┌───────────────────┐
│ PREFIX-SUFFIX           │  │ INPUT-OUTPUT PAIRS│  │ CHAIN-OF-THOUGHT  │
│ （前缀-后缀）             │  │ （输入-输出对）     │  │ （思维链）          │
├─────────────────────────┤  ├───────────────────┤  ├───────────────────┤
│ <instruction>           │  │ <instruction>     │  │ <instruction>     │
│                         │  │                   │  │                   │
│ <example1> → <result1>  │  │ Input: <example1> │  │ Input: <example1> │
│                         │  │ Output: <result1> │  │ Thinking: <step1> │
│ <example2> → <result2>  │  │                   │  │           <step2> │
│                         │  │ Input: <example2> │  │ Output: <result1> │
│ <new_input> →           │  │ Output: <result2> │  │                   │
└─────────────────────────┘  │                   │  │ Input: <example2> │
                             │ Input: <new_input>│  │ Thinking: <step1> │
                             │ Output:           │  │           <step2> │
                             └───────────────────┘  │ Output: <result2> │
                                                    │                   │
                                                    │ Input: <new_input>│
                                                    │ Thinking:         │
                                                    └───────────────────┘
```

Each template has strengths for different tasks:
- **Prefix-Suffix**: Simplest, works well for straightforward tasks
- **Input-Output Pairs**: Clear demarcation, good for structured data
- **Chain-of-Thought**: Exposes reasoning steps, best for complex tasks

每种模板对于不同的任务都有其优势：
- **前缀-后缀**：最简单，适用于直接的任务
- **输入-输出对**：界限清晰，适用于结构化数据
- **思维链**：揭示推理步骤，最适合复杂任务

## The Science of Example Selection （示例选择的科学）

Not all examples are created equal. When choosing examples for your molecular context:

并非所有示例都生而平等。为分子上下文选择示例时：

```
┌──────────────────────────────────────────────────────────────┐
│ EXAMPLE SELECTION STRATEGIES                                 │
│ （示例选择策略）                                               │
├──────────────────────────────────────────────────────────────┤
│ ✓ Cover diverse cases to show range                          │
│ ✓ Include edge cases that clarify boundaries                 │
│ ✓ Order from simple to complex when possible                 │
│ ✓ Use recent or common examples (recency and frequency bias) │
│ ✓ Include near-misses to establish precise boundaries        │
└──────────────────────────────────────────────────────────────┘
```

## Measuring Molecular Efficiency （衡量分子效率）

As context size grows, so does token count. Let's empirically measure the trade-off:

随着上下文大小的增长，令牌数量也会增加。让我们通过经验测量一下这种权衡：

```
                   [Accuracy] （准确性）
                       ▲
                       │                                    ● 4-shot
                       │                           ● 3-shot
                       │                              
                       │                   ● 2-shot 
                       │              
                       │           
                       │           ● 1-shot 
                       │      
                       │
                       │  
                       │   ● 0-shot
                       └─────────────────────────────────────────────────►
                                [Tokens] （令牌）
```

The key insight: **diminishing returns**. Each additional example costs tokens but yields less improvement than the previous one.

关键的见解是：**收益递减**。每个额外的示例都会消耗令牌，但其带来的改进却比前一个少。

## Finding the Molecular Sweet Spot （寻找分子最佳点）

For most tasks, there's an optimal number of examples that balances quality and token efficiency:

对于大多数任务，存在一个最佳的示例数量，可以在质量和令牌效率之间取得平衡：

```
┌─────────────────────────────────────────────────────────────────┐
│ EXAMPLE COUNT HEURISTICS BY TASK TYPE                           │
│ （按任务类型划分的示例数量启发式）                                │
├───────────────────────────┬─────────────────────────────────────┤
│ Classification            │ 1-3 examples per class              │
│ （分类）                    │ （每个类别1-3个示例）                 │
├───────────────────────────┼─────────────────────────────────────┤
│ Generation                │ 2-5 examples                        │
│ （生成）                    │ （2-5个示例）                       │
├───────────────────────────┼─────────────────────────────────────┤
│ Structured Extraction     │ 2-4 examples covering all fields    │
│ （结构化提取）              │ （覆盖所有字段的2-4个示例）             │
├───────────────────────────┼─────────────────────────────────────┤
│ Reasoning                 │ 2-3 examples with thinking steps    │
│ （推理）                    │ （包含思考步骤的2-3个示例）             │
├───────────────────────────┼─────────────────────────────────────┤
│ Translation               │ 3-5 examples with varying complexity│
│ （翻译）                    │ （3-5个不同复杂度的示例）               │
└───────────────────────────┴─────────────────────────────────────┘
```

## Dynamic Molecule Construction （动态分子构建）

Advanced context engineering involves dynamically selecting the most relevant examples for each input:

高级上下文工程涉及为每个输入动态选择最相关的示例：

```
┌───────────────────────────────────────────────────────────────────┐
│                                                                   │
│   User Query （用户查询）                                           │
│       │                                                           │
│       ▼                                                           │
│  ┌─────────────┐      ┌─────────────────┐                         │
│  │ Query       │      │                 │                         │
│  │ Analysis    │─────▶│ Example         │                         │
│  │ （查询分析）    │      │ Database        │                         │
│  └─────────────┘      │ （示例数据库）      │                         │
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

This approach:
1. Analyzes the user query
2. Retrieves the most relevant examples
3. Constructs a tailored molecular context
4. Sends the optimized context to the LLM

这种方法：
1. 分析用户查询
2. 检索最相关的示例
3. 构建定制的分子上下文
4. 将优化后的上下文发送给大型语言模型（LLM）

## Putting It Into Practice: A Simple Implementation （付诸实践：一个简单的实现）

Here's a Python function that constructs a molecular context from examples:

这是一个从示例构建分子上下文的 Python 函数：

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

## Key Takeaways （主要收获）

1. **Molecular contexts** combine instructions with examples to improve LLM performance
2. **Few-shot learning** lets models recognize and continue patterns
3. **Template structure** matters; different formats work better for different tasks
4. **Example selection** is a science; diversity, edge cases, and ordering all matter
5. **Diminishing returns** exist; each additional example costs tokens with decreasing benefit
6. **Dynamic construction** can optimize the context for each specific input

1. **分子上下文**将指令与示例结合，以提高大型语言模型（LLM）的性能
2. **少样本学习**让模型识别并继续模式
3. **模板结构**很重要；不同的格式适用于不同的任务
4. **示例选择**是一门科学；多样性、边缘情况和排序都很重要
5. 存在**收益递减**；每个额外的示例都会消耗令牌，但收益递减
6. **动态构建**可以优化每个特定输入的上下文

## Exercises for Practice （练习）

1. Take a simple classification task and measure performance with 0, 1, 3, and 5 examples
2. Compare different template structures on the same task
3. Implement dynamic example selection based on similarity to the new input
4. Find the "minimum viable molecule" for a task you care about

1. 选择一个简单的分类任务，并测量使用0、1、3和5个示例时的性能
2. 在同一任务上比较不同的模板结构
3. 根据与新输入的相似性实现动态示例选择
4. 为你关心的任务找到“最小可行分子”

## Next Steps （下一步）

In the next section, we'll explore **cells** — context structures that maintain memory and state across multiple interactions.

在下一节中，我们将探讨**细胞**——在多次交互中保持记忆和状态的上下文结构。

[Continue to 03_cells_memory.md →](03_cells_memory.md)

---

## Deeper Dive: Prompt Engineering vs. Context Engineering （深入探讨：提示工程与上下文工程）

Prompt engineering focuses on crafting the perfect instruction. Context engineering encompasses that and more:

提示工程侧重于精心设计完美的指令。上下文工程则涵盖了这一点以及更多：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT ENGINEERING LAYERS                                          │
│ （上下文工程层）                                                      │
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

上下文工程让您能够控制更多这些层，从而实现更强大的应用程序。