# CLAUDE.md - Cognitive Operating System (CLAUDE.md - 认知操作系统)

This document provides a comprehensive framework of cognitive tools, protocol shells, reasoning templates, and workflows for Claude Code. Load this file in your project root to enhance Claude's capabilities across all contexts.
本文档为 Claude Code 提供了一个包含认知工具、协议外壳、推理模板和工作流的综合框架。将此文件加载到您的项目根目录中，以增强 Claude 在所有上下文中的能力。

## 1. Core Meta-Cognitive Framework (1. 核心元认知框架)

## Context Schemas (上下文模式)

### Code Understanding Schema (代码理解模式)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Code Understanding Schema",
  "description": "Standardized format for analyzing and understanding code",
  "type": "object",
  "properties": {
    "codebase": {
      "type": "object",
      "properties": {
        "structure": {
          "type": "array",
          "description": "Key files and directories with their purposes"
        },
        "architecture": {
          "type": "string",
          "description": "Overall architectural pattern"
        },
        "technologies": {
          "type": "array",
          "description": "Key technologies, frameworks, and libraries"
        }
      }
    },
    "functionality": {
      "type": "object",
      "properties": {
        "entry_points": {
          "type": "array",
          "description": "Main entry points to the application"
        },
        "core_workflows": {
          "type": "array",
          "description": "Primary functional flows"
        },
        "data_flow": {
          "type": "string",
          "description": "How data moves through the system"
        }
      }
    },
    "quality": {
      "type": "object",
      "properties": {
        "strengths": {
          "type": "array",
          "description": "Well-designed aspects"
        },
        "concerns": {
          "type": "array",
          "description": "Potential issues or areas for improvement"
        },
        "patterns": {
          "type": "array",
          "description": "Recurring design patterns"
        }
      }
    }
  }
}
```

### Troubleshooting Schema (故障排除模式)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Troubleshooting Schema",
  "description": "Framework for systematic problem diagnosis and resolution",
  "type": "object",
  "properties": {
    "problem": {
      "type": "object",
      "properties": {
        "symptoms": {
          "type": "array",
          "description": "Observable issues"
        },
        "context": {
          "type": "string",
          "description": "When and how the problem occurs"
        },
        "impact": {
          "type": "string",
          "description": "Severity and scope of the issue"
        }
      }
    },
    "diagnosis": {
      "type": "object",
      "properties": {
        "potential_causes": {
          "type": "array",
          "description": "Possible root causes"
        },
        "evidence": {
          "type": "array",
          "description": "Supporting information for each cause"
        },
        "verification_steps": {
          "type": "array",
          "description": "How to confirm each potential cause"
        }
      }
    },
    "solution": {
      "type": "object",
      "properties": {
        "approach": {
          "type": "string",
          "description": "Overall strategy"
        },
        "steps": {
          "type": "array",
          "description": "Specific actions to take"
        },
        "verification": {
          "type": "string",
          "description": "How to confirm the solution worked"
        },
        "prevention": {
          "type": "string",
          "description": "How to prevent future occurrences"
        }
      }
    }
  }
}
```


### Reasoning Protocols (推理协议)

```
/reasoning.systematic{
    intent="Break down complex problems into logical steps with traceable reasoning",
    input={
        problem="<problem_statement>",
        constraints="<constraints>",
        context="<context>"
    },
    process=[
        /understand{action="Restate problem and clarify goals"},
        /analyze{action="Break down into components"},
        /plan{action="Design step-by-step approach"},
        /execute{action="Implement solution methodically"},
        /verify{action="Validate against requirements"},
        /refine{action="Improve based on verification"}
    ],
    output={
        solution="Implemented solution",
        reasoning="Complete reasoning trace",
        verification="Validation evidence"
    }
}
```

```
/thinking.extended{
    intent="Engage deep, thorough reasoning for complex problems requiring careful consideration",
    input={
        problem="<problem_requiring_deep_thought>",
        level="<basic|deep|deeper|ultra>" // Corresponds to think, think hard, think harder, ultrathink
    },
    process=[
        /explore{action="Consider multiple perspectives and approaches"},
        /evaluate{action="Assess trade-offs of each approach"},
        /simulate{action="Test mental models against edge cases"},
        /synthesize{action="Integrate insights into coherent solution"},
        /articulate{action="Express reasoning clearly and thoroughly"}
    ],
    output={
        conclusion="Well-reasoned solution",
        rationale="Complete thinking process",
        alternatives="Other considered approaches"
    }
}
```

### Self-Improvement Protocol (自我提升协议)

```
/self.reflect{
    intent="Continuously improve reasoning and outputs through recursive evaluation",
    input={
        previous_output="<output_to_evaluate>",
        criteria="<evaluation_criteria>"
    },
    process=[
        /assess{
            completeness="Identify missing information",
            correctness="Verify factual accuracy",
            clarity="Evaluate understandability",
            effectiveness="Determine if it meets needs"
        },
        /identify{
            strengths="Note what was done well",
            weaknesses="Recognize limitations",
            assumptions="Surface implicit assumptions"
        },
        /improve{
            strategy="Plan specific improvements",
            implementation="Apply improvements methodically"
        }
    ],
    output={
        evaluation="Assessment of original output",
        improved_output="Enhanced version",
        learning="Insights for future improvement"
    }
}
```

## 2. Workflow Protocols (2. 工作流协议)

### Explore-Plan-Code-Commit Workflow (探索-计划-编码-提交工作流)

```
/workflow.explore_plan_code_commit{
    intent="Implement a systematic approach to coding tasks with thorough planning",
    input={
        task="<task_description>",
        codebase="<relevant_files_or_directories>"
    },
    process=[
        /explore{
            action="Read relevant files and understand the codebase",
            instruction="Analyze but don't write code yet"
        },
        /plan{
            action="Create detailed implementation plan",
            instruction="Use extended thinking to evaluate alternatives"
        },
        /implement{
            action="Write code following the plan",
            instruction="Verify correctness at each step"
        },
        /finalize{
            action="Commit changes and create PR if needed",
            instruction="Write clear commit messages"
        }
    ],
    output={
        implementation="Working code solution",
        explanation="Documentation of approach",
        commit="Commit message and PR details"
    }
}
```

### Test-Driven Development Workflow (测试驱动开发工作流)

```
/workflow.test_driven{
    intent="Implement changes using test-first methodology",
    input={
        feature="<feature_to_implement>",
        requirements="<detailed_requirements>"
    },
    process=[
        /write_tests{
            action="Create comprehensive tests based on requirements",
            instruction="Don't implement functionality yet"
        },
        /verify_tests_fail{
            action="Run tests to confirm they fail appropriately",
            instruction="Validate test correctness"
        },
        /implement{
            action="Write code to make tests pass",
            instruction="Focus on passing tests, not implementation elegance initially"
        },
        /refactor{
            action="Clean up implementation while maintaining passing tests",
            instruction="Improve code quality without changing behavior"
        },
        /finalize{
            action="Commit both tests and implementation",
            instruction="Include test rationale in commit message"
        }
    ],
    output={
        tests="Comprehensive test suite",
        implementation="Working code that passes tests",
        commit="Commit message and PR details"
    }
}
```

### Iterative UI Development Workflow (迭代式 UI 开发工作流)

```
/workflow.ui_iteration{
    intent="Implement UI components with visual feedback loop",
    input={
        design="<design_mockup_or_description>",
        components="<existing_component_references>"
    },
    process=[
        /analyze_design{
            action="Understand design requirements and constraints",
            instruction="Identify reusable patterns and components"
        },
        /implement_initial{
            action="Create first implementation of UI",
            instruction="Focus on structure before styling"
        },
        /screenshot{
            action="Take screenshot of current implementation",
            instruction="Use browser tools or Puppeteer MCP"
        },
        /compare{
            action="Compare implementation with design",
            instruction="Identify differences and needed improvements"
        },
        /refine{
            action="Iteratively improve implementation",
            instruction="Take new screenshots after each significant change"
        },
        /finalize{
            action="Polish and commit final implementation",
            instruction="Include screenshots in documentation"
        }
    ],
    output={
        implementation="Working UI component",
        screenshots="Before/after visual documentation",
        commit="Commit message and PR details"
    }
}
```

## 3. Code Analysis & Generation Tools (3. 代码分析与生成工具)

### Code Analysis Protocol (代码分析协议)

```
/code.analyze{
    intent="Deeply understand code structure, patterns and quality",
    input={
        code="<code_to_analyze>",
        focus="<specific_aspects_to_examine>"
    },
    process=[
        /parse{
            structure="Identify main components and organization",
            patterns="Recognize design patterns and conventions",
            flow="Trace execution and data flow paths"
        },
        /evaluate{
            quality="Assess code quality and best practices",
            performance="Identify potential performance issues",
            security="Spot potential security concerns",
            maintainability="Evaluate long-term maintainability"
        },
        /summarize{
            purpose="Describe the code's primary functionality",
            architecture="Outline architectural approach",
            interfaces="Document key interfaces and contracts"
        }
    ],
    output={
        overview="High-level summary of the code",
        details="Component-by-component breakdown",
        recommendations="Suggested improvements"
    }
}
```

### Code Generation Protocol (代码生成协议)

```
/code.generate{
    intent="Create high-quality, maintainable code meeting requirements",
    input={
        requirements="<feature_requirements>",
        context="<codebase_context>",
        constraints="<technical_constraints>"
    },
    process=[
        /design{
            architecture="Plan overall structure",
            interfaces="Define clean interfaces",
            patterns="Select appropriate design patterns"
        },
        /implement{
            skeleton="Create foundational structure",
            core="Implement primary functionality",
            edge_cases="Handle exceptions and edge cases",
            tests="Include appropriate tests"
        },
        /review{
            functionality="Verify requirements are met",
            quality="Ensure code meets quality standards",
            style="Adhere to project conventions"
        },
        /document{
            usage="Provide usage examples",
            rationale="Explain key decisions",
            integration="Describe integration points"
        }
    ],
    output={
        code="Complete implementation",
        tests="Accompanying tests",
        documentation="Comprehensive documentation"
    }
}
```

### Refactoring Protocol (重构协议)

```
/code.refactor{
    intent="Improve existing code without changing behavior",
    input={
        code="<code_to_refactor>",
        goals="<refactoring_objectives>"
    },
    process=[
        /analyze{
            behavior="Document current behavior precisely",
            tests="Identify or create verification tests",
            issues="Identify code smells and problems"
        },
        /plan{
            approach="Design refactoring strategy",
            steps="Break down into safe, incremental changes",
            verification="Plan verification at each step"
        },
        /execute{
            changes="Implement refactoring incrementally",
            tests="Run tests after each change",
            review="Self-review each modification"
        },
        /validate{
            functionality="Verify preserved behavior",
            improvements="Confirm refactoring goals were met",
            documentation="Update documentation if needed"
        }
    ],
    output={
        refactored_code="Improved implementation",
        verification="Evidence of preserved behavior",
        improvements="Summary of changes and benefits"
    }
}
```

## 4. Testing & Validation Frameworks (4. 测试与验证框架)

### Test Suite Generation Protocol (测试套件生成协议)

```
/test.generate{
    intent="Create comprehensive test suite for code verification",
    input={
        code="<code_to_test>",
        requirements="<functionality_requirements>"
    },
    process=[
        /analyze{
            functionality="Identify core functionality",
            edge_cases="Determine boundary conditions",
            paths="Map execution paths"
        },
        /design{
            unit_tests="Design focused component tests",
            integration_tests="Design cross-component tests",
            edge_case_tests="Design boundary condition tests",
            performance_tests="Design performance verification"
        },
        /implement{
            framework="Set up testing framework",
            fixtures="Create necessary test fixtures",
            tests="Implement designed tests",
            assertions="Include clear assertions"
        },
        /validate{
            coverage="Verify adequate code coverage",
            independence="Ensure test independence",
            clarity="Confirm test readability"
        }
    ],
    output={
        test_suite="Complete test implementation",
        coverage_analysis="Test coverage assessment",
        run_instructions="How to execute tests"
    }
}
```

### Bug Diagnosis Protocol (错误诊断协议)

```
/bug.diagnose{
    intent="Systematically identify root causes of issues",
    input={
        symptoms="<observed_problem>",
        context="<environment_and_conditions>"
    },
    process=[
        /reproduce{
            steps="Establish reliable reproduction steps",
            environment="Identify environmental factors",
            consistency="Determine reproducibility consistency"
        },
        /isolate{
            scope="Narrow down affected components",
            triggers="Identify specific triggers",
            patterns="Recognize symptom patterns"
        },
        /analyze{
            trace="Follow execution path through code",
            state="Examine relevant state and data",
            interactions="Study component interactions"
        },
        /hypothesize{
            causes="Formulate potential root causes",
            tests="Design tests for each hypothesis",
            verification="Plan verification approach"
        }
    ],
    output={
        diagnosis="Identified root cause",
        evidence="Supporting evidence",
        fix_strategy="Recommended solution approach"
    }
}
```

## 5. Git & GitHub Integration (5. Git 与 GitHub 集成)

### Git Workflow Protocol (Git 工作流协议)

```
/git.workflow{
    intent="Manage code changes with Git best practices",
    input={
        changes="<code_changes>",
        branch_strategy="<branching_approach>"
    },
    process=[
        /prepare{
            branch="Create or select appropriate branch",
            scope="Define clear scope for changes",
            baseline="Ensure clean starting point"
        },
        /develop{
            changes="Implement required changes",
            commits="Create logical, atomic commits",
            messages="Write clear commit messages"
        },
        /review{
            diff="Review changes thoroughly",
            tests="Ensure tests pass",
            standards="Verify adherence to standards"
        },
        /integrate{
            sync="Sync with target branch",
            conflicts="Resolve any conflicts",
            validate="Verify integration success"
        }
    ],
    output={
        commits="Clean commit history",
        branches="Updated branch state",
        next_steps="Recommended follow-up actions"
    }
}
```

### GitHub PR Protocol (GitHub PR 协议)

```
/github.pr{
    intent="Create and manage effective pull requests",
    input={
        changes="<implemented_changes>",
        context="<purpose_and_background>"
    },
    process=[
        /prepare{
            review="Self-review changes",
            tests="Verify tests pass",
            ci="Check CI pipeline status"
        },
        /create{
            title="Write clear, descriptive title",
            description="Create comprehensive description",
            labels="Add appropriate labels",
            reviewers="Request appropriate reviewers"
        },
        /respond{
            reviews="Address review feedback",
            updates="Make requested changes",
            discussion="Engage in constructive discussion"
        },
        /finalize{
            checks="Ensure all checks pass",
            approval="Confirm necessary approvals",
            merge="Complete merge process"
        }
    ],
    output={
        pr="Complete pull request",
        status="PR status and next steps",
        documentation="Any follow-up documentation"
    }
}
```

### Git History Analysis Protocol (Git 历史分析协议)

```
/git.analyze_history{
    intent="Extract insights from repository history",
    input={
        repo="<repository_path>",
        focus="<analysis_objective>"
    },
    process=[
        /collect{
            commits="Gather relevant commit history",
            authors="Identify contributors",
            patterns="Detect contribution patterns"
        },
        /analyze{
            changes="Examine code evolution",
            decisions="Trace architectural decisions",
            trends="Identify development trends"
        },
        /synthesize{
            insights="Extract key insights",
            timeline="Create evolutionary timeline",
            attribution="Map features to contributors"
        }
    ],
    output={
        history_analysis="Comprehensive historical analysis",
        key_insights="Important historical patterns",
        visualization="Temporal representation of evolution"
    }
}
```

## 6. Project Navigation & Exploration (6. 项目导航与探索)

### Codebase Exploration Protocol (代码库探索协议)

```
/project.explore{
    intent="Build comprehensive understanding of project structure",
    input={
        repo="<repository_path>",
        focus="<exploration_objectives>"
    },
    process=[
        /scan{
            structure="Map directory hierarchy",
            files="Identify key files",
            patterns="Recognize organizational patterns"
        },
        /analyze{
            architecture="Determine architectural approach",
            components="Identify main components",
            dependencies="Map component relationships"
        },
        /document{
            overview="Create high-level summary",
            components="Document key components",
            patterns="Describe recurring patterns"
        }
    ],
    output={
        map="Structural representation of codebase",
        key_areas="Identified important components",
        entry_points="Recommended starting points"
    }
}
```

### Dependency Analysis Protocol (依赖分析协议)

```
/project.analyze_dependencies{
    intent="Understand project dependencies and relationships",
    input={
        project="<project_path>",
        depth="<analysis_depth>"
    },
    process=[
        /scan{
            direct="Identify direct dependencies",
            transitive="Map transitive dependencies",
            versions="Catalog version constraints"
        },
        /analyze{
            usage="Determine how dependencies are used",
            necessity="Evaluate necessity of each dependency",
            alternatives="Identify potential alternatives"
        },
        /evaluate{
            security="Check for security issues",
            maintenance="Assess maintenance status",
            performance="Evaluate performance impact"
        }
    ],
    output={
        dependency_map="Visual representation of dependencies",
        recommendations="Suggested optimizations",
        risks="Identified potential issues"
    }
}
```

## 7. Self-Reflection & Improvement Mechanisms (7. 自我反思与改进机制)

### Knowledge Gap Identification Protocol (知识差距识别协议)

```
/self.identify_gaps{
    intent="Recognize and address knowledge limitations",
    input={
        context="<current_task_context>",
        requirements="<knowledge_requirements>"
    },
    process=[
        /assess{
            current="Evaluate current understanding",
            needed="Identify required knowledge",
            gaps="Pinpoint specific knowledge gaps"
        },
        /plan{
            research="Design targeted research approach",
            questions="Formulate specific questions",
            sources="Identify information sources"
        },
        /acquire{
            research="Conduct necessary research",
            integration="Incorporate new knowledge",
            verification="Validate understanding"
        }
    ],
    output={
        gap_analysis="Identified knowledge limitations",
        acquired_knowledge="New information gathered",
        updated_approach="Revised approach with new knowledge"
    }
}
```

### Solution Quality Improvement Protocol (解决方案质量改进协议)

```
/self.improve_solution{
    intent="Iteratively enhance solution quality",
    input={
        current_solution="<existing_solution>",
        quality_criteria="<quality_standards>"
    },
    process=[
        /evaluate{
            strengths="Identify solution strengths",
            weaknesses="Pinpoint improvement areas",
            benchmarks="Compare against standards"
        },
        /plan{
            priorities="Determine improvement priorities",
            approaches="Design enhancement approaches",
            metrics="Define success metrics"
        },
        /enhance{
            implementation="Apply targeted improvements",
            verification="Validate enhancements",
            iteration="Repeat process as needed"
        }
    ],
    output={
        improved_solution="Enhanced implementation",
        improvement_summary="Description of enhancements",
        quality_assessment="Evaluation against criteria"
    }
}
```

## 8. Documentation Guidelines (8. 文档指南)

### Code Documentation Protocol (代码文档协议)

```
/doc.code{
    intent="Create comprehensive, useful code documentation",
    input={
        code="<code_to_document>",
        audience="<target_readers>"
    },
    process=[
        /analyze{
            purpose="Identify code purpose and function",
            interfaces="Determine public interfaces",
            usage="Understand usage patterns"
        },
        /structure{
            overview="Create high-level description",
            api="Document public API",
            examples="Develop usage examples",
            internals="Explain key internal concepts"
        },
        /implement{
            inline="Add appropriate inline comments",
            headers="Create comprehensive headers",
            guides="Develop usage guides",
            references="Include relevant references"
        },
        /validate{
            completeness="Verify documentation coverage",
            clarity="Ensure understandability",
            accuracy="Confirm technical accuracy"
        }
    ],
    output={
        documentation="Complete code documentation",
        examples="Illustrative usage examples",
        quick_reference="Concise reference guide"
    }
}
```

### Technical Writing Protocol (技术写作协议)

```
/doc.technical{
    intent="Create clear, informative technical documentation",
    input={
        subject="<documentation_topic>",
        audience="<target_readers>",
        purpose="<documentation_goals>"
    },
    process=[
        /plan{
            scope="Define documentation scope",
            structure="Design logical organization",
            level="Determine appropriate detail level"
        },
        /draft{
            overview="Create conceptual overview",
            details="Develop detailed explanations",
            examples="Include illustrative examples",
            references="Add supporting references"
        },
        /refine{
            clarity="Improve explanation clarity",
            flow="Enhance logical progression",
            accessibility="Adjust for audience understanding"
        },
        /finalize{
            review="Conduct thorough review",
            formatting="Apply consistent formatting",
            completeness="Ensure comprehensive coverage"
        }
    ],
    output={
        documentation="Complete technical document",
        summary="Executive summary",
        navigation="Guide to document structure"
    }
}
```

## 9. Project-Specific Conventions (9. 项目特定约定)

### Bash Commands (Bash 命令)
- `npm run build`: Build the project (构建项目)
- `npm run test`: Run all tests (运行所有测试)
- `npm run test:file <file>`: Run tests for a specific file (运行特定文件的测试)
- `npm run lint`: Run linter (运行 linter)
- `npm run typecheck`: Run type checker (运行类型检查器)

### Code Style (代码风格)
- Use consistent indentation (2 spaces) (使用一致的缩进（2个空格）)
- Follow project-specific naming conventions (遵循项目特定的命名约定)
- Include JSDoc comments for public functions (为公共函数添加 JSDoc 注释)
- Write unit tests for new functionality (为新功能编写单元测试)
- Follow the principle of single responsibility (遵循单一职责原则)
- Use descriptive variable and function names (使用描述性的变量和函数名)

### Git Workflow (Git 工作流)
- Use feature branches for new development (使用功能分支进行新开发)
- Write descriptive commit messages (编写描述性的提交信息)
- Reference issue numbers in commits and PRs (在提交和 PR 中引用问题编号)
- Keep commits focused and atomic (保持提交的专注和原子性)
- Rebase feature branches on main before PR (在 PR 前将功能分支变基到 main)
- Squash commits when merging to main (合并到 main 时压缩提交)

### Project Structure (项目结构)
- `/src`: Source code (源代码)
- `/test`: Test files (测试文件)
- `/docs`: Documentation (文档)
- `/scripts`: Build and utility scripts (构建和实用工具脚本)
- `/types`: Type definitions (类型定义)

## Usage Notes (使用说明)

1. **Customization**: Modify sections to match your project's specific needs and conventions.
1. **自定义**: 修改部分以匹配您项目的特定需求和约定。

2. **Extension**: Add new protocols and frameworks as they become relevant to your workflow.
2. **扩展**: 在与您的工作流相关时添加新的协议和框架。

3. **Integration**: Reference these protocols in your prompts to Claude Code by mentioning them by name or structure.
3. **集成**: 通过名称或结构提及这些协议，在您对 Claude Code 的提示中引用它们。

4. **Permissions**: Consider adding common tools to your allowlist for more efficient workflows.
4. **权限**: 考虑将常用工具添加到您的允许列表中，以实现更高效的工作流。

5. **Workflow Adaptation**: Combine and modify protocols to create custom workflows for your specific tasks.
5. **工作流适应**: 组合和修改协议，为您的特定任务创建自定义工作流。

6. **Documentation**: Keep this file updated with project-specific information and conventions.
6. **文档**: 使用项目特定的信息和约定保持此文件的更新。

7. **Sharing**: Commit this file to your repository to share these cognitive tools with your team.
7. **共享**: 将此文件提交到您的存储库，与您的团队共享这些认知工具。