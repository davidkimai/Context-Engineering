# Interpretability Protocols (可解释性协议)

> *"The greatest enemy of knowledge is not ignorance, it is the illusion of knowledge."*
> *“知识最大的敌人不是无知，而是知识的幻觉。”*
>
> **— Daniel J. Boorstin (丹尼尔·J·布尔斯廷)**

## Introduction to Interpretability Protocols (可解释性协议简介)

Interpretability protocols transform the often opaque nature of AI interactions into transparent, understandable processes. By establishing explicit frameworks for explanation, reasoning visibility, and decision transparency, these protocols help you navigate the critical boundary between powerful capabilities and trustworthy understanding.
可解释性协议将人工智能交互中通常不透明的性质转变为透明、可理解的过程。通过为解释、推理可见性和决策透明度建立明确的框架，这些协议帮助您在强大的能力和值得信赖的理解之间驾驭关键的边界。

```
┌─────────────────────────────────────────────────────┐
│                                                     │
│           INTERPRETABILITY PROTOCOL BENEFITS (可解释性协议的好处)        │
│                                                     │
│  • Transparent reasoning and decision processes (透明的推理和决策过程)     │
│  • Clear understanding of system capabilities (清晰地了解系统能力)       │
│  • Reduced "black box" risk in critical contexts (在关键情境中降低“黑箱”风险)    │
│  • Appropriate trust calibration for users (为用户进行适当的信任校准)          │
│  • Effective error detection and correction (有效的错误检测和纠正)         │
│  • Alignment between human and AI understanding (人与人工智能理解之间的一致性)                 │
│                                                     │
└─────────────────────────────────────────────────────┘
```

This guide provides ready-to-use interpretability protocols for creating transparent AI interactions, along with implementation guidance and performance metrics. Each protocol follows our NOCODE principles: Navigate, Orchestrate, Control, Optimize, Deploy, and Evolve.
本指南提供了即用型可解释性协议，用于创建透明的人工智能交互，并附有实施指南和性能指标。每个协议都遵循我们的无代码原则：导航、编排、控制、优化、部署和演进。

## How to Use This Guide (如何使用本指南)

1. **Select a protocol** that matches your transparency goal
   **选择一个协议**，使其与您的透明度目标相匹配
2. **Copy the protocol template** including the prompt and customize
   **复制协议模板**，包括提示并进行自定义
3. **Provide the complete protocol** to your AI assistant at the beginning of your interaction
   在交互开始时向您的 AI 助手**提供完整的协议**
4. **Follow the structured process** for transparent understanding
   **遵循结构化流程**以实现透明的理解
5. **Monitor metrics** to evaluate interpretability effectiveness
   **监控指标**以评估可解释性的有效性
6. **Iterate and refine** your protocol for future interactions
   为未来的交互**迭代和完善**您的协议

**Socratic Question**: In what contexts do you find AI systems most opaque or difficult to understand? When does the "black box" nature of AI create the most significant challenges for you?
**苏格拉底式提问**：在哪些情境下，您觉得人工智能系统最不透明或最难理解？人工智能的“黑箱”性质何时给您带来最重大的挑战？

---

## 1. The Process Transparency Protocol (1. 过程透明度协议)

**When to use this protocol:**
Need to understand the reasoning process behind AI outputs? This protocol guides you through making AI thinking visible—perfect for decision explanation, reasoning audits, thought process understanding, or educational insights.
**何时使用此协议：**
需要了解人工智能输出背后的推理过程吗？该协议将指导您使人工智能的思维过程可见——非常适合决策解释、推理审计、思维过程理解或教育见解。

```
Prompt: I'm working on a complex market entry strategy for our company's expansion into Southeast Asia. I need an AI assistant that can help me analyze the opportunity but with complete transparency about its reasoning process. I want to understand not just the recommendations, but how you arrive at them, what factors you're considering, and the logical steps behind your analysis.

Protocol:
/interpret.process{
    intent="Make AI reasoning process visible and understandable",
    input={
        subject="Market entry strategy analysis for Southeast Asia expansion",
        transparency_needs=[
            "Explicit reasoning steps and their sequence",
            "Factor weighting and prioritization logic",
            "Assumption identification and influence",
            "Alternative considerations and elimination rationale",
            "Confidence assessment and its basis"
        ],
        process_depth="Comprehensive but focused on decision-critical elements",
        transparency_format="Step-by-step reasoning with clear signposting"
    },
    process=[
        /structure{
            action="Establish clear reasoning framework",
            elements=[
                "explicit process stages",
                "logical progression indicators",
                "decision point signposting",
                "assumption highlighting",
                "inference transparency"
            ]
        },
        /expose{
            action="Reveal underlying reasoning components",
            elements=[
                "factor identification and relevance",
                "weighting approach and rationale",
                "information evaluation criteria",
                "connection and relationship logic",
                "confidence calibration basis"
            ]
        },
        /explain{
            action="Communicate reasoning clearly",
            approaches=[
                "appropriate abstraction selection",
                "technical concept translation",
                "process visualization cues",
                "complexity management techniques",
                "analogical bridges when helpful"
            ]
        },
        /verify{
            action="Ensure reasoning validity and completeness",
            methods=[
                "logical coherence checking",
                "assumption validation",
                "gap identification",
                "alternative consideration",
                "conclusion-evidence alignment"
            ]
        },
        /adapt{
            action="Tailor transparency to context",
            elements=[
                "detail level adjustment",
                "technical language calibration",
                "focus area responsiveness",
                "explanation format flexibility"
            ]
        }
    ],
    output={
        transparent_analysis="Market entry strategy assessment with visible reasoning",
        process_explanation="Clear articulation of analytical approach",
        assumption_map="Explicit identification of underlying assumptions",
        confidence_assessment="Transparent evaluation of conclusion reliability"
    }
}
```

### Implementation Guide (实施指南)

1. **Subject Definition**:
   **主题定义**：
   - Clearly specify the topic for analysis
     清晰地指定分析主题
   - Define scope and boundaries
     定义范围和边界
   - Note specific aspects requiring transparency
     注意需要透明度的具体方面

2. **Transparency Need Identification**:
   **透明度需求识别**：
   - Specify which process elements need visibility
     指定哪些流程元素需要可见性
   - Prioritize based on decision importance
     根据决策重要性确定优先级
   - Consider both technical and conceptual transparency
     考虑技术和概念上的透明度

3. **Process Depth Selection**:
   **流程深度选择**：
   - Determine appropriate level of detail
     确定适当的细节级别
   - Balance comprehensiveness with clarity
     平衡全面性与清晰度
   - Consider user expertise and context
     考虑用户专业知识和上下文

4. **Format Specification**:
   **格式规范**：
   - Define how reasoning should be presented
     定义应如何呈现推理
   - Consider structure and organization
     考虑结构和组织
   - Note any visualization or formatting preferences
     注意任何可视化或格式化偏好

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Process Clarity | Understandability of reasoning steps | User can restate key reasoning elements |
| Assumption Visibility | Transparency of underlying premises | All significant assumptions explicitly identified |
| Logic Traceability | Ability to follow chain of reasoning | Clear path from premises to conclusions |
| Appropriate Detail | Right level of depth for context | Sufficient without overwhelming |

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 过程清晰度 | 推理步骤的可理解性 | 用户可以重述关键推理元素 |
| 假设可见性 | 基础前提的透明度 | 所有重要假设都明确标识 |
| 逻辑可追溯性 | 遵循推理链的能力 | 从前提到结论的清晰路径 |
| 适当的细节 | 适合上下文的深度级别 | 足够但不过于繁琐 |

## 2. The Capability Boundary Protocol (2. 能力边界协议)

**When to use this protocol:**
Need to understand where AI systems can and can't perform reliably? This protocol guides you through capability mapping—perfect for reliability assessment, limitation understanding, confidence evaluation, or appropriate trust calibration.
**何时使用此协议：**
需要了解人工智能系统在哪些方面可以可靠地执行，哪些方面不行吗？该协议将指导您进行能力映射——非常适合可靠性评估、局限性理解、置信度评估或适当的信任校准。

```
Prompt: I'm implementing an AI assistant in our healthcare organization to help with administrative tasks, patient communication, and clinical information summarization. I need to clearly understand where the system is reliable and where it has limitations, particularly in a healthcare context where accuracy is critical. Help me map the capability boundaries so we can implement appropriate human oversight and verification steps.

Protocol:
/interpret.boundary{
    intent="Clearly map and communicate AI capability boundaries",
    input={
        domain="Healthcare administrative and information processing",
        application_context="Hospital setting with administrative, communication, and clinical information needs",
        critical_functions=[
            "Patient data summarization",
            "Medical information explanation",
            "Administrative process management",
            "Communication drafting and management",
            "Resource allocation suggestions"
        ],
        boundary_focus="Reliability boundaries, knowledge limitations, and uncertainty zones",
        risk_profile="High sensitivity due to healthcare context"
    },
    process=[
        /identify{
            action="Map capability and limitation landscape",
            elements=[
                "core strength areas and parameters",
                "known limitation categories",
                "uncertainty and ambiguity zones",
                "contextual performance variations",
                "knowledge boundary identification"
            ]
        },
        /assess{
            action="Evaluate boundary characteristics",
            approaches=[
                "reliability gradient mapping",
                "failure mode identification",
                "uncertainty trigger recognition",
                "context sensitivity analysis",
                "confidence calibration assessment"
            ]
        },
        /clarify{
            action="Communicate boundaries clearly",
            methods=[
                "capability distinction frameworks",
                "limitation explanation approaches",
                "uncertainty signaling mechanisms",
                "contextual qualification techniques",
                "appropriate confidence expression"
            ]
        },
        /recommend{
            action="Develop boundary management strategies",
            elements=[
                "human oversight integration points",
                "verification and validation processes",
                "failure prevention mechanisms",
                "escalation criteria and pathways",
                "continuous monitoring approaches"
            ]
        },
        /demonstrate{
            action="Illustrate boundaries through examples",
            approaches=[
                "clear capability examples",
                "boundary case demonstrations",
                "limitation scenario illustrations",
                "appropriate use case guidance",
                "misuse risk examples"
            ]
        }
    ],
    output={
        capability_map="Comprehensive assessment of system strengths and limitations",
        boundary_framework="Clear structure for understanding reliability zones",
        implementation_guidance="Recommendations for appropriate system deployment",
        oversight_strategy="Approach for human verification at boundary points"
    }
}
```

### Implementation Guide (实施指南)

1. **Domain Specification**:
   **领域规范**：
   - Clearly specify subject area
     清晰地指定主题领域
   - Note specific subdomains or specialties
     注意特定的子领域或专业
   - Consider knowledge requirements and challenges
     考虑知识要求和挑战

2. **Application Context Description**:
   **应用上下文描述**：
   - Describe usage environment and scenarios
     描述使用环境和场景
   - Note stakeholders and their needs
     注意利益相关者及其需求
   - Consider practical application factors
     考虑实际应用因素

3. **Critical Function Identification**:
   **关键功能识别**：
   - List key tasks and capabilities
     列出关键任务和能力
   - Prioritize based on importance and risk
     根据重要性和风险确定优先级
   - Consider both routine and edge cases
     考虑常规和边缘情况

4. **Boundary Focus Definition**:
   **边界焦点定义**：
   - Specify types of limitations to assess
     指定要评估的限制类型
   - Note specific concerns or priorities
     注意具体的关注点或优先级
   - Consider both known and potential limitations
     考虑已知和潜在的限制

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Boundary Clarity | Understandability of capability limits | Clear delineation between reliable and unreliable areas |
| Risk Recognition | Identification of potential failure points | Comprehensive coverage of high-risk boundaries |
| Implementation Guidance | Actionability of boundary management | Specific, practical oversight recommendations |
| Confidence Calibration | Accuracy of reliability self-assessment | High correlation between expressed and actual confidence |

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 边界清晰度 | 能力限制的可理解性 | 可靠和不可靠区域之间的清晰划分 |
| 风险识别 | 识别潜在的故障点 | 全面覆盖高风险边界 |
| 实施指导 | 边界管理的可操作性 | 具体、实用的监督建议 |
| 置信度校准 | 可靠性自我评估的准确性 | 表达的置信度与实际置信度之间的高度相关性 |

## 3. The Decision Explanation Protocol (3. 决策解释协议)

**When to use this protocol:**
Need to understand the factors and reasoning behind specific AI recommendations? This protocol guides you through decision transparency—perfect for recommendation explanation, choice justification, option evaluation, or decision auditing.
**何时使用此协议：**
需要了解人工智能具体建议背后的因素和推理吗？该协议将指导您实现决策透明度——非常适合推荐解释、选择理由、选项评估或决策审计。

```
Prompt: I'm using AI to help select investment opportunities for our portfolio, but I need complete transparency about how investment recommendations are made. I want to understand what factors are being considered, how they're weighted, and the underlying reasoning for any suggestions. This transparency is essential for our investment committee's due diligence process and regulatory compliance.

Protocol:
/interpret.decision{
    intent="Provide clear explanation of factors and reasoning behind specific recommendations",
    input={
        decision_context="Investment opportunity selection for portfolio management",
        recommendation_needs="Clear explanation of investment suggestions with comprehensive reasoning",
        explanation_dimensions=[
            "Factor identification and relevance",
            "Information weighting and prioritization",
            "Risk assessment methodology",
            "Comparative evaluation approach",
            "Confidence level and its basis"
        ],
        transparency_requirements="Sufficient detail for investment committee review and regulatory compliance",
        stakeholder_context="Financial professionals with investment expertise"
    },
    process=[
        /enumerate{
            action="Identify all relevant decision factors",
            elements=[
                "primary evaluation criteria",
                "information sources and inputs",
                "contextual considerations",
                "constraint factors",
                "uncertainty elements"
            ]
        },
        /evaluate{
            action="Explain factor assessment approach",
            methods=[
                "weighting methodology and rationale",
                "measurement and comparison approaches",
                "threshold and boundary definitions",
                "aggregation and integration techniques",
                "uncertainty handling strategies"
            ]
        },
        /trace{
            action="Show decision derivation process",
            elements=[
                "reasoning pathway visualization",
                "critical decision point identification",
                "alternative consideration explanation",
                "conclusion development tracking",
                "confidence calibration basis"
            ]
        },
        /justify{
            action="Provide recommendation rationale",
            approaches=[
                "evidence-conclusion connection clarity",
                "comparative advantage articulation",
                "limitation and risk acknowledgment",
                "confidence level explanation",
                "alternative consideration rationale"
            ]
        },
        /contextualize{
            action="Frame decision in appropriate context",
            elements=[
                "domain-specific considerations",
                "stakeholder requirement alignment",
                "practical implementation factors",
                "temporal and situational context",
                "limitation and boundary conditions"
            ]
        }
    ],
    output={
        decision_explanation="Clear articulation of investment recommendation rationale",
        factor_analysis="Detailed assessment of all relevant decision factors",
        methodology_transparency="Explicit description of evaluation approach",
        limitation_acknowledgment="Recognition of uncertainties and constraints"
    }
}
```

### Implementation Guide (实施指南)

1. **Decision Context Definition**:
   **决策上下文定义**：
   - Clearly specify decision domain and situation
     清晰地指定决策领域和情况
   - Define scope and boundaries
     定义范围和边界
   - Note specific contextual factors
     注意特定的上下文因素

2. **Recommendation Need Clarification**:
   **推荐需求澄清**：
   - Specify type of recommendations needed
     指定所需的推荐类型
   - Define success criteria
     定义成功标准
   - Consider practical application requirements
     考虑实际应用要求

3. **Explanation Dimension Selection**:
   **解释维度选择**：
   - Identify key aspects requiring transparency
     识别需要透明度的关键方面
   - Prioritize based on decision importance
     根据决策重要性确定优先级
   - Consider both process and outcome explanation
     考虑过程和结果的解释

4. **Transparency Requirement Definition**:
   **透明度要求定义**：
   - Specify necessary level of detail
     指定必要的细节级别
   - Note any compliance or audit needs
     注意任何合规性或审计需求
   - Consider stakeholder expectations
     考虑利益相关者的期望

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Factor Comprehensiveness | Coverage of relevant decision elements | All significant factors explicitly identified |
| Reasoning Clarity | Understandability of decision logic | Clear path from factors to recommendations |
| Contextualization Quality | Appropriateness for domain and stakeholders | Domain-relevant explanation with proper terminology |
| Confidence Transparency | Clarity about certainty levels | Explicit uncertainty and confidence assessment |

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 因素全面性 | 相关决策元素的覆盖范围 | 所有重要因素都明确标识 |
| 推理清晰度 | 决策逻辑的可理解性 | 从因素到建议的清晰路径 |
| 情境化质量 | 对领域和利益相关者的适宜性 | 具有适当术语的领域相关解释 |
| 置信度透明度 | 关于确定性水平的清晰度 | 明确的不确定性和置信度评估 |

## 4. The Model Attribution Protocol (4. 模型归因协议)

**When to use this protocol:**
Need to understand how AI systems derive their outputs from training or data? This protocol guides you through source and influence transparency—perfect for source attribution, influence understanding, novelty assessment, or originality evaluation.
**何时使用此协议：**
需要了解人工智能系统如何从训练或数据中得出其输出吗？该协议将指导您实现来源和影响的透明度——非常适合来源归因、影响理解、新颖性评估或原创性评估。

```
Prompt: I'm using AI to help with content creation for our marketing materials, and I need to understand the influences behind the content being generated. For compliance and intellectual property reasons, I need to know whether outputs are derived from specific sources, how novel they are, and what influences might be present in the generated content. This transparency is essential for our legal and brand integrity requirements.

Protocol:
/interpret.attribution{
    intent="Provide transparency about sources and influences behind AI outputs",
    input={
        content_domain="Marketing materials and creative content",
        attribution_concerns=[
            "Source identification and influence",
            "Degree of novelty and derivation",
            "Stylistic influences and patterns",
            "Conceptual origins and inspirations",
            "Training influence transparency"
        ],
        transparency_purpose="Legal compliance and brand integrity protection",
        required_detail="Sufficient for intellectual property assessment and attribution decisions"
    },
    process=[
        /analyze{
            action="Assess output characteristics and influences",
            elements=[
                "stylistic pattern identification",
                "conceptual source recognition",
                "structural influence assessment",
                "distinctive element analysis",
                "common pattern identification"
            ]
        },
        /describe{
            action="Explain influence landscape transparently",
            approaches=[
                "general influence category identification",
                "specific attribution assessment",
                "degree of derivation estimation",
                "novelty vs. convention balance",
                "multiple influence integration explanation"
            ]
        },
        /distinguish{
            action="Differentiate types of influence clearly",
            elements=[
                "direct vs. indirect influence distinction",
                "specific vs. general pattern recognition",
                "intentional vs. emergent similarity explanation",
                "structural vs. surface influence separation",
                "statistical vs. specific attribution"
            ]
        },
        /contextualize{
            action="Frame attribution appropriately",
            methods=[
                "domain convention explanation",
                "common practice articulation",
                "originality spectrum placement",
                "influence inevitability clarification",
                "practical implication assessment"
            ]
        },
        /advise{
            action="Provide attribution guidance",
            elements=[
                "appropriate attribution recommendations",
                "intellectual property risk assessment",
                "mitigation strategy suggestions",
                "documentation approach recommendations",
                "compliance guidance frameworks"
            ]
        }
    ],
    output={
        influence_analysis="Transparent assessment of content derivation and influences",
        attribution_guidance="Recommendations for appropriate source acknowledgment",
        novelty_assessment="Evaluation of content originality and derivation",
        compliance_considerations="Intellectual property and attribution risk guidance"
    }
}
```

### Implementation Guide (实施指南)

1. **Content Domain Specification**:
   **内容领域规范**：
   - Clearly specify the content area
     清晰地指定内容领域
   - Note specific genres or formats
     注意特定的体裁或格式
   - Consider creative vs. factual distinctions
     考虑创意与事实的区别

2. **Attribution Concern Identification**:
   **归因关注点识别**：
   - Specify key transparency needs
     指定关键的透明度需求
   - Prioritize based on legal or ethical importance
     根据法律或伦理重要性确定优先级
   - Consider both obvious and subtle influences
     考虑明显和微妙的影响

3. **Transparency Purpose Clarification**:
   **透明度目的澄清**：
   - Define why attribution matters in this context
     定义为什么归因在此上下文中很重要
   - Note specific requirements or regulations
     注意具体的要求或规定
   - Consider stakeholder expectations
     考虑利益相关者的期望

4. **Detail Requirement Definition**:
   **细节要求定义**：
   - Specify necessary level of attribution granularity
     指定必要的归因粒度级别
   - Note practical application needs
     注意实际应用需求
   - Consider documentation requirements
     考虑文档要求

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Influence Transparency | Clarity about content derivation | Explicit identification of significant influences |
| Attribution Accuracy | Correctness of source recognition | Appropriate distinction between specific and general attribution |
| Novelty Clarity | Transparency about originality | Clear assessment of derivative vs. original elements |
| Guidance Practicality | Usefulness of attribution recommendations | Actionable advice for appropriate attribution |

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 影响透明度 | 内容派生的清晰度 | 明确识别重大影响 |
| 归因准确性 | 来源识别的正确性 | 适当区分特定归因和一般归因 |
| 新颖性清晰度 | 原创性的透明度 | 清晰评估派生元素与原创元素 |
| 指导实用性 | 归因建议的有用性 | 针对适当归因的可操作建议 |

## 5. The Confidence Calibration Protocol (5. 置信度校准协议)

**When to use this protocol:**
Need to understand how certain AI systems are about their outputs? This protocol guides you through uncertainty transparency—perfect for reliability assessment, confidence evaluation, certainty communication, or appropriate trust calibration.
**何时使用此协议：**
需要了解人工智能系统对其输出的确定性如何吗？该协议将指导您实现不确定性透明度——非常适合可靠性评估、置信度评估、确定性沟通或适当的信任校准。

```
Prompt: I'm implementing an AI system to help with medical diagnosis support for our clinical team. In this critical healthcare context, I need complete transparency about the system's confidence in its suggestions, clear communication about uncertainty, and explicit identification of when human judgment is essential. Help me establish a reliable confidence calibration framework that our clinicians can trust.

Protocol:
/interpret.confidence{
    intent="Provide transparency about certainty levels and confidence calibration",
    input={
        application_domain="Medical diagnosis support for clinical teams",
        confidence_dimensions=[
            "Diagnostic suggestion reliability",
            "Evidence strength assessment",
            "Knowledge boundary recognition",
            "Ambiguity and uncertainty identification",
            "Confidence calibration accuracy"
        ],
        calibration_purpose="Ensure appropriate clinician trust and judgment integration",
        risk_context="High-stakes healthcare environment with potential patient impact"
    },
    process=[
        /assess{
            action="Evaluate confidence factors comprehensively",
            elements=[
                "knowledge coverage assessment",
                "evidence quality evaluation",
                "reasoning reliability analysis",
                "ambiguity recognition",
                "limitation boundary identification"
            ]
        },
        /quantify{
            action="Measure and express confidence appropriately",
            approaches=[
                "confidence level articulation",
                "uncertainty quantification methods",
                "probability expression frameworks",
                "confidence interval communication",
                "limitation boundary measurement"
            ]
        },
        /explain{
            action="Communicate confidence foundations clearly",
            methods=[
                "confidence basis explanation",
                "uncertainty source identification",
                "knowledge limitation articulation",
                "alternative possibility exploration",
                "confidence calibration transparency"
            ]
        },
        /calibrate{
            action="Ensure appropriate confidence levels",
            techniques=[
                "overconfidence prevention mechanisms",
                "appropriate hesitation signals",
                "confidence-evidence alignment",
                "domain-appropriate certainty calibration",
                "context-sensitive confidence adaptation"
            ]
        },
        /guide{
            action="Provide confidence-based usage guidance",
            elements=[
                "human judgment integration recommendations",
                "verification requirement identification",
                "appropriate reliance guidelines",
                "confidence threshold frameworks",
                "escalation criteria based on uncertainty"
            ]
        }
    ],
    output={
        confidence_framework="Comprehensive approach to certainty communication",
        uncertainty_assessment="Transparent evaluation of suggestion reliability",
        verification_guidance="Recommendations for human oversight based on confidence",
        confidence_explanation="Clear articulation of certainty level bases"
    }
}
```

### Implementation Guide (实施指南)

1. **Domain Specification**:
   **领域规范**：
   - Clearly specify application area
     清晰地指定应用领域
   - Note specific subject matter
     注意具体的主题
   - Consider stakes and risk factors
     考虑利害关系和风险因素

2. **Confidence Dimension Selection**:
   **置信度维度选择**：
   - Identify key aspects requiring calibration
     识别需要校准的关键方面
   - Prioritize based on decision importance
     根据决策重要性确定优先级
   - Consider both absolute and relative confidence
     考虑绝对和相对置信度

3. **Calibration Purpose Clarification**:
   **校准目的澄清**：
   - Define specific goals for confidence transparency
     为置信度透明度定义具体目标
   - Note stakeholder needs and expectations
     注意利益相关者的需求和期望
   - Consider trust and reliability requirements
     考虑信任和可靠性要求

4. **Risk Context Description**:
   **风险上下文描述**：
   - Specify stakes and potential consequences
     指定利害关系和潜在后果
   - Note appropriate caution level
     注意适当的谨慎级别
   - Consider domain-specific risk factors
     考虑特定领域的风险因素

### Performance Metrics (性能指标)

| Metric | Description | Target |
|--------|-------------|--------|
| Calibration Accuracy | Alignment between expressed and actual confidence | High correlation between confidence and correctness |
| Uncertainty Transparency | Clarity about knowledge limitations | Explicit identification of uncertain areas |
| Guidance Specificity | Clarity of verification recommendations | Actionable oversight suggestions based on confidence |
| Appropriate Caution | Risk-appropriate confidence expression | Conservatism in high-stakes contexts |

| 指标 | 描述 | 目标 |
|--------|-------------|--------|
| 校准准确性 | 表达的置信度与实际置信度之间的一致性 | 置信度与正确性之间的高度相关性 |
| 不确定性透明度 | 关于知识局限性的清晰度 | 明确识别不确定区域 |
| 指导特异性 | 验证建议的清晰度 | 基于置信度的可操作监督建议 |
| 适当的谨慎 | 适合风险的置信度表达 | 在高风险情境下的保守性 |

## 6. The Knowledge Representation Protocol (6. 知识表示协议)

**When to use this protocol:**
Need to understand how AI systems represent and organize information? This protocol guides you through knowledge structure transparency—perfect for mental model understanding, knowledge organization insight, concept relationship mapping, or information architecture transparency.
**何时使用此协议：**
需要了解人工智能系统如何表示和组织信息吗？该协议将指导您实现知识结构透明度——非常适合心智模型理解、知识组织洞察、概念关系映射或信息架构透明度。

```
Prompt: I'm working with an AI system to develop an educational curriculum on climate science, and I need to understand how the system organizes and represents knowledge in this domain. I want visibility into conceptual relationships, information hierarchies, and knowledge structures so I can ensure the curriculum has appropriate progression and coherence. This transparency will help me create more effective educational materials.

Protocol:
/interpret.knowledge{
    intent="Provide transparency about knowledge representation and organization",
    input={
        knowledge_domain="Climate science for educational curriculum development",
        representation_interests=[
            "Conceptual relationship mapping",
            "Information hierarchy structures",
            "Prerequisite knowledge chains",
            "Cross-disciplinary connections",
            "Knowledge progression pathways"
        ],
        transparency_purpose="Creating coherent, well-structured educational materials",
        application_context="Curriculum development for diverse educational levels"
    },
    process=[
        /map{
            action="Reveal knowledge organization structures",
            elements=[
                "conceptual relationship visualization",
                "hierarchical knowledge mapping",
                "prerequisite chain identification",
                "connection network representation",
                "cluster and category recognition"
            ]
        },
        /explain{
            action="Clarify knowledge structure rationale",
            approaches=[
                "organizational logic articulation",
                "relationship basis explanation",
                "hierarchy justification",
                "connection significance description",
                "boundary and category rationale"
            ]
        },
        /analyze{
            action="Assess knowledge representation characteristics",
            dimensions=[
                "completeness evaluation",
                "coherence assessment",
                "progressive structure analysis",
                "cross-connection density examination",
                "representational bias recognition"
            ]
        },
        /adapt{
            action="Contextu
```