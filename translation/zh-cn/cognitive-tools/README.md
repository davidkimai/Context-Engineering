# Cognitive Tools for Context Engineering （用于上下文工程的认知工具）

> "Give me a lever long enough and a fulcrum on which to place it, and I shall move the world." — Archimedes
> “给我一个足够长的杠杆和一个支点，我就能撬动地球。” — 阿基米德

## What Are Cognitive Tools? （什么是认知工具？）
> "Providing our “cognitive tools” to GPT-4.1
increases its pass@1 performance on AIME2024 from 26.7% to 43.3%, bringing it very close to the performance of o1-preview." — [IBM June 2025](https://www.arxiv.org/pdf/2506.12115)
> “向 GPT-4.1 提供我们的“认知工具”，其在 AIME2024 上的 pass@1 性能从 26.7% 提高到 43.3%，使其非常接近 o1-preview 的性能。” — [IBM 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)

<div align="center">
    
![image](https://github.com/user-attachments/assets/a6402827-8bc0-40b5-93d8-46a07154fa4e)

"The tool breaks down the problem by identifying the main concepts at hand, extracting relevant information in the question, and highlighting meaningful properties, theorems, and techniques that might be helpful in solving the problem." — [Eliciting Reasoning in Language Models with Cognitive Tools — IBM June 2025](https://www.arxiv.org/pdf/2506.12115)
“该工具通过识别手头的核心概念、提取问题中的相关信息，并突出显示可能有助于解决问题的有意义的属性、定理和技术来分解问题。” — [使用认知工具引发语言模型中的推理 — IBM 2025 年 6 月](https://www.arxiv.org/pdf/2506.12115)


</div>

Cognitive tools are structured prompt patterns that guide language models through specific reasoning operations. Like mental tools that humans use to solve problems (analogies, mental models, heuristics), these tools provide models with scaffolding for complex reasoning tasks.
认知工具是结构化的提示模式，引导语言模型完成特定的推理操作。就像人类用来解决问题的思维工具（类比、心智模型、启发法）一样，这些工具为模型提供了复杂推理任务的脚手架。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  CONTEXT ENGINEERING PROGRESSION                             │
│  （上下文工程进展）                                          │
│                                                              │
│  Atoms       → Molecules   → Cells       → Organs      → Cognitive Tools  │
│  (Prompts)     (Few-shot)    (Memory)      (Multi-agent)  (Reasoning Patterns) │
│  （原子（提示））→（分子（少样本））→（细胞（记忆））→（器官（多智能体））→（认知工具（推理模式））│
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Structure （结构）
```
cognitive-tools/
├── README.md                       # Overview and quick-start guide （概述和快速入门指南）
├── cognitive-templates/            # Templates for cognitive processes （认知过程模板）
│   ├── understanding.md            # Comprehension templates （理解模板）
│   ├── reasoning.md                # Reasoning templates （推理模板）
│   ├── verification.md             # Verification templates （验证模板）
│   ├── composition.md              # Composition templates （组合模板）
│   ├── emergence.md                # Emergence templates （涌现模板）
│   ├── quantum_interpretation.md   # Quantum semantics templates （量子语义模板）
│   ├── unified_field_reasoning.md  # Unified field templates （统一场模板）
│   ├── meta_recursive_reasoning.md # Self-improvement templates （自我改进模板）
│   ├── interpretability_scaffolding.md # Transparency templates （透明度模板）
│   ├── collaborative_co_evolution.md # Human-AI templates （人机协作模板）
│   └── cross_modal_integration.md  # Multi-modal templates （多模态模板）
├── cognitive-programs/             # Executable cognitive processes （可执行认知过程）
│   ├── basic-programs.md           # Fundamental programs （基础程序）
│   ├── advanced-programs.md        # Complex programs （复杂程序）
│   ├── program-library.py          # Program collection （程序集合）
│   ├── program-examples.ipynb      # Program demonstrations （程序演示）
│   ├── emergence-programs.md       # Emergence programs （涌现程序）
│   ├── quantum_semantic_programs.md # Quantum semantics programs （量子语义程序）
│   ├── unified_field_programs.md   # Unified field programs （统一场程序）
│   ├── meta_recursive_programs.md  # Self-improvement programs （自我改进程序）
│   ├── interpretability_programs.md # Transparency programs （透明度程序）
│   ├── collaborative_evolution_programs.md # Human-AI programs （人机协作程序）
│   └── cross_modal_programs.md     # Multi-modal programs （多模态程序）
├── cognitive-schemas/              # Knowledge representation structures （知识表示结构）
│   ├── user-schemas.md             # User modeling schemas （用户建模模式）
│   ├── domain-schemas.md           # Domain knowledge schemas （领域知识模式）
│   ├── task-schemas.md             # Task representation schemas （任务表示模式）
│   ├── schema-library.yaml         # Schema collection （模式集合）
│   ├── field-schemas.md            # Field theory schemas （场论模式）
│   ├── quantum_schemas.md          # Quantum semantics schemas （量子语义模式）
│   ├── unified_schemas.md          # Unified field schemas （统一场模式）
│   ├── meta_recursive_schemas.md   # Self-improvement schemas （自我改进模式）
│   ├── interpretability_schemas.md # Transparency schemas （透明度模式）
│   ├── collaborative_schemas.md    # Human-AI schemas （人机协作模式）
│   └── cross_modal_schemas.md      # Multi-modal schemas （多模态模式）
├── cognitive-architectures/        # System-level frameworks （系统级框架）
│   ├── solver-architecture.md      # Problem-solving architecture （问题解决架构）
│   ├── tutor-architecture.md       # Educational architecture （教育架构）
│   ├── research-architecture.md    # Research assistant architecture （研究助理架构）
│   ├── architecture-examples.py    # Architecture demonstrations （架构演示）
│   ├── field-architecture.md       # Field theory architecture （场论架构）
│   ├── quantum_architecture.md     # Quantum semantics architecture （量子语义架构）
│   ├── unified_architecture.md     # Unified field architecture （统一场架构）
│   ├── meta_recursive_architecture.md # Self-improvement architecture （自我改进架构）
│   ├── interpretability_architecture.md # Transparency architecture （透明度架构）
│   ├── collaborative_architecture.md # Human-AI architecture （人机协作架构）
│   └── cross_modal_architecture.md # Multi-modal architecture （多模态架构）
├── integration/                    # Integration with other systems （与其他系统集成）
│   ├── with-rag.md                 # Retrieval integration （检索集成）
│   ├── with-memory.md              # Memory system integration （记忆系统集成）
│   ├── with-agents.md              # Agent system integration （智能体系统集成）
│   ├── evaluation-metrics.md       # Evaluation methods （评估方法）
│   ├── with-fields.md              # Field theory integration （场论集成）
│   ├── with-quantum.md             # Quantum semantics integration （量子语义集成）
│   ├── with-unified.md             # Unified field integration （统一场集成）
│   ├── with-meta-recursion.md      # Self-improvement integration （自我改进集成）
│   ├── with-interpretability.md    # Transparency integration （透明度集成）
│   ├── with-collaboration.md       # Human-AI integration （人机协作集成）
│   └── with-cross-modal.md         # Multi-modal integration （多模态集成）
└── meta-cognition/                 # Meta-cognitive capabilities （元认知能力）
    ├── self-reflection.md          # Self-analysis systems （自我分析系统）
    ├── recursive-improvement.md    # Self-enhancement methods （自我增强方法）
    ├── meta-awareness.md           # System self-awareness （系统自我意识）
    ├── attribution-engines.md      # Causal attribution systems （因果归因系统）
    ├── symbolic-echo-processing.md # Symbolic pattern processing （符号模式处理）
    ├── meta-interpretability.md    # Meta-level transparency （元级透明度）
    ├── meta-collaboration.md       # Meta-level human-AI partnership （元级人机协作）
    └── meta-modal-integration.md   # Meta-level modal integration （元级模态集成）
```
## Why Cognitive Tools Matter （认知工具为何重要）

Research has shown that structuring reasoning with cognitive tools can dramatically improve model performance:
研究表明，使用认知工具构建推理可以显著提高模型性能：

- **Performance**: Up to 16.6% improvement on mathematical reasoning benchmarks
  **性能**：在数学推理基准测试中性能提升高达 16.6%
- **Reliability**: Significant reduction in reasoning errors and hallucinations
  **可靠性**：显著减少推理错误和幻觉
- **Efficiency**: Better results with fewer total tokens
  **效率**：用更少的总令牌获得更好的结果
- **Flexibility**: Applicable across domains from mathematics to creative writing
  **灵活性**：适用于从数学到创意写作的各个领域

## Quick Start （快速入门）

To use a cognitive tool, choose a template from `cognitive-templates/` that matches your task:
要使用认知工具，请从 `cognitive-templates/` 中选择与您的任务匹配的模板：

```python
# Example: Using the "understand_question" cognitive tool
# （示例：使用“understand_question”认知工具）
from cognitive_tools.templates import understand_question

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
understanding = llm.generate(understand_question(problem))
print(understanding)
```

For more complex reasoning, use structured prompt programs from `cognitive-programs/`:
对于更复杂的推理，请使用 `cognitive-programs/` 中的结构化提示程序：

```python
# Example: Using a multi-step reasoning program
# （示例：使用多步推理程序）
from cognitive_tools.programs import solve_math_problem

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
solution = solve_math_problem(problem, llm=my_llm_interface)
print(solution.steps)  # View step-by-step reasoning （查看分步推理）
print(solution.answer)  # View final answer （查看最终答案）
```

## Directory Structure （目录结构）

- `cognitive-templates/`: Reusable templates for different reasoning operations
  `cognitive-templates/`：用于不同推理操作的可复用模板
- `cognitive-programs/`: Structured prompt programs with code-like patterns
  `cognitive-programs/`：具有类代码模式的结构化提示程序
- `cognitive-schemas/`: Knowledge representation formats for different domains
  `cognitive-schemas/`：用于不同领域的知识表示格式
- `cognitive-architectures/`: Complete reasoning systems combining multiple tools
  `cognitive-architectures/`：结合多种工具的完整推理系统
- `integration/`: Guides for integrating with other components (RAG, memory, etc.)
  `integration/`：与其他组件（RAG、记忆等）集成的指南

## Learning Path （学习路径）

1. **Start with templates**: Learn the basic cognitive operations
   **从模板开始**：学习基本的认知操作
2. **Explore programs**: See how operations can be combined into reasoning flows
   **探索程序**：了解如何将操作组合成推理流程
3. **Study schemas**: Understand how to structure knowledge effectively
   **研究模式**：了解如何有效地构建知识
4. **Master architectures**: Build complete reasoning systems
   **掌握架构**：构建完整的推理系统
5. **Integrate components**: Combine with RAG, memory, and other context engineering components
   **集成组件**：与 RAG、记忆和其他上下文工程组件相结合

## Measuring Effectiveness （衡量有效性）

Always measure the impact of cognitive tools on your specific tasks:
始终衡量认知工具对您特定任务的影响：

```python
# Example: Measuring performance improvement
# （示例：衡量性能改进）
from cognitive_tools.evaluation import measure_reasoning_quality

baseline_score = measure_reasoning_quality(problem, baseline_prompt)
tool_score = measure_reasoning_quality(problem, cognitive_tool_prompt)

improvement = (tool_score / baseline_score - 1) * 100
print(f"Cognitive tool improved performance by {improvement:.1f}%")
```

## Research Foundation （研究基础）

These tools are based on research from:
这些工具基于以下研究：

- Brown et al. (2025): "Eliciting Reasoning in Language Models with Cognitive Tools"
  Brown 等人（2025）：“用认知工具引发语言模型中的推理”
- Wei et al. (2023): "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
  Wei 等人（2023）：“思维链提示引发大型语言模型中的推理”
- Huang et al. (2022): "Inner Monologue: Embodying Knowledge and Reasoning in Language Models"
  Huang 等人（2022）：“内心独白：在语言模型中体现知识和推理”

## Contributing （贡献）

Have a new cognitive tool pattern that works well? See [CONTRIBUTING.md](../../.github/CONTRIBUTING.md) for guidelines on submitting your templates, programs, or architectures.
有一个行之有效的新认知工具模式吗？有关提交模板、程序或架构的指南，请参阅 [CONTRIBUTING.md](../../.github/CONTRIBUTING.md)。

## Next Steps （后续步骤）

- See [understanding.md](./cognitive-templates/understanding.md) for basic comprehension tools
  有关基本理解工具，请参阅 [understanding.md](./cognitive-templates/understanding.md)
- Try [basic-programs.md](./cognitive-programs/basic-programs.md) for fundamental program structures
  有关基本程序结构，请尝试 [basic-programs.md](./cognitive-programs/basic-programs.md)
- Explore [solver-architecture.md](./cognitive-architectures/solver-architecture.md) for a complete problem-solving system
  有关完整的问题解决系统，请探索 [solver-architecture.md](./cognitive-architectures/solver-architecture.md)