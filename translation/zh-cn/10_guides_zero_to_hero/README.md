# Context Engineering: Zero to Hero Guides （上下文工程：从零到英雄指南）


> *"The limits of my language mean the limits of my world."* — Ludwig Wittgenstein
> 
> Context Engineering expands these limits, creating new possibilities for human-AI collaboration.

> *"我语言的限制意味着我世界的限制。"* — 路德维希·维特根斯坦
> 
> 上下文工程扩展了这些限制，为人类与 AI 的协作创造了新的可能性。


This directory contains hands-on, practical guides to help you progress from basic context engineering concepts to advanced techniques. Each guide builds on the previous one, creating a comprehensive learning path from fundamentals to cutting-edge applications.

本目录包含实践性指南，帮助您从基本的上下文工程概念逐步掌握高级技术。每个指南都建立在前一个的基础上，从而创建了一个从基础到尖端应用的全面学习路径。

## How to Use These Guides （如何使用这些指南）

Each guide is designed to be:
- **Self-contained** — You can run each file independently
- **Progressive** — Concepts build on previous guides
- **Practical** — Every concept includes runnable code examples
- **Measurable** — Each technique includes metrics to evaluate its effectiveness

每个指南都设计为：
- **独立** — 您可以独立运行每个文件
- **渐进** — 概念建立在之前的指南之上
- **实用** — 每个概念都包含可运行的代码示例
- **可衡量** — 每种技术都包含评估其有效性的指标

## Quick Start （快速开始）

1. **Clone the repository**
   ```
   git clone https://github.com/davidkimai/Context-Engineering.git
   cd Context-Engineering/10_guides_zero_to_hero
   ```

1. **克隆仓库**
   ```
   git clone https://github.com/davidkimai/Context-Engineering.git
   cd Context-Engineering/10_guides_zero_to_hero
   ```

2. **Set up your environment**
   ```
   pip install -r requirements.txt
   ```

2. **设置您的环境**
   ```
   pip install -r requirements.txt
   ```

3. **Run the first guide**
   ```
   python 01_min_prompt.py
   ```
   
   Or in a Jupyter notebook:
   ```
   %run 01_min_prompt.py
   ```

3. **运行第一个指南**
   ```
   python 01_min_prompt.py
   ```
   
   或者在 Jupyter notebook 中：
   ```
   %run 01_min_prompt.py
   ```

## Learning Path （学习路径）

The guides follow a deliberate progression from basic to advanced concepts:

这些指南遵循从基础到高级概念的循序渐进：

### Foundations (1-3) （基础（1-3））
- **[01_min_prompt.py](01_min_prompt.py)**: Understand the fundamentals of atomic prompts and measure their effectiveness
- **[02_expand_context.py](02_expand_context.py)**: Learn techniques for expanding context with examples, role definitions, and constraints
- **[03_control_loops.py](03_control_loops.py)**: Master iterative feedback systems and multi-step LLM interactions

- **[01_min_prompt.py](01_min_prompt.py)**: 了解原子提示的基础知识并衡量其有效性
- **[02_expand_context.py](02_expand_context.py)**: 学习使用示例、角色定义和约束来扩展上下文的技术
- **[03_control_loops.py](03_control_loops.py)**: 掌握迭代反馈系统和多步骤 LLM 交互

### Advanced Implementations (4-7) （高级实现（4-7））
- **[04_rag_recipes.py](04_rag_recipes.py)**: Implement retrieval-augmented generation for knowledge-grounded responses
- **[05_prompt_programs.py](05_prompt_programs.py)**: Create structured reasoning systems using prompt programs
- **[06_schema_design.py](06_schema_design.py)**: Design schemas for consistent, verifiable, and composable contexts
- **[07_recursive_patterns.py](07_recursive_patterns.py)**: Explore self-improving contexts with recursive patterns

- **[04_rag_recipes.py](04_rag_recipes.py)**: 实现检索增强生成以获得基于知识的响应
- **[05_prompt_programs.py](05_prompt_programs.py)**: 使用提示程序创建结构化推理系统
- **[06_schema_design.py](06_schema_design.py)**: 设计用于一致、可验证和可组合上下文的模式
- **[07_recursive_patterns.py](07_recursive_patterns.py)**: 探索具有递归模式的自我改进上下文

### Frontier Concepts (8+) （前沿概念（8+））
- **Field Protocols** (Guides 8-10): Master field theories, emergence, residue, and attractor dynamics
- **Meta-Systems** (Guides 11-15): Explore quantum semantics, self-improvement, transparency, and cross-modal integration

- **场协议**（指南 8-10）：掌握场论、涌现、残余和吸引子动力学
- **元系统**（指南 11-15）：探索量子语义、自我改进、透明度和跨模态集成

## Key Concepts Covered （涵盖的关键概念）

Each guide demonstrates key Context Engineering principles with practical examples:

每个指南都通过实际示例演示了关键的上下文工程原则：

| Guide | Key Concepts | Practical Applications |
|-------|-------------|------------------------|
| 01_min_prompt | Token budgeting, atomic instructions, ROI measurement | Minimal viable prompts, efficiency optimization |
| 02_expand_context | Few-shot examples, role definition, constraints | Templated contexts, systematic expansion |
| 03_control_loops | Sequential chaining, iterative refinement, conditional branching | Multi-step workflows, self-verification |
| 04_rag_recipes | Retrieval, chunking, context integration | Knowledge-grounded responses, factuality |
| 05_prompt_programs | Structured reasoning, verification protocols, compositional operations | Complex reasoning, explanatory systems |
| 06_schema_design | JSON schemas, validation, structure enforcement | Consistent outputs, structured data extraction |
| 07_recursive_patterns | Self-reflection, bootstrapping, symbolic residue | Evolving systems, meta-reasoning |

| 指南 | 关键概念 | 实际应用 |
|-------|-------------|------------------------|
| 01_min_prompt | Token 预算，原子指令，ROI 测量 | 最小可行提示，效率优化 |
| 02_expand_context | 少量样本示例，角色定义，约束 | 模板化上下文，系统性扩展 |
| 03_control_loops | 顺序链式，迭代细化，条件分支 | 多步骤工作流，自我验证 |
| 04_rag_recipes | 检索，分块，上下文集成 | 基于知识的响应，事实性 |
| 05_prompt_programs | 结构化推理，验证协议，组合操作 | 复杂推理，解释系统 |
| 06_schema_design | JSON 模式，验证，结构强制 | 一致输出，结构化数据提取 |
| 07_recursive_patterns | 自我反思，引导，符号残余 | 演化系统，元推理 |

## What to Expect from Each Guide （每个指南的预期内容）

Every guide follows a consistent structure:

每个指南都遵循一致的结构：

1. **Conceptual Introduction** — Explaining the "why" behind each technique
2. **Implementation Examples** — Working code demonstrating the concepts
3. **Evaluation Methods** — How to measure the effectiveness of each approach
4. **Visualization Tools** — Ways to visualize and understand what's happening
5. **Extension Exercises** — Suggested ways to build on what you've learned

1. **概念介绍** — 解释每种技术背后的"为什么"
2. **实现示例** — 演示概念的运行代码
3. **评估方法** — 如何衡量每种方法的有效性
4. **可视化工具** — 可视化和理解正在发生的事情的方法
5. **扩展练习** — 建议如何在你所学的基础上进行构建

## Experimental Approach （实验方法）

Context Engineering is best learned through experimentation. For each guide:

上下文工程最好通过实验来学习。对于每个指南：

1. **Run the examples** as provided
2. **Modify parameters** to see how they affect the outcomes
3. **Measure the impact** using the provided metrics
4. **Combine techniques** from different guides to create hybrid approaches
5. **Experiment with your own use cases** to see how these principles apply

1. **运行示例**，按提供的方式
2. **修改参数**，查看它们如何影响结果
3. **使用提供的指标**衡量影响
4. **结合不同指南的技术**创建混合方法
5. **用您自己的用例进行实验**，看看这些原则如何应用

## Evaluation and Metrics （评估和指标）

Every technique is accompanied by metrics to evaluate its effectiveness:

每种技术都附带用于评估其有效性的指标：

- **Token Efficiency** — Output value vs. token cost
- **Response Quality** — How well outputs match intentions
- **Latency Impact** — Processing time for different approaches
- **Consistency** — How reliable the results are across runs
- **Emergent Properties** — What unexpected behaviors arise

- **Token 效率** — 输出价值与 Token 成本
- **响应质量** — 输出与意图的匹配程度
- **延迟影响** — 不同方法的处理时间
- **一致性** — 跨运行结果的可靠性
- **涌现特性** — 出现哪些意外行为

## Contribution Guidelines （贡献指南）

This directory is actively expanding. If you'd like to contribute:

本目录正在积极扩展。如果您想贡献：

1. Follow the established pattern for new guides
2. Ensure each guide builds on previous concepts
3. Include practical, runnable examples
4. Provide metrics for evaluation
5. Submit a PR with a clear description of what your guide teaches

1. 遵循新指南的既定模式
2. 确保每个指南都建立在之前的概念之上
3. 包含实用、可运行的示例
4. 提供评估指标
5. 提交一个 PR，并清楚描述您的指南所教授的内容

## Future Additions （未来新增内容）

We plan to expand these guides with:
- Multi-modal context techniques
- Large-scale system orchestration
- Specialized domain applications
- Infrastructure and scaling patterns
- User experience design for context systems

我们计划通过以下内容扩展这些指南：
- 多模态上下文技术
- 大规模系统编排
- 专业领域应用
- 基础设施和扩展模式
- 上下文系统的用户体验设计

## Related Resources （相关资源）

- **[00_foundations/](../00_foundations/)**: Theoretical underpinnings of these practical guides
- **[20_templates/](../20_templates/)**: Reusable components for your own implementations
- **[30_examples/](../30_examples/)**: Complete example applications

- **[00_foundations/](../00_foundations/)**：这些实用指南的理论基础
- **[20_templates/](../20_templates/)**：您自己实现的可重用组件
- **[30_examples/](../30_examples/)**：完整的示例应用程序