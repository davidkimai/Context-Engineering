# Minimal Context Template （最小上下文模板）

## Summary （摘要）
A streamlined template for creating minimal but effective context for AI systems, focusing on clarity and essential information.
一个精简的模板，用于为 AI 系统创建最小但有效的上下文，侧重于清晰度和基本信息。

## Context & Application （背景与应用）
Use this template when you need to provide just enough context for an AI system to perform effectively without unnecessary information. It establishes clear boundaries, expectations, and essential information in a structured format.
当您需要为 AI 系统提供恰到好处的上下文，使其有效运行而无需不必要的信息时，请使用此模板。它以结构化格式建立清晰的边界、期望和基本信息。

This template is ideal for:
此模板非常适合：
- First-time interactions with AI systems
- 首次与 AI 系统交互
- Well-defined tasks with clear deliverables
- 具有明确可交付成果的明确任务
- Situations where minimizing prompt length is important
- 最小化提示长度很重要的场景
- Establishing a baseline for more complex prompts
- 为更复杂的提示建立基线

## Template Structure （模板结构）

```
# Task: {{specific_task}}

## Context
- {{key_background_point_1}}
- {{key_background_point_2}}
- {{additional_context_if_needed}}

## Constraints
- {{constraint_1}}
- {{constraint_2}}

## Expected Output
- Format: {{output_format}}
- Length: {{approximate_length}}
- Style: {{style_guidelines}}

## Examples
{{optional_example}}
```

## Parameters （参数）

- `{{specific_task}}`: Clear description of what you want the AI to do (e.g., "Write a product description" or "Analyze the following data")
- `{{specific_task}}`：您希望 AI 执行任务的清晰描述（例如，“撰写产品描述”或“分析以下数据”）
- `{{key_background_point_X}}`: Essential information needed to complete the task correctly (limit to 2-4 points)
- `{{key_background_point_X}}`：正确完成任务所需的基本信息（限制在 2-4 点）
- `{{constraint_X}}`: Limitations or requirements that must be followed (e.g., "Do not include pricing information")
- `{{constraint_X}}`：必须遵守的限制或要求（例如，“不包含定价信息”）
- `{{output_format}}`: The structure, format or file type for the output (e.g., "Bulleted list" or "JSON object")
- `{{output_format}}`：输出的结构、格式或文件类型（例如，“项目符号列表”或“JSON 对象”）
- `{{approximate_length}}`: Guidelines on how extensive the output should be (e.g., "300-400 words" or "5 bullet points")
- `{{approximate_length}}`：关于输出应有多广泛的指南（例如，“300-400 字”或“5 个项目符号”）
- `{{style_guidelines}}`: Tone, voice, and stylistic expectations (e.g., "Professional and formal" or "Conversational and engaging")
- `{{style_guidelines}}`：语气、语调和风格期望（例如，“专业和正式”或“会话和引人入胜”）
- `{{optional_example}}`: A sample of the expected output (highly recommended for first-time tasks)
- `{{optional_example}}`：预期输出的示例（强烈建议用于首次任务）

## Examples （示例）

### Example 1: Data Analysis Report （示例 1：数据分析报告）

```
# Task: Analyze the provided sales data and create a summary report

## Context
- Data represents quarterly sales figures for 2022
- Company has 3 product lines: Basic, Premium, and Enterprise
- Previous year showed seasonal trends with Q4 strongest

## Constraints
- Focus on significant changes year-over-year
- Do not speculate beyond what the data shows
- Include at least one actionable recommendation

## Expected Output
- Format: Executive summary followed by bullet points
- Length: Approximately 300-400 words
- Style: Professional, data-focused, actionable

## Examples
Executive Summary:
Q2 2022 shows a 15% increase in overall sales compared to Q2 2021, with the Premium product line showing the strongest growth at 23%. This continues the upward trend observed in Q1...
```

```
# 任务：分析提供的销售数据并创建摘要报告

## 背景
- 数据代表 2022 年的季度销售额
- 公司有 3 条产品线：基础版、高级版和企业版
- 去年显示出季节性趋势，第四季度最强

## 约束
- 关注同比显著变化
- 不要超出数据显示的范围进行推测
- 至少包含一项可操作的建议

## 预期输出
- 格式：执行摘要，后跟项目符号
- 长度：约 300-400 字
- 风格：专业、以数据为中心、可操作

## 示例
执行摘要：
2022 年第二季度总销售额比 2021 年第二季度增长 15%，其中高级产品线增长最强劲，达到 23%。这延续了第一季度观察到的上升趋势……
```

### Example 2: Creative Content Creation （示例 2：创意内容创作）

```
# Task: Write a product description for our new wireless headphones

## Context
- Target audience: tech-savvy professionals ages 25-40
- Key features: noise cancellation, 30-hour battery life, voice assistant integration
- Main selling points: comfort for all-day wear, premium sound quality

## Constraints
- Keep technical specifications to a minimum
- Don't mention competitors by name
- Focus on benefits, not just features

## Expected Output
- Format: Two paragraphs of flowing text
- Length: 150-200 words
- Style: Modern, enthusiastic but not overly promotional

## Examples
Experience music as it was meant to be heard with our new XDR Wireless Headphones. Designed for professionals who demand the best, these headphones deliver crystal-clear sound while intelligent noise cancellation technology creates your own personal sanctuary of sound—whether you're in a busy office or on a crowded commute...
```

```
# 任务：为我们的新款无线耳机撰写产品描述

## 背景
- 目标受众：25-40 岁的精通技术的专业人士
- 主要特点：降噪、30 小时电池续航、语音助手集成
- 主要卖点：全天佩戴舒适、优质音质

## 约束
- 将技术规格保持在最低限度
- 不要提及竞争对手的名称
- 侧重于优点，而不仅仅是功能

## 预期输出
- 格式：两段流畅的文本
- 长度：150-200 字
- 风格：现代、热情但不过度宣传

## 示例
使用我们全新的 XDR 无线耳机，体验音乐本应有的听觉享受。这些耳机专为追求卓越的专业人士设计，提供水晶般清晰的声音，同时智能降噪技术为您打造专属的个人声音圣殿——无论您是在繁忙的办公室还是拥挤的通勤路上……
```

## Variations （变体）

### Technical Specification Template （技术规范模板）
For technical tasks requiring precise instructions:
对于需要精确指令的技术任务：

```
# Task: {{specific_technical_task}}

## Context
- {{technical_background_point_1}}
- {{technical_background_point_2}}
- {{system_dependencies}}

## Requirements
- {{functional_requirement_1}}
- {{functional_requirement_2}}
- {{performance_requirement}}

## Technical Constraints
- {{technical_limitation_1}}
- {{compatibility_requirement}}

## Expected Output
- Format: {{technical_format}}
- Testing Criteria: {{validation_method}}
- Documentation: {{documentation_requirements}}

## Examples
{{technical_example}}
```

### Creative Brief Template （创意简报模板）
For creative tasks like writing or design:
对于写作或设计等创意任务：

```
# Task: {{creative_task}}

## Context
- Audience: {{target_audience}}
- Purpose: {{communication_goal}}
- Brand Voice: {{brand_personality}}

## Creative Direction
- {{inspiration_point_1}}
- {{inspiration_point_2}}
- {{emotional_response_desired}}

## Constraints
- {{brand_guideline_1}}
- {{content_restriction}}
- {{technical_limitation}}

## Expected Output
- Format: {{creative_format}}
- Length/Size: {{dimension_guidelines}}
- Style: {{stylistic_direction}}

## Examples
{{creative_example}}
```

## Best Practices （最佳实践）

- **Be specific about the task** - Avoid vague instructions like "write something about headphones"; instead use "write a product description for wireless headphones targeting young professionals"
- **具体说明任务** - 避免模糊的指令，例如“写一些关于耳机的东西”；而是使用“为针对年轻专业人士的无线耳机撰写产品描述”
- **Provide only necessary context** - Excessive information can dilute focus and lead to less relevant outputs
- **仅提供必要的上下文** - 过多的信息会分散注意力，导致输出的相关性降低
- **Use bullet points for clarity** - Breaking information into bullet points makes it easier to process than dense paragraphs
- **使用项目符号以提高清晰度** - 将信息分解为项目符号比密集的段落更容易处理
- **Include at least one example** whenever possible - Examples dramatically improve understanding of expectations
- **尽可能包含至少一个示例** - 示例能显著提高对期望的理解
- **List constraints explicitly** rather than embedding them in paragraphs - Makes them harder to miss
- **明确列出约束**，而不是将其嵌入段落中 - 这样更不容易遗漏
- **For complex tasks, break down into clear steps** or components - Helps maintain focus and structure
- **对于复杂任务，分解为清晰的步骤**或组件 - 有助于保持重点和结构
- **Match context to output expectations** - Ensure the context provided supports the expected output format and style
- **将上下文与输出期望匹配** - 确保提供的上下文支持预期的输出格式和样式

## Related Templates （相关模板）

- **Few-Shot Learning Template**: When you need to teach the AI through multiple examples
- **少样本学习模板**：当您需要通过多个示例教授 AI 时
- **Chain of Thought Template**: When the task requires step-by-step reasoning
- **思维链模板**：当任务需要逐步推理时
- **Persona-Based Context Template**: When adopting a specific role or perspective would improve results
- **基于角色的上下文模板**：当采用特定角色或视角可以改善结果时