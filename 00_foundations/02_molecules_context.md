# Molecules: Combining Prompts with Examples

> "The whole is greater than the sum of its parts." — Aristotle

## From Atoms to Molecules

In the previous section, we explored **atomic prompts** — single instructions that form the basic unit of LLM interaction. Now we'll combine these atoms into **molecules**: structured contexts that include examples and patterns for the model to follow.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  MOLECULE = [INSTRUCTION] + [EXAMPLES] + [CONTEXT] + [NEW INPUT]            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

This molecular approach leverages a powerful capability of LLMs: **few-shot learning**.

## Few-Shot Learning: Teaching by Example

Few-shot learning is when we provide examples of the desired input-output pattern, allowing the model to recognize and continue the pattern.

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

## The Molecular Advantage: Measurable Improvements

Let's compare atomic vs. molecular approaches to the same task:

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
- Higher accuracy (10-30% improvement on many tasks)
- Greater consistency (lower variance in outputs)
- Better format adherence
- Clearer handling of edge cases

## Designing Effective Molecular Templates

The structure of your molecular context matters greatly. Here are common patterns:

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
- **Prefix-Suffix**: Simplest, works well for straightforward tasks
- **Input-Output Pairs**: Clear demarcation, good for structured data
- **Chain-of-Thought**: Exposes reasoning steps, best for complex tasks

## The Science of Example Selection

Not all examples are created equal. When choosing examples for your molecular context:

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

As context size grows, so does token count. Let's empirically measure the trade-off:

```
                   [Accuracy]
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
                                [Tokens]
```

The key insight: **diminishing returns**. Each additional example costs tokens but yields less improvement than the previous one.

## Finding the Molecular Sweet Spot

For most tasks, there's an optimal number of examples that balances quality and token efficiency:

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

Advanced context engineering involves dynamically selecting the most relevant examples for each input:

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

This approach:
1. Analyzes the user query
2. Retrieves the most relevant examples
3. Constructs a tailored molecular context
4. Sends the optimized context to the LLM

## Putting It Into Practice: A Simple Implementation

Here's a Python function that constructs a molecular context from examples:

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

## Key Takeaways

1. **Molecular contexts** combine instructions with examples to improve LLM performance
2. **Few-shot learning** lets models recognize and continue patterns
3. **Template structure** matters; different formats work better for different tasks
4. **Example selection** is a science; diversity, edge cases, and ordering all matter
5. **Diminishing returns** exist; each additional example costs tokens with decreasing benefit
6. **Dynamic construction** can optimize the context for each specific input

## Exercises for Practice

1. Take a simple classification task and measure performance with 0, 1, 3, and 5 examples
2. Compare different template structures on the same task
3. Implement dynamic example selection based on similarity to the new input
4. Find the "minimum viable molecule" for a task you care about

## Next Steps

In the next section, we'll explore **cells** — context structures that maintain memory and state across multiple interactions.

[Continue to 03_cells_memory.md →](03_cells_memory.md)

---

## Deeper Dive: Prompt Engineering vs. Context Engineering

Prompt engineering focuses on crafting the perfect instruction. Context engineering encompasses that and more:

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
