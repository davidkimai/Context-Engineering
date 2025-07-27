# Conversation Protocols (对话协议)

> *"The quality of your communication determines the quality of your result."*
> *“沟通的质量决定了结果的质量。”*
>
> **— Peter Drucker (彼得·德鲁克)**

## Introduction to Conversation Protocols (对话协议简介)

Conversation protocols are structured templates that guide your interactions with AI systems. They transform unpredictable, meandering dialogues into efficient, purposeful exchanges with consistent outcomes.
对话协议是指导您与人工智能系统交互的结构化模板。它们将不可预测、漫无目的的对话转变为高效、有目的、结果一致的交流。

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            CONVERSATION PROTOCOL BENEFITS (对话协议的好处)           │
│                                                     │
│  • Consistent outcomes across interactions (跨交互的一致结果)          │
│  • Clear expectations for both human and AI (对人类和人工智能的明确期望)         │
│  • Efficient use of context window (有效利用上下文窗口)                  │
│  • Reduced cognitive load for humans (减轻人类的认知负荷)                │
│  • Trackable progress through complex discussions (通过复杂讨论可跟踪的进展)   │
│  • Portable templates across different AI systems (跨不同人工智能系统的可移植模板)   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

This guide provides practical, ready-to-use conversation protocols for common scenarios, along with implementation guidance and performance metrics. Each protocol follows our NOCODE principles: Navigate, Orchestrate, Control, Optimize, Deploy, and Evolve.
本指南为常见场景提供了实用、即用型的对话协议，以及实施指南和性能指标。每个协议都遵循我们的“无代码”原则：导航、编排、控制、优化、部署和演进。

## How to Use This Guide (如何使用本指南)

1. **Identify your conversation goal** from the categories below
2. **Copy the protocol template** that best matches your need
3. **Customize the placeholders** with your specific information
4. **Paste the complete protocol** at the beginning of your conversation
5. **Monitor the metrics** to evaluate effectiveness
6. **Iterate and refine** based on results

1. **从以下类别中确定您的对话目标**
2. **复制最符合您需求的协议模板**
3. **使用您的特定信息自定义占位符**
4. **在对话开始时粘贴完整的协议**
5. **监控指标以评估有效性**
6. **根据结果进行迭代和优化**

**Socratic Question**: What conversation types currently frustrate you the most with AI systems? Which would benefit most from a structured approach?
**苏格拉底式提问**：目前哪些对话类型最让您对人工智能系统感到沮丧？哪种对话类型最能从结构化方法中受益？

---

## 1. The Information Extraction Protocol (1. 信息提取协议)

### Purpose (目的)
Extract specific, structured information from unstructured content or knowledge domains.
从非结构化内容或知识领域中提取特定的结构化信息。

### When to Use (何时使用)
- Analyzing documents or content
- Gathering specific data points
- Creating structured datasets from unstructured text
- Distilling key points from complex sources

- 分析文档或内容
- 收集特定的数据点
- 从非结构化文本创建结构化数据集
- 从复杂来源中提取要点

### Protocol Template (协议模板)

```
/extract.information{
    intent="Extract specific, structured information from content",
    input={
        content="[PASTE_CONTENT_OR_DESCRIBE_DOMAIN]",
        target_structure={
            categories: ["[CATEGORY_1]", "[CATEGORY_2]", "[CATEGORY_3]"],
            format: "[FORMAT: table/list/JSON/etc.]",
            level_of_detail: "[brief/moderate/comprehensive]"
        },
        special_focus="[ANY_SPECIFIC_ASPECTS_TO_EMPHASIZE]"
    },
    process=[
        /analyze{action="Scan content for relevant information"},
        /categorize{action="Organize information into specified categories"},
        /structure{action="Format according to target structure"},
        /verify{action="Check completeness and accuracy"},
        /summarize{action="Provide overview of extracted information"}
    ],
    output={
        extracted_information="[Structured information according to specifications]",
        coverage_assessment="[Evaluation of information completeness]",
        confidence_metrics="[Reliability indicators for extracted information]"
    }
}

I'd like you to extract information from the content I've provided following this protocol. Please acknowledge and proceed with the extraction.
```

### Implementation Guide (实施指南)

1. **Content Specification**:
   - For document analysis: Paste the full text or upload the document
   - For knowledge extraction: Clearly describe the domain (e.g., "information about renewable energy technologies")

1. **内容规范**：
   - 对于文档分析：粘贴全文或上传文档
   - 对于知识提取：清楚地描述领域（例如，“关于可再生能源技术的信息”）

2. **Target Structure Definition**:
   - Categories: Define 3-7 specific categories (e.g., "costs," "benefits," "limitations")
   - Format: Specify the output format that will be most useful (table, list, JSON, etc.)
   - Detail Level: Choose based on your needs (brief for overviews, comprehensive for deep analysis)

2. **目标结构定义**：
   - 类别：定义 3-7 个特定类别（例如，“成本”、“收益”、“限制”）
   - 格式：指定最有用的输出格式（表格、列表、JSON 等）
   - 详细程度：根据您的需求选择（简要用于概述，全面用于深入分析）

3. **Special Focus**:
   - Highlight any specific aspects that deserve particular attention
   - Can include timeframes, geographic focus, or specific sub-topics

3. **特别关注**：
   - 突出任何值得特别关注的特定方面
   - 可以包括时间范围、地理重点或特定子主题

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Category Coverage | Percentage of categories with substantive information | 100% |
| Information Density | Relevant data points per category | 3-5 minimum |
| Structural Integrity | Adherence to requested format | 100% |
| Confidence Score | AI's assessment of information reliability | >80% |

| 指标 | 描述 | 目标 |
|---|---|---|
| 类别覆盖率 | 具有实质性信息的类别百分比 | 100% |
| 信息密度 | 每个类别的相关数据点 | 最少 3-5 个 |
| 结构完整性 | 对请求格式的遵守程度 | 100% |
| 置信度分数 | 人工智能对信息可靠性的评估 | >80% |

### Example Application (应用示例)

```
/extract.information{
    intent="Extract specific, structured information from content",
    input={
        content="[Research paper on climate change mitigation strategies]",
        target_structure={
            categories: ["Technology Solutions", "Policy Approaches", "Economic Impacts", "Implementation Challenges", "Success Metrics"],
            format: "markdown table with categories as rows",
            level_of_detail: "moderate"
        },
        special_focus="Solutions applicable to urban environments with limited resources"
    },
    process=[...],
    output={...}
}
```

---

## 2. The Structured Debate Protocol (2. 结构化辩论协议)

### Purpose (目的)
Explore multiple perspectives on complex or controversial topics with balanced, thoughtful analysis.
以平衡、周到的分析探讨复杂或有争议主题的多种视角。

### When to Use (何时使用)
- Evaluating competing approaches or solutions
- Understanding controversial topics
- Making complex decisions with multiple factors
- Testing the strength of arguments and counterarguments

- 评估相互竞争的方法或解决方案
- 理解有争议的话题
- 做出涉及多个因素的复杂决策
- 测试论点和反驳论点的说服力

### Protocol Template (协议模板)

```
/debate.structured{
    intent="Explore multiple perspectives on a complex topic",
    input={
        topic="[TOPIC_OR_QUESTION]",
        perspectives=["[PERSPECTIVE_1]", "[PERSPECTIVE_2]", "[PERSPECTIVE_3_OPTIONAL]"],
        evaluation_criteria=["[CRITERION_1]", "[CRITERION_2]", "[CRITERION_3]"],
        constraints="[ANY_LIMITATIONS_OR_GUIDELINES]"
    },
    process=[
        /establish{action="Define key terms and establish shared foundations"},
        /present{action="Present each perspective with strongest arguments"},
        /challenge{action="Identify weaknesses in each perspective"},
        /evaluate{action="Assess each perspective against criteria"},
        /synthesize{action="Identify potential integrations or resolutions"},
        /conclude{action="Summarize key insights and implications"}
    ],
    output={
        perspective_analysis="[Structured analysis of each perspective]",
        comparative_evaluation="[Side-by-side assessment using criteria]",
        synthesis_insights="[Potential integrations or novel approaches]",
        key_takeaways="[Most important insights from the debate]"
    }
}

I'd like to explore this topic through a structured debate using the perspectives and criteria I've provided. Please acknowledge and proceed with the debate.
```

### Implementation Guide (实施指南)

1. **Topic Definition**:
   - Frame as a clear question or statement
   - Ensure scope is manageable but substantive

1. **主题定义**：
   - 以清晰的问题或陈述形式提出
   - 确保范围可控但内容充实

2. **Perspective Selection**:
   - Include 2-3 distinct viewpoints (more becomes unwieldy)
   - Choose perspectives that genuinely differ in approach or values
   - Can include conventional vs. unconventional, theoretical vs. practical, etc.

2. **视角选择**：
   - 包括 2-3 个不同的观点（更多会变得难以处理）
   - 选择在方法或价值观上真正不同的观点
   - 可以包括传统与非传统、理论与实践等

3. **Evaluation Criteria**:
   - Select 3-5 relevant criteria for assessment
   - Include a mix of practical and principled considerations
   - Examples: cost-effectiveness, ethical implications, implementation feasibility

3. **评估标准**：
   - 选择 3-5 个相关的评估标准
   - 包括实际和原则性考虑的混合
   - 示例：成本效益、伦理影响、实施可行性

4. **Constraints**:
   - Specify any limitations on scope
   - Note any assumptions that should be held constant

4. **约束**：
   - 指定范围的任何限制
   - 注意任何应保持不变的假设

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Steel-Manning | Strength of arguments for each perspective | Best possible case made |
| Balance | Equal depth and charity across perspectives | <10% variation |
| Criteria Application | Thorough application of all criteria | 100% coverage |
| Integration Quality | Value added through synthesis | Novel insights identified |

| 指标 | 描述 | 目标 |
|---|---|---|
| 钢铁侠 | 每个观点的论证强度 | 提出最佳论证 |
| 平衡 | 各个观点的深度和善意程度相同 | <10% 的差异 |
| 标准应用 | 全面应用所有标准 | 100% 覆盖 |
| 整合质量 | 通过综合增加的价值 | 识别出新颖的见解 |

### Example Application (应用示例)

```
/debate.structured{
    intent="Explore multiple perspectives on a complex topic",
    input={
        topic="Should cities prioritize public transit or autonomous vehicles for future mobility?",
        perspectives=["Public Transit Focus", "Autonomous Vehicle Priority", "Hybrid Approach"],
        evaluation_criteria=["Environmental Impact", "Social Equity", "Economic Efficiency", "Implementation Timeline"],
        constraints="Focus on mid-sized urban areas in developed economies"
    },
    process=[...],
    output={...}
}
```

---

## 3. The Progressive Feedback Protocol (3. 渐进式反馈协议)

### Purpose (目的)
Iteratively improve a work product through structured, multi-stage feedback.
通过结构化的多阶段反馈，迭代地改进工作产品。

### When to Use (何时使用)
- Refining drafts of written content
- Improving design concepts
- Enhancing problem solutions
- Developing ideas through iteration

- 优化书面内容的草稿
- 改进设计概念
- 增强问题解决方案
- 通过迭代发展想法

### Protocol Template (协议模板)

```
/feedback.progressive{
    intent="Iteratively improve work through structured feedback stages",
    input={
        work_product="[CONTENT_TO_IMPROVE]",
        improvement_focus=["[FOCUS_AREA_1]", "[FOCUS_AREA_2]", "[FOCUS_AREA_3]"],
        iteration_count="[NUMBER_OF_FEEDBACK_CYCLES]",
        constraints="[ANY_LIMITATIONS_OR_GUIDELINES]"
    },
    process=[
        /baseline{action="Establish strengths and weaknesses of current version"},
        /prioritize{action="Identify highest-impact improvement opportunities"},
        /iterate{
            action="For each focus area:",
            substeps=[
                /analyze{action="Identify specific improvement opportunities"},
                /suggest{action="Provide specific enhancement recommendations"},
                /implement{action="Apply recommended changes"},
                /review{action="Assess improvements and identify next steps"}
            ]
        },
        /synthesize{action="Integrate improvements across all focus areas"},
        /compare{action="Contrast final version with original baseline"}
    ],
    output={
        improved_work="[Enhanced version of original work]",
        improvement_summary="[Overview of changes and enhancements]",
        future_directions="[Recommendations for further development]",
        version_comparison="[Before/after analysis showing progress]"
    }
}

I'd like to improve this work through progressive feedback cycles. Please acknowledge and begin the feedback process.
```

### Implementation Guide (实施指南)

1. **Work Product Specification**:
   - Provide the complete work to be improved
   - For longer works, consider specifying sections for focused attention

1. **工作产品规范**：
   - 提供需要改进的完整工作
   - 对于较长的工作，考虑指定需要重点关注的部分

2. **Improvement Focus Areas**:
   - Define 2-4 specific aspects for enhancement
   - Examples for writing: clarity, structure, evidence, persuasiveness
   - Examples for design: usability, aesthetics, functionality, coherence

2. **改进重点领域**：
   - 定义 2-4 个需要增强的特定方面
   - 写作示例：清晰度、结构、证据、说服力
   - 设计示例：可用性、美学、功能性、连贯性

3. **Iteration Count**:
   - Specify how many feedback cycles to perform (2-3 is often optimal)
   - For complex works, consider focusing on different aspects in each cycle

3. **迭代次数**：
   - 指定要执行的反馈周期数（2-3 次通常是最佳的）
   - 对于复杂的作品，考虑在每个周期中关注不同的方面

4. **Constraints**:
   - Note any elements that should remain unchanged
   - Specify any stylistic or content guidelines to maintain

4. **约束**：
   - 注意任何应保持不变的元素
   - 指定任何要维护的风格或内容指南

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Improvement Delta | Measurable enhancement from baseline | Significant positive change |
| Focus Area Coverage | Attention to all specified focus areas | 100% coverage |
| Implementation Quality | Thoroughness of applying feedback | All high-priority suggestions |
| Coherence | Integration of improvements across areas | Unified, not patchwork |

| 指标 | 描述 | 目标 |
|---|---|---|
| 改进增量 | 从基线可衡量的增强 | 显著的积极变化 |
| 重点领域覆盖率 | 对所有指定重点领域的关注 | 100% 覆盖 |
| 实施质量 | 应用反馈的彻底性 | 所有高优先级建议 |
| 连贯性 | 跨领域改进的整合 | 统一，而非拼凑 |

### Example Application (应用示例)

```
/feedback.progressive{
    intent="Iteratively improve work through structured feedback stages",
    input={
        work_product="[Draft marketing email for new productivity software]",
        improvement_focus=["Persuasiveness", "Clarity", "Call-to-action effectiveness"],
        iteration_count="3",
        constraints="Must maintain professional tone and stay under 300 words"
    },
    process=[...],
    output={...}
}
```

---

## 4. The Decision Analysis Protocol (4. 决策分析协议)

### Purpose (目的)
Systematically analyze options and make recommendations for complex decisions.
系统地分析选项并为复杂决策提出建议。

### When to Use (何时使用)
- Evaluating multiple options with tradeoffs
- Making high-stakes decisions
- Breaking down complex choice scenarios
- Creating decision frameworks for recurring choices

- 评估具有权衡的多个选项
- 做出高风险决策
- 分解复杂的选择场景
- 为重复性选择创建决策框架

### Protocol Template (协议模板)

```
/decision.analyze{
    intent="Systematically analyze options and provide decision support",
    input={
        decision_context="[DECISION_SITUATION_DESCRIPTION]",
        options=["[OPTION_1]", "[OPTION_2]", "[OPTION_3_OPTIONAL]"],
        criteria={
            "[CRITERION_1]": {"weight": [1-10], "description": "[DESCRIPTION]"},
            "[CRITERION_2]": {"weight": [1-10], "description": "[DESCRIPTION]"},
            "[CRITERION_3]": {"weight": [1-10], "description": "[DESCRIPTION]"}
        },
        constraints="[ANY_LIMITATIONS_OR_REQUIREMENTS]",
        decision_maker_profile="[RELEVANT_PREFERENCES_OR_CONTEXT]"
    },
    process=[
        /frame{action="Clarify decision context and goals"},
        /evaluate{
            action="For each option:",
            substeps=[
                /assess{action="Evaluate against each weighted criterion"},
                /identify{action="Determine key strengths and weaknesses"},
                /quantify{action="Assign scores based on criteria performance"}
            ]
        },
        /compare{action="Conduct comparative analysis across options"},
        /analyze{action="Examine sensitivity to assumption changes"},
        /recommend{action="Provide structured recommendation with rationale"}
    ],
    output={
        option_analysis="[Detailed assessment of each option]",
        comparative_matrix="[Side-by-side comparison using criteria]",
        recommendation="[Primary recommendation with rationale]",
        sensitivity_notes="[How recommendation might change with different assumptions]",
        implementation_considerations="[Key factors for executing the decision]"
    }
}

I'd like to analyze this decision using the options and criteria I've provided. Please acknowledge and proceed with the analysis.
```

### Implementation Guide (实施指南)

1. **Decision Context**:
   - Describe the situation requiring a decision
   - Include relevant background and constraints
   - Clarify the specific decision to be made

1. **决策背景**：
   - 描述需要做出决策的情况
   - 包括相关的背景和约束
   - 澄清需要做出的具体决策

2. **Options Definition**:
   - List all viable alternatives (typically 2-5)
   - Provide enough detail for meaningful comparison
   - Ensure options are genuinely distinct

2. **选项定义**：
   - 列出所有可行的备选方案（通常为 2-5 个）
   - 提供足够的细节以进行有意义的比较
   - 确保选项真正不同

3. **Criteria Specification**:
   - Define 3-7 evaluation criteria
   - Assign weights to reflect relative importance (1-10 scale)
   - Include descriptions to ensure consistent application

3. **标准规范**：
   - 定义 3-7 个评估标准
   - 分配权重以反映相对重要性（1-10 分制）
   - 包括描述以确保一致的应用

4. **Decision Maker Profile**:
   - Include relevant preferences, risk tolerance, values
   - Note any specific priorities or constraints
   - Mention timeline or resource limitations

4. **决策者简介**：
   - 包括相关的偏好、风险承受能力、价值观
   - 注意任何特定的优先级或约束
   - 提及时间表或资源限制

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Criteria Coverage | Thorough application of all criteria | 100% coverage |
| Analysis Depth | Substantive evaluation of each option | Comparable depth across options |
| Quantification Quality | Meaningful scoring with rationales | Clear justification for all scores |
| Recommendation Clarity | Unambiguous guidance with rationale | Specific, actionable advice |

| 指标 | 描述 | 目标 |
|---|---|---|
| 标准覆盖率 | 全面应用所有标准 | 100% 覆盖 |
| 分析深度 | 对每个选项进行实质性评估 | 各选项的深度相当 |
| 量化质量 | 有意义的评分及理由 | 所有评分都有明确的理由 |
| 建议清晰度 | 明确的指导及理由 | 具体、可操作的建议 |

### Example Application (应用示例)

```
/decision.analyze{
    intent="Systematically analyze options and provide decision support",
    input={
        decision_context="Selecting a technology stack for a new e-commerce platform",
        options=["MERN Stack (MongoDB, Express, React, Node.js)", "Python/Django with PostgreSQL and React", "Ruby on Rails with React and PostgreSQL"],
        criteria={
            "Development Speed": {"weight": 8, "description": "How quickly can we build and iterate"},
            "Scalability": {"weight": 9, "description": "Ability to handle growing user base and traffic"},
            "Maintenance Complexity": {"weight": 7, "description": "Ease of ongoing maintenance and updates"},
            "Talent Availability": {"weight": 6, "description": "Ease of finding developers"}
        },
        constraints="Must be able to integrate with existing payment processing system",
        decision_maker_profile="Mid-sized company with limited in-house development team, moderate technical debt aversion, timeline of 6 months to launch"
    },
    process=[...],
    output={...}
}
```

---

## 5. The Alignment Protocol (5. 对齐协议)

### Purpose (目的)
Ensure mutual understanding and establish shared goals, terminology, and approaches.
确保相互理解并建立共同的目标、术语和方法。

### When to Use (何时使用)
- Beginning complex projects
- Establishing collaboration frameworks
- Clarifying expectations and deliverables
- Aligning on problem definitions and success criteria

- 开始复杂的项目
- 建立协作框架
- 澄清期望和可交付成果
- 就问题定义和成功标准达成一致

### Protocol Template (协议模板)

```
/align.mutual{
    intent="Establish shared understanding and aligned expectations",
    input={
        topic="[TOPIC_OR_PROJECT_DESCRIPTION]",
        key_terms=["[TERM_1]", "[TERM_2]", "[TERM_3_OPTIONAL]"],
        goals=["[GOAL_1]", "[GOAL_2]", "[GOAL_3_OPTIONAL]"],
        constraints="[ANY_LIMITATIONS_OR_BOUNDARIES]",
        success_criteria="[HOW_SUCCESS_WILL_BE_MEASURED]"
    },
    process=[
        /define{action="Establish clear definitions for key terms"},
        /clarify{action="Ensure mutual understanding of goals and success criteria"},
        /explore{action="Identify potential misalignments or ambiguities"},
        /resolve{action="Address and clarify any identified misalignments"},
        /confirm{action="Establish explicitly shared understanding"},
        /document{action="Record aligned definitions, goals, and criteria"}
    ],
    output={
        term_definitions="[Explicit definitions of key terms]",
        goal_clarifications="[Detailed understanding of each goal]",
        boundary_conditions="[Clear articulation of constraints and limitations]",
        success_metrics="[Specific, measurable indicators of success]",
        alignment_summary="[Confirmation of mutual understanding]"
    }
}

I'd like to establish alignment on this topic using the terms, goals, and criteria I've provided. Please acknowledge and proceed with the alignment process.
```

### Implementation Guide (实施指南)

1. **Topic Specification**:
   - Clearly define the subject of alignment
   - For projects, include scope and general purpose
   - For concepts, establish the domain and importance

1. **主题规范**：
   - 清楚地定义对齐的主题
   - 对于项目，包括范围和一般目的
   - 对于概念，建立领域和重要性

2. **Key Terms Selection**:
   - Identify 3-7 terms requiring explicit definition
   - Focus on terms with potential for ambiguity
   - Include domain-specific jargon needing clarification

2. **关键术语选择**：
   - 识别 3-7 个需要明确定义的术语
   - 关注可能存在歧义的术语
   - 包括需要澄清的领域特定术语

3. **Goals Articulation**:
   - List 2-5 specific goals
   - Ensure goals are concrete enough to be actionable
   - Include both process and outcome goals when relevant

3. **目标阐述**：
   - 列出 2-5 个具体目标
   - 确保目标足够具体，可以采取行动
   - 在相关时包括过程和结果目标

4. **Success Criteria**:
   - Define how achievement will be measured
   - Include both qualitative and quantitative indicators
   - Specify timeframes when applicable

4. **成功标准**：
   - 定义如何衡量成就
   - 包括定性和定量指标
   - 在适用时指定时间范围

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Definition Clarity | Precision and usefulness of term definitions | Unambiguous, operational definitions |
| Goal Specificity | Concreteness and actionability of goals | Specific, measurable, achievable |
| Boundary Clarity | Precision in constraint definition | Clear limitation parameters |
| Alignment Confirmation | Degree of mutual understanding | Explicit confirmation of shared understanding |

| 指标 | 描述 | 目标 |
|---|---|---|
| 定义清晰度 | 术语定义的精确性和实用性 | 明确、可操作的定义 |
| 目标具体性 | 目标的具体性和可操作性 | 具体、可衡量、可实现 |
| 边界清晰度 | 约束定义的精确性 | 清晰的限制参数 |
| 对齐确认 | 相互理解的程度 | 明确确认共同理解 |

### Example Application (应用示例)

```
/align.mutual{
    intent="Establish shared understanding and aligned expectations",
    input={
        topic="Development of a customer feedback analysis system",
        key_terms=["Customer Sentiment", "Actionable Insight", "Implementation Priority", "Success Metric"],
        goals=["Create automated sentiment analysis", "Identify top customer pain points", "Develop prioritization framework for addressing feedback"],
        constraints="Must work with existing CRM system and respect customer privacy regulations",
        success_criteria="System should identify 90% of actionable feedback and reduce manual analysis time by 70%"
    },
    process=[...],
    output={...}
}
```

---

## 6. The Problem Definition Protocol (6. 问题定义协议)

### Purpose (目的)
Precisely define and frame problems to ensure effective solution development.
精确定义和构建问题，以确保有效的解决方案开发。

### When to Use (何时使用)
- When facing complex or ambiguous problems
- Before beginning solution development
- When stakeholders have different problem understandings
- To reframe seemingly intractable problems

- 面对复杂或模棱两可的问题时
- 在开始解决方案开发之前
- 当利益相关者对问题有不同理解时
- 重新构建看似棘手的问题

### Protocol Template (协议模板)

```
/problem.define{
    intent="Clearly define and frame a problem for effective solution development",
    input={
        initial_problem_statement="[CURRENT_PROBLEM_DESCRIPTION]",
        context="[RELEVANT_BACKGROUND_INFORMATION]",
        stakeholders=["[STAKEHOLDER_1]", "[STAKEHOLDER_2]", "[STAKEHOLDER_3_OPTIONAL]"],
        attempted_solutions="[PREVIOUS_APPROACHES_IF_ANY]",
        constraints="[ANY_LIMITATIONS_OR_BOUNDARIES]"
    },
    process=[
        /analyze{action="Examine initial problem statement for clarity and accuracy"},
        /deconstruct{action="Break down problem into components and dimensions"},
        /reframe{action="Consider alternative problem framings and perspectives"},
        /validate{action="Test problem definition against stakeholder needs"},
        /synthesize{action="Develop comprehensive problem definition"},
        /scope{action="Establish clear boundaries and success criteria"}
    ],
    output={
        refined_problem_statement="[Clear, precise problem definition]",
        root_causes="[Identified underlying factors]",
        success_criteria="[How a successful solution will be recognized]",
        constraints_and_boundaries="[Explicit limitations and scope]",
        reframing_insights="[Alternative perspectives that provide new approaches]",
        solution_directions="[Potential solution paths based on problem definition]"
    }
}

I'd like to clearly define this problem using the information I've provided. Please acknowledge and proceed with the problem definition process.
```

### Implementation Guide (实施指南)

1. **Initial Problem Statement**:
   - State the problem as currently understood
   - Include symptoms and apparent challenges
   - Note any assumptions embedded in current understanding

1. **初始问题陈述**：
   - 陈述当前理解的问题
   - 包括症状和明显的挑战
   - 注意当前理解中嵌入的任何假设

2. **Context Provision**:
   - Provide relevant background information
   - Include organizational, historical, or technical context
   - Note any recent changes or developments

2. **上下文提供**：
   - 提供相关的背景信息
   - 包括组织、历史或技术背景
   - 注意任何最近的变化或发展

3. **Stakeholder Identification**:
   - List primary parties affected by or interested in the problem
   - Include their perspectives and priorities if known
   - Note any conflicting stakeholder interests

3. **利益相关者识别**：
   - 列出受问题影响或对问题感兴趣的主要各方
   - 如果知道，包括他们的观点和优先事项
   - 注意任何冲突的利益相关者利益

4. **Attempted Solutions**:
   - Describe previous approaches and their outcomes
   - Note specific limitations or failures
   - Include partial successes and learnings

4. **尝试的解决方案**：
   - 描述以前的方法及其结果
   - 注意具体的局限性或失败
   - 包括部分成功和经验教训

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Clarity | Precision and understandability of problem definition | Unambiguous, concise statement |
| Root Cause Depth | Identification of underlying factors | Beyond symptoms to fundamental causes |
| Stakeholder Validation | Alignment with stakeholder perspectives | Addresses all key stakeholder concerns |
| Actionability | How directly the definition enables solution development | Clear path to solution approaches |

| 指标 | 描述 | 目标 |
|---|---|---|
| 清晰度 | 问题定义的精确性和可理解性 | 明确、简洁的陈述 |
| 根本原因深度 | 识别潜在因素 | 超越症状，触及根本原因 |
| 利益相关者验证 | 与利益相关者观点的一致性 | 解决所有关键利益相关者的关切 |
| 可操作性 | 定义如何直接促成解决方案的开发 | 清晰的解决方案路径 |

### Example Application (应用示例)

```
/problem.define{
    intent="Clearly define and frame a problem for effective solution development",
    input={
        initial_problem_statement="Customer churn rate has increased by 15% over the past quarter",
        context="SaaS business with subscription model, recent UI redesign, and price increase of 10%",
        stakeholders=["Product Team", "Customer Success Team", "Executive Leadership", "Customers"],
        attempted_solutions="Implemented win-back campaigns and exit surveys with limited success",
        constraints="Solutions must work within existing technology stack and maintain current pricing strategy"
    },
    process=[...],
    output={...}
}
```

---

## 7. The Learning Facilitation Protocol (7. 学习促进协议)

### Purpose (目的)
Structure the learning process for effective knowledge acquisition and skill development.
构建学习过程，以有效获取知识和发展技能。

### When to Use (何时使用)
- When learning new subjects or skills
- Teaching complex topics to others
- Creating educational materials
- Developing learning paths or curricula

- 学习新学科或技能时
- 向他人教授复杂主题时
- 创建教育材料时
- 开发学习路径或课程时

### Protocol Template (协议模板)

```
/learning.facilitate{
    intent="Structure effective learning experiences for knowledge acquisition",
    input={
        subject="[TOPIC_OR_SKILL_TO_LEARN]",
        current_knowledge="[EXISTING_KNOWLEDGE_LEVEL]",
        learning_goals=["[GOAL_1]", "[GOAL_2]", "[GOAL_3_OPTIONAL]"],
        learning_style_preferences="[PREFERRED_LEARNING_APPROACHES]",
        time_constraints="[AVAILABLE_TIME_AND_SCHEDULE]"
    },
    process=[
        /assess{action="Evaluate current knowledge and identify gaps"},
        /structure{action="Organize subject into logical learning sequence"},
        /scaffold{action="Build progressive framework from fundamentals to advanced concepts"},
        /contextualize{action="Connect abstract concepts to real applications"},
        /reinforce{action="Design practice activities and knowledge checks"},
        /adapt{action="Tailor approach based on progress and feedback"}
    ],
    output={
        learning_path="[Structured sequence of topics and skills]",
        key_concepts="[Fundamental ideas and principles to master]",
        learning_resources="[Recommended materials and sources]",
        practice_activities="[Exercises to reinforce learning]",
        progress_indicators="[How to measure learning advancement]",
        next_steps="[Guidance for continuing development]"
    }
}

I'd like to structure a learning experience for this subject based on the information I've provided. Please acknowledge and proceed with developing the learning facilitation.
```

### Implementation Guide (实施指南)

1. **Subject Specification**:
   - Clearly define the topic or skill to be learned
   - Include specific sub-areas of focus if applicable
   - Note any particular applications or contexts of interest

1. **主题规范**：
   - 清楚地定义要学习的主题或技能
   - 如果适用，包括具体的重点子领域
   - 注意任何特别感兴趣的应用或背景

2. **Current Knowledge Assessment**:
   - Honestly evaluate existing familiarity and competence
   - Note specific areas of strength or weakness
   - Identify any misconceptions to be addressed

2. **当前知识评估**：
   - 诚实地评估现有的熟悉程度和能力
   - 注意具体的优势或劣势领域
   - 识别任何需要纠正的误解

3. **Learning Goals Definition**:
   - Specify 2-5 concrete learning outcomes
   - Include both knowledge and application goals
   - Set appropriate ambition level for time available

3. **学习目标定义**：
   - 指定 2-5 个具体的学习成果
   - 包括知识和应用目标
   - 根据可用时间设定适当的抱负水平

4. **Learning Style Preferences**:
   - Note preferred approaches (visual, hands-on, theoretical, etc.)
   - Specify any particularly effective past learning experiences
   - Identify any approaches to avoid

4. **学习风格偏好**：
   - 注意偏好的方法（视觉、动手、理论等）
   - 指定任何特别有效的过去学习经历
   - 识别任何要避免的方法

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Sequencing Logic | Appropriate progression of concepts | Clear dependencies honored |
| Engagement Level | Alignment with learning preferences | Multiple modalities included |
| Practice Quality | Effectiveness of reinforcement activities | Active learning opportunities |
| Goal Alignment | Connection between activities and stated goals | Direct path to goal achievement |

| 指标 | 描述 | 目标 |
|---|---|---|
| 排序逻辑 | 概念的适当进展 | 尊重明确的依赖关系 |
| 参与度 | 与学习偏好的一致性 | 包括多种模式 |
| 练习质量 | 强化活动的有效性 | 积极的学习机会 |
| 目标一致性 | 活动与既定目标之间的联系 | 实现目标的直接路径 |

### Example Application (应用示例)

```
/learning.facilitate{
    intent="Structure effective learning experiences for knowledge acquisition",
    input={
        subject="Data visualization with Python (matplotlib and seaborn)",
        current_knowledge="Intermediate Python programming, basic statistics, no visualization experience",
        learning_goals=["Create publication-quality visualizations", "Develop interactive dashboards", "Implement automated visualization pipelines"],
        learning_style_preferences="Hands-on projects with practical applications, visual examples, iterative building",
        time_constraints="10 hours per week for 4 weeks"
    },
    process=[...],
    output={...}
}
```

---

## 8. The Scenario Planning Protocol (8. 情景规划协议)

### Purpose (目的)
Explore possible futures and develop robust strategies for uncertain environments.
探索可能的未来，并为不确定的环境制定稳健的策略。

### When to Use (何时使用)
- Strategic planning in uncertain environments
- Risk assessment and contingency planning
- Innovation and future-proofing efforts
- Decision-making with long-term implications

- 在不确定的环境中进行战略规划
- 风险评估和应急计划
- 创新和面向未来的努力
- 具有长期影响的决策

### Protocol Template (协议模板)

```
/scenario.plan{
    intent="Explore possible futures and develop robust strategies",
    input={
        focal_question="[CENTRAL_STRATEGIC_QUESTION]",
        time_horizon="[PLANNING_TIMEFRAME]",
        key_uncertainties=["[UNCERTAINTY_1]", "[UNCERTAINTY_2]", "[UNCERTAINTY_3_OPTIONAL]"],
        driving_forces=["[FORCE_1]", "[FORCE_2]", "[FORCE_3_OPTIONAL]"],
        current_situation="[RELEVANT_CONTEXT_AND_STARTING_POINT]"
    },
    process=[
        /identify{action="Define key factors and driving forces"},
        /analyze{action="Assess impact and uncertainty of factors"},
        /construct{
            action="Develop 3-4 distinct, plausible scenarios",
            substeps=[
                /name{action="Create memorable scenario title"},
                /narrate{action="Describe scenario evolution and key events"},
                /detail{action="Explore implications for stakeholders"}
            ]
        },
        /identify{action="Extract strategic insights across scenarios"},
        /develop{action="Create robust strategies and early indicators"}
    ],
    output={
        scenarios=[
            {name="[SCENARIO_1_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"},
            {name="[SCENARIO_2_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"},
            {name="[SCENARIO_3_NAME]", description="[DETAILED_DESCRIPTION]", implications="[STRATEGIC_IMPLICATIONS]"}
        ],
        robust_strategies="[APPROACHES_EFFECTIVE_ACROSS_SCENARIOS]",
        early_indicators="[SIGNS_INDICATING_SCENARIO_EMERGENCE]",
        key_uncertainties="[CRITICAL_FACTORS_TO_MONITOR]",
        strategic_recommendations="[IMMEDIATE_AND_LONG-TERM_ACTIONS]"
    }
}

I'd like to develop scenario plans around this focal question using the information I've provided. Please acknowledge and proceed with the scenario planning process.
```

### Implementation Guide (实施指南)

1. **Focal Question Definition**:
   - Frame the central strategic question clearly
   - Ensure appropriate scope and relevance
   - Focus on decision-making needs

1. **焦点问题定义**：
   - 清楚地提出核心战略问题
   - 确保适当的范围和相关性
   - 关注决策需求

2. **Time Horizon Selection**:
   - Choose appropriate timeframe (typically 3-10 years)
   - Balance between foreseeable future and meaningful change
   - Consider industry-specific timing factors

2. **时间范围选择**：
   - 选择合适的时间范围（通常为 3-10 年）
   - 在可预见的未来和有意义的变化之间取得平衡
   - 考虑行业特定的时间因素

3. **Key Uncertainties Identification**:
   - Select 2-4 critical uncertainties with high impact
   - Focus on genuinely uncertain factors (not predetermined)
   - Include diverse types (technological, social, economic, etc.)

3. **关键不确定性识别**：
   - 选择 2-4 个具有高影响的关键不确定性
   - 关注真正不确定的因素（而非预先确定的）
   - 包括不同类型（技术、社会、经济等）

4. **Driving Forces Analysis**:
   - Identify major trends and factors shaping the environment
   - Include both external and internal forces
   - Consider STEEP factors (Social, Technological, Economic, Environmental, Political)

4. **驱动力分析**：
   - 识别塑造环境的主要趋势和因素
   - 包括外部和内部力量
   - 考虑 STEEP 因素（社会、技术、经济、环境、政治）

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Scenario Plausibility | Logical coherence and believability | No magical thinking or contradictions |
| Scenario Distinctiveness | Meaningful differences between scenarios | Clear, contrasting futures |
| Strategic Utility | Actionable insights derived from scenarios | Concrete implications for decisions |
| Indicator Quality | Usefulness of early warning signals | Observable, leading indicators |

| 指标 | 描述 | 目标 |
|---|---|---|
| 情景合理性 | 逻辑连贯性和可信度 | 没有不切实际的想法或矛盾 |
| 情景独特性 | 情景之间的有意义差异 | 清晰、对比鲜明的未来 |
| 战略效用 | 从情景中得出的可操作见解 | 对决策的具体影响 |
| 指标质量 | 预警信号的有用性 | 可观察的领先指标 |

### Example Application (应用示例)

```
/scenario.plan{
    intent="Explore possible futures and develop robust strategies",
    input={
        focal_question="How should our retail business adapt to changing consumer behavior and technology over the next decade?",
        time_horizon="10 years (2025-2035)",
        key_uncertainties=["Pace and nature of AI/automation adoption", "Consumer preferences for physical vs. digital experiences", "Regulatory environment for data and privacy"],
        driving_forces=["Aging demographics in core markets", "Climate change impacts on supply chains", "Increasing economic inequality", "Metaverse and virtual reality development"],
        current_situation="Mid-sized retail chain with 60% revenue from physical stores, growing e-commerce presence, limited data analytics capabilities"
    },
    process=[...],
    output={...}
}
```

---

## Advanced Protocol Integration (高级协议集成)

### Combining Protocols for Complex Interactions (组合协议以实现复杂交互)

For sophisticated needs, protocols can be combined sequentially or nested:
对于复杂的需求，协议可以按顺序或嵌套组合：

```
/sequence{
    steps=[
        /problem.define{...},
        /debate.structured{...},
        /decision.analyze{...}
    ]
}
```

### Protocol Adaptation Guidelines (协议适应指南)

1. **Add Specialized Process Steps**:
   ```
   /extract.information{
       ...
       process=[
           ...,
           /specialize{action="Domain-specific analysis step"}
       ]
   }
   ```

1. **添加专门的处理步骤**：
   ```
   /extract.information{
       ...
       process=[
           ...,
           /specialize{action="特定领域的分析步骤"}
       ]
   }
   ```

2. **Extend Input Parameters**:
   ```
   /learning.facilitate{
       ...
       input={
           ...,
           accessibility_needs="[SPECIFIC_ACCESSIBILITY_REQUIREMENTS]"
       }
   }
   ```

2. **扩展输入参数**：
   ```
   /learning.facilitate{
       ...
       input={
           ...,
           accessibility_needs="[特定的可访问性要求]"
       }
   }
   ```

3. **Enhance Output Specifications**:
   ```
   /scenario.plan{
       ...
       output={
           ...,
           visual_timeline="[GRAPHICAL_REPRESENTATION_OF_SCENARIOS]"
       }
   }
   ```

3. **增强输出规范**：
   ```
   /scenario.plan{
       ...
       output={
           ...,
           visual_timeline="[情景的图形表示]"
       }
   }
   ```

## Performance Optimization Tips (性能优化技巧)

### Token Efficiency (令牌效率)

1. **Prioritize Input Elements**:
   - Include only essential context
   - Use bullet points for lists instead of narrative
   - Reference external information when possible

1. **优先考虑输入元素**：
   - 仅包含必要的上下文
   - 使用项目符号列表代替叙述
   - 在可能的情况下引用外部信息

2. **Process Streamlining**:
   - For simpler tasks, reduce process steps
   - Combine related steps when appropriate
   - Remove substeps that don't add value

2. **流程精简**：
   - 对于较简单的任务，减少流程步骤
   - 在适当的时候合并相关步骤
   - 删除不增加价值的子步骤

3. **Output Focus**:
   - Specify only needed output elements
   - Request appropriate detail level
   - Use structured formats for efficiency

3. **输出重点**：
   - 仅指定所需的输出元素
   - 请求适当的详细程度
   - 使用结构化格式以提高效率

### Mental Models for Protocol Selection (协议选择的心智模型)

1. **Garden Model**:
   - Which protocol will best cultivate the ideas I need?
   - What tending and pruning is required?
   - How can I ensure sustainable growth?

1. **花园模型**：
   - 哪个协议最能培养我需要的想法？
   - 需要哪些照料和修剪？
   - 我如何确保可持续增长？

2. **River Model**:
   - What's the source of the information flow?
   - Where do I want the conversation to flow?
   - What obstacles might divert the flow?

2. **河流模型**：
   - 信息流的来源是什么？
   - 我希望对话流向何方？
   - 哪些障碍可能会转移水流？

3. **Budget Model**:
   - What's my token budget for this interaction?
   - Which investments will yield highest returns?
   - How can I minimize waste?

3. **预算模型**：
   - 我这次互动的令牌预算是多少？
   - 哪些投资会产生最高的回报？
   - 我如何才能最大限度地减少浪费？

## Continuous Improvement (持续改进)

### Protocol Refinement Process (协议优化流程)

1. **Capture Results**:
   - Document protocol outputs
   - Note any deviations or challenges
   - Track AI behavior throughout the interaction

1. **捕获结果**：
   - 记录协议输出
   - 注意任何偏差或挑战
   - 跟踪整个交互过程中的人工智能行为

2. **Evaluate Performance**:
   - Compare against specified metrics
   - Identify strengths and weaknesses
   - Note unexpected benefits or limitations

2. **评估性能**：
   - 与指定的指标进行比较
   - 识别优势和劣势
   - 注意意外的收益或局限性

3. **Refine Elements**:
   - Adjust input parameters for clarity and completeness
   - Modify process steps based on observed effectiveness
   - Update output specifications to better match needs

3. **优化元素**：
   - 调整输入参数以确保清晰和完整
   - 根据观察到的有效性修改流程步骤
   - 更新输出规范以更好地满足需求

4. **Test Iterations**:
   - Apply refined protocol to similar scenarios
   - Compare performance across iterations
   - Document progressive improvements

4. **测试迭代**：
   - 将优化的协议应用于类似场景
   - 比较不同迭代的性能
   - 记录渐进式改进

### Protocol Versioning System (协议版本控制系统)

To track protocol evolution, use simple versioning notation:
要跟踪协议的演变，请使用简单的版本控制表示法：

```
/protocol.name.v1.2{...}
```

Where:
- First number (1): Major version (structural changes)
- Second number (2): Minor version (parameter or process refinements)

其中：
- 第一个数字 (1)：主版本（结构性更改）
- 第二个数字 (2)：次版本（参数或流程优化）

Include change notes for each version:
为每个版本添加更改说明：

```
/extract.information.v1.2{
    meta={
        version_history=[
            {version="1.0", date="2025-02-10", changes="Initial release"},
            {version="1.1", date="2025-03-15", changes="Added confidence metrics to output"},
            {version="1.2", date="2025-04-22", changes="Enhanced special_focus parameter"}
        ]
    },
    ...
}
```

## Field Dynamics in Conversation Protocols (对话协议中的场动力学)

> *"The quality of your field determines the nature of what emerges within it."*
> *“你的领域的质量决定了其中涌现事物的性质。”*

Conversation protocols create semantic fields that shape interactions in subtle but powerful ways. Understanding field dynamics can help you design more effective protocols.
对话协议创建了语义场，以微妙而强大的方式塑造交互。了解场动力学可以帮助您设计更有效的协议。

### Key Field Dynamics Concepts (关键场动力学概念)

1. **Attractors**: Stable patterns that conversations naturally gravitate toward
   - Each protocol creates specific attractor basins
   - Well-designed protocols maintain desired attractors

1. **吸引子**：对话自然倾向于的稳定模式
   - 每个协议都会创建特定的吸引子盆地
   - 精心设计的协议会维护所需的吸引子

2. **Boundaries**: Limits that define the conversation space
   - Clear boundaries prevent drift and maintain focus
   - Permeable boundaries allow beneficial exploration

2. **边界**：定义对话空间的限制
   - 清晰的边界可以防止漂移并保持专注
   - 可渗透的边界允许有益的探索

3. **Resonance**: Amplification of certain themes or patterns
   - Protocols can create resonant fields that enhance certain qualities
   - Intentional resonance improves coherence and depth

3. **共振**：某些主题或模式的放大
   - 协议可以创建共振场，增强某些品质
   - 有意的共振可以提高连贯性和深度

4. **Residue**: Persistent effects that carry forward
   - Effective protocols leave productive residue
   - Symbolic residue creates foundation for future interactions

4. **残留**：持续存在并向前传递的影响
   - 有效的协议会留下富有成效的残留
   - 符号残留为未来的互动奠定了基础

### Applying Field Dynamics (应用场动力学)

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            FIELD DYNAMICS ENHANCEMENT (场动力学增强)               │
│                                                     │
│  Add to any protocol: (添加到任何协议：)                               │
│                                                     │
│  field_dynamics={                                   │
│    attractors: ["[PRIMARY_ATTRACTOR]", "[SECONDARY]"],│
│    boundaries: {                                    │
│      firm: ["[FIRM_BOUNDARY]"],                     │
│      permeable: ["[PERMEABLE_BOUNDARY]"]            │
│    },                                               │
│    resonance: ["[RESONANCE_PATTERN]"],              │
│    residue: {                                       │
│      target: "[DESIRED_SYMBOLIC_RESIDUE]",          │
│      persistence: "[HIGH|MEDIUM|LOW]"               │
│    }                                                │
│  }                                                  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

**Example Application**:
**应用示例**：

```
/debate.structured{
    ...
    field_dynamics={
        attractors: ["evidence-based reasoning", "charitable interpretation"],
        boundaries: {
            firm: ["personal attacks", "logical fallacies"],
            permeable: ["creative analogies", "interdisciplinary connections"]
        },
        resonance: ["intellectual curiosity", "nuanced understanding"],
        residue: {
            target: "multiple valid perspectives can coexist",
            persistence: "HIGH"
        }
    },
    ...
}
```

## Protocol Library Management (协议库管理)

As you develop your protocol collection, organizing them becomes essential for reuse and improvement.
随着您协议集的不断发展，对其进行组织对于重用和改进至关重要。

### Personal Protocol Library Template (个人协议库模板)

Create a personal library markdown file:
创建一个个人库 markdown 文件：

```markdown
# Personal Protocol Library

## Conversation Protocols

### Daily Use
- [Extract Information v1.2](#extract-information)
- [Structured Debate v2.0](#structured-debate)

### Special Purpose
- [Scenario Planning v1.0](#scenario-planning)
- [Problem Definition v1.3](#problem-definition)

## Protocol Definitions

### Extract Information
```
/extract.information.v1.2{
    // Full protocol definition
}
```

### Structured Debate
```
/debate.structured.v2.0{
    // Full protocol definition
}
```
```

### Integration with Note-Taking Systems (与笔记系统集成)

Protocols can be integrated with popular note-taking and knowledge management systems:
协议可以与流行的笔记和知识管理系统集成：

1. **Obsidian**:
   - Create a dedicated protocols folder
   - Use template plugin for quick insertion
   - Link protocols to related notes

1. **Obsidian**：
   - 创建一个专门的协议文件夹
   - 使用模板插件快速插入
   - 将协议链接到相关笔记

2. **Notion**:
   - Create a protocol database
   - Include metadata like use cases, effectiveness rating
   - Use templates for quick addition to pages

2. **Notion**：
   - 创建一个协议数据库
   - 包括用例、有效性评级等元数据
   - 使用模板快速添加到页面

3. **Roam Research**:
   - Create protocol blocks with block references
   - Tag protocols for different use cases
   - Build workflow templates that incorporate protocols

3. **Roam Research**：
   - 创建带有块引用的协议块
   - 为不同的用例标记协议
   - 构建包含协议的工作流模板

## The Protocol Development Process (协议开发过程)

Creating your own protocols follows a structured path:
创建您自己的协议遵循一个结构化的路径：

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│            PROTOCOL DEVELOPMENT CYCLE (协议开发周期)               │
│                                                     │
│  1. IDENTIFY NEED (识别需求)                                   │
│     • Recognize recurring conversation pattern (识别重复的对话模式)      │
│     • Identify frustrations or inefficiencies (识别挫折或低效率)       │
│     • Define desired outcomes (定义期望的结果)                       │
│                                                     │
│  2. DESIGN STRUCTURE (设计结构)                                │
│     • Define core components (input, process, output) (定义核心组件（输入、过程、输出）)│
│     • Outline key process steps (概述关键过程步骤)                     │
│     • Determine required parameters (确定所需参数)                 │
│                                                     │
│  3. PROTOTYPE & TEST (原型和测试)                                │
│     • Create minimal viable protocol (创建最小可行协议)                │
│     • Test with various AI systems (使用各种人工智能系统进行测试)                  │
│     • Document performance (记录性能)                          │
│                                                     │
│  4. REFINE & OPTIMIZE (优化和完善)                               │
│     • Enhance based on test results (根据测试结果进行增强)                 │
│     • Optimize for token efficiency (优化令牌效率)                 │
│     • Improve clarity and usability (提高清晰度和可用性)                 │
│                                                     │
│  5. DOCUMENT & SHARE (记录和分享)                                │
│     • Create usage guidelines (创建使用指南)                       │
│     • Define performance metrics (定义性能指标)                    │
│     • Share with community (与社区分享)                          │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Protocol Design Worksheet (协议设计工作表)

Use this worksheet to develop new protocols:
使用此工作表开发新协议：

```
## Protocol Design Worksheet

### 1. Basic Information
- Protocol Name: _______________
- Purpose: _______________
- Use Cases: _______________

### 2. Core Components
- Input Parameters:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- Process Steps:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________
- Output Elements:
  - [ ] _______________
  - [ ] _______________
  - [ ] _______________

### 3. Field Dynamics
- Primary Attractors: _______________
- Firm Boundaries: _______________
- Desired Resonance: _______________
- Target Residue: _______________

### 4. Implementation Notes
- Token Efficiency Considerations: _______________
- Integration With Other Protocols: _______________
- Version History Plan: _______________

### 5. Evaluation Plan
- Success Metrics: _______________
- Testing Approach: _______________
- Refinement Criteria: _______________
```

## Conclusion: The Future of Conversation Protocols (结论：对话协议的未来)

Conversation protocols represent a fundamental shift in human-AI interaction. By structuring conversations through explicit protocols, we move from unpredictable, ad-hoc exchanges to consistent, efficient, and purposeful collaboration.
对话协议代表了人机交互的根本性转变。通过明确的协议来构建对话，我们从不可预测的、临时的交流转向了一致、高效和有目的的协作。

As you build your protocol library, remember these principles:
在构建您的协议库时，请记住以下原则：

1. **Start Simple**: Begin with basic protocols for common needs
2. **Iterate Continuously**: Refine based on real-world use
3. **Share and Collaborate**: Exchange protocols with others
4. **Think in Fields**: Consider the conversational field you're creating
5. **Prioritize Clarity**: Clear structure leads to clear outcomes

1. **从简单开始**：从满足常见需求的基本协议开始
2. **持续迭代**：根据实际使用情况进行优化
3. **分享与协作**：与他人交流协议
4. **以场为单位思考**：考虑您正在创建的对话场
5. **优先考虑清晰度**：清晰的结构带来清晰的结果

With these principles and the protocol templates in this guide, you're well-equipped to transform your AI conversations from unpredictable exchanges to reliable, efficient collaborations.
有了这些原则和本指南中的协议模板，您就具备了将您的人工智能对话从不可预测的交流转变为可靠、高效的协作的能力。

**Reflective Question**: How might these protocols change not just your interactions with AI, but also your understanding of effective communication in general?
**反思性问题**：这些协议不仅会改变您与人工智能的互动方式，还会如何改变您对有效沟通的总体理解？

---

> *"The difference between a good conversation and a great one isn't luck—it's architecture."*
> *“一次好的对话和一次伟大的对话之间的区别不在于运气，而在于架构。”*

---

## Appendix: Quick Reference (附录：快速参考)

### Protocol Basic Structure (协议基本结构)

```
/protocol.name{
    intent="Clear statement of purpose",
    input={...},
    process=[...],
    output={...}
}
```

### Common Process Actions (常见流程操作)

- `/analyze`: Examine information systematically
- `/synthesize`: Combine elements into coherent whole
- `/evaluate`: Assess against criteria
- `/prioritize`: Determine relative importance
- `/structure`: Organize information logically
- `/verify`: Confirm accuracy or validity
- `/explore`: Investigate possibilities
- `/refine`: Improve through iteration

- `/analyze`：系统地检查信息
- `/synthesize`：将元素组合成连贯的整体
- `/evaluate`：根据标准进行评估
- `/prioritize`：确定相对重要性
- `/structure`：逻辑地组织信息
- `/verify`：确认准确性或有效性
- `/explore`：调研可能性
- `/refine`：通过迭代进行改进

### Field Dynamics Quick Setup (场动力学快速设置)

```
field_dynamics={
    attractors: ["focus", "clarity"],
    boundaries: {
        firm: ["off-topic", "vagueness"],
        permeable: ["relevant examples", "useful analogies"]
    },
    resonance: ["understanding", "insight"],
    residue: {
        target: "actionable knowledge",
        persistence: "MEDIUM"
    }
}
```

### Protocol Selection Guide (协议选择指南)

| Need | Recommended Protocol |
|------|----------------------|
| Extract specific information | `/extract.information` |
| Explore multiple perspectives | `/debate.structured` |
| Improve work through feedback | `/feedback.progressive` |
| Make complex decisions | `/decision.analyze` |
| Establish shared understanding | `/align.mutual` |
| Define problems clearly | `/problem.define` |
| Structure learning experiences | `/learning.facilitate` |
| Explore possible futures | `/scenario.plan` |

| 需求 | 推荐协议 |
|---|---|
| 提取特定信息 | `/extract.information` |
| 探索多个视角 | `/debate.structured` |
| 通过反馈改进工作 | `/feedback.progressive` |
| 做出复杂决策 | `/decision.analyze` |
| 建立共同理解 | `/align.mutual` |
| 清楚地定义问题 | `/problem.define` |
| 构建学习体验 | `/learning.facilitate` |
| 探索可能的未来 | `/scenario.plan` |