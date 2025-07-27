# Context-Engineering – Structural Overview （上下文工程 – 结构概述）
_A pragmatic, first-principles handbook for the next generation of LLM orchestration_
_一份务实的、第一性原理的下一代大型语言模型编排手册_

> **Why this repo exists**  
> Prompt engineering = thinking about **what** you say.  
> **Context engineering** = thinking about **everything else** the model sees.  
> Our goal is to teach that "everything else" from the ground-up, with humility and a bias toward simple, working code.
> 
> As models evolve, so does our approach: from discrete tokens to continuous fields, from static prompts to resonant patterns.

> **本仓库存在的原因**  
> 提示工程 = 思考你**说什么**。  
> **上下文工程** = 思考模型看到的**其他一切**。  
> 我们的目标是从头开始教授“其他一切”，以谦逊的态度和对简单、可工作的代码的偏好。
> 
> 随着模型的发展，我们的方法也在演变：从离散的令牌到连续的场，从静态的提示到共振的模式。

---

## 1. Map of the Territory （领域地图）

| Folder | Role (Plain English) | First-Principles Metaphor |
|--------|----------------------|---------------------------|
| `00_foundations` | Theory & intuition. Tiny, self-contained readings. | Atoms → Molecules → Cells → Organs → Neural Systems → Fields |
| `10_guides_zero_to_hero` | Interactive guides you **run**, tweak, break. | Chemistry set |
| `20_templates` | Drop-in snippets you can copy/paste. | Lego bricks |
| `30_examples` | End-to-end mini-apps, each harder than the last. | Model organisms |
| `40_reference` | Deeper dives & evaluation cookbooks. | Textbook appendix |
| `50_contrib` | Space for community pull requests. | Open lab bench |
| `60_protocols` | Protocol shells, schemas, and frameworks. | DNA sequences |
| `70_agents` | Self-contained agent demos using protocols. | Stem-cell cultures |
| `80_field_integration` | End-to-end projects with field protocols. | Whole organisms |
| `cognitive-tools` | Advanced cognitive frameworks and architectures. | Extended neural systems |

| 文件夹 | 角色（通俗易懂的英语） | 第一性原理隐喻 |
|--------|----------------------|---------------------------|
| `00_foundations` | 理论与直觉。简短、独立的读物。 | 原子 → 分子 → 细胞 → 器官 → 神经系统 → 场 |
| `10_guides_zero_to_hero` | 你可以**运行**、调整、破坏的交互式指南。 | 化学实验套装 |
| `20_templates` | 你可以复制/粘贴的即用型代码片段。 | 乐高积木 |
| `30_examples` | 端到端的迷你应用，难度递增。 | 模型生物 |
| `40_reference` | 深入探讨和评估手册。 | 教科书附录 |
| `50_contrib` | 社区拉取请求的空间。 | 开放式实验台 |
| `60_protocols` | 协议外壳、模式和框架。 | DNA 序列 |
| `70_agents` | 使用协议的独立代理演示。 | 干细胞培养 |
| `80_field_integration` | 使用场协议的端到端项目。 | 完整生物体 |
| `cognitive-tools` | 高级认知框架和架构。 | 扩展神经系统 |

---

## 2. Learning Path (0 → Zero → Hero) （学习路径（0 → 从零到英雄））

### Foundations (Understanding the Basics) （基础（理解基础））

1. **Skim `README.md` (2 min)**  
   See what "context" even means beyond prompts.
   了解“上下文”在提示之外的含义。

2. **Read `00_foundations/01_atoms_prompting.md` (5 min)**  
   *Atoms*: a single instruction / example.  
   Why atoms alone often underperform.
   *原子*：单个指令/示例。  
   为什么仅有原子通常表现不佳。

3. **Continue through the biological metaphor chain:**  
   **继续学习生物学隐喻链：**
   - `02_molecules_context.md`: Few-shot packs and examples
     `02_molecules_context.md`：少样本包和示例
   - `03_cells_memory.md`: Memory & logs for persistence
     `03_cells_memory.md`：用于持久化的记忆和日志
   - `04_organs_applications.md`: Multi-step control flows and orchestration
     `04_organs_applications.md`：多步控制流和编排
   - `05_cognitive_tools.md`: Mental model extensions for reasoning
     `05_cognitive_tools.md`：用于推理的心智模型扩展
   - `06_advanced_applications.md`: Real-world implementations
     `06_advanced_applications.md`：实际应用
   - `07_prompt_programming.md`: Code-like reasoning patterns
     `07_prompt_programming.md`：类代码推理模式
   - `08_neural_fields_foundations.md`: Context as continuous fields
     `08_neural_fields_foundations.md`：作为连续场的上下文
   - `09_persistence_and_resonance.md`: Field dynamics and attractors
     `09_persistence_and_resonance.md`：场动力学和吸引子
   - `10_field_orchestration.md`: Coordinating multiple fields
     `10_field_orchestration.md`：协调多个场

### Hands-On Practice (Learning by Doing) （动手实践（边做边学））

4. **Open `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   Run, modify, observe token counts.  
   Notebook cells highlight **why** each extra line helps (or hurts).
   **打开 `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   运行、修改、观察令牌计数。  
   笔记本单元格突出显示了**为什么**每一行额外的代码都有帮助（或有害）。

5. **Experiment through progressive notebooks:**
   **通过渐进式笔记本进行实验：**
   - Basic context manipulation
     基本上下文操作
   - Control flow and reasoning patterns
     控制流和推理模式
   - Retrieval augmentation strategies
     检索增强策略
   - Prompt programming techniques
     提示编程技术
   - Schema design principles
     模式设计原则
   - Recursive context patterns
     递归上下文模式
   - Neural field implementation
     神经场实现

### Applied Skills (Building Real Solutions) （应用技能（构建真实解决方案））

6. **Copy a template from `20_templates/`**  
   Use as starting points for your projects:
   **从 `20_templates/` 复制一个模板**  
   用作您项目的起点：
   - `minimal_context.yaml` for basic projects
     `minimal_context.yaml` 用于基础项目
   - `control_loop.py` for interactive systems
     `control_loop.py` 用于交互式系统
   - `scoring_functions.py` for evaluation
     `scoring_functions.py` 用于评估
   - `prompt_program_template.py` for reasoning tasks
     `prompt_program_template.py` 用于推理任务
   - `schema_template.yaml` for structured data
     `schema_template.yaml` 用于结构化数据
   - `recursive_framework.py` for self-improving systems
     `recursive_framework.py` 用于自我改进系统
   - `neural_field_context.yaml` for field-based approaches
     `neural_field_context.yaml` 用于基于场的方法

7. **Study examples in `30_examples/`**  
   See complete implementations of progressively complex systems:
   **研究 `30_examples/` 中的示例**  
   查看逐步复杂的系统的完整实现：
   - Basic conversational agents
     基础对话代理
   - Data annotation systems
     数据标注系统
   - Multi-agent orchestration
     多智能体编排
   - Cognitive assistants
     认知助手
   - RAG implementations
     RAG 实现
   - Neural field orchestrators
     神经场编排器

### Advanced Topics (Mastering the Craft) （高级主题（精通技艺））

8. **Explore cognitive tools and protocols:**
   **探索认知工具和协议：**
   - Advanced reasoning frameworks in `cognitive-tools/`
     `cognitive-tools/` 中的高级推理框架
   - Protocol shells and schemas in `60_protocols/`
     `60_protocols/` 中的协议外壳和模式
   - Agent demonstrations in `70_agents/`
     `70_agents/` 中的代理演示
   - Complete field integration projects in `80_field_integration/`
     `80_field_integration/` 中的完整场集成项目

9. **Contribute back to the community:**
   **回馈社区：**
   - Review the contribution guidelines in `50_contrib/README.md`
     查看 `50_contrib/README.md` 中的贡献指南
   - Check the evaluation criteria in `40_reference/eval_checklist.md`
     检查 `40_reference/eval_checklist.md` 中的评估标准
   - Open a PR with your improvements or extensions
     用您的改进或扩展打开一个拉取请求

---

## 3. Biological Metaphor Evolution （生物学隐喻演化）

Our repository is organized around an extended biological metaphor that helps make abstract concepts concrete and shows how simple components build into complex systems:
我们的存储库围绕一个扩展的生物学隐喻进行组织，这有助于将抽象概念具体化，并展示简单的组件如何构建成复杂的系统：

```
                                   ┌───────────────────┐
                                   │  Neural Fields    │  08_neural_fields_foundations.md
                                   │  (Continuous      │  09_persistence_and_resonance.md
                                   │   Context Medium) │  10_field_orchestration.md
                                   │  （神经场（连续上下文介质））│
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                                   ┌───────┴───────────┐
                                   │ Neurobiological   │  05_cognitive_tools.md
                                   │ Systems           │  06_advanced_applications.md
                                   │ (Cognitive Tools) │  07_prompt_programming.md
                                   │ （神经生物学系统（认知工具））│
                                   └───────┬───────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Organs            │  04_organs_applications.md
                             │  (Multi-Agent Systems)    │
                             │  （器官（多智能体系统））  │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Cells             │  03_cells_memory.md
                             │   (Memory Systems)        │
                             │   （细胞（记忆系统））      │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │       Molecules           │  02_molecules_context.md
                             │   (Few-Shot Examples)     │
                             │   （分子（少样本示例））    │
                             └─────────────┬─────────────┘
                                           │
                                           ▲
                                           │
                             ┌─────────────┴─────────────┐
                             │         Atoms             │  01_atoms_prompting.md
                             │    (Single Prompts)       │
                             │    （原子（单个提示））      │
                             └───────────────────────────┘
```

This evolution follows the natural progression of complexity in biological systems and mirrors the development of increasingly sophisticated context engineering approaches.
这种演变遵循生物系统中复杂性的自然演进，并反映了日益复杂的上下文工程方法的发展。

---

## 4. Advanced Context Frameworks （高级上下文框架）

### Protocol Shell Framework （协议外壳框架）

Protocols provide structured shells for orchestrating complex context operations. Found in the `60_protocols/` directory:
协议为编排复杂的上下文操作提供了结构化的外壳。位于 `60_protocols/` 目录中：

```
/recursive.field{
    intent="Define field properties and operations",
    （意图="定义场属性和操作"）
    input={
        field_state=<current_state>,
        new_information=<incoming_data>
    },
    process=[
        /field.measure{resonance, coherence, entropy},
        /pattern.detect{across="field_state"},
        /attractor.form{where="pattern_strength > threshold"},
        /field.evolve{with="new_information"}
    ],
    output={
        updated_field=<new_state>,
        metrics={resonance_score, coherence_delta}
    }
}
```

These protocol shells enable:
这些协议外壳能够：
- Declarative definition of context operations
  上下文操作的声明性定义
- Recursive self-improvement patterns
  递归的自我改进模式
- Field-based context manipulation
  基于场的上下文操作
- Auditability through explicit process steps
  通过明确的过程步骤实现可审计性

### Cognitive Tool Framework （认知工具框架）

Cognitive tools provide reusable reasoning patterns that extend model capabilities. Found in the `cognitive-tools/` directory:
认知工具提供了可复用的推理模式，扩展了模型的能力。位于 `cognitive-tools/` 目录中：

```
cognitive-tools/
├── cognitive-templates/     # Pattern templates for different reasoning modes （不同推理模式的模式模板）
├── cognitive-programs/      # Structured prompt programs with code-like patterns （具有类代码模式的结构化提示程序）
├── cognitive-schemas/       # Knowledge representation formats （知识表示格式）
├── cognitive-architectures/ # Complete reasoning systems （完整的推理系统）
└── integration/            # Guides for integrating with other components （与其他组件集成的指南）
```

This framework supports:
该框架支持：
- Modular reasoning components
  模块化推理组件
- Domain-specific reasoning patterns
  特定领域的推理模式
- Integration with retrieval and memory systems
  与检索和记忆系统的集成
- Evaluation metrics for reasoning quality
  推理质量的评估指标

### Neural Field Framework （神经场框架）

Neural fields represent context as a continuous medium rather than discrete tokens. Implemented across:
神经场将上下文表示为连续介质，而非离散的令牌。实现于：

```
00_foundations/08_neural_fields_foundations.md  # Conceptual foundation （概念基础）
00_foundations/09_persistence_and_resonance.md  # Field dynamics （场动力学）
00_foundations/10_field_orchestration.md        # Multi-field coordination （多场协调）
20_templates/neural_field_context.yaml          # Implementation template （实现模板）
30_examples/05_neural_field_orchestrator/       # Complete example （完整示例）
```

Key concepts include:
关键概念包括：
- Context as a continuous semantic field
  作为连续语义场的上下文
- Information persistence through resonance
  通过共振实现信息持久性
- Attractor formation and dynamics
  吸引子形成与动力学
- Field orchestration for complex tasks
  用于复杂任务的场编排

---

## 5. Quiet Karpathy Guidelines (Style DNA) （Quiet Karpathy 指南（风格 DNA））

*Keep it atomic → build up.*  
1. **Minimal first pass** – start with the smallest viable context.  
2. **Iterative add-on** – add only what the model demonstrably lacks.  
3. **Measure everything** – token cost, latency, quality score, field resonance.  
4. **Delete ruthlessly** – pruning beats padding.  
5. **Code > slides** – every concept has a runnable cell.
6. **Recursive thinking** – contexts that evolve themselves.

*保持原子性 → 逐步构建。*  
1. **最小化初稿** – 从最小的可行上下文开始。  
2. **迭代添加** – 只添加模型明显缺乏的内容。  
3. **测量一切** – 令牌成本、延迟、质量得分、场共振。  
4. **无情删除** – 修剪胜于填充。  
5. **代码 > 幻灯片** – 每个概念都有一个可运行的单元格。
6. **递归思维** – 自我演化的上下文。

---

## 6. Repository Structure in Detail （存储库结构详解）

```
Context-Engineering/
├── LICENSE                          # MIT license （MIT 许可证）
├── README.md                        # Quick-start overview （快速入门概述）
├── structure.md                     # This structural map （此结构图）
├── context.json                     # Original schema configuration （原始模式配置）
├── context_v2.json                  # Extended schema with field protocols （带有场协议的扩展模式）
│
├── 00_foundations/                  # First-principles theory （第一性原理理论）
│   ├── 01_atoms_prompting.md        # Atomic instruction units （原子指令单元）
│   ├── 02_molecules_context.md      # Few-shot examples/context （少样本示例/上下文）
│   ├── 03_cells_memory.md           # Stateful conversation layers （有状态对话层）
│   ├── 04_organs_applications.md    # Multi-step control flows （多步控制流）
│   ├── 05_cognitive_tools.md        # Mental model extensions （心智模型扩展）
│   ├── 06_advanced_applications.md  # Real-world implementations （实际应用）
│   ├── 07_prompt_programming.md     # Code-like reasoning patterns （类代码推理模式）
│   ├── 08_neural_fields_foundations.md # Context as continuous fields （作为连续场的上下文）
│   ├── 09_persistence_and_resonance.md # Field dynamics and attractors （场动力学和吸引子）
│   └── 10_field_orchestration.md    # Coordinating multiple fields （协调多个场）
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials （动手教程）
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments （最小提示实验）
│   ├── 02_expand_context.ipynb      # Context expansion techniques （上下文扩展技术）
│   ├── 03_control_loops.ipynb       # Flow control mechanisms （流控制机制）
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns （检索增强模式）
│   ├── 05_prompt_programs.ipynb     # Structured reasoning programs （结构化推理程序）
│   ├── 06_schema_design.ipynb       # Schema creation patterns （模式创建模式）
│   ├── 07_recursive_patterns.ipynb  # Self-referential contexts （自引用上下文）
│   └── 08_neural_fields.ipynb       # Working with field-based contexts （使用基于场的上下文）
│
├── 20_templates/                    # Reusable components （可复用组件）
│   ├── minimal_context.yaml         # Base context structure （基础上下文结构）
│   ├── control_loop.py              # Orchestration template （编排模板）
│   ├── scoring_functions.py         # Evaluation metrics （评估指标）
│   ├── prompt_program_template.py   # Program structure template （程序结构模板）
│   ├── schema_template.yaml         # Schema definition template （模式定义模板）
│   ├── recursive_framework.py       # Recursive context template （递归上下文模板）
│   ├── neural_field_context.yaml    # Field-based context template （基于场的上下文模板）
│   ├── field_resonance_measure.py   # Field property measurement （场属性测量）
│   └── context_audit.py             # Context analysis tool （上下文分析工具）
│
├── 30_examples/                     # Practical implementations （实际应用）
│   ├── 00_toy_chatbot/              # Simple conversation agent （简单对话代理）
│   ├── 01_data_annotator/           # Data labeling system （数据标注系统）
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system （代理协作系统）
│   ├── 03_cognitive_assistant/      # Advanced reasoning assistant （高级推理助手）
│   ├── 04_rag_minimal/              # Minimal RAG implementation （最小 RAG 实现）
│   └── 05_neural_field_orchestrator/ # Field-based orchestration （基于场的编排）
│
├── 40_reference/                    # Deep-dive documentation （深度文档）
│   ├── token_budgeting.md           # Token optimization strategies （令牌优化策略）
│   ├── retrieval_indexing.md        # Retrieval system design （检索系统设计）
│   ├── eval_checklist.md            # PR evaluation criteria （PR 评估标准）
│   ├── cognitive_patterns.md        # Reasoning pattern catalog （推理模式目录）
│   ├── schema_cookbook.md           # Schema pattern collection （模式模式集合）
│   ├── neural_field_theory.md       # Comprehensive field theory （综合场论）
│   ├── symbolic_residue_guide.md    # Guide to residue tracking （残留追踪指南）
│   └── protocol_reference.md        # Protocol shell reference （协议外壳参考）
│
├── 50_contrib/                      # Community contributions （社区贡献）
│   └── README.md                    # Contribution guidelines （贡献指南）
│
├── 60_protocols/                    # Protocol shells and frameworks （协议外壳和框架）
│   ├── README.md                    # Protocol overview （协议概述）
│   ├── shells/                      # Protocol shell definitions （协议外壳定义）
│   │   ├── attractor.co.emerge.shell      # Attractor co-emergence （吸引子共现）
│   │   ├── recursive.emergence.shell      # Recursive field emergence （递归场涌现）
│   │   ├── recursive.memory.attractor.shell # Memory persistence （记忆持久性）
│   │   └── field.resonance.scaffold.shell  # Field resonance （场共振）
│   ├── digests/                     # Simplified protocol documentation （简化协议文档）
│   └── schemas/                     # Protocol schemas （协议模式）
│       ├── fractalRepoContext.v1.json     # Repository context （存储库上下文）
│       ├── fractalConsciousnessField.v1.json # Field schema （场模式）
│       └── protocolShell.v1.json           # Shell schema （外壳模式）
│
├── 70_agents/                       # Agent demonstrations （代理演示）
│   ├── README.md                    # Agent overview （代理概述）
│   ├── 01_residue_scanner/          # Symbolic residue detection （符号残留检测）
│   └── 02_self_repair_loop/         # Self-repair protocol （自我修复协议）
│
├── 80_field_integration/            # Complete field projects （完整的场项目）
│   ├── README.md                    # Integration overview （集成概述）
│   ├── 00_protocol_ide_helper/      # Protocol development tools （协议开发工具）
│   └── 01_context_engineering_assistant/ # Field-based assistant （基于场的助手）
│
├── cognitive-tools/                 # Advanced cognitive framework （高级认知框架）
│   ├── README.md                    # Overview and quick-start guide （概述和快速入门指南）
│   ├── cognitive-templates/         # Templates for reasoning （推理模板）
│   │   ├── understanding.md         # Comprehension operations （理解操作）
│   │   ├── reasoning.md             # Analytical operations （分析操作）
│   │   ├── verification.md          # Checking and validation （检查和验证）
│   │   └── composition.md           # Combining multiple tools （组合多个工具）
│   │
│   ├── cognitive-programs/          # Structured prompt programs （结构化提示程序）
│   │   ├── basic-programs.md        # Fundamental program structures （基本程序结构）
│   │   ├── advanced-programs.md     # Complex program architectures （复杂程序架构）
│   │   ├── program-library.py       # Python implementations （Python 实现）
│   │   └── program-examples.ipynb   # Interactive examples （交互式示例）
│   │
│   ├── cognitive-schemas/           # Knowledge representations （知识表示）
│   │   ├── user-schemas.md          # User information schemas （用户信息模式）
│   │   ├── domain-schemas.md        # Domain knowledge schemas （领域知识模式）
│   │   ├── task-schemas.md          # Reasoning task schemas （推理任务模式）
│   │   └── schema-library.yaml      # Reusable schema library （可复用模式库）
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems （完整的推理系统）
│   │   ├── solver-architecture.md   # Problem-solving systems （问题解决系统）
│   │   ├── tutor-architecture.md    # Educational systems （教育系统）
│   │   ├── research-architecture.md # Information synthesis （信息综合）
│   │   └── architecture-examples.py # Implementation examples （实现示例）
│   │
│   └── integration/                 # Integration patterns （集成模式）
│       ├── with-rag.md              # Integration with retrieval （与检索集成）
│       ├── with-memory.md           # Integration with memory （与记忆集成）
│       ├── with-agents.md           # Integration with agents （与代理集成）
│       └── evaluation-metrics.md    # Effectiveness measurement （有效性测量）
│
└── .github/                         # GitHub configuration （GitHub 配置）
    ├── CONTRIBUTING.md              # Contribution guidelines （贡献指南）
    ├── workflows/ci.yml             # CI pipeline configuration （CI 管道配置）
    ├── workflows/eval.yml           # Evaluation automation （评估自动化）
    └── workflows/protocol_tests.yml # Protocol testing （协议测试）
```

---

## 7. How to Contribute （如何贡献）

Open a PR in `50_contrib/`.  
Checklist lives in `40_reference/eval_checklist.md`—run it before submitting.
在 `50_contrib/` 中打开一个拉取请求。  
清单位于 `40_reference/eval_checklist.md`——在提交前运行它。

When contributing:
贡献时：
1. Follow the Karpathy style guidelines
   遵循 Karpathy 风格指南
2. Include runnable code examples
   包含可运行的代码示例
3. Measure token usage and performance
   测量令牌使用情况和性能
4. Maintain the biological metaphor consistency
   保持生物学隐喻的一致性
5. Add tests for any new functionality
   为任何新功能添加测试

---

## 8. License & Attribution （许可证和归属）

MIT. No gate-keeping: copy, remix, redistribute.  
A respectful nod to Andrej Karpathy for coining the framing.  
All errors are ours; improvements are welcome.
麻省理工学院许可证。没有门槛：复制、混搭、重新分发。  
向 Andrej Karpathy 致敬，感谢他创造了这个框架。  
所有错误都是我们的；欢迎改进。