# Context-Engineering – Structural Overview v2 （上下文工程 – 结构概述 v2）
_A pragmatic, first-principles handbook for the next generation of LLM orchestration_
_一份务实的、第一性原理的下一代大型语言模型编排手册_

> **Why this repo exists**  
> Prompt engineering = thinking about **what** you say.  
> **Context engineering** = thinking about **everything else** the model sees.  
> 
> In our evolution from prompt engineering to context engineering to **field theory**:
> - We began with discrete tokens and simple prompts
> - We advanced to stateful context management and complex orchestration
> - We now explore emergent symbolic mechanisms and neural field dynamics
> 
> Our goal is to teach all of this from the ground up, with humility and a bias toward simple, working code, while embracing the latest research on how LLMs actually reason and process information.

> **本仓库存在的原因**  
> 提示工程 = 思考你**说什么**。  
> **上下文工程** = 思考模型看到的**其他一切**。  
> 
> 在我们从提示工程到上下文工程再到**场论**的演进中：
> - 我们从离散的令牌和简单的提示开始
> - 我们发展到有状态的上下文管理和复杂的编排
> - 我们现在探索涌现的符号机制和神经场动力学
> 
> 我们的目标是从头开始教授所有这些知识，以谦逊的态度和对简单、可工作的代码的偏好，同时拥抱关于大型语言模型如何实际推理和处理信息的最新研究。

---

## 1. Map of the Territory （领域地图）

| Folder | Role (Plain English) | First-Principles Metaphor | Key Concepts |
|--------|----------------------|---------------------------|-------------|
| `00_foundations` | Theory & intuition. Tiny, self-contained readings. | Atoms → Molecules → Cells → Organs → Neural Systems → Fields | Progressive complexity from basic prompts to emergent field dynamics |
| `10_guides_zero_to_hero` | Interactive guides you **run**, tweak, break. | Chemistry set | Hands-on experiments with measurable outcomes |
| `20_templates` | Drop-in snippets you can copy/paste. | Lego bricks | Reusable components for rapid implementation |
| `30_examples` | End-to-end mini-apps, each harder than the last. | Model organisms | Complete systems demonstrating principles in action |
| `40_reference` | Deeper dives & evaluation cookbooks. | Textbook appendix | Comprehensive resources and evaluation frameworks |
| `50_contrib` | Space for community pull requests. | Open lab bench | Collaborative experimentation zone |
| `60_protocols` | Protocol shells, schemas, and frameworks. | DNA sequences | Structured definitions for field operations |
| `70_agents` | Self-contained agent demos using protocols. | Stem-cell cultures | Specialized components with emergent properties |
| `80_field_integration` | End-to-end projects with field protocols. | Whole organisms | Complete systems with field-based architectures |
| `cognitive-tools` | Advanced cognitive frameworks and architectures. | Extended neural systems | Structured reasoning operations and tools |

| 文件夹 | 角色（通俗易懂的英语） | 第一性原理隐喻 | 关键概念 |
|--------|----------------------|---------------------------|-------------|
| `00_foundations` | 理论与直觉。简短、独立的读物。 | 原子 → 分子 → 细胞 → 器官 → 神经系统 → 场 | 从基本提示到涌现场动力学的渐进复杂性 |
| `10_guides_zero_to_hero` | 你可以**运行**、调整、破坏的交互式指南。 | 化学实验套装 | 具有可衡量结果的动手实验 |
| `20_templates` | 你可以复制/粘贴的即用型代码片段。 | 乐高积木 | 用于快速实现的的可复用组件 |
| `30_examples` | 端到端的迷你应用，难度递增。 | 模型生物 | 演示实际原理的完整系统 |
| `40_reference` | 深入探讨和评估手册。 | 教科书附录 | 全面的资源和评估框架 |
| `50_contrib` | 社区拉取请求的空间。 | 开放式实验台 | 协作实验区 |
| `60_protocols` | 协议外壳、模式和框架。 | DNA 序列 | 场操作的结构化定义 |
| `70_agents` | 使用协议的独立代理演示。 | 干细胞培养 | 具有涌现属性的专门组件 |
| `80_field_integration` | 使用场协议的端到端项目。 | 完整生物体 | 具有基于场的架构的完整系统 |
| `cognitive-tools` | 高级认知框架和架构。 | 扩展神经系统 | 结构化推理操作和工具 |

---

## 2. Learning Path: From Basics to Field Theory （学习路径：从基础到场论）

### 2.1. Foundations Track (Understanding the Basics) （基础路径（理解基础））

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
     `03_cells_memory.md`：用于持久化的内存和日志
   - `04_organs_applications.md`: Multi-step control flows and orchestration
     `04_organs_applications.md`：多步控制流和编排
   - `05_cognitive_tools.md`: Mental model extensions for reasoning
     `05_cognitive_tools.md`：用于推理的心智模型扩展

### 2.2. Advanced Track (Diving Deeper) （高级路径（深入探索））

4. **Explore advanced applications and patterns:**
   **探索高级应用和模式：**
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
   - `11_emergence_and_attractor_dynamics.md`: Emergent properties
     `11_emergence_and_attractor_dynamics.md`：涌现属性
   - `12_symbolic_mechanisms.md`: Symbolic reasoning in LLMs
     `12_symbolic_mechanisms.md`：大型语言模型中的符号推理

### 2.3. Hands-On Practice (Learning by Doing) （动手实践（边做边学））

5. **Start with `10_guides_zero_to_hero/01_min_prompt.ipynb`**  
   Run, modify, observe token counts.  
   Notebook cells highlight **why** each extra line helps (or hurts).
   **从 `10_guides_zero_to_hero/01_min_prompt.ipynb` 开始**  
   运行、修改、观察令牌计数。  
   笔记本单元格突出显示了**为什么**每一行额外的代码都有帮助（或有害）。

6. **Explore more complex patterns:**
   **探索更复杂的模式：**
   - `02_expand_context.ipynb`: Adding context effectively
     `02_expand_context.ipynb`：有效地添加上下文
   - `03_control_loops.ipynb`: Building flow control
     `03_control_loops.ipynb`：构建流控制
   - `04_rag_recipes.ipynb`: Retrieval-augmented generation
     `04_rag_recipes.ipynb`：检索增强生成
   - `05_protocol_bootstrap.ipynb`: Working with field protocols
     `05_protocol_bootstrap.ipynb`：使用场协议
   - `06_protocol_token_budget.ipynb`: Measuring efficiency
     `06_protocol_token_budget.ipynb`：衡量效率

7. **Advance to field-based approaches:**
   **进阶到基于场的方法：**
   - `07_streaming_context.ipynb`: Real-time context management
     `07_streaming_context.ipynb`：实时上下文管理
   - `08_emergence_detection.ipynb`: Detecting emergent patterns
     `08_emergence_detection.ipynb`：检测涌现模式
   - `09_residue_tracking.ipynb`: Following symbolic residue
     `09_residue_tracking.ipynb`：追踪符号残留
   - `10_attractor_formation.ipynb`: Creating stable field patterns
     `10_attractor_formation.ipynb`：创建稳定的场模式

### 2.4. Implementation Track (Building Real Systems) （实现路径（构建真实系统））

8. **Experiment with `20_templates/`**  
   Copy a YAML or Python snippet into your own repo.  
   Tune "token_budget" or "resonance_score" like adjusting pH.
   **使用 `20_templates/` 进行实验**  
   将 YAML 或 Python 代码片段复制到您自己的存储库中。  
   像调整 pH 值一样调整“令牌预算”或“共振分数”。

9. **Examine `30_examples/` implementations:**
   **检查 `30_examples/` 的实现：**
   - `00_toy_chatbot/`: Simple but complete context management
     `00_toy_chatbot/`：简单但完整的上下文管理
   - `01_data_annotator/`: Specialized context for data labeling
     `01_data_annotator/`：用于数据标注的专门上下文
   - `02_multi_agent_orchestrator/`: Complex agent coordination
     `02_multi_agent_orchestrator/`：复杂的代理协调
   - `03_vscode_helper/`: IDE integration for context engineering
     `03_vscode_helper/`：用于上下文工程的 IDE 集成
   - `04_rag_minimal/`: Streamlined retrieval architecture
     `04_rag_minimal/`：简化的检索架构

10. **Explore field-based examples:**
    **探索基于场的示例：**
    - `05_streaming_window/`: Real-time context management
      `05_streaming_window/`：实时上下文管理
    - `06_residue_scanner/`: Symbolic residue detection
      `06_residue_scanner/`：符号残留检测
    - `07_attractor_visualizer/`: Visualizing field dynamics
      `07_attractor_visualizer/`：可视化场动力学
    - `08_field_protocol_demo/`: Protocol-based field operations
      `08_field_protocol_demo/`：基于协议的场操作
    - `09_emergence_lab/`: Detecting and measuring emergence
      `09_emergence_lab/`：检测和测量涌现

### 2.5. Advanced Integration (Field Theory in Practice) （高级集成（场论实践））

11. **Dive into field protocols with `60_protocols/`:**
    **使用 `60_protocols/` 深入研究场协议：**
    - Protocol shells for defining field operations
      用于定义场操作的协议外壳
    - Schemas for structured field representations
      用于结构化场表示的模式
    - Digests for understanding protocol functions
      用于理解协议功能的摘要

12. **Study agent implementations in `70_agents/`:**
    **研究 `70_agents/` 中的代理实现：**
    - `01_residue_scanner/`: Detecting symbolic residue
      `01_residue_scanner/`：检测符号残留
    - `02_self_repair_loop/`: Self-healing field protocols
      `02_self_repair_loop/`：自愈场协议
    - `03_attractor_modulator/`: Managing attractor dynamics
      `03_attractor_modulator/`：管理吸引子动力学
    - `04_boundary_adapter/`: Dynamic boundary tuning
      `04_boundary_adapter/`：动态边界调整
    - `05_field_resonance_tuner/`: Optimizing field resonance
      `05_field_resonance_tuner/`：优化场共振

13. **Explore integrated systems in `80_field_integration/`:**
    **探索 `80_field_integration/` 中的集成系统：**
    - `00_protocol_ide_helper/`: Development tools for protocols
      `00_protocol_ide_helper/`：协议开发工具
    - `01_context_engineering_assistant/`: Field-based assistant
      `01_context_engineering_assistant/`：基于场的助手
    - `02_recursive_reasoning_system/`: Recursive reasoning architecture
      `02_recursive_reasoning_system/`：递归推理架构
    - `03_emergent_field_laboratory/`: Experimental field environments
      `03_emergent_field_laboratory/`：实验场环境
    - `04_symbolic_reasoning_engine/`: Symbolic mechanism integration
      `04_symbolic_reasoning_engine/`：符号机制集成

14. **Understand cognitive tools in `cognitive-tools/`:**
    **理解 `cognitive-tools/` 中的认知工具：**
    - Cognitive templates for structured reasoning
      用于结构化推理的认知模板
    - Cognitive programs for complex operations
      用于复杂操作的认知程序
    - Cognitive schemas for knowledge representation
      用于知识表示的认知模式
    - Cognitive architectures for complete systems
      用于完整系统的认知架构
    - Integration patterns for connecting with other components
      用于与其他组件连接的集成模式

---

## 3. Conceptual Foundations （概念基础）

### 3.1. Biological Metaphor Evolution （生物学隐喻演化）

Our biological metaphor has evolved from simple components to complex, field-based systems:
我们的生物学隐喻已从简单的组件演变为复杂的、基于场的系统：

```
Atoms         → Individual instructions or constraints
（原子）        → 单个指令或约束
Molecules     → Instructions with examples (few-shot learning)
（分子）        → 带示例的指令（少样本学习）
Cells         → Context with memory that persists across interactions
（细胞）        → 具有跨交互持久性记忆的上下文
Organs        → Coordinated systems of context cells working together
（器官）        → 协同工作的上下文细胞系统
Neural Systems → Cognitive tools extending reasoning capabilities
（神经系统）  → 扩展推理能力的认知工具
Neural Fields  → Context as continuous medium with emergent properties
（神经场）    → 作为具有涌现属性的连续介质的上下文
```

### 3.2. Field Theory Concepts （场论概念）

As we advance to neural field theory, we incorporate several key concepts:
随着我们向神经场论迈进，我们融合了几个关键概念：

1. **Continuity**: Context as continuous semantic landscape rather than discrete tokens
   **连续性**：上下文作为连续的语义景观，而非离散的令牌
2. **Resonance**: How information patterns interact and reinforce each other
   **共振**：信息模式如何相互作用和加强
3. **Persistence**: How information maintains influence over time
   **持久性**：信息如何随时间保持影响力
4. **Attractor Dynamics**: Stable patterns that organize the field
   **吸引子动力学**：组织场的稳定模式
5. **Boundary Dynamics**: How information enters and exits the field
   **边界动力学**：信息如何进入和退出场
6. **Symbolic Residue**: Fragments of meaning that persist and influence the field
   **符号残留**：持续存在并影响场的意义碎片
7. **Emergence**: How new patterns and behaviors arise from field interactions
   **涌现**：新模式和行为如何从场交互中产生

### 3.3. Emergent Symbolic Mechanisms （涌现符号机制）

Research has identified an emergent three-stage architecture for symbolic reasoning in LLMs:
研究已经确定了大型语言模型中符号推理的涌现三阶段架构：

1. **Symbol Abstraction**: Heads in early layers convert input tokens to abstract variables based on relations
   **符号抽象**：早期层中的头根据关系将输入令牌转换为抽象变量
2. **Symbolic Induction**: Heads in intermediate layers perform sequence induction over abstract variables
   **符号归纳**：中间层中的头对抽象变量执行序列归纳
3. **Retrieval**: Heads in later layers predict next tokens by retrieving values associated with abstract variables
   **检索**：后期层中的头通过检索与抽象变量关联的值来预测下一个令牌

These mechanisms support our field-based approach to context engineering by providing a mechanistic understanding of how LLMs actually process and reason with information.
这些机制通过提供对大型语言模型如何实际处理和推理信息的机械理解，支持我们基于场的上下文工程方法。

### 3.4. Cognitive Tools Framework （认知工具框架）

To enhance reasoning capabilities, we incorporate a cognitive tools framework:
为了增强推理能力，我们融合了一个认知工具框架：

1. **Tool-Based Approach**: Modular, predetermined cognitive operations executed sequentially
   **基于工具的方法**：模块化、预定的认知操作按顺序执行
2. **Key Operations**:
   **关键操作**：
   - **Recall Related**: Retrieving relevant knowledge to guide reasoning
     **回忆相关**：检索相关知识以指导推理
   - **Examine Answer**: Self-reflection on reasoning and answers
     **检查答案**：对推理和答案进行自我反思
   - **Backtracking**: Exploring alternative reasoning paths when blocked
     **回溯**：在受阻时探索替代的推理路径
3. **Integration**: These tools can be combined with field-based approaches for more powerful systems
   **集成**：这些工具可以与基于场的方法相结合，以构建更强大的系统

---

## 4. Quiet Karpathy Guidelines (Style DNA) （Quiet Karpathy 指南（风格 DNA））

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

## 5. Repository Structure in Detail （存储库结构详解）

```
Context-Engineering/
├── LICENSE                          # MIT license （MIT 许可证）
├── README.md                        # Quick-start overview （快速入门概述）
├── structure.md                     # Original structural map （原始结构图）
├── STRUCTURE_v2.md                  # Enhanced structural map with field theory （带有场论的增强结构图）
├── context.json                     # Original schema configuration （原始模式配置）
├── context_v2.json                  # Extended schema with field protocols （带有场协议的扩展模式）
├── context_v3.json                  # Neural field extensions （神经场扩展）
├── context_v3.5.json                # Symbolic mechanism integration （符号机制集成）
├── CITATIONS.md                     # Research references and bridges （研究参考文献和桥梁）
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
│   ├── 10_field_orchestration.md    # Coordinating multiple fields （协调多个场）
│   ├── 11_emergence_and_attractor_dynamics.md # Emergent properties （涌现属性）
│   └── 12_symbolic_mechanisms.md    # Symbolic reasoning in LLMs （大型语言模型中的符号推理）
│
├── 10_guides_zero_to_hero/          # Hands-on tutorials （动手教程）
│   ├── 01_min_prompt.ipynb          # Minimal prompt experiments （最小提示实验）
│   ├── 02_expand_context.ipynb      # Context expansion techniques （上下文扩展技术）
│   ├── 03_control_loops.ipynb       # Flow control mechanisms （流控制机制）
│   ├── 04_rag_recipes.ipynb         # Retrieval-augmented patterns （检索增强模式）
│   ├── 05_protocol_bootstrap.ipynb  # Field protocol bootstrap （场协议引导）
│   ├── 06_protocol_token_budget.ipynb # Protocol efficiency （协议效率）
│   ├── 07_streaming_context.ipynb   # Real-time context （实时上下文）
│   ├── 08_emergence_detection.ipynb # Detecting emergence （检测涌现）
│   ├── 09_residue_tracking.ipynb    # Tracking symbolic residue （追踪符号残留）
│   └── 10_attractor_formation.ipynb # Creating field attractors （创建场吸引子）
│
├── 20_templates/                    # Reusable components （可复用组件）
│   ├── minimal_context.yaml         # Base context structure （基础上下文结构）
│   ├── control_loop.py              # Orchestration template （编排模板）
│   ├── scoring_functions.py         # Evaluation metrics （评估指标）
│   ├── prompt_program_template.py   # Program structure template （程序结构模板）
│   ├── schema_template.yaml         # Schema definition template （模式定义模板）
│   ├── recursive_framework.py       # Recursive context template （递归上下文模板）
│   ├── field_protocol_shells.py     # Field protocol templates （场协议外壳）
│   ├── symbolic_residue_tracker.py  # Residue tracking tools （残留追踪工具）
│   ├── context_audit.py             # Context analysis tool （上下文分析工具）
│   ├── shell_runner.py              # Protocol shell runner （协议外壳运行器）
│   ├── resonance_measurement.py     # Field resonance metrics （场共振指标）
│   ├── attractor_detection.py       # Attractor analysis tools （吸引子分析工具）
│   ├── boundary_dynamics.py         # Boundary operation tools （边界操作工具）
│   └── emergence_metrics.py         # Emergence measurement （涌现测量）
│
├── 30_examples/                     # Practical implementations （实际应用）
│   ├── 00_toy_chatbot/              # Simple conversation agent （简单对话代理）
│   ├── 01_data_annotator/           # Data labeling system （数据标注系统）
│   ├── 02_multi_agent_orchestrator/ # Agent collaboration system （代理协作系统）
│   ├── 03_vscode_helper/            # IDE integration （IDE 集成）
│   ├── 04_rag_minimal/              # Minimal RAG implementation （最小 RAG 实现）
│   ├── 05_streaming_window/         # Real-time context demo （实时上下文演示）
│   ├── 06_residue_scanner/          # Symbolic residue demo （符号残留演示）
│   ├── 07_attractor_visualizer/     # Field visualization （场可视化）
│   ├── 08_field_protocol_demo/      # Protocol demonstration （协议演示）
│   └── 09_emergence_lab/            # Emergence experimentation （涌现实验）
│
├── 40_reference/                    # Deep-dive documentation （深度文档）
│   ├── token_budgeting.md           # Token optimization strategies （令牌优化策略）
│   ├── retrieval_indexing.md        # Retrieval system design （检索系统设计）
│   ├── eval_checklist.md            # PR evaluation criteria （PR 评估标准）
│   ├── cognitive_patterns.md        # Reasoning pattern catalog （推理模式目录）
│   ├── schema_cookbook.md           # Schema pattern collection （模式模式集合）
│   ├── patterns.md                  # Context pattern library （上下文模式库）
│   ├── field_mapping.md             # Field theory fundamentals （场论基础）
│   ├── symbolic_residue_types.md    # Residue classification （残留分类）
│   ├── attractor_dynamics.md        # Attractor theory and practice （吸引子理论与实践）
│   ├── emergence_signatures.md      # Detecting emergence （检测涌现）
│   └── boundary_operations.md       # Boundary management guide （边界管理指南）
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
│   │   ├── field.resonance.scaffold.shell  # Field resonance （场共振）
│   │   ├── field.self_repair.shell        # Self-repair mechanisms （自我修复机制）
│   │   └── context.memory.persistence.attractor.shell # Context persistence （上下文持久性）
│   ├── digests/                     # Simplified protocol documentation （简化协议文档）
│   └── schemas/                     # Protocol schemas （协议模式）
│       ├── fractalRepoContext.v3.5.json    # Repository context （存储库上下文）
│       ├── fractalConsciousnessField.v1.json # Field schema （场模式）
│       ├── protocolShell.v1.json           # Shell schema （外壳模式）
│       ├── symbolicResidue.v1.json         # Residue schema （残留模式）
│       └── attractorDynamics.v1.json       # Attractor schema （吸引子模式）
│
├── 70_agents/                       # Agent demonstrations （代理演示）
│   ├── README.md                    # Agent overview （代理概述）
│   ├── 01_residue_scanner/          # Symbolic residue detection （符号残留检测）
│   ├── 02_self_repair_loop/         # Self-repair protocol （自我修复协议）
│   ├── 03_attractor_modulator/      # Attractor dynamics （吸引子动力学）
│   ├── 04_boundary_adapter/         # Dynamic boundary tuning （动态边界调整）
│   └── 05_field_resonance_tuner/    # Field resonance optimization （场共振优化）
│
├── 80_field_integration/            # Complete field projects （完整的场项目）
│   ├── README.md                    # Integration overview （集成概述）
│   ├── 00_protocol_ide_helper/      # Protocol development tools （协议开发工具）
│   ├── 01_context_engineering_assistant/ # Field-based assistant （基于场的助手）
│   ├── 02_recursive_reasoning_system/    # Recursive reasoning （递归推理）
│   ├── 03_emergent_field_laboratory/     # Field experimentation （场实验）
│   └── 04_symbolic_reasoning_engine/     # Symbolic mechanisms （符号机制）
│
├── cognitive-tools/                 # Advanced cognitive framework （高级认知框架）
│   ├── README.md                    # Overview and quick-start guide （概述和快速入门指南）
│   ├── cognitive-templates/         # Templates for reasoning （推理模板）
│   │   ├── understanding.md         # Comprehension operations （理解操作）
│   │   ├── reasoning.md             # Analytical operations （分析操作）
│   │   ├── verification.md          # Checking and validation （检查和验证）
│   │   ├── composition.md           # Combining multiple tools （组合多个工具）
│   │   └── emergence.md             # Emergent reasoning patterns （涌现推理模式）
│   │
│   ├── cognitive-programs/          # Structured prompt programs （结构化提示程序）
│   │   ├── basic-programs.md        # Fundamental program structures （基本程序结构）
│   │   ├── advanced-programs.md     # Complex program architectures （复杂程序架构）
│   │   ├── program-library.py       # Python implementations （Python 实现）
│   │   ├── program-examples.ipynb   # Interactive examples （交互式示例）
│   │   └── emergence-programs.md    # Emergent program patterns （涌现程序模式）
│   │
│   ├── cognitive-schemas/           # Knowledge representations （知识表示）
│   │   ├── user-schemas.md          # User information schemas （用户信息模式）
│   │   ├── domain-schemas.md        # Domain knowledge schemas （领域知识模式）
│   │   ├── task-schemas.md          # Reasoning task schemas （推理任务模式）
│   │   ├── schema-library.yaml      # Reusable schema library （可复用模式库）
│   │   └── field-schemas.md         # Field representation schemas （场表示模式）
│   │
│   ├── cognitive-architectures/     # Complete reasoning systems （完整的推理系统）
│   │   ├── solver-architecture.md   # Problem-solving systems （问题解决系统）
│   │   ├── tutor-architecture.md    # Educational systems （教育系统）
│   │   ├── research-architecture.md # Information synthesis （信息综合）
│   │   ├── architecture-examples.py # Implementation examples （实现示例）
│   │   └── field-architecture.md    # Field-based architectures （基于场的架构）
│   │
│   └── integration/                 # Integration patterns （集成模式）
│       ├── with-rag.md              # Integration with retrieval （与检索集成）
│       ├── with-memory.md           # Integration with memory （与记忆集成）
│       ├── with-agents.md           # Integration with agents （与代理集成）
│       ├── evaluation-metrics.md    # Effectiveness measurement （有效性测量）
│       └── with-fields.md           # Integration with field protocols （与场协议集成）
│
└── .github/                         # GitHub configuration （GitHub 配置）
    ├── CONTRIBUTING.md              # Contribution guidelines （贡献指南）
    ├── workflows/ci.yml             # CI pipeline configuration （CI 管道配置）
    ├── workflows/eval.yml           # Evaluation automation （评估自动化）
    └── workflows/protocol_tests.yml # Protocol testing （协议测试）
```

---

## 6. Implementation Patterns （实施模式）

### 6.1. Context Structure Patterns （上下文结构模式）

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Atomic Prompt** | Single instruction with constraints | Simple, well-defined tasks |
| **Few-Shot Examples** | Instruction with examples | Pattern demonstration |
| **Chain-of-Thought** | Reasoning steps explicit in prompt | Complex reasoning tasks |
| **Stateful Context** | Context with memory | Multi-turn conversations |
| **Multi-Agent** | Multiple specialized agents | Complex, multi-step tasks |
| **Field-Based** | Context as continuous field | Emergent reasoning needs |

| 模式 | 描述 | 用例 |
|---------|-------------|----------|
| **原子提示** | 带约束的单个指令 | 简单、明确定义的任务 |
| **少样本示例** | 带示例的指令 | 模式演示 |
| **思维链** | 提示中明确的推理步骤 | 复杂的推理任务 |
| **有状态上下文** | 带记忆的上下文 | 多轮对话 |
| **多智能体** | 多个专门的智能体 | 复杂的多步任务 |
| **基于场** | 作为连续场的上下文 | 涌现的推理需求 |

### 6.2. Field Operation Patterns （场操作模式）

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Attractor Formation** | Creating stable semantic patterns | `attractor_detection.py` |
| **Resonance Amplification** | Strengthening pattern interactions | `resonance_measurement.py` |
| **Boundary Tuning** | Controlling information flow | `boundary_dynamics.py` |
| **Residue Integration** | Managing symbolic fragments | `symbolic_residue_tracker.py` |
| **Emergence Detection** | Identifying novel patterns | `emergence_metrics.py` |
| **Self-Repair** | Automatic context healing | `field.self_repair.shell` |

| 模式 | 描述 | 实现 |
|---------|-------------|----------------|
| **吸引子形成** | 创建稳定的语义模式 | `attractor_detection.py` |
| **共振放大** | 加强模式交互 | `resonance_measurement.py` |
| **边界调整** | 控制信息流 | `boundary_dynamics.py` |
| **残留整合** | 管理符号碎片 | `symbolic_residue_tracker.py` |
| **涌现检测** | 识别新颖模式 | `emergence_metrics.py` |
| **自我修复** | 自动上下文修复 | `field.self_repair.shell` |

### 6.3. Cognitive Tool Patterns （认知工具模式）

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Recall Related** | Retrieving relevant knowledge | `cognitive-programs/basic-programs.md` |
| **Examine Answer** | Self-reflection and verification | `cognitive-templates/verification.md` |
| **Backtracking** | Exploring alternative paths | `cognitive-programs/advanced-programs.md` |
| **Decomposition** | Breaking problems into parts | `cognitive-templates/reasoning.md` |
| **Integration** | Combining multiple results | `cognitive-templates/composition.md` |

| 模式 | 描述 | 实现 |
|---------|-------------|----------------|
| **回忆相关** | 检索相关知识 | `cognitive-programs/basic-programs.md` |
| **检查答案** | 自我反思和验证 | `cognitive-templates/verification.md` |
| **回溯** | 探索替代路径 | `cognitive-programs/advanced-programs.md` |
| **分解** | 将问题分解为多个部分 | `cognitive-templates/reasoning.md` |
| **集成** | 合并多个结果 | `cognitive-templates/composition.md` |

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
6. Consider field dynamics and symbolic mechanisms
   考虑场动力学和符号机制

### 7.1. Contribution Focus Areas （贡献重点领域）

We especially welcome contributions in these areas:
我们特别欢迎在这些领域的贡献：

1. **Field Dynamics Tools**: Tools for measuring and visualizing field properties
   **场动力学工具**：用于测量和可视化场属性的工具
2. **Symbolic Mechanism Experiments**: Demonstrations of emergent symbolic processing
   **符号机制实验**：涌现符号处理的演示
3. **Cognitive Tool Implementations**: New cognitive operations and patterns
   **认知工具实现**：新的认知操作和模式
4. **Protocol Shell Developments**: Novel protocol shells for field operations
   **协议外壳开发**：用于场操作的新颖协议外壳
5. **Integration Examples**: Combining multiple approaches in practical applications
   **集成示例**：在实际应用中组合多种方法
6. **Evaluation Metrics**: Better ways to measure context effectiveness
   **评估指标**：衡量上下文有效性的更好方法

---

## 8. License & Attribution （许可证和归属）

MIT. No gate-keeping: copy, remix, redistribute.  
A respectful nod to Andrej Karpathy for coining the framing.  
Research acknowledgments in CITATIONS.md.  
All errors are ours; improvements are welcome.
麻省理工学院许可证。没有门槛：复制、混搭、重新分发。  
向 Andrej Karpathy 致敬，感谢他创造了这个框架。  
研究致谢见 CITATIONS.md。  
所有错误都是我们的；欢迎改进。

---

## 9. Roadmap （路线图）

### 9.1. Near-Term Priorities （近期优先事项）

1. **Symbolic Mechanism Integration**: Better leverage of emergent symbolic mechanisms
   **符号机制集成**：更好地利用涌现的符号机制
2. **Field Visualization Tools**: Tools for understanding field dynamics
   **场可视化工具**：用于理解场动力学的工具
3. **Protocol Shell Expansion**: More protocol shells for field operations
   **协议外壳扩展**：更多用于场操作的协议外壳
4. **Evaluation Framework Enhancement**: Improved metrics for field-based systems
   **评估框架增强**：改进基于场的系统的指标
5. **Cognitive Tool Integration**: Better integration with field-based approaches
   **认知工具集成**：更好地与基于场的方法集成

### 9.2. Long-Term Vision （长期愿景）

1. **Self-Evolving Context Systems**: Contexts that improve themselves
   **自我演化的上下文系统**：能够自我改进的上下文
2. **Field Theory Formalization**: More rigorous mathematical foundation
   **场论形式化**：更严谨的数学基础
3. **Unified Framework**: Integrating symbolic mechanisms, field theory, and cognitive tools
   **统一框架**：集成符号机制、场论和认知工具
4. **Cross-Model Compatibility**: Ensuring techniques work across different model architectures
   **跨模型兼容性**：确保技术在不同模型架构中都能工作
5. **Automated Context Optimization**: Tools for automatic context tuning
   **自动化上下文优化**：用于自动上下文调整的工具