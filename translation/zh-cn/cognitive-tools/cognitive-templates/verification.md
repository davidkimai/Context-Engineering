# Verification Templates （验证模板）

> "Trust, but verify." — Russian proverb
> “信任，但要核实。” — 俄罗斯谚语

## Overview （概述）

Verification templates help language models check their own work, catch errors, and ensure the quality of their outputs. These templates are crucial for increasing reliability, reducing hallucinations, and improving overall accuracy.
验证模板可帮助语言模型检查自身工作、发现错误并确保其输出质量。这些模板对于提高可靠性、减少幻觉和提升整体准确性至关重要。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  VERIFICATION PROCESS                                        │
│  （验证流程）                                                │
│                                                              │
│  Solution → Check Logic → Test Assumptions → Correct → Final │
│  （解决方案 → 检查逻辑 → 测试假设 → 修正 → 最终方案）        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Basic Templates （基础模板）

### 1. Solution Verification （解决方案验证）

The fundamental template for checking a solution or answer.
用于检查解决方案或答案的基本模板。

```markdown
# Solution Verification Template （解决方案验证模板）

Task: Verify the correctness of the following solution.
任务：验证以下解决方案的正确性。

Problem: {{problem}}
问题：{{problem}}
Proposed Solution: {{solution}}
提议的解决方案：{{solution}}

Please follow this verification process:
请遵循此验证流程：
1. **Restate the Problem**: Confirm understanding of what was asked.
   **重述问题**：确认对所提问题的理解。
2. **Check Methodology**: Is the approach used appropriate for this problem?
   **检查方法**：所用方法是否适用于此问题？
3. **Verify Calculations**: Check all mathematical operations for accuracy.
   **验证计算**：检查所有数学运算的准确性。
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
   **检查逻辑**：审查推理过程中是否存在逻辑错误或漏洞。
5. **Test with Examples**: Test the solution with specific examples or edge cases.
   **用例测试**：使用具体示例或边缘案例测试解决方案。
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
   **检查约束**：确保满足原始问题的所有约束条件。
7. **Final Assessment**: State whether the solution is:
   **最终评估**：说明解决方案是：
   - Correct: The solution is completely accurate
     正确：解决方案完全准确
   - Partially Correct: The solution has minor errors (specify)
     部分正确：解决方案存在次要错误（请指明）
   - Incorrect: The solution has major flaws (specify)
     不正确：解决方案存在重大缺陷（请指明）

If errors are found, explain them clearly and suggest corrections.
如果发现错误，请清晰解释并提出修正建议。
```

**Token Count**: ~160 tokens (template only)
**令牌数**：约 160 个令牌（仅模板）

**Usage Example**:
- For mathematical solutions
- When checking logical arguments
- For any output where accuracy is crucial

**使用示例**：
- 用于数学解决方案
- 用于检查逻辑论证
- 用于任何对准确性要求至关重要的输出

### 2. Fact Checking （事实核查）

For verifying factual claims and statements.
用于核实事实性声明和陈述。

```markdown
# Fact Checking Template （事实核查模板）

Task: Verify the accuracy of the following statement(s).
任务：核实以下陈述的准确性。

Statement(s): {{statements}}
陈述：{{statements}}

Please follow this verification process:
请遵循此核查流程：
1. **Break Down Claims**: Identify each distinct factual claim.
   **分解声明**：识别每个独立的事实性声明。
2. **Assess Knowledge Base**: Determine if you have reliable information about each claim.
   **评估知识库**：确定您是否拥有关于每个声明的可靠信息。
3. **Verify Each Claim**:
   **核实每个声明**：
   - Claim 1: [Restate the claim]
     - 声明 1：[重述声明]
     - Assessment: [Accurate / Inaccurate / Partially Accurate / Uncertain]
       评估：[准确 / 不准确 / 部分准确 / 不确定]
     - Explanation: [Provide relevant facts and context]
       解释：[提供相关事实和背景]
     - Confidence: [High / Medium / Low]
       置信度：[高 / 中 / 低]
   - Claim 2: [Continue for each claim]
     - 声明 2：[继续处理每个声明]
4. **Check for Omissions**: Identify any relevant context that's missing.
   **检查遗漏**：识别任何缺失的相关背景信息。
5. **Overall Assessment**: Summarize the overall accuracy.
   **总体评估**：总结整体准确性。
6. **Knowledge Limitations**: Note any claims you cannot verify with confidence.
   **知识局限**：注明任何您无法自信核实的声明。

Provide corrections for any inaccurate information.
为任何不准确的信息提供修正。
```

**Token Count**: ~150 tokens (template only)
**令牌数**：约 150 个令牌（仅模板）

**Usage Example**:
- For checking historical or scientific claims
- When verifying information in summaries
- For any output containing factual assertions

**使用示例**：
- 用于核查历史或科学声明
- 用于核实摘要中的信息
- 用于任何包含事实性断言的输出

### 3. Consistency Check （一致性检查）

For ensuring internal consistency in content.
用于确保内容内部一致性。

```markdown
# Consistency Check Template （一致性检查模板）

Task: Check the following content for internal consistency.
任务：检查以下内容的内部一致性。

Content: {{content}}
内容：{{content}}

Please follow this verification process:
请遵循此验证流程：
1. **Identify Key Elements**: Note the main claims, definitions, and arguments.
   **识别关键元素**：记录主要声明、定义和论点。
2. **Create Consistency Map**:
   **创建一致性映射**：
   - Element 1: [Description]
     - 元素 1：[描述]
   - Element 2: [Description]
     - 元素 2：[描述]
   - [Continue for all important elements]
     - [继续处理所有重要元素]
3. **Check for Contradictions**:
   **检查矛盾**：
   - Between Elements: Compare each element with others for compatibility
     - 元素之间：比较每个元素与其他元素的兼容性
   - Within Elements: Check each element for internal contradictions
     - 元素内部：检查每个元素是否存在内部矛盾
4. **Temporal Consistency**: Ensure events and developments follow a logical timeline.
   **时间一致性**：确保事件和发展遵循逻辑时间线。
5. **Terminology Consistency**: Verify that terms are used consistently throughout.
   **术语一致性**：验证术语在整个过程中使用一致。
6. **Logical Flow**: Check that conclusions follow from premises.
   **逻辑流程**：检查结论是否源于前提。
7. **Final Assessment**: Summarize any inconsistencies found.
   **最终评估**：总结发现的任何不一致之处。

For each inconsistency, explain the contradiction and suggest a resolution.
对于每个不一致之处，解释其矛盾并提出解决方案。
```

**Token Count**: ~160 tokens (template only)
**令牌数**：约 160 个令牌（仅模板）

**Usage Example**:
- For long-form content
- When checking complex arguments
- For any output that builds on multiple premises

**使用示例**：
- 用于长篇内容
- 用于检查复杂论点
- 用于任何建立在多个前提之上的输出

## Advanced Templates （高级模板）

### 4. Comprehensive Error Analysis （综合错误分析）

For detailed examination of potential errors across multiple dimensions.
用于跨多个维度详细检查潜在错误。

```markdown
# Comprehensive Error Analysis Template （综合错误分析模板）

Task: Perform a thorough error analysis on the following content.
任务：对以下内容进行彻底的错误分析。

Content: {{content}}
内容：{{content}}
Context: {{context}}
背景：{{context}}

Please examine for these error types:
请检查以下错误类型：
1. **Factual Errors**:
   **事实错误**：
   - Incorrect statements: [Identify and correct]
     - 不正确的陈述：[识别并纠正]
   - Outdated information: [Identify and update]
     - 过时的信息：[识别并更新]
   - Misattributed statements: [Identify and correct]
     - 错误归属的陈述：[识别并纠正]

2. **Logical Errors**:
   **逻辑错误**：
   - False equivalences: [Identify]
     - 错误等同：[识别]
   - Non sequiturs: [Identify]
     - 不合逻辑的推论：[识别]
   - Circular reasoning: [Identify]
     - 循环推理：[识别]
   - Hasty generalizations: [Identify]
     - 轻率概括：[识别]

3. **Mathematical/Computational Errors**:
   **数学/计算错误**：
   - Calculation mistakes: [Identify and correct]
     - 计算错误：[识别并纠正]
   - Formula application errors: [Identify and correct]
     - 公式应用错误：[识别并纠正]
   - Unit conversion issues: [Identify and correct]
     - 单位转换问题：[识别并纠正]

4. **Contextual Errors**:
   **背景错误**：
   - Misunderstanding of context: [Clarify]
     - 对背景的误解：[澄清]
   - Inappropriate assumptions: [Identify]
     - 不恰当的假设：[识别]
   - Missing relevant information: [Supply]
     - 缺少相关信息：[补充]

5. **Linguistic Errors**:
   **语言错误**：
   - Ambiguous statements: [Clarify]
     - 模棱两可的陈述：[澄清]
   - Incorrect terminology: [Correct]
     - 不正确的术语：[纠正]
   - Inconsistent language: [Standardize]
     - 语言不一致：[标准化]

6. **Structural Errors**:
   **结构错误**：
   - Organizational problems: [Identify]
     - 组织问题：[识别]
   - Missing components: [Identify]
     - 缺少组件：[识别]
   - Redundancies: [Identify]
     - 冗余：[识别]

For each error found, explain:
对于发现的每个错误，请解释：
- What the error is
  - 错误是什么
- Why it's problematic
  - 为什么它有问题
- How it should be corrected
  - 应该如何纠正

Conclude with an overall assessment of the content's accuracy and reliability.
最后对内容的准确性和可靠性进行总体评估。
```

**Token Count**: ~240 tokens (template only)
**令牌数**：约 240 个令牌（仅模板）

**Usage Example**:
- For critical review of important content
- When maximum accuracy is required
- For peer review or editorial processes

**使用示例**：
- 用于对重要内容进行批判性审查
- 当要求最高准确性时
- 用于同行评审或编辑流程

### 5. Alternative Perspective Analysis （替代视角分析）

For checking bias and exploring alternative viewpoints.
用于检查偏见和探索替代观点。

```markdown
# Alternative Perspective Analysis Template （替代视角分析模板）

Task: Analyze the following content from alternative perspectives to check for bias or blind spots.
任务：从替代视角分析以下内容，以检查偏见或盲点。

Content: {{content}}
内容：{{content}}

Please follow this process:
请遵循此流程：
1. **Identify the Content's Perspective**: What worldview, assumptions, or values underlie the content?
   **识别内容的视角**：内容背后是何种世界观、假设或价值观？

2. **Explore Alternative Perspectives**:
   **探索替代视角**：
   - Perspective A: [Description of a different viewpoint]
     - 视角 A：[描述一个不同的观点]
     - How would this perspective view the content?
       - 这个视角会如何看待该内容？
     - What would it critique or question?
       - 它会批判或质疑什么？
     - What additional considerations would it raise?
       - 它会提出哪些额外的考虑？
   
   - Perspective B: [Description of another different viewpoint]
     - 视角 B：[描述另一个不同的观点]
     - How would this perspective view the content?
       - 这个视角会如何看待该内容？
     - What would it critique or question?
       - 它会批判或质疑什么？
     - What additional considerations would it raise?
       - 它会提出哪些额外的考虑？
   
   - [Continue with additional relevant perspectives]
     - [继续使用其他相关视角]

3. **Identify Blind Spots**: What important considerations are missing from the original content?
   **识别盲点**：原始内容中缺少哪些重要考虑？

4. **Check for Unstated Assumptions**: What does the content take for granted that might be questioned?
   **检查未言明的假设**：内容理所当然地认为哪些可能受到质疑的东西？

5. **Balance Assessment**: Is the content fair and balanced, or does it favor certain perspectives?
   **平衡评估**：内容是否公平、平衡，还是偏向某些视角？

6. **Recommendations**: Suggest modifications that would make the content more comprehensive and balanced.
   **建议**：提出能使内容更全面、更平衡的修改建议。

This analysis helps ensure that the content accounts for diverse viewpoints and avoids unintentional bias.
此分析有助于确保内容考虑到不同观点并避免无意的偏见。
```

**Token Count**: ~220 tokens (template only)
**令牌数**：约 220 个令牌（仅模板）

**Usage Example**:
- For policy analysis
- When checking for cultural or ideological bias
- For any content addressing controversial topics

**使用示例**：
- 用于政策分析
- 用于检查文化或意识形态偏见
- 用于处理任何有争议主题的内容

### 6. Implementation Verification （实施验证）

For checking that a solution can actually be implemented.
用于检查解决方案是否可以实际实施。

```markdown
# Implementation Verification Template （实施验证模板）

Task: Verify that the following solution can be practically implemented.
任务：验证以下解决方案是否可以实际实施。

Proposed Solution: {{solution}}
提议的解决方案：{{solution}}
Implementation Context: {{context}}
实施背景：{{context}}

Please follow this verification process:
请遵循此验证流程：
1. **Feasibility Assessment**:
   **可行性评估**：
   - Technical feasibility: Can this be built with available technology?
     - 技术可行性：这可以用现有技术构建吗？
   - Resource requirements: What resources (time, money, skills) would be needed?
     - 资源需求：需要哪些资源（时间、金钱、技能）？
   - Scalability: Would the solution work at the required scale?
     - 可扩展性：该解决方案能否在所需规模下工作？

2. **Constraints Check**:
   **约束检查**：
   - Technical constraints: Does the solution respect technical limitations?
     - 技术约束：解决方案是否尊重技术限制？
   - Regulatory constraints: Does it comply with relevant regulations?
     - 法规约束：是否符合相关法规？
   - Operational constraints: Can it be implemented within operational parameters?
     - 操作约束：能否在操作参数内实施？

3. **Risk Analysis**:
   **风险分析**：
   - Implementation risks: What could go wrong during implementation?
     - 实施风险：实施过程中可能出现什么问题？
   - Operational risks: What could go wrong once implemented?
     - 操作风险：一旦实施，可能出现什么问题？
   - Mitigation strategies: How could these risks be addressed?
     - 缓解策略：如何应对这些风险？

4. **Dependency Analysis**:
   **依赖分析**：
   - External dependencies: What does this solution depend on?
     - 外部依赖：此解决方案依赖什么？
   - Critical path: Which dependencies are on the critical path?
     - 关键路径：哪些依赖项在关键路径上？
   - Vulnerability points: Where could dependencies cause problems?
     - 漏洞点：依赖项可能在何处引起问题？

5. **Testing Approach**:
   **测试方法**：
   - Validation methods: How could the implementation be tested?
     - 验证方法：如何测试实施？
   - Success criteria: How would success be measured?
     - 成功标准：如何衡量成功？
   - Failure scenarios: How would failures be detected and addressed?
     - 失败场景：如何检测和处理失败？

6. **Overall Assessment**: Is the solution implementable as described? What modifications would improve implementability?
   **总体评估**：该解决方案是否如所述可实施？哪些修改可以提高可实施性？

This verification ensures that solutions are not just theoretically sound but practically viable.
此验证确保解决方案不仅在理论上合理，而且在实践中可行。
```

**Token Count**: ~240 tokens (template only)
**令牌数**：约 240 个令牌（仅模板）

**Usage Example**:
- For engineering solutions
- When evaluating project proposals
- For any solution that requires practical implementation

**使用示例**：
- 用于工程解决方案
- 用于评估项目提案
- 用于任何需要实际实施的解决方案

## Implementation Patterns （实施模式）

Here's a simple Python function to implement the Solution Verification template:
这是一个实现解决方案验证模板的简单 Python 函数：

```python
def verify_solution(problem, solution):
    """
    Create a prompt that verifies a proposed solution.
    （创建一个验证提议解决方案的提示。）
    
    Args:
        problem (str): The original problem
        （problem (str): 原始问题）
        solution (str): The proposed solution to verify
        （solution (str): 待验证的提议解决方案）
        
    Returns:
        str: A formatted prompt for solution verification
        （str: 用于解决方案验证的格式化提示）
    """
    return f"""
Task: Verify the correctness of the following solution.
（任务：验证以下解决方案的正确性。）

Problem: {problem}
（问题：{problem}）
Proposed Solution: {solution}
（提议的解决方案：{solution}）

Please follow this verification process:
（请遵循此验证流程：）
1. **Restate the Problem**: Confirm understanding of what was asked.
   （**重述问题**：确认对所提问题的理解。）
2. **Check Methodology**: Is the approach used appropriate for this problem?
   （**检查方法**：所用方法是否适用于此问题？）
3. **Verify Calculations**: Check all mathematical operations for accuracy.
   （**验证计算**：检查所有数学运算的准确性。）
4. **Check Logic**: Examine the reasoning for logical errors or gaps.
   （**检查逻辑**：审查推理过程中是否存在逻辑错误或漏洞。）
5. **Test with Examples**: Test the solution with specific examples or edge cases.
   （**用例测试**：使用具体示例或边缘案例测试解决方案。）
6. **Check Constraints**: Ensure all constraints from the original problem are satisfied.
   （**检查约束**：确保满足原始问题的所有约束条件。）
7. **Final Assessment**: State whether the solution is:
   （**最终评估**：说明解决方案是：）
   - Correct: The solution is completely accurate
     （正确：解决方案完全准确）
   - Partially Correct: The solution has minor errors (specify)
     （部分正确：解决方案存在次要错误（请指明））
   - Incorrect: The solution has major flaws (specify)
     （不正确：解决方案存在重大缺陷（请指明））

If errors are found, explain them clearly and suggest corrections.
（如果发现错误，请清晰解释并提出修正建议。）
"""
```

## Self-Correction Loop （自修正循环）

One of the most powerful applications of verification templates is the self-correction loop:
验证模板最强大的应用之一是自修正循环：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Initial Solution                                                   │
│  （初始解决方案）                                                   │
│       │                                                             │
│       ▼                                                             │
│  Apply Verification Template                                        │
│  （应用验证模板）                                                   │
│       │                                                             │
│       ▼                                                             │
│  Errors Found?                                                      │
│  （发现错误？）                                                     │
│       │                                                             │
│       ├─────────────Yes─────────────┐                               │
│       │             （是）          │                               │
│       ▼                             ▼                               │
│  No   │                        Apply Corrections                    │
│ （否）│                        （应用修正）                         │
│       │                             │                               │
│       ▼                             ▼                               │
│  Final Verified Solution ◄──────────┘                               │
│  （最终验证解决方案）                                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

Implementation example:
实施示例：

```python
def self_correction_loop(problem, max_iterations=3):
    """
    Implement a self-correction loop for problem solving.
    （为问题解决实施一个自修正循环。）
    
    Args:
        problem (str): The problem to solve
        （problem (str): 待解决的问题）
        max_iterations (int): Maximum number of correction iterations
        （max_iterations (int): 最大修正迭代次数）
        
    Returns:
        dict: The final solution and verification history
        （dict: 最终解决方案和验证历史）
    """
    # Initial solution
    # （初始解决方案）
    solution = llm.generate(f"Solve this problem: {problem}")
    
    history = [{"type": "solution", "content": solution}]
    iteration = 0
    
    while iteration < max_iterations:
        # Verify the current solution
        # （验证当前解决方案）
        verification = llm.generate(verify_solution(problem, solution))
        history.append({"type": "verification", "content": verification})
        
        # Check if corrections are needed
        # （检查是否需要修正）
        if "Correct: The solution is completely accurate" in verification:
            break
        
        # Generate corrected solution
        # （生成修正后的解决方案）
        correction_prompt = f"""
        Based on the verification feedback below, provide a corrected solution to the original problem.
        （根据以下验证反馈，为原始问题提供一个修正后的解决方案。）
        
        Original Problem: {problem}
        （原始问题：{problem}）
        
        Previous Solution: {solution}
        （先前的解决方案：{solution}）
        
        Verification Feedback: {verification}
        （验证反馈：{verification}）
        
        Please provide a fully corrected solution that addresses all issues identified in the verification.
        （请提供一个完全修正的解决方案，以解决验证中发现的所有问题。）
        """
        
        corrected_solution = llm.generate(correction_prompt)
        history.append({"type": "correction", "content": corrected_solution})
        
        # Update solution for next iteration
        # （更新解决方案以进行下一次迭代）
        solution = corrected_solution
        iteration += 1
    
    return {
        "problem": problem,
        "final_solution": solution,
        "verification_history": history,
        "iterations": iteration
    }
```

## Measurement and Optimization （测量与优化）

When using verification templates, measure their effectiveness by:
在使用验证模板时，通过以下方式衡量其有效性：

1. **Error Detection Rate**: What percentage of injected errors are caught?
   **错误检测率**：捕获到的注入错误百分比是多少？
2. **False Positive Rate**: How often are correct elements incorrectly flagged?
   **误报率**：正确元素被错误标记的频率是多少？
3. **Correction Quality**: How effective are the suggested corrections?
   **修正质量**：建议的修正有多有效？
4. **Iteration Efficiency**: How many iterations to reach a correct solution?
   **迭代效率**：需要多少次迭代才能得出正确解决方案？

Optimize your templates by:
通过以下方式优化您的模板：
- Adding domain-specific verification steps for specialized fields
  - 为专业领域添加特定于领域的验证步骤
- Tuning the level of scrutiny based on the importance of accuracy
  - 根据准确性的重要性调整审查级别
- Focusing on common error types for particular tasks
  - 针对特定任务关注常见错误类型

## Combining with Other Tools （与其他工具结合）

Verification templates complete the cognitive workflow:
验证模板完善了认知工作流程：

```
┌─────────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                     │     │                 │     │                 │
│ Understanding       │────►│ Reasoning       │────►│ Verification    │
│ Template            │     │ Template        │     │ Template        │
│ （理解模板）        │     │ （推理模板）      │     │ （验证模板）      │
│                     │     │                 │     │                 │
└─────────────────────┘     └─────────────────┘     └─────────────────┘
          ▲                                                │
          │                                                │
          └────────────────────────────────────────────────┘
                        (Correction Loop)
                        （修正循环）
```

This creates a complete cognitive system that can:
这创建了一个完整的认知系统，可以：
1. Understand a problem
   理解问题
2. Generate a solution
   生成解决方案
3. Verify and correct the solution
   验证并修正解决方案
4. Iterate until a satisfactory result is achieved
   迭代直至达到满意结果

## Next Steps （后续步骤）

- Explore [composition.md](./composition.md) for ways to combine multiple templates
- See how these templates can be integrated into complete cognitive programs in [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md)
- Learn about complete cognitive architectures in [../cognitive-architectures/solver-architecture.md](../cognitive-architectures/solver-architecture.md)

- 探索 [composition.md](./composition.md) 以了解组合多个模板的方法
- 在 [../cognitive-programs/basic-programs.md](../cognitive-programs/basic-programs.md) 中查看如何将这些模板集成到完整的认知程序中
- 在 [../cognitive-architectures/solver-architecture.md](../cognitive-architectures/solver-architecture.md) 中了解完整的认知架构