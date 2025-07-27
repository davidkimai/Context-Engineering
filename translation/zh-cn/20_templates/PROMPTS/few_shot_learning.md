# Few-Shot Learning Template （少样本学习模板）

## Summary （摘要）
A template for teaching AI systems through examples, enabling them to learn patterns and apply them to new cases without explicit instructions.
一个通过示例教授 AI 系统的模板，使其能够在没有明确指令的情况下学习模式并将其应用于新案例。

## Context & Application （背景与应用）
Use this template when you want the AI to learn from examples rather than from explicit rules or instructions. Few-shot learning is powerful because it shows rather than tells, allowing the AI to infer patterns and apply them to new situations.
当您希望 AI 从示例而不是明确的规则或指令中学习时，请使用此模板。少样本学习功能强大，因为它通过展示而非讲述的方式，使 AI 能够推断模式并将其应用于新情况。

This template is ideal for:
此模板非常适合：
- Tasks that are difficult to explain but easy to demonstrate
- 难以解释但易于演示的任务
- Pattern-based tasks where examples communicate the pattern better than rules
- 基于模式的任务，其中示例比规则更能传达模式
- Situations where you want consistent formatting or style
- 您希望格式或样式保持一致的情况
- Teaching nuanced judgments or classifications
- 教授细微的判断或分类

## Template Structure （模板结构）

```
# Task: {{task_description}}

## Examples

### Example 1
Input: {{input_1}}
Output: {{output_1}}

### Example 2
Input: {{input_2}}
Output: {{output_2}}

### Example 3
Input: {{input_3}}
Output: {{output_3}}

## Your Turn
Input: {{new_input}}
Output:
```

## Parameters （参数）

- `{{task_description}}`: Brief description of the task to perform (e.g., "Classify the sentiment of these reviews")
- `{{task_description}}`：要执行任务的简要描述（例如，“对这些评论的情绪进行分类”）
- `{{input_X}}`: Example inputs that demonstrate the pattern (3-5 examples recommended)
- `{{input_X}}`：演示模式的示例输入（建议 3-5 个示例）
- `{{output_X}}`: Corresponding outputs that show the expected response for each input
- `{{output_X}}`：显示每个输入预期响应的相应输出
- `{{new_input}}`: The new case you want the AI to handle using the pattern it learned
- `{{new_input}}`：您希望 AI 使用其学习到的模式处理的新案例

## Examples （示例）

### Example 1: Sentiment Classification （示例 1：情感分类）

```
# Task: Classify the sentiment of customer feedback as positive, negative, or neutral

## Examples

### Example 1
Input: "The product arrived on time and works perfectly. Couldn't be happier with my purchase!"
Output: Positive

### Example 2
Input: "Delivery was quick but the product has several scratches on the surface."
Output: Neutral

### Example 3
Input: "Terrible customer service. Had to call three times and still haven't resolved my issue."
Output: Negative

## Your Turn
Input: "Package was delivered two days late, but the quality of the item exceeded my expectations."
Output:
```

```
# 任务：将客户反馈的情绪分类为积极、消极或中性

## 示例

### 示例 1
输入：“产品按时送达，运行完美。对我的购买非常满意！”
输出：积极

### 示例 2
输入：“交货很快，但产品表面有几处划痕。”
输出：中性

### 示例 3
输入：“糟糕的客户服务。不得不打了三次电话，问题仍未解决。”
输出：消极

## 轮到你了
输入：“包裹迟了两天送达，但物品质量超出了我的预期。”
输出：
```

### Example 2: Data Transformation （示例 2：数据转换）

```
# Task: Convert the given product information into a standardized JSON format

## Examples

### Example 1
Input: 
Product: Wireless Headphones
Brand: SoundCore
Price: $79.99
Features: Noise cancellation, 30-hour battery, Bluetooth 5.0

Output:
```json
{
  "product_name": "Wireless Headphones",
  "manufacturer": "SoundCore",
  "price_usd": 79.99,
  "specifications": [
    "Noise cancellation",
    "30-hour battery",
    "Bluetooth 5.0"
  ]
}
```

### Example 2
Input:
Product: Smart Watch Pro
Brand: TechFit
Price: $129.95
Features: Heart rate monitor, GPS tracking, Water resistant

Output:
```json
{
  "product_name": "Smart Watch Pro",
  "manufacturer": "TechFit",
  "price_usd": 129.95,
  "specifications": [
    "Heart rate monitor",
    "GPS tracking",
    "Water resistant"
  ]
}
```

## Your Turn
Input:
Product: Portable Bluetooth Speaker
Brand: AudioMax
Price: $45.50
Features: Waterproof, 12-hour playback, Built-in microphone

Output:
```

```
# 任务：将给定的产品信息转换为标准化的 JSON 格式

## 示例

### 示例 1
输入：
产品：无线耳机
品牌：SoundCore
价格：$79.99
特点：降噪，30 小时电池续航，蓝牙 5.0

输出：
```json
{
  "product_name": "无线耳机",
  "manufacturer": "SoundCore",
  "price_usd": 79.99,
  "specifications": [
    "降噪",
    "30 小时电池续航",
    "蓝牙 5.0"
  ]
}
```

### 示例 2
输入：
产品：智能手表 Pro
品牌：TechFit
价格：$129.95
特点：心率监测，GPS 跟踪，防水

输出：
```json
{
  "product_name": "智能手表 Pro",
  "manufacturer": "TechFit",
  "price_usd": 129.95,
  "specifications": [
    "心率监测",
    "GPS 跟踪",
    "防水"
  ]
}
```

## 轮到你了
输入：
产品：便携式蓝牙音箱
品牌：AudioMax
价格：$45.50
特点：防水，12 小时播放，内置麦克风

输出：
```

```

## Variations （变体）

### Zero-Shot Extension （零样本扩展）
For when you have no examples but can describe the pattern:
当您没有示例但可以描述模式时：

```
# Task: {{task_description}}

## Pattern
{{detailed_pattern_description}}

## Format
{{output_format_specification}}

## Your Turn
Input: {{new_input}}
Output:
```

### One-Shot Learning （单样本学习）
For simple patterns that can be communicated with a single example:
对于可以通过单个示例进行交流的简单模式：

```
# Task: {{task_description}}

## Example
Input: {{input_example}}
Output: {{output_example}}

## Your Turn
Input: {{new_input}}
Output:
```

### Many-Shot Learning （多样本学习）
For complex patterns requiring many examples:
对于需要许多示例的复杂模式：

```
# Task: {{task_description}}

## Examples
[Examples 1-10 formatted as input/output pairs]

## Test Cases
[Additional examples to validate understanding]

## Your Turn
Input: {{new_input}}
Output:
```

## Best Practices （最佳实践）

- **Use diverse examples** that cover different cases and edge conditions
- **使用多样化的示例**，涵盖不同的情况和边缘条件
- **Order examples strategically** from simple to complex to build understanding
- **策略性地排序示例**，从简单到复杂，以建立理解
- **Include 3-5 examples** for most tasks (fewer for simple patterns, more for complex ones)
- **大多数任务包含 3-5 个示例**（简单模式少一些，复杂模式多一些）
- **Ensure consistency** in formatting across all examples
- **确保所有示例的格式一致性**
- **Choose representative examples** that clearly demonstrate the pattern
- **选择能清晰展示模式的代表性示例**
- **Make examples distinct enough** to highlight the pattern rather than superficial similarities
- **使示例足够独特**，以突出模式而不是表面相似性
- **For classification tasks**, include examples of all possible categories
- **对于分类任务**，包括所有可能类别的示例
- **For generative tasks**, show range in style, length, and content as appropriate
- **对于生成任务**，酌情展示风格、长度和内容的范围
- **Test the pattern** by trying different inputs to ensure the AI has properly learned it
- **通过尝试不同的输入来测试模式**，以确保 AI 已正确学习它

## Related Templates （相关模板）

- **Minimal Context Template**: When examples aren't necessary and direct instructions suffice
- **最小上下文模板**：当不需要示例且直接指令足够时
- **Chain of Thought Template**: When you need to demonstrate reasoning processes step-by-step
- **思维链模板**：当您需要逐步演示推理过程时
- **Pattern and Anti-Pattern Template**: When showing both good and bad examples helps clarify expectations
- **模式和反模式模板**：当展示好坏示例有助于澄清预期时