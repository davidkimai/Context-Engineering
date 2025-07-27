# Attractor Design Template （吸引子设计模板）

## Summary （摘要）
A template for creating semantic attractors that guide AI reasoning toward specific conceptual frameworks, approaches, or outcomes without explicit instruction.
一个用于创建语义吸引子的模板，它可以在没有明确指令的情况下，引导 AI 推理趋向特定的概念框架、方法或结果。

## Context & Application （背景与应用）
Use this template when you want to subtly guide AI reasoning toward specific types of responses by creating "attractors" in the semantic space—conceptual gravity wells that naturally pull thinking in certain directions. Unlike direct instructions, attractors work by establishing patterns that the AI naturally continues or completes.
当您希望通过在语义空间中创建“吸引子”来巧妙地引导 AI 推理趋向特定类型的响应时，请使用此模板——这些概念引力井自然地将思维拉向特定方向。与直接指令不同，吸引子通过建立 AI 自然延续或完成的模式来发挥作用。

This template is ideal for:
此模板非常适合：
- Encouraging particular thinking styles or frameworks without explicitly requiring them
- 鼓励特定的思维方式或框架，而无需明确要求它们
- Creating subtle guidance that feels natural rather than forced
- 创建感觉自然而非强制的微妙指导
- Establishing "centers of gravity" for reasoning to orbit around
- 为推理建立“重心”以围绕其运行
- Guiding reasoning while preserving flexibility and creativity
- 在引导推理的同时保留灵活性和创造力
- Influencing without dictating specific outcomes
- 在不规定具体结果的情况下施加影响

## Template Structure （模板结构）

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following concepts may be relevant to consider:*

{{primary_attractor_concept_1}}:
- {{supporting_element_1a}}
- {{supporting_element_1b}}
- {{supporting_element_1c}}

{{primary_attractor_concept_2}}:
- {{supporting_element_2a}}
- {{supporting_element_2b}}
- {{supporting_element_2c}}

{{resonant_concept}}:
- {{resonant_element_a}}
- {{resonant_element_b}}

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
{{output_specifications}}
```

## Parameters （参数）

- `{{task_description}}`: Description of the task that doesn't explicitly mention the attractor concepts
- `{{task_description}}`：任务描述，不明确提及吸引子概念
- `{{neutral_context}}`: Background information that establishes context without biasing toward the attractors
- `{{neutral_context}}`：建立上下文的背景信息，不偏向吸引子
- `{{primary_attractor_concept_X}}`: Main concept(s) you want to function as semantic attractors
- `{{primary_attractor_concept_X}}`：您希望作为语义吸引子的主要概念
- `{{supporting_element_X}}`: Elements that reinforce and define the attractor concept
- `{{supporting_element_X}}`：强化和定义吸引子概念的元素
- `{{resonant_concept}}`: A concept that resonates with and amplifies the primary attractors
- `{{resonant_concept}}`：与主要吸引子产生共鸣并放大其作用的概念
- `{{output_specifications}}`: Format and structure specifications for the output
- `{{output_specifications}}`：输出的格式和结构规范

## Examples （示例）

### Example 1: Systems Thinking Attractor （示例 1：系统思维吸引子）

```
# Task: Analyze the challenges facing urban transportation in growing cities

## Context
Urban areas worldwide are experiencing population growth, putting pressure on existing transportation infrastructure. Many cities are seeking solutions to mobility challenges.

## Conceptual Framework
*The following concepts may be relevant to consider:*

Interconnectedness:
- Relationship between transportation and land use
- Impact of transportation choices on environmental systems
- Connection between mobility and economic opportunity

Feedback Loops:
- How infrastructure investments shape development patterns
- Relationship between congestion and behavior adaptation
- Environmental impacts that affect future transportation choices

Emergence:
- Patterns that arise from individual transportation decisions
- Unexpected consequences of transportation policies
- Self-organizing aspects of urban mobility

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
A comprehensive analysis of urban transportation challenges that identifies key issues, explores underlying dynamics, and suggests potential approaches. Include both short-term and long-term perspectives.
```

```
# 任务：分析发展中城市面临的城市交通挑战

## 背景
全球城市地区正在经历人口增长，给现有交通基础设施带来压力。许多城市正在寻求解决出行挑战的方案。

## 概念框架
*以下概念可能与考虑相关：*

相互关联性：
- 交通与土地利用之间的关系
- 交通选择对环境系统的影响
- 出行与经济机会之间的联系

反馈循环：
- 基础设施投资如何塑造发展模式
- 拥堵与行为适应之间的关系
- 影响未来交通选择的环境影响

涌现：
- 源于个人交通决策的模式
- 交通政策的意外后果
- 城市出行的自组织方面

## 方法
在您的分析中考虑上述概念，并根据任务适当纳入它们。

## 预期输出
对城市交通挑战进行全面分析，识别关键问题，探索潜在动态，并提出潜在方法。包括短期和长期视角。
```

### Example 2: Creative Innovation Attractor （示例 2：创意创新吸引子）

```
# Task: Suggest product improvement ideas for a smart home thermostat

## Context
Smart thermostats have become increasingly common in homes, allowing temperature programming, remote control, and some learning capabilities. The company is looking to develop their next generation product.

## Conceptual Framework
*The following concepts may be relevant to consider:*

Boundary Breaking:
- Extending functionality beyond traditional temperature control
- Integration with unexpected systems or services
- Challenging assumptions about what a thermostat should be

Recombination:
- Merging features from different product categories
- Novel combinations of existing technologies
- Unexpected applications of familiar capabilities

User-Centered Surprise:
- Features that anticipate needs users didn't know they had
- Delightful interactions that exceed expectations
- Transformative experiences rather than incremental improvements

## Approach
Consider the above concepts in your analysis, incorporating them as appropriate to the task.

## Expected Output
A list of 5-7 innovative product improvement ideas, each with a brief description, potential user benefit, and implementation considerations. Focus on distinctive ideas rather than obvious incremental improvements.
```

```
# 任务：为智能家居恒温器提出产品改进想法

## 背景
智能恒温器在家庭中越来越普遍，允许温度编程、远程控制和一些学习功能。该公司正在寻求开发其下一代产品。

## 概念框架
*以下概念可能与考虑相关：*

打破边界：
- 将功能扩展到传统温度控制之外
- 与意想不到的系统或服务集成
- 挑战关于恒温器应该是什么的假设

重组：
- 合并不同产品类别的功能
- 现有技术的新颖组合
- 熟悉功能的意外应用

以用户为中心的惊喜：
- 预测用户不知道自己有需求的功能
- 超出预期的愉悦互动
- 变革性体验而非渐进式改进

## 方法
在您的分析中考虑上述概念，并根据任务适当纳入它们。

## 预期输出
5-7 个创新产品改进想法的列表，每个想法都附有简要描述、潜在用户利益和实施考虑。侧重于独特的想法，而不是明显的渐进式改进。
```

## Variations （变体）

### Multi-Attractor Field （多吸引子场）
For creating multiple attractors with different strengths:
用于创建具有不同强度的多个吸引子：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following concepts may be relevant to consider (in no particular order):*

{{primary_attractor}} [strength: high]:
- {{supporting_elements}}

{{secondary_attractor}} [strength: medium]:
- {{supporting_elements}}

{{tertiary_attractor}} [strength: low]:
- {{supporting_elements}}

## Approach
Consider these concepts in your response, giving each appropriate consideration.

## Expected Output
{{output_specifications}}
```

### Attractor-Repeller Dynamics （吸引子-排斥子动力学）
For creating both attractive and repulsive conceptual forces:
用于创建吸引和排斥的概念力：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*Consider the following as you develop your response:*

Relevant Approaches:
- {{attractor_concept_1}}
- {{attractor_concept_2}}
- {{attractor_concept_3}}

Approaches to Avoid:
- {{repeller_concept_1}}
- {{repeller_concept_2}}

## Approach
Develop your response drawing from the relevant approaches while avoiding the limitations of approaches to avoid.

## Expected Output
{{output_specifications}}
```

### Resonant Field Attractor （共振场吸引子）
For creating mutually reinforcing concepts that amplify each other:
用于创建相互增强的概念，使其相互放大：

```
# Task: {{task_description}}

## Context
{{neutral_context}}

## Conceptual Framework
*The following interconnected concepts may be relevant:*

{{concept_1}} ↔ {{concept_2}}:
- How {{concept_1}} influences {{concept_2}}
- How {{concept_2}} reinforces {{concept_1}}

{{concept_2}} ↔ {{concept_3}}:
- Ways {{concept_2}} shapes {{concept_3}}
- Ways {{concept_3}} enhances {{concept_2}}

{{concept_3}} ↔ {{concept_1}}:
- The relationship between {{concept_3}} and {{concept_1}}
- Mutual amplification effects

## Approach
Consider these resonant relationships in your analysis.

## Expected Output
{{output_specifications}}
```

## Best Practices （最佳实践）

- **Be subtle rather than heavy-handed** - attractors work best when they feel like natural considerations rather than forced requirements
- **要微妙而非强硬** - 吸引子在感觉像是自然考虑而非强制要求时效果最佳
- **Create coherent attractor fields** - use concepts that naturally complement each other
- **创建连贯的吸引子场** - 使用自然互补的概念
- **Balance specificity and openness** - too vague won't create enough pull, too specific becomes prescriptive
- **平衡特异性和开放性** - 过于模糊不会产生足够的吸引力，过于具体则会变成规定性
- **Use supporting elements to define attractors clearly** - help establish exactly what the attractor concept encompasses
- **使用支持元素清晰定义吸引子** - 帮助准确确定吸引子概念的范围
- **Position attractors as "concepts to consider" rather than requirements** - preserves flexibility while creating subtle gravity
- **将吸引子定位为“要考虑的概念”而非要求** - 在创建微妙引力的同时保留灵活性
- **Use familiar concepts as bridges to unfamiliar ones** - helps create paths to novel thinking
- **使用熟悉的概念作为通向不熟悉概念的桥梁** - 有助于开辟新颖思维的路径
- **For complex tasks, use multiple resonant attractors** - creates a rich conceptual field
- **对于复杂任务，使用多个共振吸引子** - 创建丰富的概念场
- **Test attractor strength** - if too weak, enhance supporting elements; if too dominant, reduce specificity
- **测试吸引子强度** - 如果太弱，增强支持元素；如果太强，降低特异性
- **Align attractors with the true goal** - the pull should lead toward genuinely useful approaches
- **将吸引子与真实目标对齐** - 吸引力应导向真正有用的方法
- **Design attractors to be discovery-friendly** - they should feel like insights rather than instructions
- **设计吸引子以利于发现** - 它们应该感觉像是洞察力而非指令

## Related Templates （相关模板）

- **Field Boundary Establishment Template**: For creating conceptual boundaries to complement attractors
- **场边界建立模板**：用于创建概念边界以补充吸引子
- **Resonance Prompting Template**: For creating resonant effects between concepts
- **共振提示模板**：用于在概念之间创建共振效应
- **Persona Attractor Template**: For using personas as semantic attractors
- **角色吸引子模板**：用于将角色作为语义吸引子
- **Emergence Engineering Template**: For fostering emergent properties through attractor fields
- **涌现工程模板**：用于通过吸引子场培养涌现特性