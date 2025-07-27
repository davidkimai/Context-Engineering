# Reasoning Templates （推理模板）

> "Logic is the anatomy of thought." — John Locke
> “逻辑是思想的解剖学。” — 约翰·洛克

## Overview （概述）

Reasoning templates guide language models through structured thinking processes to solve problems, generate insights, or make decisions. These templates build upon understanding templates by providing systematic approaches to processing information and reaching conclusions.
推理模板引导语言模型通过结构化的思维过程来解决问题、产生见解或做出决策。这些模板建立在理解模板的基础上，通过提供系统化的方法来处理信息和得出结论。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  REASONING PROCESS                                           │
│  （推理过程）                                                │
│                                                              │
│  Input → Structure → Apply Logic → Step-by-Step → Conclusion │
│  （输入 → 结构化 → 应用逻辑 → 逐步推理 → 结论）              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Basic Templates （基础模板）

### 1. Step-by-Step Reasoning （分步推理）

The fundamental template for breaking down complex reasoning into manageable steps.
将复杂推理分解为可管理步骤的基本模板。

```markdown
# Step-by-Step Reasoning Template （分步推理模板）

Task: Solve the following problem by breaking it down into clear, logical steps.
任务：通过将以下问题分解为清晰、合乎逻辑的步骤来解决它。

Problem: {{problem}}
问题：{{problem}}

Please follow this process:
请遵循此过程：
1. **Understand**: Restate the problem and identify what you need to find.
   **理解**：重述问题并确定你需要找到什么。
2. **Plan**: Outline your approach to solving the problem.
   **计划**：概述你解决问题的方法。
3. **Execute**: Work through each step of your plan in detail.
   **执行**：详细地完成你计划的每一步。
   - Step 1: [Description of the first step]
     - 步骤 1：[第一步的描述]
   - Step 2: [Description of the second step]
     - 步骤 2：[第二步的描述]
   - Step 3: [Continue with additional steps as needed]
     - 步骤 3：[根据需要继续添加步骤]
4. **Verify**: Check your solution against the original problem.
   **验证**：对照原始问题检查你的解决方案。
5. **Conclude**: State your final answer or conclusion clearly.
   **总结**：清晰地陈述你的最终答案或结论。

Show all your work and explain your reasoning at each step.
展示你所有的工作并在每一步解释你的推理过程。
```

**Token Count**: ~130 tokens (template only)
**令牌数**：约 130 个令牌（仅模板）

**Usage Example**:
- For mathematical problem solving
- When working through complex logical arguments
- For any task requiring transparent reasoning

**使用示例**：
- 用于解决数学问题
- 在处理复杂的逻辑论证时
- 用于任何需要透明推理的任务

### 2. Compare and Contrast （比较与对比）

For analytical reasoning that evaluates similarities and differences.
用于评估异同的分析性推理。

```markdown
# Compare and Contrast Template （比较与对比模板）

Task: Analyze the similarities and differences between the following items.
任务：分析以下项目之间的异同。

Items to Compare: {{item_a}} and {{item_b}}
要比较的项目：{{item_a}} 和 {{item_b}}

Please follow this structured approach:
请遵循此结构化方法：
1. **Background**: Briefly introduce both items and their context.
   **背景**：简要介绍两个项目及其背景。
2. **Criteria Selection**: Identify the key dimensions for comparison.
   **标准选择**：确定比较的关键维度。
3. **Systematic Comparison**:
   **系统比较**：
   - Dimension 1: [Explain how both items relate to this dimension]
     - 维度 1：[解释两个项目如何与此维度相关]
   - Dimension 2: [Explain how both items relate to this dimension]
     - 维度 2：[解释两个项目如何与此维度相关]
   - Dimension 3: [Continue with additional dimensions as needed]
     - 维度 3：[根据需要继续添加维度]
4. **Key Similarities**: Explicitly list the most important similarities.
   **关键相似点**：明确列出最重要的相似点。
5. **Key Differences**: Explicitly list the most important differences.
   **关键不同点**：明确列出最重要的不同点。
6. **Synthesis**: Explain what these similarities and differences reveal.
   **综合**：解释这些异同揭示了什么。
7. **Conclusion**: Summarize the most significant insights from this comparison.
   **结论**：总结此次比较得出的最重要见解。
```

**Token Count**: ~140 tokens (template only)
**令牌数**：约 140 个令牌（仅模板）

**Usage Example**:
- For comparing theories, products, or approaches
- When analyzing competing solutions
- For evaluating alternative explanations

**使用示例**：
- 用于比较理论、产品或方法
- 在分析竞争性解决方案时
- 用于评估替代性解释

### 3. Causal Analysis （因果分析）

For reasoning about cause and effect relationships.
用于推理因果关系。

```markdown
# Causal Analysis Template （因果分析模板）

Task: Analyze the causes and effects related to the following situation or phenomenon.
任务：分析与以下情况或现象相关的因果。

Situation: {{situation}}
情况：{{situation}}

Please follow this structured approach:
请遵循此结构化方法：
1. **Describe the Phenomenon**: Clearly state what needs to be explained.
   **描述现象**：清晰地陈述需要解释的内容。
2. **Identify Potential Causes**:
   **识别潜在原因**：
   - Immediate Causes: [Direct factors that led to the situation]
     - 直接原因：[导致该情况的直接因素]
   - Underlying Causes: [Deeper factors that created conditions for the situation]
     - 根本原因：[为该情况创造条件的深层因素]
   - Contributory Factors: [Elements that amplified or enabled the causes]
     - 促成因素：[放大或促成原因的因素]
3. **Evaluate Each Cause**:
   **评估每个原因**：
   - Evidence: [What evidence supports this as a cause?]
     - 证据：[什么证据支持这是一个原因？]
   - Significance: [How important was this cause?]
     - 重要性：[这个原因有多重要？]
   - Mechanism: [How did this cause lead to the effect?]
     - 机制：[这个原因如何导致了结果？]
4. **Analyze Effects**:
   **分析影响**：
   - Immediate Effects: [Direct consequences]
     - 直接影响：[直接后果]
   - Long-term Effects: [Ongoing or future consequences]
     - 长期影响：[持续或未来的后果]
   - Secondary Effects: [Indirect consequences]
     - 次要影响：[间接后果]
5. **Examine Interactions**: How do these causes and effects interact with each other?
   **检查相互作用**：这些因果之间如何相互作用？
6. **Conclusion**: Summarize the most significant causal relationships.
   **结论**：总结最重要的因果关系。
```

**Token Count**: ~160 tokens (template only)
**令牌数**：约 160 个令牌（仅模板）

**Usage Example**:
- For historical analysis
- When investigating complex systems
- For understanding social or economic phenomena

**使用示例**：
- 用于历史分析
- 在调查复杂系统时
- 用于理解社会或经济现象

## Advanced Templates （高级模板）

### 4. Hypothesis Testing （假设检验）

For systematically evaluating a hypothesis against evidence.
用于系统地根据证据评估假设。

```markdown
# Hypothesis Testing Template （假设检验模板）

Task: Systematically evaluate the following hypothesis based on available evidence.
任务：根据现有证据系统地评估以下假设。

Hypothesis: {{hypothesis}}
假设：{{hypothesis}}

Evidence: {{evidence}}
证据：{{evidence}}

Please follow this structured approach:
请遵循此结构化方法：
1. **Clarify the Hypothesis**: Restate the hypothesis in precise terms.
   **澄清假设**：用精确的术语重述假设。
2. **Identify Testable Predictions**: What should be true if the hypothesis is correct?
   **识别可检验的预测**：如果假设正确，什么应该是真的？
3. **Evaluate Evidence**:
   **评估证据**：
   - Supporting Evidence: [Evidence that confirms predictions]
     - 支持性证据：[证实预测的证据]
     - Strength: [How strongly does this evidence support the hypothesis?]
       - 强度：[该证据对假设的支持程度如何？]
     - Reliability: [How reliable is this evidence?]
       - 可靠性：[该证据的可靠性如何？]
   - Contradictory Evidence: [Evidence that contradicts predictions]
     - 矛盾证据：[与预测相矛盾的证据]
     - Strength: [How strongly does this evidence oppose the hypothesis?]
       - 强度：[该证据对假设的反驳程度如何？]
     - Reliability: [How reliable is this evidence?]
       - 可靠性：[该证据的可靠性如何？]
   - Missing Evidence: [Evidence that should exist but isn't present]
     - 缺失证据：[本应存在但不存在的证据]
4. **Consider Alternative Hypotheses**: What other explanations could account for the evidence?
   **考虑替代假设**：还有哪些其他解释可以说明这些证据？
5. **Weigh Comparative Explanatory Power**: How well does the hypothesis explain the evidence compared to alternatives?
   **权衡比较解释力**：与替代方案相比，该假设对证据的解释程度如何？
6. **Conclusion**: Assess the overall credibility of the hypothesis.
   **结论**：评估假设的总体可信度。
7. **Confidence Level**: Indicate your level of confidence in this assessment.
   **置信水平**：表明你对此评估的置信水平。
```

**Token Count**: ~180 tokens (template only)
**令牌数**：约 180 个令牌（仅模板）

**Usage Example**:
- For scientific reasoning
- When evaluating theories or claims
- For evidence-based decision making

**使用示例**：
- 用于科学推理
- 在评估理论或主张时
- 用于循证决策

### 5. Decision Matrix （决策矩阵）

For structured decision making across multiple criteria.
用于跨多个标准的结构化决策。

```markdown
# Decision Matrix Template （决策矩阵模板）

Task: Evaluate options against criteria to make a structured decision.
任务：根据标准评估选项，以做出结构化决策。

Decision Context: {{decision_context}}
决策背景：{{decision_context}}
Options: {{options}}
选项：{{options}}
Criteria: {{criteria}}
标准：{{criteria}}

Please follow this structured approach:
请遵循此结构化方法：
1. **Define the Decision**: Clearly state what decision needs to be made.
   **定义决策**：清晰地陈述需要做出的决策。
2. **Establish Criteria Weights**:
   **确定标准权重**：
   - Criterion 1: [Importance weight (1-10)]
     - 标准 1：[重要性权重 (1-10)]
   - Criterion 2: [Importance weight (1-10)]
     - 标准 2：[重要性权重 (1-10)]
   - [Continue for all criteria]
     - [继续处理所有标准]
3. **Evaluate Each Option**:
   **评估每个选项**：
   Create a matrix with options as rows and criteria as columns.
   创建一个以选项为行、标准为列的矩阵。
   
   | Option | Criterion 1 | Criterion 2 | ... | Total |
   |--------|-------------|-------------|-----|-------|
   | 选项 A | [分数]      | [分数]      | ... | [总分]  |
   | 选项 B | [分数]      | [分数]      | ... | [总分]  |
   
   For each cell, provide:
   对于每个单元格，提供：
   - Score: [Rating (1-10)]
     - 分数：[评分 (1-10)]
   - Justification: [Brief explanation]
     - 理由：[简要说明]
   
4. **Calculate Weighted Scores**: Multiply each score by the criterion weight.
   **计算加权分数**：将每个分数乘以标准权重。
5. **Rank Options**: Order options based on their total weighted scores.
   **对选项进行排序**：根据其总加权分数对选项进行排序。
6. **Sensitivity Analysis**: How would the ranking change if weights were adjusted?
   **敏感性分析**：如果调整权重，排名会如何变化？
7. **Recommendation**: State the recommended option with justification.
   **建议**：陈述推荐的选项并说明理由。
```

**Token Count**: ~180 tokens (template only)
**令牌数**：约 180 个令牌（仅模板）

**Usage Example**:
- For choosing between alternatives
- When balancing multiple factors
- For transparent decision processes

**使用示例**：
- 用于在备选方案之间进行选择
- 在平衡多个因素时
- 用于透明的决策过程

### 6. Argument Construction （论证构建）

For building well-structured arguments.
用于构建结构良好的论证。

```markdown
# Argument Construction Template （论证构建模板）

Task: Construct a well-reasoned argument for the following position.
任务：为以下立场构建一个理由充分的论证。

Position: {{position}}
立场：{{position}}

Please follow this structured approach:
请遵循此结构化方法：
1. **Thesis Statement**: Clearly articulate the main claim or position.
   **论点陈述**：清晰地阐明主要主张或立场。
2. **Define Key Terms**: Clarify any ambiguous or technical terms.
   **定义关键术语**：澄清任何模糊或技术性的术语。
3. **Establish Premises**:
   **建立前提**：
   - Premise 1: [State first supporting claim]
     - 前提 1：[陈述第一个支持性主张]
     - Evidence: [Support for this premise]
       - 证据：[对此前提的支持]
     - Reasoning: [How this evidence supports the premise]
       - 推理：[此证据如何支持该前提]
   - Premise 2: [State second supporting claim]
     - 前提 2：[陈述第二个支持性主张]
     - Evidence: [Support for this premise]
       - 证据：[对此前提的支持]
     - Reasoning: [How this evidence supports the premise]
       - 推理：[此证据如何支持该前提]
   - [Continue with additional premises as needed]
     - [根据需要继续添加前提]
4. **Logical Structure**: Explain how these premises lead to the conclusion.
   **逻辑结构**：解释这些前提如何得出结论。
5. **Address Counterarguments**:
   **回应反驳论点**：
   - Counterargument 1: [Potential objection]
     - 反驳论点 1：[潜在的反对意见]
     - Response: [Rebuttal or accommodation]
       - 回应：[反驳或调和]
   - Counterargument 2: [Potential objection]
     - 反驳论点 2：[潜在的反对意见]
     - Response: [Rebuttal or accommodation]
       - 回应：[反驳或调和]
6. **Conclusion**: Restate the thesis and summarize the supporting arguments.
   **结论**：重申论点并总结支持性论据。
```

**Token Count**: ~170 tokens (template only)
**令牌数**：约 170 个令牌（仅模板）

**Usage Example**:
- For persuasive writing
- When developing position papers
- For constructing logical cases

**使用示例**：
- 用于说服性写作
- 在撰写立场文件时
- 用于构建逻辑案例

## Implementation Patterns （实施模式）

Here's a simple Python function to implement the Step-by-Step Reasoning template:
这是一个实现分步推理模板的简单 Python 函数：

```python
def step_by_step_reasoning(problem, steps=None):
    """
    Create a prompt that guides through step-by-step reasoning.
    （创建一个引导分步推理的提示。）
    
    Args:
        problem (str): The problem to solve
        （problem (str): 要解决的问题）
        steps (list, optional): Custom steps for the reasoning process
        （steps (list, optional): 推理过程的自定义步骤）
        
    Returns:
        str: A formatted prompt for step-by-step reasoning
        （str: 用于分步推理的格式化提示）
    """
    if steps is None:
        steps = [
            "Understand: Restate the problem and identify what you need to find.",
            "Plan: Outline your approach to solving the problem.",
            "Execute: Work through each step of your plan in detail.",
            "Verify: Check your solution against the original problem.",
            "Conclude: State your final answer or conclusion clearly."
        ]
    
    steps_text = "\n".join([f"{i+1}. **{step.split(':', 1)[0]}**:{step.split(':', 1)[1]}" 
                           for i, step in enumerate(steps)])
    
    return f"""
Task: Solve the following problem by breaking it down into clear, logical steps.
（任务：通过将以下问题分解为清晰、合乎逻辑的步骤来解决它。）

Problem: {problem}
（问题：{problem}）

Please follow this process:
（请遵循此过程：）
{steps_text}

Show all your work and explain your reasoning at each step.
（展示你所有的工作并在每一步解释你的推理过程。）
"""
```

## Measurement and Optimization （测量与优化）

When using reasoning templates, measure their effectiveness by:
在使用推理模板时，通过以下方式衡量其有效性：

1. **Logical Validity**: Are the conclusions properly supported by the premises?
   **逻辑有效性**：结论是否得到前提的充分支持？
2. **Completeness**: Does the reasoning address all aspects of the problem?
   **完整性**：推理是否涵盖了问题的所有方面？
3. **Transparency**: Is each step clearly explained and justified?
   **透明度**：每一步是否都得到了清晰的解释和证明？
4. **Efficiency**: Does the reasoning take a direct path to the solution?
   **效率**：推理是否采取了直接通往解决方案的路径？
5. **Correctness**: Does the reasoning lead to the right answer or conclusion?
   **正确性**：推理是否得出了正确的答案或结论？

Optimize your templates by:
通过以下方式优化您的模板：
- Adjusting the level of detail based on problem complexity
  - 根据问题的复杂性调整细节级别
- Adding domain-specific reasoning steps for specialized fields
  - 为专业领域添加特定于领域的推理步骤
- Customizing evaluation criteria for particular types of problems
  - 为特定类型的问题定制评估标准

## Combining with Other Tools （与其他工具结合）

Reasoning templates work best as part of a complete cognitive workflow:
推理模板作为完整认知工作流程的一部分效果最佳：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│ （理解模板）        │     │ （推理模板）      │     │ （验证模板）      │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
```

For example, use an Understanding template to analyze a problem, apply a Reasoning template to solve it, and then use a Verification template to check the solution.
例如，使用理解模板分析问题，应用推理模板解决问题，然后使用验证模板检查解决方案。

## Advanced Reasoning Patterns （高级推理模式）

For complex problems, consider these advanced patterns:
对于复杂问题，请考虑这些高级模式：

### Divide and Conquer （分而治之）

Break the problem into independent sub-problems, solve each separately, then combine the results.
将问题分解为独立的子问题，分别解决每个子问题，然后合并结果。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Main Problem                                                 │
│  （主问题）                                                   │
│       │                                                       │
│       ├────────────────┬────────────────┬────────────────┐    │
│       │                │                │                │    │
│       ▼                ▼                ▼                ▼    │
│  Sub-Problem 1    Sub-Problem 2    Sub-Problem 3    Sub-Problem 4 │
│  （子问题 1）     （子问题 2）     （子问题 3）     （子问题 4） │
│       │                │                │                │    │
│       ├────────────────┼────────────────┼────────────────┘    │
│       │                │                │                     │
│       ▼                ▼                ▼                     │
│  Combine Solutions and Integrate Results                      │
│  （合并解决方案并整合结果）                                   │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

### Iterative Refinement （迭代求精）

Start with a simple solution, then iteratively improve it.
从一个简单的解决方案开始，然后迭代地改进它。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Initial Solution                                             │
│  （初始解决方案）                                             │
│       │                                                       │
│       ▼                                                       │
│  Identify Weaknesses                                          │
│  （识别弱点）                                                 │
│       │                                                       │
│       ▼                                                       │
│  Improve Solution           ◄─────────────┐                   │
│  （改进解决方案）           │                   │
│       │                                    │                   │
│       ▼                                    │                   │
│  Evaluate Improvement                      │                   │
│  （评估改进）                              │
│       │                                    │                   │
│       └────────────────────────────────────┘                   │
│       │                                                        │
│       ▼                                                        │
│  Final Solution (when satisfactory)                            │
│  （最终解决方案（当满意时））                                  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Analogical Reasoning （类比推理）

Apply reasoning patterns from a known domain to a new problem.
将已知领域的推理模式应用于新问题。

```
┌───────────────────────────────────────────────────────────────┐
│                                                               │
│  Target Problem                                               │
│  （目标问题）                                                 │
│       │                                                       │
│       ▼                                                       │
│  Identify Similar Solved Problem                              │
│  （识别相似的已解决问题）                                     │
│       │                                                       │
│       ▼                                                       │
│  Map Elements from Solved Problem to Target Problem           │
│  （将已解决问题的元素映射到目标问题）                         │
│       │                                                       │
│       ▼                                                       │
│  Apply Similar Solution Strategy                              │
│  （应用相似的解决方案策略）                                   │
│       │                                                       │
│       ▼                                                       │
│  Adapt as Needed for Target Problem                           │
│  （根据目标问题需要进行调整）                                 │
│                                                               │
└───────────────────────────────────────────────────────────────┘
```

## Next Steps （后续步骤）

- Explore [verification.md](./verification.md) for templates that check reasoning
- See [composition.md](./composition.md) for ways to combine multiple templates
- Check out [../cognitive-programs/advanced-programs.md](../cognitive-programs/advanced-programs.md) for programmatic approaches that leverage these reasoning patterns

- 探索 [verification.md](./verification.md) 以了解检查推理的模板
- 查看 [composition.md](./composition.md) 以了解组合多个模板的方法
- 查看 [../cognitive-programs/advanced-programs.md](../cognitive-programs/advanced-programs.md) 以了解利用这些推理模式的程序化方法