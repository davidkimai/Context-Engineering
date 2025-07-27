# Verification Loop Template （验证循环模板）

## Summary （摘要）
A template for implementing self-verification processes that catch errors, validate results, and improve overall reliability through structured checking mechanisms.
一个用于实现自我验证过程的模板，通过结构化检查机制捕获错误、验证结果并提高整体可靠性。

## Context & Application （背景与应用）
Use this template when accuracy is critical and you want to build explicit verification into the reasoning process. The verification loop reduces errors by encouraging systematic checking of assumptions, calculations, and conclusions before finalizing results.
当准确性至关重要且您希望在推理过程中构建显式验证时，请使用此模板。验证循环通过鼓励在最终确定结果之前系统地检查假设、计算和结论来减少错误。

This template is ideal for:
此模板非常适合：
- Tasks with high stakes where errors could be costly
- 错误可能代价高昂的高风险任务
- Complex calculations or logical reasoning chains
- 复杂计算或逻辑推理链
- Situations prone to common reasoning fallacies
- 容易出现常见推理谬误的情况
- Cases where thoroughness is more important than speed
- 彻底性比速度更重要的案例
- Any task where verifiability of results matters
- 结果可验证性很重要的任何任务

## Template Structure （模板结构）

```
# Task: {{task_description}}

## Approach
Complete this task using a verification loop:

1. Initial Solution
   - {{solution_approach}}
   - Develop your initial answer

2. Verification Process
   - Check assumptions: {{assumption_verification}}
   - Verify calculations/logic: {{process_verification}}
   - Test edge cases: {{edge_case_verification}}
   - Consider alternatives: {{alternative_verification}}

3. Error Correction
   - Identify any issues found during verification
   - Make necessary corrections

4. Final Answer
   - Present your verified solution
   - Note any uncertainty or limitations

## Expected Output
Show your complete process including initial solution, verification steps, any corrections, and final verified answer.
```

## Parameters （参数）

- `{{task_description}}`: Clear description of the task to complete
- `{{task_description}}`：要完成任务的清晰描述
- `{{solution_approach}}`: Method to use for initial solution (e.g.,