# Template Composition （模板组合）

> "The whole is greater than the sum of its parts." — Aristotle
> “整体大于部分之和。” — 亚里士多德

## Overview （概述）

Template composition involves combining multiple cognitive templates to tackle complex problems that require multiple reasoning stages. By sequencing templates strategically, we can create sophisticated cognitive workflows that guide language models through intricate tasks while maintaining structure and clarity.
模板组合涉及将多个认知模板结合起来，以解决需要多个推理阶段的复杂问题。通过有策略地对模板进行排序，我们可以创建复杂的认知工作流，引导语言模型完成复杂的任务，同时保持结构和清晰度。

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  TEMPLATE COMPOSITION                                                │
│  （模板组合）                                                        │
│                                                                      │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐             │
│  │             │     │             │     │             │             │
│  │ Template A  │────►│ Template B  │────►│ Template C  │─────► ...   │
│  │ （模板 A）  │     │ （模板 B）  │     │ （模板 C）  │             │
│  │             │     │             │     │             │             │
│  └─────────────┘     └─────────────┘     └─────────────┘             │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## Basic Composition Patterns （基本组合模式）

### 1. Linear Sequence （线性序列）

The simplest composition pattern chains templates in a fixed sequence.
最简单的组合模式是按固定顺序链接模板。

```markdown
# Linear Sequence Template （线性序列模板）

Task: Solve the following complex problem through a structured multi-stage approach.
任务：通过结构化的多阶段方法解决以下复杂问题。

Problem: {{problem}}
问题：{{problem}}

## Stage 1: Understanding the Problem （阶段 1：理解问题）
{{understanding_template}}

## Stage 2: Planning the Solution （阶段 2：规划解决方案）
{{reasoning_template}}

## Stage 3: Executing the Plan （阶段 3：执行计划）
{{step_by_step_template}}

## Stage 4: Verifying the Solution （阶段 4：验证解决方案）
{{verification_template}}

## Stage 5: Final Answer （阶段 5：最终答案）
Based on the above analysis and verification, provide your final answer to the original problem.
根据以上分析和验证，提供你对原始问题的最终答案。
```

**Token Count**: Varies based on component templates
**令牌数**：根据组件模板而异

**Usage Example**:
- For mathematical problem solving
- When approaching complex reasoning tasks
- For any multi-stage problem-solving process

**使用示例**：
- 用于解决数学问题
- 在处理复杂推理任务时
- 用于任何多阶段问题解决过程

### 2. Conditional Branching （条件分支）

This pattern introduces decision points that determine the next template to apply.
此模式引入了决定下一步应用哪个模板的决策点。

```markdown
# Conditional Branching Template （条件分支模板）

Task: Analyze and solve the following problem using the appropriate approach based on problem characteristics.
任务：根据问题特征，使用适当的方法分析和解决以下问题。

Problem: {{problem}}
问题：{{problem}}

## Stage 1: Problem Analysis （阶段 1：问题分析）
{{understanding_template}}

## Stage 2: Approach Selection （阶段 2：方法选择）
Based on your analysis, determine which of the following approaches is most appropriate:
根据你的分析，确定以下哪种方法最合适：

A) If this is primarily a mathematical calculation problem:
   如果这主要是一个数学计算问题：
   {{mathematical_reasoning_template}}

B) If this is primarily a logical reasoning problem:
   如果这主要是一个逻辑推理问题：
   {{logical_reasoning_template}}

C) If this is primarily a data analysis problem:
   如果这主要是一个数据分析问题：
   {{data_analysis_template}}

## Stage 3: Solution Verification （阶段 3：解决方案验证）
{{verification_template}}

## Stage 4: Final Answer （阶段 4：最终答案）
Provide your final answer to the original problem.
提供你对原始问题的最终答案。
```

**Token Count**: Varies based on component templates
**令牌数**：根据组件模板而异

**Usage Example**:
- For problems that might require different approaches
- When the problem type isn't clear initially
- For systems that handle diverse query types

**使用示例**：
- 对于可能需要不同方法的问题
- 当问题类型最初不明确时
- 用于处理不同查询类型的系统

### 3. Iterative Refinement （迭代求精）

This pattern applies templates repeatedly until a satisfactory result is achieved.
此模式重复应用模板，直到达到满意的结果。

```markdown
# Iterative Refinement Template （迭代求精模板）

Task: Iteratively develop and refine a solution to the following problem.
任务：迭代地开发和完善以下问题的解决方案。

Problem: {{problem}}
问题：{{problem}}

## Iteration 1: Initial Solution （迭代 1：初始解决方案）
{{reasoning_template}}

## Evaluation of Iteration 1 （迭代 1 的评估）
{{evaluation_template}}

## Iteration 2: Refined Solution （迭代 2：完善的解决方案）
Based on the evaluation of your first attempt, provide an improved solution.
根据你第一次尝试的评估，提供一个改进的解决方案。
{{reasoning_template}}

## Evaluation of Iteration 2 （迭代 2 的评估）
{{evaluation_template}}

## Iteration 3: Final Solution （迭代 3：最终解决方案）
Based on the evaluation of your second attempt, provide your final solution.
根据你第二次尝试的评估，提供你的最终解决方案。
{{reasoning_template}}

## Final Verification （最终验证）
{{verification_template}}

## Final Answer （最终答案）
Provide your final answer to the original problem.
提供你对原始问题的最终答案。
```

**Token Count**: Varies based on component templates and number of iterations
**令牌数**：根据组件模板和迭代次数而异

**Usage Example**:
- For creative tasks that benefit from refinement
- When approaching difficult problems
- For generating high-quality content

**使用示例**：
- 用于需要完善的创意任务
- 在处理难题时
- 用于生成高质量内容

## Advanced Composition Patterns （高级组合模式）

### 4. Divide and Conquer （分而治之）

This pattern breaks a complex problem into sub-problems, solves each independently, then combines the results.
此模式将复杂问题分解为子问题，独立解决每个子问题，然后合并结果。

```markdown
# Divide and Conquer Template （分而治之模板）

Task: Solve the following complex problem by breaking it into manageable sub-problems.
任务：通过将以下复杂问题分解为可管理的子问题来解决它。

Problem: {{problem}}
问题：{{problem}}

## Stage 1: Problem Decomposition （阶段 1：问题分解）
{{decomposition_template}}

## Stage 2: Solving Sub-Problems （阶段 2：解决子问题）
For each sub-problem identified above:
对于上面确定的每个子问题：

### Sub-Problem 1: （子问题 1：）
{{reasoning_template}}

### Sub-Problem 2: （子问题 2：）
{{reasoning_template}}

### Sub-Problem 3: （子问题 3：）
{{reasoning_template}}
(Add additional sub-problems as needed)
（根据需要添加其他子问题）

## Stage 3: Solution Integration （阶段 3：解决方案集成）
{{integration_template}}

## Stage 4: Verification （阶段 4：验证）
{{verification_template}}

## Stage 5: Final Answer （阶段 5：最终答案）
Provide your final answer to the original problem.
提供你对原始问题的最终答案。
```

**Token Count**: Varies based on component templates and number of sub-problems
**令牌数**：根据组件模板和子问题数量而异

**Usage Example**:
- For complex problems with distinct components
- When tackling systems with multiple interacting parts
- For projects requiring multiple types of analysis

**使用示例**：
- 用于具有不同组件的复杂问题
- 在处理具有多个交互部分的系统时
- 用于对复杂情况进行全面分析

### 5. Dialectical Reasoning （辩证推理）

This pattern explores opposing perspectives to reach a nuanced conclusion.
此模式探讨对立的观点，以得出细致入微的结论。

```markdown
# Dialectical Reasoning Template （辩证推理模板）

Task: Analyze the following issue through a dialectical approach to reach a nuanced conclusion.
任务：通过辩证方法分析以下问题，以得出细致入微的结论。

Issue: {{issue}}
问题：{{issue}}

## Stage 1: Issue Analysis （阶段 1：问题分析）
{{understanding_template}}

## Stage 2: Thesis (Position A) （阶段 2：正题（立场 A））
{{argument_template}}

## Stage 3: Antithesis (Position B) （阶段 3：反题（立场 B））
{{argument_template}}

## Stage 4: Synthesis （阶段 4：综合）
{{synthesis_template}}

## Stage 5: Verification （阶段 5：验证）
{{verification_template}}

## Stage 6: Conclusion （阶段 6：结论）
Provide your final conclusion on the issue.
就该问题提供你的最终结论。
```

**Token Count**: Varies based on component templates
**令牌数**：根据组件模板而异

**Usage Example**:
- For controversial or complex topics
- When multiple valid perspectives exist
- For philosophical or ethical questions

**使用示例**：
- 用于有争议或复杂的主题
- 当存在多个有效观点时
- 用于哲学或伦理问题

### 6. Multi-Agent Simulation （多智能体模拟）

This pattern simulates different expertise or perspectives through distinct "agents."
此模式通过不同的“智能体”模拟不同的专业知识或视角。

```markdown
# Multi-Agent Simulation Template （多智能体模拟模板）

Task: Analyze the following problem from multiple expert perspectives to reach a comprehensive solution.
任务：从多个专家视角分析以下问题，以得出全面的解决方案。

Problem: {{problem}}
问题：{{problem}}

## Stage 1: Problem Analysis （阶段 1：问题分析）
{{understanding_template}}

## Stage 2: Expert Perspectives （阶段 2：专家视角）

### Perspective 1: {{expert_1}} (e.g., "Mathematician")
### 视角 1：{{expert_1}}（例如，“数学家”）
{{reasoning_template}}

### Perspective 2: {{expert_2}} (e.g., "Economist")
### 视角 2：{{expert_2}}（例如，“经济学家”）
{{reasoning_template}}

### Perspective 3: {{expert_3}} (e.g., "Historian")
### 视角 3：{{expert_3}}（例如，“历史学家”）
{{reasoning_template}}
(Add additional perspectives as needed)
（根据需要添加其他视角）

## Stage 3: Collaborative Integration （阶段 3：协作集成）
{{integration_template}}

## Stage 4: Verification （阶段 4：验证）
{{verification_template}}

## Stage 5: Final Solution （阶段 5：最终解决方案）
Provide your final solution to the problem, incorporating insights from all perspectives.
提供问题的最终解决方案，并综合所有视角的见解。
```

**Token Count**: Varies based on component templates and number of perspectives
**令牌数**：根据组件模板和视角数量而异

**Usage Example**:
- For interdisciplinary problems
- When diverse expertise is valuable
- For comprehensive analysis of complex situations

**使用示例**：
- 用于跨学科问题
- 当多样化的专业知识很有价值时
- 用于对复杂情况进行全面分析

## Implementation Patterns （实施模式）

Here's a Python function to implement a basic linear sequence composition:
这是一个实现基本线性序列组合的 Python 函数：

```python
def linear_sequence(problem, templates):
    """
    Create a prompt that composes multiple templates in a linear sequence.
    （创建一个以线性序列组合多个模板的提示。）
    
    Args:
        problem (str): The problem to solve
        （problem (str): 要解决的问题）
        templates (dict): A dictionary of template functions keyed by stage names
        （templates (dict): 一个以阶段名称为键的模板函数字典）
        
    Returns:
        str: A formatted prompt for a linear sequence of templates
        （str: 用于线性序列模板的格式化提示）
    """
    prompt = f"""
Task: Solve the following complex problem through a structured multi-stage approach.
（任务：通过结构化的多阶段方法解决以下复杂问题。）

Problem: {problem}
（问题：{problem}）
"""
    
    for i, (stage_name, template_func) in enumerate(templates.items()):
        prompt += f"\n## Stage {i+1}: {stage_name}\n"
        
        # For each template, we only include the instructions, not the problem statement again
        # （对于每个模板，我们只包含说明，不再重复问题陈述）
        template_content = template_func(problem)
        # Extract just the instructions, assuming the problem statement is at the beginning
        # （仅提取说明，假设问题陈述在开头）
        instructions = "\n".join(template_content.split("\n")[3:])
        
        prompt += instructions
    
    prompt += """
## Final Answer
Based on the above analysis, provide your final answer to the original problem.
（## 最终答案
根据以上分析，提供你对原始问题的最终答案。）
"""
    
    return prompt

# Example usage
# （示例用法）
from cognitive_templates import understanding, step_by_step_reasoning, verify_solution

templates = {
    "Understanding the Problem": understanding,
    "Solving Step by Step": step_by_step_reasoning,
    "Verifying the Solution": verify_solution
}

problem = "If a train travels at 60 mph for 2.5 hours, how far does it go?"
composed_prompt = linear_sequence(problem, templates)
```

## Template Composition Strategies （模板组合策略）

When combining templates, consider these strategies for optimal results:
组合模板时，请考虑以下策略以获得最佳结果：

### 1. State Management （状态管理）

Ensure information flows correctly between templates:
确保信息在模板之间正确流动：

```python
def managed_sequence(problem, llm):
    """
    Execute a sequence of templates with explicit state management.
    （使用显式状态管理执行模板序列。）
    
    Args:
        problem (str): The problem to solve
        （problem (str): 要解决的问题）
        llm: LLM interface for generating responses
        （llm: 用于生成响应的 LLM 接口）
        
    Returns:
        dict: Complete solution with intermediate results
        （dict: 包含中间结果的完整解决方案）
    """
    # Initialize state
    # （初始化状态）
    state = {"problem": problem, "stages": {}}
    
    # Stage 1: Understanding
    # （阶段 1：理解）
    understanding_prompt = understanding(problem)
    understanding_result = llm.generate(understanding_prompt)
    state["stages"]["understanding"] = understanding_result
    
    # Stage 2: Planning with context from understanding
    # （阶段 2：根据理解的背景进行规划）
    planning_prompt = f"""
Task: Plan a solution approach based on this problem analysis.
（任务：根据此问题分析规划解决方案。）

Problem: {problem}
（问题：{problem}）

Problem Analysis:
{understanding_result}
（问题分析：
{understanding_result}）

Please outline a step-by-step approach to solve this problem.
（请概述解决此问题的分步方法。）
"""
    planning_result = llm.generate(planning_prompt)
    state["stages"]["planning"] = planning_result
    
    # Stage 3: Execution with context from planning
    # （阶段 3：根据规划的背景执行）
    execution_prompt = f"""
Task: Execute the solution plan for this problem.
（任务：执行此问题的解决方案计划。）

Problem: {problem}
（问题：{problem}）

Problem Analysis:
{understanding_result}
（问题分析：
{understanding_result}）

Solution Plan:
{planning_result}
（解决方案计划：
{planning_result}）

Please implement this plan step by step to solve the problem.
（请逐步实施此计划以解决问题。）
"""
    execution_result = llm.generate(execution_prompt)
    state["stages"]["execution"] = execution_result
    
    # Stage 4: Verification with context from execution
    # （阶段 4：根据执行的背景进行验证）
    verification_prompt = verify_solution(problem, execution_result)
    verification_result = llm.generate(verification_prompt)
    state["stages"]["verification"] = verification_result
    
    # Return complete solution with all intermediate stages
    # （返回包含所有中间阶段的完整解决方案）
    return state
```

### 2. Adaptive Selection （自适应选择）

Choose templates dynamically based on problem characteristics:
根据问题特征动态选择模板：

```python
def adaptive_composition(problem, llm):
    """
    Adaptively select and compose templates based on problem characteristics.
    （根据问题特征自适应地选择和组合模板。）
    
    Args:
        problem (str): The problem to solve
        （problem (str): 要解决的问题）
        llm: LLM interface for generating responses
        （llm: 用于生成响应的 LLM 接口）
        
    Returns:
        dict: Complete solution with template selection rationale
        （dict: 包含模板选择理由的完整解决方案）
    """
    # Stage 1: Problem classification
    # （阶段 1：问题分类）
    classification_prompt = f"""
Task: Classify the following problem to determine the most appropriate solution approach.
（任务：对以下问题进行分类，以确定最合适的解决方法。）

Problem: {problem}
（问题：{problem}）

Please classify this problem into ONE of the following categories:
（请将此问题归入以下类别之一：）
1. Mathematical Calculation
   （数学计算）
2. Logical Reasoning
   （逻辑推理）
3. Data Analysis
   （数据分析）
4. Creative Writing
   （创意写作）
5. Decision Making
   （决策）

Provide your classification and a brief explanation of your reasoning.
（提供你的分类和你推理的简要说明。）
"""
    classification_result = llm.generate(classification_prompt)
    
    # Parse the classification (in a real implementation, use more robust parsing)
    # （解析分类（在实际实现中，使用更强大的解析））
    problem_type = "Unknown"
    for category in ["Mathematical", "Logical", "Data", "Creative", "Decision"]:
        if category in classification_result:
            problem_type = category
            break
    
    # Select templates based on problem type
    # （根据问题类型选择模板）
    if "Mathematical" in problem_type:
        templates = {
            "Understanding": understanding,
            "Solution": step_by_step_reasoning,
            "Verification": verify_solution
        }
    elif "Logical" in problem_type:
        templates = {
            "Understanding": understanding,
            "Argument Analysis": lambda p: logical_argument_template(p),
            "Verification": verify_solution
        }
    # Add more conditions for other problem types
    # （为其他问题类型添加更多条件）
    
    # Execute the selected template sequence
    # （执行选定的模板序列）
    result = {
        "problem": problem,
        "classification": classification_result,
        "selected_approach": problem_type,
        "stages": {}
    }
    
    for stage_name, template_func in templates.items():
        prompt = template_func(problem)
        response = llm.generate(prompt)
        result["stages"][stage_name] = response
    
    return result
```

### 3. Feedback-Driven Refinement （反馈驱动的完善）

Use evaluation results to guide template selection and refinement:
使用评估结果指导模板选择和完善：

```python
def feedback_driven_composition(problem, llm, max_iterations=3):
    """
    Use feedback to drive template selection and refinement.
    （使用反馈来驱动模板选择和完善。）
    
    Args:
        problem (str): The problem to solve
        （problem (str): 要解决的问题）
        llm: LLM interface for generating responses
        （llm: 用于生成响应的 LLM 接口）
        max_iterations (int): Maximum number of refinement iterations
        （max_iterations (int): 最大完善迭代次数）
        
    Returns:
        dict: Complete solution with refinement history
        （dict: 包含完善历史的完整解决方案）
    """
    # Initialize state
    # （初始化状态）
    state = {
        "problem": problem,
        "iterations": [],
        "final_solution": None,
        "quality_score": 0
    }
    
    # Initial solution
    # （初始解决方案）
    solution = llm.generate(step_by_step_reasoning(problem))
    
    for i in range(max_iterations):
        # Evaluate current solution
        # （评估当前解决方案）
        evaluation_prompt = f"""
Task: Evaluate the quality and correctness of this solution.
（任务：评估此解决方案的质量和正确性。）

Problem: {problem}
（问题：{problem}）

Proposed Solution:
{solution}
（提议的解决方案：
{solution}）

Please evaluate this solution on a scale of 1-10 for:
（请在 1-10 的范围内评估此解决方案的以下方面：）
1. Correctness (is the answer right?)
   （正确性（答案是否正确？））
2. Clarity (is the reasoning clear?)
   （清晰度（推理是否清晰？））
3. Completeness (are all aspects addressed?)
   （完整性（是否涵盖了所有方面？））

For each criterion, provide a score and brief explanation.
（对于每个标准，提供一个分数和简要说明。）
Then suggest specific improvements that could be made.
（然后提出可以做出的具体改进建议。）
"""
        evaluation = llm.generate(evaluation_prompt)
        
        # Extract quality score (in a real implementation, use more robust parsing)
        # （提取质量分数（在实际实现中，使用更强大的解析））
        quality_score = 0
        for line in evaluation.split("\n"):
            if "Correctness" in line and ":" in line:
                try:
                    quality_score += int(line.split(":")[1].strip().split("/")[0])
                except:
                    pass
            if "Clarity" in line and ":" in line:
                try:
                    quality_score += int(line.split(":")[1].strip().split("/")[0])
                except:
                    pass
            if "Completeness" in line and ":" in line:
                try:
                    quality_score += int(line.split(":")[1].strip().split("/")[0])
                except:
                    pass
        
        quality_score = quality_score / 3  # Average score
        # （平均分）
        
        # Record this iteration
        # （记录此次迭代）
        state["iterations"].append({
            "solution": solution,
            "evaluation": evaluation,
            "quality_score": quality_score
        })
        
        # Check if quality is satisfactory
        # （检查质量是否满意）
        if quality_score >= 8:
            break
        
        # Select template for improvement based on evaluation
        # （根据评估选择改进模板）
        if "Correctness" in evaluation and "clarity" not in evaluation.lower():
            # If correctness is the main issue, focus on verification
            # （如果正确性是主要问题，则专注于验证）
            improvement_template = verify_solution
        elif "clarity" in evaluation.lower():
            # If clarity is the main issue, focus on explanation
            # （如果清晰度是主要问题，则专注于解释）
            improvement_template = lambda p: step_by_step_reasoning(p, steps=["Understand", "Plan", "Execute with clear explanations", "Verify", "Conclude"])
        else:
            # Default to general improvement
            # （默认为一般改进）
            improvement_template = step_by_step_reasoning
        
        # Generate improved solution
        # （生成改进的解决方案）
        improvement_prompt = f"""
Task: Improve the following solution based on this evaluation feedback.
（任务：根据此评估反馈改进以下解决方案。）

Problem: {problem}
（问题：{problem}）

Current Solution:
{solution}
（当前解决方案：
{solution}）

Evaluation:
{evaluation}
（评估：
{evaluation}）

Please provide an improved solution that addresses the issues identified in the evaluation.
（请提供一个改进的解决方案，以解决评估中发现的问题。）
"""
        solution = llm.generate(improvement_prompt)
    
    # Select best solution based on quality score
    # （根据质量分数选择最佳解决方案）
    best_iteration = max(state["iterations"], key=lambda x: x["quality_score"])
    state["final_solution"] = best_iteration["solution"]
    state["quality_score"] = best_iteration["quality_score"]
    
    return state
```

## Measuring Composition Effectiveness （衡量组合有效性）

When using template compositions, measure their effectiveness by:
使用模板组合时，通过以下方式衡量其有效性：

1. **End-to-End Accuracy**: Does the full composition produce correct results?
   **端到端准确性**：完整的组合是否产生正确的结果？
2. **Stage Contribution**: How much does each template contribute to the final quality?
   **阶段贡献**：每个模板对最终质量的贡献有多大？
3. **Information Flow**: Is important context preserved between templates?
   **信息流**：模板之间是否保留了重要的背景信息？
4. **Efficiency**: What is the token overhead of the composition versus simpler approaches?
   **效率**：与更简单的方法相比，组合的令牌开销是多少？
5. **Adaptability**: How well does the composition handle different problem variations?
   **适应性**：组合处理不同问题变体的能力如何？

## Tips for Effective Composition （有效组合的技巧）

1. **Start Simple**: Begin with linear sequences before attempting more complex patterns
   **从简单开始**：在尝试更复杂的模式之前，从线性序列开始
2. **Minimize Redundancy**: Avoid repeating instructions across templates
   **最小化冗余**：避免在模板之间重复说明
3. **Preserve Context**: Ensure critical information flows between templates
   **保留背景**：确保关键信息在模板之间流动
4. **Balance Structure vs. Flexibility**: Too rigid compositions limit the model's strengths
   **平衡结构与灵活性**：过于僵化的组合会限制模型的优势
5. **Test with Variations**: Verify that your composition works across problem variations
   **用变体测试**：验证你的组合在不同问题变体下都能正常工作
6. **Include Self-Correction**: Build in verification and refinement opportunities
   **包含自我修正**：内置验证和完善的机会

## Next Steps （后续步骤）

- See how these composition patterns are implemented in [../cognitive-programs/program-library.py](../cognitive-programs/program-library.py)
- Explore complete cognitive architectures in [../cognitive-architectures/solver-architecture.md](../cognitive-architectures/solver-architecture.md)
- Learn how to integrate these compositions with retrieval and memory in [../integration/with-rag.md](../integration/with-rag.md) and [../integration/with-memory.md](../integration/with-memory.md)

- 在 [../cognitive-programs/program-library.py](../cognitive-programs/program-library.py) 中查看这些组合模式的实现方式
- 在 [../cognitive-architectures/solver-architecture.md](../cognitive-architectures/solver-architecture.md) 中探索完整的认知架构
- 在 [../integration/with-rag.md](../integration/with-rag.md) 和 [../integration/with-memory.md](../integration/with-memory.md) 中学习如何将这些组合与检索和记忆集成

---

## Deeper Dive: Metaprogramming with Templates （深入探讨：使用模板进行元编程）

Advanced practitioners can create systems that generate templates dynamically:
高级实践者可以创建动态生成模板的系统：

```python
def generate_specialized_template(domain, complexity, llm):
    """
    Generate a specialized template for a specific domain and complexity level.
    （为特定领域和复杂性级别生成专门的模板。）
    
    Args:
        domain (str): The domain area (e.g., "mathematics", "legal")
        （domain (str): 领域区域（例如，“数学”、“法律”））
        complexity (str): The complexity level (e.g., "basic", "advanced")
        （complexity (str): 复杂性级别（例如，“基础”、“高级”））
        llm: LLM interface for generating the template
        （llm: 用于生成模板的 LLM 接口）
        
    Returns:
        function: A generated template function
        （function: 一个生成的模板函数）
    """
    prompt = f"""
Task: Create a specialized cognitive template for solving {complexity} problems in the {domain} domain.
（任务：创建一个专门的认知模板，用于解决 {domain} 领域中 {complexity} 级别的问题。）

The template should:
（模板应：）
1. Include appropriate domain-specific terminology and concepts
   （包含适当的领域特定术语和概念）
2. Break down the reasoning process into clear steps
   （将推理过程分解为清晰的步骤）
3. Include domain-specific verification checks
   （包含领域特定的验证检查）
4. Be calibrated for {complexity} complexity level
   （针对 {complexity} 复杂性级别进行校准）

Format the template as a markdown document with:
（将模板格式化为包含以下内容的 markdown 文档：）
1. A clear task description
   （清晰的任务描述）
2. Structured steps for solving problems in this domain
   （解决此领域问题的结构化步骤）
3. Domain-specific guidance for each step
   （每个步骤的领域特定指导）
4. Verification criteria specific to this domain
   （此领域特定的验证标准）

Please generate the complete template text.
（请生成完整的模板文本。）
"""
    
    template_text = llm.generate(prompt)
    
    # Create a function that applies this template
    # （创建一个应用此模板的函数）
    def specialized_template(problem):
        return f"""
Task: Solve the following {complexity} {domain} problem using a specialized approach.
（任务：使用专门的方法解决以下 {complexity} {domain} 问题。）

Problem: {problem}
（问题：{problem}）

{template_text}
"""
    
    return specialized_template

# Example usage
# （示例用法）
legal_reasoning_template = generate_specialized_template("legal", "advanced", llm)
math_template = generate_specialized_template("mathematics", "intermediate", llm)

# Apply the generated template
# （应用生成的模板）
legal_problem = "Analyze the liability implications in this contract clause..."
legal_prompt = legal_reasoning_template(legal_problem)
```

This meta-level approach enables the creation of highly specialized templates tailored to specific domains and complexity levels.
这种元级别的方法能够创建针对特定领域和复杂性级别量身定制的高度专业化模板。