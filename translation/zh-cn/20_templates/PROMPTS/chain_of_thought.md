# Chain of Thought Template （思维链模板）

## Summary （摘要）
A template for guiding AI systems through explicit step-by-step reasoning processes, improving accuracy and transparency for complex tasks.
一个用于指导 AI 系统通过明确的逐步推理过程的模板，提高复杂任务的准确性和透明度。

## Context & Application （背景与应用）
Use this template when a task requires careful reasoning or when the process of reaching a conclusion is as important as the conclusion itself. By breaking down complex thinking into explicit steps, chain of thought prompting improves accuracy, enables verification, and makes the reasoning process transparent.
当任务需要仔细推理，或者得出结论的过程与结论本身同样重要时，请使用此模板。通过将复杂的思维分解为明确的步骤，思维链提示可以提高准确性，实现验证，并使推理过程透明化。

This template is ideal for:
此模板非常适合：
- Complex problem-solving tasks
- 复杂的解决问题任务
- Situations requiring logical reasoning
- 需要逻辑推理的情况
- Multi-step calculations or analyses
- 多步骤计算或分析
- Tasks where explaining the "why" is important
- 解释“为什么”很重要的任务
- Reducing errors on challenging problems
- 减少难题中的错误

## Template Structure （模板结构）

```
# Task: {{task_description}}

## Approach
Think through this step-by-step:

1. {{first_reasoning_step}}
2. {{second_reasoning_step}}
3. {{additional_steps_as_needed}}
4. Formulate your conclusion based on this reasoning.

## Expected Output
Provide your complete reasoning process and then your final answer.
```

## Parameters （参数）

- `{{task_description}}`: Clear description of the problem to solve or question to answer
- `{{task_description}}`：要解决的问题或要回答的问题的清晰描述
- `{{first_reasoning_step}}`: Initial step in the reasoning process (e.g., "Identify the key variables")
- `{{first_reasoning_step}}`：推理过程中的初始步骤（例如，“识别关键变量”）
- `{{second_reasoning_step}}`: Next logical step (e.g., "Determine the relationships between variables")
- `{{second_reasoning_step}}`：下一个逻辑步骤（例如，“确定变量之间的关系”）
- `{{additional_steps_as_needed}}`: Further steps to guide complete reasoning
- `{{additional_steps_as_needed}}`：指导完整推理的进一步步骤

## Examples （示例）

### Example 1: Mathematical Problem Solving （示例 1：数学问题解决）

```
# Task: Solve the following word problem

A store sells notebooks for $4 each and pens for $2 each. Emma bought some notebooks and twice as many pens. If she spent $24 in total, how many notebooks did she buy?

## Approach
Think through this step-by-step:

1. Define variables for what we're looking for
2. Set up equations based on the given information
3. Solve the equations to find the unknown values
4. Verify your answer makes sense with the original conditions

## Expected Output
Provide your complete reasoning process and then your final answer.
```

```
# 任务：解决以下应用题

一家商店笔记本售价 4 美元，钢笔售价 2 美元。艾玛买了一些笔记本，钢笔的数量是笔记本的两倍。如果她总共花了 24 美元，她买了多少本笔记本？

## 方法
逐步思考：

1. 定义我们正在寻找的变量
2. 根据给定信息建立方程
3. 求解方程以找到未知值
4. 验证您的答案与原始条件是否一致

## 预期输出
提供完整的推理过程，然后给出最终答案。
```

### Example 2: Ethical Decision Analysis （示例 2：伦理决策分析）

```
# Task: Analyze the ethical implications of the following scenario

A pharmaceutical company has developed a drug that shows promise for treating a rare disease. The clinical trials indicate 70% efficacy but also reveal potentially serious side effects in 15% of patients. The company needs to decide whether to bring this drug to market.

## Approach
Think through this step-by-step:

1. Identify the key stakeholders in this scenario
2. Analyze the potential benefits of making the drug available
3. Consider the potential harms and risks involved
4. Evaluate alternative options that might be available
5. Balance competing ethical principles (beneficence, non-maleficence, autonomy, justice)
6. Formulate a nuanced recommendation with potential safeguards or conditions

## Expected Output
Provide your complete reasoning process and then your final recommendation.
```

```
# 任务：分析以下情景的伦理影响

一家制药公司开发了一种有望治疗罕见疾病的药物。临床试验表明其有效率为 70%，但也揭示了 15% 的患者可能出现严重的副作用。该公司需要决定是否将这种药物推向市场。

## 方法
逐步思考：

1. 识别此情景中的关键利益相关者
2. 分析提供药物的潜在好处
3. 考虑所涉及的潜在危害和风险
4. 评估可能可用的替代方案
5. 平衡相互竞争的伦理原则（善行、无害、自主、公正）
6. 制定包含潜在保障或条件的细致入微的建议

## 预期输出
提供完整的推理过程，然后给出最终建议。
```

## Variations （变体）

### Self-Prompted Chain of Thought （自提示思维链）
For encouraging the AI to develop its own reasoning steps:
鼓励 AI 开发自己的推理步骤：

```
# Task: {{task_description}}

## Approach
- First, break this problem down into logical steps
- Work through each step systematically
- Show your complete reasoning process
- Only then provide your final answer

## Expected Output
Step-by-step reasoning followed by conclusion.
```

### Guided Problem Decomposition （引导式问题分解）
For highly complex problems requiring more structured guidance:
对于需要更结构化指导的高度复杂问题：

```
# Task: {{task_description}}

## Problem Decomposition
1. Sub-problem 1: {{sub_problem_description}}
   - Consider: {{relevant_factor_1}}
   - Consider: {{relevant_factor_2}}

2. Sub-problem 2: {{sub_problem_description}}
   - Consider: {{relevant_factor_1}}
   - Consider: {{relevant_factor_2}}

3. Integration: Combine your analyses from the sub-problems

## Expected Output
Analysis of each sub-problem, integration of insights, and final conclusion.
```

### Scenario Analysis Chain of Thought （情景分析思维链）
For decisions requiring consideration of multiple scenarios:
对于需要考虑多种情景的决策：

```
# Task: {{decision_task}}

## Approach
Think through this step-by-step:

1. Scenario A: If {{condition_A}} happens
   - Probable outcomes:
   - Benefits:
   - Risks:

2. Scenario B: If {{condition_B}} happens
   - Probable outcomes:
   - Benefits:
   - Risks:

3. Compare scenarios and determine the most robust approach

## Expected Output
Analysis of each scenario and reasoned recommendation.
```

## Best Practices （最佳实践）

- **Match reasoning steps to the problem type** - Different problems require different reasoning approaches
- **将推理步骤与问题类型匹配** - 不同的问题需要不同的推理方法
- **Be explicit about the reasoning process** - Clearly articulate what thinking should happen at each step
- **明确推理过程** - 清楚地阐明每个步骤应该进行何种思考
- **Include verification steps** - Add steps to check work or validate conclusions
- **包含验证步骤** - 添加检查工作或验证结论的步骤
- **For mathematical problems**, include steps for checking units and order of magnitude
- **对于数学问题**，包括检查单位和数量级的步骤
- **For ethical or subjective analyses**, include steps for considering multiple perspectives
- **对于伦理或主观分析**，包括考虑多个视角的步骤
- **Don't skip steps** - Breaking reasoning into smaller steps improves accuracy
- **不要跳过步骤** - 将推理分解为更小的步骤可以提高准确性
- **Use 3-7 steps** for most problems - Too few lacks guidance, too many becomes overwhelming
- **大多数问题使用 3-7 个步骤** - 太少缺乏指导，太多则会让人不知所措
- **Encourage metacognition** - Include steps that prompt reflection on the reasoning process itself
- **鼓励元认知** - 包含促使反思推理过程本身的步骤
- **For complex problems**, consider breaking into sub-problems before integration
- **对于复杂问题**，考虑在集成之前将其分解为子问题

## Related Templates （相关模板）

- **Verification Loop Template**: Extends chain of thought with explicit verification steps
- **验证循环模板**：通过明确的验证步骤扩展思维链
- **Few-Shot Learning Template**: Can be combined to show examples of chain of thought reasoning
- **少样本学习模板**：可以结合使用以展示思维链推理的示例
- **Metacognitive Reflection Template**: For deeper thinking about the reasoning process itself
- **元认知反思模板**：用于更深入地思考推理过程本身