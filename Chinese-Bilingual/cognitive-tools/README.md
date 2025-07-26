# Cognitive Tools for Context Engineering  
上下文工程的认知工具

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#cognitive-tools-for-context-engineering)

> "Give me a lever long enough and a fulcrum on which to place it, and I shall move the world." — Archimedes  
> “给我一个足够长的杠杆和一个支点，我就能撬动地球。”——阿基米德

## What Are Cognitive Tools?  
什么是认知工具？

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#what-are-cognitive-tools)

> "Providing our “cognitive tools” to GPT-4.1 increases its pass@1 performance on AIME2024 from 26.7% to 43.3%, bringing it very close to the performance of o1-preview." — [IBM June 2025](https://www.arxiv.org/pdf/2506.12115)  
> “将我们的‘认知工具’提供给 GPT-4.1，可将其在 AIME2024 上的 pass@1 性能从 26.7% 提升至 43.3%，非常接近 o1-preview 的性能。”—— [IBM 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)

[![image](https://private-user-images.githubusercontent.com/208424706/460370968-a6402827-8bc0-40b5-93d8-46a07154fa4e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MTAwOTAsIm5iZiI6MTc1MTcwOTc5MCwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYwMzcwOTY4LWE2NDAyODI3LThiYzAtNDBiNS05M2Q4LTQ2YTA3MTU0ZmE0ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQxMDAzMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iN2JiNGU1MGE1YTA2NDhhY2JmNThhMGRkY2UwY2E1NDQ2MmYwYWVmNGVkMzMxZWZmMTI1YjU5MTFlY2FlNWY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.W86Ur-SnRJbZz_P060-rYre77q2RRuHq-ajgU3Rjt08)](https://private-user-images.githubusercontent.com/208424706/460370968-a6402827-8bc0-40b5-93d8-46a07154fa4e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTE3MTAwOTAsIm5iZiI6MTc1MTcwOTc5MCwicGF0aCI6Ii8yMDg0MjQ3MDYvNDYwMzcwOTY4LWE2NDAyODI3LThiYzAtNDBiNS05M2Q4LTQ2YTA3MTU0ZmE0ZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcwNVQxMDAzMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iN2JiNGU1MGE1YTA2NDhhY2JmNThhMGRkY2UwY2E1NDQ2MmYwYWVmNGVkMzMxZWZmMTI1YjU5MTFlY2FlNWY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.W86Ur-SnRJbZz_P060-rYre77q2RRuHq-ajgU3Rjt08)

"The tool breaks down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that might be helpful in solving the problem." — [Eliciting Reasoning in Language Models with Cognitive Tools — IBM June 2025](https://www.arxiv.org/pdf/2506.12115)  
该工具通过识别主要概念、提取问题中的相关信息以及突出显示可能有助于解决问题的有意义的属性、定理和技术来分解问题。—— [利用认知工具在语言模型中引出推理——IBM 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)

Cognitive tools are structured prompt patterns that guide language models through specific reasoning operations. Like mental tools that humans use to solve problems (analogies, mental models, heuristics), these tools provide models with scaffolding for complex reasoning tasks.  
认知工具是结构化的提示模式，用于引导语言模型完成特定的推理操作。如同人类用来解决问题的心理工具（类比、心理模型、启发式方法）一样，这些工具为模型提供了执行复杂推理任务的支架。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  CONTEXT ENGINEERING PROGRESSION                             │
│                                                              │
│  Atoms       → Molecules   → Cells       → Organs      → Cognitive Tools  │
│  (Prompts)     (Few-shot)    (Memory)      (Multi-agent)  (Reasoning Patterns) │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Structure  结构

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#structure)

```
cognitive-tools/
├── README.md                  # Overview and quick-start guide
├── cognitive-templates/       # Reusable templates for different reasoning patterns
│   ├── understanding.md       # Templates for comprehension operations
│   ├── reasoning.md           # Templates for analytical operations
│   ├── verification.md        # Templates for checking and validation
│   └── composition.md         # Templates for combining multiple tools
│
├── cognitive-programs/        # Structured prompt programs with code-like patterns
│   ├── basic-programs.md      # Fundamental program structures (conditionals, loops)
│   ├── advanced-programs.md   # Complex program architectures (meta-programming)
│   ├── program-library.py     # Python implementation of common prompt programs
│   └── program-examples.ipynb # Interactive examples showing programs in action
│
├── cognitive-schemas/         # Structured knowledge representation formats
│   ├── user-schemas.md        # Schemas for representing user information
│   ├── domain-schemas.md      # Schemas for different knowledge domains
│   ├── task-schemas.md        # Schemas for different reasoning tasks
│   └── schema-library.yaml    # YAML library of reusable schemas
│
├── cognitive-architectures/   # Complete reasoning systems combining multiple tools
│   ├── solver-architecture.md # Architecture for problem-solving applications
│   ├── tutor-architecture.md  # Architecture for educational applications
│   ├── research-architecture.md # Architecture for information synthesis
│   └── architecture-examples.py # Implementation examples of complete architectures
│
└── integration/               # Guides for integrating with other components
    ├── with-rag.md            # Combining cognitive tools with retrieval
    ├── with-memory.md         # Integrating with memory systems
    ├── with-agents.md         # Using in multi-agent architectures
    └── evaluation-metrics.md  # Measuring cognitive tool effectiveness
```

## Why Cognitive Tools Matter  
为什么认知工具很重要

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#why-cognitive-tools-matter)

Research has shown that structuring reasoning with cognitive tools can dramatically improve model performance:  
研究表明，利用认知工具进行结构化推理可以显著提高模型性能：

- **Performance**: Up to 16.6% improvement on mathematical reasoning benchmarks  
    **性能** ：数学推理基准测试提升高达 16.6%
- **Reliability**: Significant reduction in reasoning errors and hallucinations  
    **可靠性** ：推理错误和幻觉显著减少
- **Efficiency**: Better results with fewer total tokens  
    **效率** ：用更少的 token 获得更好的结果
- **Flexibility**: Applicable across domains from mathematics to creative writing  
    **灵活性** ：适用于从数学到创意写作的各个领域

## Quick Start  快速入门

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#quick-start)

To use a cognitive tool, choose a template from `cognitive-templates/` that matches your task:  
要使用认知工具，请从 `cognitive-templates/` 中选择与您的任务相匹配的模板：

```python
# Example: Using the "understand_question" cognitive tool
from cognitive_tools.templates import understand_question

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
understanding = llm.generate(understand_question(problem))
print(understanding)
```

For more complex reasoning, use structured prompt programs from `cognitive-programs/`:  
对于更复杂的推理，请使用来自 `cognitive-programs/` 结构化提示程序：

```python
# Example: Using a multi-step reasoning program
from cognitive_tools.programs import solve_math_problem

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
solution = solve_math_problem(problem, llm=my_llm_interface)
print(solution.steps)  # View step-by-step reasoning
print(solution.answer)  # View final answer
```

## Directory Structure  目录结构

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#directory-structure)

- `cognitive-templates/`: Reusable templates for different reasoning operations  
    `cognitive-templates/` ：用于不同推理操作的可重复使用模板
- `cognitive-programs/`: Structured prompt programs with code-like patterns  
    `cognitive-programs/` ：具有类似代码模式的结构化提示程序
- `cognitive-schemas/`: Knowledge representation formats for different domains  
    `cognitive-schemas/` ：不同领域的知识表示格式
- `cognitive-architectures/`: Complete reasoning systems combining multiple tools  
    `cognitive-architectures/` ：结合多种工具的完整推理系统
- `integration/`: Guides for integrating with other components (RAG, memory, etc.)  
    `integration/` ：与其他组件（RAG、记忆等）集成的指南

## Learning Path  学习路径

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#learning-path)

1. **Start with templates**: Learn the basic cognitive operations  
    **从模板开始** ：学习基本的认知操作
2. **Explore programs**: See how operations can be combined into reasoning flows  
    **探索程序** ：了解如何将操作组合成推理流程
3. **Study schemas**: Understand how to structure knowledge effectively  
    **学习图式** ：了解如何有效地构建知识
4. **Master architectures**: Build complete reasoning systems  
    **主架构** ：构建完整的推理系统
5. **Integrate components**: Combine with RAG, memory, and other context engineering components  
    **集成组件** ：与 RAG、记忆和其他上下文工程组件结合

## Measuring Effectiveness  衡量有效性

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#measuring-effectiveness)

Always measure the impact of cognitive tools on your specific tasks:  
始终衡量认知工具对你的特定任务的影响：

```python
# Example: Measuring performance improvement
from cognitive_tools.evaluation import measure_reasoning_quality

baseline_score = measure_reasoning_quality(problem, baseline_prompt)
tool_score = measure_reasoning_quality(problem, cognitive_tool_prompt)

improvement = (tool_score / baseline_score - 1) * 100
print(f"Cognitive tool improved performance by {improvement:.1f}%")
```

## Research Foundation  研究基金会

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#research-foundation)

These tools are based on research from:  
这些工具基于以下研究：

- Brown et al. (2025): "Eliciting Reasoning in Language Models with Cognitive Tools"  
    Brown 等人（2025 年）：“利用认知工具在语言模型中引出推理”
- Wei et al. (2023): "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"  
    Wei 等人（2023 年）：“思路链提示在大型语言模型中引发推理”
- Huang et al. (2022): "Inner Monologue: Embodying Knowledge and Reasoning in Language Models"  
    Huang 等人（2022 年）：“内心独白：在语言模型中体现知识和推理”

## Contributing  贡献

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#contributing)

Have a new cognitive tool pattern that works well? See [CONTRIBUTING.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/.github/CONTRIBUTING.md) for guidelines on submitting your templates, programs, or architectures.  
你有一个新的、运行良好的认知工具模式吗？请参阅 [CONTRIBUTING.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/.github/CONTRIBUTING.md) ，了解如何提交模板、程序或架构。

## Next Steps  后续步骤

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/README.md#next-steps)

- See [understanding.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/cognitive-templates/understanding.md) for basic comprehension tools  
    请参阅 [understanding.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/cognitive-templates/understanding.md) 了解基本理解工具
- Try [basic-programs.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/cognitive-programs/basic-programs.md) for fundamental program structures  
    尝试 [basic-programs.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/cognitive-programs/basic-programs.md) 了解基本程序结构
- Explore [solver-architecture.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/cognitive-architectures/solver-architecture.md) for a complete problem-solving system  
    探索 [solver-architecture.md](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/cognitive-tools/cognitive-architectures/solver-architecture.md) ，了解完整的问题解决系统