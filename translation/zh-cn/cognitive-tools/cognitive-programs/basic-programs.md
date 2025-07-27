# Basic Cognitive Programs （基础认知程序）

> "Programs must be written for people to read, and only incidentally for machines to execute." — Harold Abelson
> “程序首先是写给人看的，只是顺便给机器执行。” — Harold Abelson

## Overview （概述）

Cognitive programs are structured, reusable prompt patterns that guide language models through specific reasoning processes. Unlike traditional templates, cognitive programs incorporate programming concepts such as variables, functions, control structures, and composition to create more sophisticated and adaptable reasoning frameworks.
认知程序是结构化、可复用的提示模式，引导语言模型完成特定的推理过程。与传统模板不同，认知程序融合了变量、函数、控制结构和组合等编程概念，以创建更复杂、适应性更强的推理框架。

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│  COGNITIVE PROGRAM STRUCTURE                                 │
│  （认知程序结构）                                            │
│                                                              │
│  function programName(parameters) {                          │
│    // Processing logic                                       │
│    // （处理逻辑）                                           │
│    return promptText;                                        │
│  }                                                           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## Fundamental Programming Concepts （基本编程概念）

### 1. Functions and Parameters （函数与参数）

The basic building block of cognitive programs is the function with parameters.
认知程序的基本构建块是带参数的函数。

```javascript
function analyze(topic, depth="detailed", focus=null) {
  // Function implementation
  // （函数实现）
  let depthInstructions = {
    "brief": "Provide a high-level overview with 1-2 key points.",
    "detailed": "Explore major aspects with supporting evidence.",
    "comprehensive": "Conduct an exhaustive analysis with nuanced considerations."
  };
  
  let focusInstruction = focus ? 
    `Focus particularly on aspects related to ${focus}.` : 
    "Cover all relevant aspects evenly.";
  
  return `
    Task: Analyze ${topic} at a ${depth} level.
    
    Instructions:
    ${depthInstructions[depth]}
    ${focusInstruction}
    
    Please structure your analysis with clear headings and bullet points where appropriate.
  `;
}
```

**Key Components**:
- **Function Name**: Describes the cognitive operation (e.g., `analyze`)
- **Parameters**: Customize the operation (e.g., topic, depth, focus)
- **Default Values**: Provide sensible defaults that can be overridden
- **Return Value**: The complete prompt to be sent to the LLM

**关键组成部分**：
- **函数名称**：描述认知操作（例如，`analyze`）
- **参数**：自定义操作（例如，主题、深度、焦点）
- **默认值**：提供可被覆盖的合理默认值
- **返回值**：发送给大型语言模型的完整提示

**Usage Example**:
```javascript
// Generate prompts with different parameter combinations
// （使用不同的参数组合生成提示）
const climatePrompt = analyze("climate change", "detailed", "economic impacts");
const aiPrompt = analyze("artificial intelligence", "comprehensive");
const quickCovidPrompt = analyze("COVID-19", "brief");
```

### 2. Conditional Logic （条件逻辑）

Conditional statements allow cognitive programs to adapt based on inputs or context.
条件语句允许认知程序根据输入或上下文进行调整。

```javascript
function solve_problem(problem, show_work=true, difficulty=null) {
  // Detect problem type and difficulty if not specified
  // （如果未指定，则检测问题类型和难度）
  let problemType = detect_problem_type(problem);
  let problemDifficulty = difficulty || estimate_difficulty(problem);
  
  // Determine appropriate approach based on problem type
  // （根据问题类型确定适当的方法）
  let approach;
  let steps;
  
  if (problemType === "mathematical") {
    approach = "mathematical";
    steps = [
      "Identify the variables and given information",
      "Determine the appropriate formulas or techniques",
      "Apply the formulas step-by-step",
      "Verify the solution"
    ];
  } else if (problemType === "logical") {
    approach = "logical reasoning";
    steps = [
      "Identify the logical structure of the problem",
      "Determine the key premises and conclusions",
      "Apply logical inference rules",
      "Verify the argument validity"
    ];
  } else {
    approach = "analytical";
    steps = [
      "Break down the problem into components",
      "Analyze each component systematically",
      "Synthesize insights to form a solution",
      "Verify the solution addresses the original problem"
    ];
  }
  
  // Adjust detail level based on difficulty
  // （根据难度调整细节级别）
  let detailLevel;
  if (problemDifficulty === "basic") {
    detailLevel = "Provide straightforward explanations suitable for beginners.";
  } else if (problemDifficulty === "intermediate") {
    detailLevel = "Include relevant concepts and techniques with clear explanations.";
  } else {
    detailLevel = "Provide detailed explanations and consider edge cases or alternative approaches.";
  }
  
  // Construct the prompt
  // （构建提示）
  return `
    Task: Solve the following ${approach} problem.
    
    Problem: ${problem}
    
    ${show_work ? "Show your work using these steps:" : "Provide the solution:"}
    ${show_work ? steps.map((step, i) => `${i+1}. ${step}`).join("\n") : ""}
    
    ${detailLevel}
    
    ${show_work ? "Conclude with a clear final answer." : ""}
  `;
}

// Helper functions (simplified for illustration)
// （辅助函数（为便于说明而简化））
function detect_problem_type(problem) {
  // In a real implementation, this would use heuristics or LLM classification
  // （在实际实现中，这将使用启发式或 LLM 分类）
  if (problem.includes("calculate") || problem.includes("equation")) {
    return "mathematical";
  } else if (problem.includes("valid") || problem.includes("argument")) {
    return "logical";
  } else {
    return "general";
  }
}

function estimate_difficulty(problem) {
  // Simplified difficulty estimation
  // （简化的难度估计）
  const wordCount = problem.split(" ").length;
  if (wordCount < 20) return "basic";
  if (wordCount < 50) return "intermediate";
  return "advanced";
}
```

**Key Components**:
- **Condition Checks**: Branch based on problem characteristics
- **Variable Assignment**: Set values based on conditions
- **Dynamic Content**: Build different prompts based on conditions

**关键组成部分**：
- **条件检查**：根据问题特征进行分支
- **变量赋值**：根据条件设置值
- **动态内容**：根据条件构建不同的提示

**Usage Example**:
```javascript
// Generate prompts for different problem types
// （为不同类型的问题生成提示）
const mathPrompt = solve_problem("Solve for x in the equation 2x + 5 = 17");
const logicPrompt = solve_problem("Determine if the following argument is valid...", true, "advanced");
```

### 3. Loops and Iteration （循环与迭代）

Loops allow for repeated operations or building complex structures.
循环允许重复操作或构建复杂结构。

```javascript
function multi_perspective_analysis(topic, perspectives=["economic", "social", "political"], depth="detailed") {
  // Base prompt
  // （基础提示）
  let prompt = `
    Task: Analyze ${topic} from multiple perspectives.
    
    Instructions:
    Please provide a ${depth} analysis of ${topic} from each of the following perspectives.
  `;
  
  // Add sections for each perspective
  // （为每个视角添加部分）
  for (let i = 0; i < perspectives.length; i++) {
    const perspective = perspectives[i];
    prompt += `
    
    Perspective ${i+1}: ${perspective.charAt(0).toUpperCase() + perspective.slice(1)}
    - Analyze ${topic} through a ${perspective} lens
    - Identify key ${perspective} factors and implications
    - Consider important ${perspective} stakeholders and their interests
    `;
  }
  
  // Add integration section
  // （添加整合部分）
  prompt += `
  
  Integration:
  After analyzing from these individual perspectives, synthesize the insights to provide a holistic understanding of ${topic}.
  Identify areas of alignment and tension between different perspectives.
  
  Conclusion:
  Summarize the most significant insights from this multi-perspective analysis.
  `;
  
  return prompt;
}
```

**Key Components**:
- **Loop Construction**: Iterate through a collection (e.g., perspectives)
- **Content Accumulation**: Build up prompt content incrementally
- **Dynamic Generation**: Create variable numbers of sections based on inputs

**关键组成部分**：
- **循环构建**：遍历一个集合（例如，视角）
- **内容累积**：逐步构建提示内容
- **动态生成**：根据输入创建可变数量的部分

**Usage Example**:
```javascript
// Standard perspectives
// （标准视角）
const climatePrompt = multi_perspective_analysis("climate change");

// Custom perspectives
// （自定义视角）
const aiPrompt = multi_perspective_analysis(
  "artificial intelligence ethics",
  ["technological", "ethical", "regulatory", "business"]
);
```

### 4. Function Composition （函数组合）

Function composition enables building complex cognitive programs from simpler ones.
函数组合能够从更简单的认知程序构建复杂的认知程序。

```javascript
function research_and_analyze(topic, research_depth="comprehensive", analysis_type="cause-effect") {
  // First, generate a research prompt
  // （首先，生成一个研究提示）
  const researchPrompt = research(topic, research_depth);
  
  // Then, set up the analysis to use the research results
  // （然后，设置分析以使用研究结果）
  return `
    First, conduct research on ${topic}:
    
    ${researchPrompt}
    
    After completing the research above, analyze your findings using this framework:
    
    ${analyze(topic, "detailed", analysis_type)}
    
    Finally, synthesize your research and analysis into a coherent conclusion that addresses the most significant aspects of ${topic}.
  `;
}

// Component functions
// （组件函数）
function research(topic, depth="comprehensive") {
  const depthInstructions = {
    "brief": "Identify 3-5 key facts about",
    "standard": "Research the main aspects of",
    "comprehensive": "Conduct in-depth research on all significant dimensions of"
  };
  
  return `
    Task: ${depthInstructions[depth]} ${topic}.
    
    Instructions:
    - Identify credible information sources
    - Extract relevant facts, statistics, and expert opinions
    - Organize findings by subtopic
    - Note areas of consensus and disagreement
    
    Present your research in a structured format with clear headings and bullet points.
  `;
}

function analyze(topic, depth="detailed", framework="general") {
  const frameworkInstructions = {
    "general": "Analyze the key aspects and implications of",
    "cause-effect": "Analyze the causes and effects related to",
    "compare-contrast": "Compare and contrast different perspectives on",
    "swot": "Conduct a SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis of"
  };
  
  return `
    Task: ${frameworkInstructions[framework]} ${topic}.
    
    Instructions:
    - Apply the ${framework} analytical framework
    - Support analysis with evidence from reliable sources
    - Consider multiple viewpoints and potential biases
    - Identify the most significant insights
    
    Structure your analysis logically with clear sections and supporting points.
  `;
}
```

**Key Components**:
- **Function Calls**: Using one function inside another
- **Result Integration**: Combining outputs from multiple functions
- **Modular Design**: Building complex operations from simpler ones

**关键组成部分**：
- **函数调用**：在一个函数内部使用另一个函数
- **结果整合**：合并来自多个函数的输出
- **模块化设计**：从更简单的操作构建复杂的操作

**Usage Example**:
```javascript
// Combined research and analysis prompts
// （组合的研究和分析提示）
const climatePrompt = research_and_analyze("climate change mitigation strategies", "comprehensive", "swot");
const aiPrompt = research_and_analyze("artificial intelligence regulation", "standard", "compare-contrast");
```

## Basic Cognitive Program Templates （基础认知程序模板）

### 1. Problem Solver Program （问题解决程序）

A comprehensive program for solving structured problems.
一个用于解决结构化问题的综合程序。

```javascript
function problem_solver(problem, options = {}) {
  // Default options
  // （默认选项）
  const defaults = {
    show_work: true,
    verify_solution: true,
    approach: "auto-detect", // Can be "auto-detect", "mathematical", "logical", "conceptual"
    detail_level: "standard" // Can be "brief", "standard", "detailed"
  };
  
  // Merge defaults with provided options
  // （将默认选项与提供的选项合并）
  const settings = {...defaults, ...options};
  
  // Determine approach if auto-detect
  // （如果自动检测，则确定方法）
  let approach = settings.approach;
  if (approach === "auto-detect") {
    // Simple heuristic detection (would be more sophisticated in practice)
    // （简单的启发式检测（在实践中会更复杂））
    if (/\d[+\-*\/=]/.test(problem) || /equation|calculate|solve for|find the value/.test(problem.toLowerCase())) {
      approach = "mathematical";
    } else if (/valid|argument|fallacy|premise|conclusion/.test(problem.toLowerCase())) {
      approach = "logical";
    } else {
      approach = "conceptual";
    }
  }
  
  // Build approach-specific instructions
  // （构建特定方法的说明）
  let approachInstructions;
  if (approach === "mathematical") {
    approachInstructions = `
      Mathematical Problem Solving Approach:
      1. Identify all variables, constants, and their relationships
      2. Determine the appropriate mathematical techniques or formulas
      3. Apply the techniques systematically
      4. Compute the solution with careful attention to units and precision
    `;
  } else if (approach === "logical") {
    approachInstructions = `
      Logical Reasoning Approach:
      1. Identify the logical structure, premises, and conclusions
      2. Determine the type of logical argument being made
      3. Apply appropriate rules of inference
      4. Evaluate the validity and soundness of the argument
    `;
  } else {
    approachInstructions = `
      Conceptual Analysis Approach:
      1. Clarify key concepts and their relationships
      2. Break down the problem into manageable components
      3. Analyze each component systematically
      4. Synthesize insights to form a comprehensive solution
    `;
  }
  
  // Adjust detail level
  // （调整细节级别）
  let detailInstructions;
  if (settings.detail_level === "brief") {
    detailInstructions = "Provide a concise solution focusing on the key steps and insights.";
  } else if (settings.detail_level === "standard") {
    detailInstructions = "Provide a clear explanation of your reasoning process with sufficient detail.";
  } else {
    detailInstructions = "Provide a thorough explanation with detailed reasoning at each step.";
  }
  
  // Build verification section if requested
  // （如果请求，则构建验证部分）
  let verificationSection = "";
  if (settings.verify_solution) {
    verificationSection = `
      Verification:
      After completing your solution, verify its correctness by:
      1. Checking that it directly addresses the original problem
      2. Testing the solution with specific examples or edge cases if applicable
      3. Reviewing calculations or logical steps for errors
      4. Confirming that all constraints and conditions are satisfied
    `;
  }
  
  // Construct the final prompt
  // （构建最终提示）
  return `
    Task: Solve the following problem.
    
    Problem: ${problem}
    
    ${settings.show_work ? "Please show your complete work and reasoning process." : "Provide your solution."}
    
    ${approachInstructions}
    
    ${detailInstructions}
    
    ${verificationSection}
    
    Conclusion:
    End with a clear, direct answer to the original problem.
  `;
}
```

**Usage Example**:
```javascript
// Mathematical problem with verification
// （带验证的数学问题）
const mathPrompt = problem_solver(
  "If a train travels at 60 mph for 2.5 hours, how far does it go?",
  { approach: "mathematical", verify_solution: true }
);

// Logical problem with brief explanation
// （带简要解释的逻辑问题）
const logicPrompt = problem_solver(
  "If all A are B, and some B are C, can we conclude that some A are C?",
  { approach: "logical", detail_level: "brief" }
);

// Conceptual problem with detailed explanation
// （带详细解释的概念问题）
const conceptPrompt = problem_solver(
  "What are the ethical implications of autonomous vehicles making life-or-death decisions?",
  { approach: "conceptual", detail_level: "detailed" }
);
```

### 2. Step-by-Step Reasoning Program （分步推理程序）

A program that guides through explicit reasoning steps.
一个引导明确推理步骤的程序。

```javascript
function step_by_step_reasoning(problem, steps = null, options = {}) {
  // Default options
  // （默认选项）
  const defaults = {
    explanations: true, // Include explanations for each step
    examples: false,    // Include examples in the instructions
    difficulty: "auto"  // Can be "auto", "basic", "intermediate", "advanced"
  };
  
  // Merge defaults with provided options
  // （将默认选项与提供的选项合并）
  const settings = {...defaults, ...options};
  
  // Determine difficulty if auto
  // （如果自动，则确定难度）
  let difficulty = settings.difficulty;
  if (difficulty === "auto") {
    // Simple heuristic (would be more sophisticated in practice)
    // （简单的启发式（在实践中会更复杂））
    const wordCount = problem.split(" ").length;
    const complexityIndicators = ["complex", "challenging", "difficult", "advanced"];
    
    const hasComplexityMarkers = complexityIndicators.some(indicator => 
      problem.toLowerCase().includes(indicator)
    );
    
    if (hasComplexityMarkers || wordCount > 50) {
      difficulty = "advanced";
    } else if (wordCount > 25) {
      difficulty = "intermediate";
    } else {
      difficulty = "basic";
    }
  }
  
  // Default steps if not provided
  // （如果未提供，则为默认步骤）
  if (!steps) {
    steps = [
      { id: "understand", name: "Understand the Problem", 
        description: "Carefully read the problem and identify what is being asked." },
      { id: "analyze", name: "Analyze Given Information", 
        description: "Identify all relevant information provided in the problem." },
      { id: "plan", name: "Plan a Solution Approach", 
        description: "Determine a strategy or method to solve the problem." },
      { id: "execute", name: "Execute the Plan", 
        description: "Carry out your solution plan step by step." },
      { id: "verify", name: "Verify the Solution", 
        description: "Check that your answer correctly solves the original problem." }
    ];
  }
  
  // Adjust explanation detail based on difficulty
  // （根据难度调整解释细节）
  let explanationPrompt;
  if (difficulty === "basic") {
    explanationPrompt = "Explain your thinking using simple, clear language.";
  } else if (difficulty === "intermediate") {
    explanationPrompt = "Provide thorough explanations that connect concepts and steps.";
  } else {
    explanationPrompt = "Include detailed explanations that address nuances and potential alternative approaches.";
  }
  
  // Build examples section if requested
  // （如果请求，则构建示例部分）
  let examplesSection = "";
  if (settings.examples) {
    examplesSection = `
      Example of Step-by-Step Reasoning:
      
      Problem: What is the area of a rectangle with length 8m and width 5m?
      
      Step 1: Understand the Problem
      I need to find the area of a rectangle with given dimensions.
      
      Step 2: Analyze Given Information
      - Length = 8 meters
      - Width = 5 meters
      
      Step 3: Plan a Solution Approach
      I'll use the formula: Area of rectangle = length × width
      
      Step 4: Execute the Plan
      Area = 8m × 5m = 40 square meters
      
      Step 5: Verify the Solution
      I can verify by dividing the area by the width: 40 ÷ 5 = 8, which equals the length.
      
      Final Answer: The area of the rectangle is 40 square meters.
    `;
  }
  
  // Build the steps instructions
  // （构建步骤说明）
  let stepsInstructions = "";
  steps.forEach((step, index) => {
    stepsInstructions += `
      Step ${index + 1}: ${step.name}
      ${step.description}
      ${settings.explanations ? `For this step: ${explanationPrompt}` : ""}
    `;
  });
  
  // Construct the final prompt
  // （构建最终提示）
  return `
    Task: Solve the following problem using a step-by-step reasoning approach.
    
    Problem: ${problem}
    
    Instructions:
    Break down your solution into the following steps, showing your work clearly at each stage.
    
    ${stepsInstructions}
    
    Conclusion:
    After completing all steps, provide your final answer clearly.
    
    ${examplesSection}
  `;
}
```

**Usage Example**:
```javascript
// Basic problem with standard steps
// （带标准步骤的基本问题）
const basicPrompt = step_by_step_reasoning(
  "A car travels 150 miles in 3 hours. What is its average speed?",
  null,
  { difficulty: "basic", examples: true }
);

// Custom steps for a specific reasoning approach
// （特定推理方法的自定义步骤）
const customSteps = [
  { id: "identify", name: "Identify Variables", 
    description: "List all variables in the problem." },
  { id: "formula", name: "Select Formula", 
    description: "Choose the appropriate formula for this problem." },
  { id: "substitute", name: "Substitute Values", 
    description: "Plug the known values into the formula." },
  { id: "solve", name: "Solve Equation", 
    description: "Solve for the unknown variable." },
  { id: "check", name: "Check Solution", 
    description: "Verify your answer makes sense." }
];

const physicsPrompt = step_by_step_reasoning(
  "An object is thrown upward with an initial velocity of 15 m/s. How high will it go?",
  customSteps,
  { difficulty: "intermediate" }
);
```

### 3. Comparative Analysis Program （比较分析程序）

A program for structured comparison between multiple items.
一个用于多个项目之间结构化比较的程序。

```javascript
function comparative_analysis(items, criteria = null, options = {}) {
  // Default options
  // （默认选项）
  const defaults = {
    format: "table",       // Can be "table", "narrative", "pros-cons"
    conclusion: true,      // Include a conclusion section
    highlight_differences: true, // Emphasize key differences
    detail_level: "balanced" // Can be "brief", "balanced", "detailed"
  };
  
  // Merge defaults with provided options
  // （将默认选项与提供的选项合并）
  const settings = {...defaults, ...options};
  
  // Ensure items is an array
  // （确保项目是一个数组）
  const itemsList = Array.isArray(items) ? items : [items];
  
  // Generate default criteria if none provided
  // （如果未提供，则生成默认标准）
  if (!criteria) {
    criteria = [
      { id: "features", name: "Key Features" },
      { id: "advantages", name: "Advantages" },
      { id: "limitations", name: "Limitations" },
      { id: "applications", name: "Applications" }
    ];
  }
  
  // Format items for display
  // （格式化项目以供显示）
  const itemsDisplay = itemsList.join(", ");
  
  // Build criteria section
  // （构建标准部分）
  let criteriaSection = "";
  criteria.forEach((criterion, index) => {
    criteriaSection += `
      ${index + 1}. ${criterion.name}${criterion.description ? `: ${criterion.description}` : ""}
    `;
  });
  
  // Build format-specific instructions
  // （构建特定格式的说明）
  let formatInstructions;
  if (settings.format === "table") {
    formatInstructions = `
      Present your analysis in a table format:
      
      | Criteria | ${itemsList.map(item => item).join(" | ")} |
      |----------|${itemsList.map(() => "---------").join("|")}|
      ${criteria.map(c => `| ${c.name} | ${itemsList.map(() => "?").join(" | ")} |`).join("\n")}
      
      For each cell, provide a concise analysis of how the item performs on that criterion.
    `;
  } else if (settings.format === "pros-cons") {
    formatInstructions = `
      For each item, provide a structured pros and cons analysis:
      
      ${itemsList.map(item => `
      ## ${item}
      
      Pros:
      - [Pro point 1]
      - [Pro point 2]
      
      Cons:
      - [Con point 1]
      - [Con point 2]
      `).join("\n")}
      
      Ensure that your pros and cons directly address the criteria.
    `;
  } else {
    formatInstructions = `
      Present your analysis in a narrative format:
      
      For each criterion, discuss how all items compare, highlighting similarities and differences.
      
      ${criteria.map(c => `## ${c.name}\n[Comparative analysis for this criterion]`).join("\n\n")}
    `;
  }
  
  // Build detail level instructions
  // （构建细节级别说明）
  let detailInstructions;
  if (settings.detail_level === "brief") {
    detailInstructions = "Focus on the most essential points for each criterion, keeping the analysis concise.";
  } else if (settings.detail_level === "balanced") {
    detailInstructions = "Provide a balanced analysis with sufficient detail to support meaningful comparison.";
  } else {
    detailInstructions = "Include comprehensive details for each criterion, exploring nuances and edge cases.";
  }
  
  // Build differences section if requested
  // （如果请求，则构建差异部分）
  let differencesSection = "";
  if (settings.highlight_differences) {
    differencesSection = `
      Key Differences:
      After completing your comparative analysis, highlight the most significant differences between the items.
      Focus on differences that would be most relevant for decision-making purposes.
    `;
  }
  
  // Build conclusion section if requested
  // （如果请求，则构建结论部分）
  let conclusionSection = "";
  if (settings.conclusion) {
    conclusionSection = `
      Conclusion:
      Synthesize your analysis into a conclusion that summarizes the comparison.
      Avoid simplistic "X is better than Y" statements unless clearly supported by the analysis.
      Instead, clarify the contexts or scenarios in which each item might be preferred.
    `;
  }
  
  // Construct the final prompt
  // （构建最终提示）
  return `
    Task: Conduct a comparative analysis of the following items: ${itemsDisplay}.
    
    Instructions:
    Compare these items across the following criteria:
    ${criteriaSection}
    
    ${detailInstructions}
    
    ${formatInstructions}
    
    ${differencesSection}
    
    ${conclusionSection}
  `;
}
```

**Usage Example**:
```javascript
// Simple comparison with default criteria
// （带默认标准的简单比较）
const phonePrompt = comparative_analysis(
  ["iPhone 14", "Samsung Galaxy S23", "Google Pixel 7"],
  null,
  { format: "table" }
);

// Custom criteria with narrative format
// （带叙述格式的自定义标准）
const customCriteria = [
  { id: "efficacy", name: "Efficacy", description: "How effective is the treatment?" },
  { id: "side_effects", name: "Side Effects", description: "What are the common side effects?" },
  { id: "cost", name: "Cost", description: "What is the typical cost?" },
  { id: "accessibility", name: "Accessibility", description: "How accessible is the treatment?" }
];

const treatmentPrompt = comparative_analysis(
  ["Cognitive Behavioral Therapy", "Medication", "Mindfulness-Based Stress Reduction"],
  customCriteria,
  { format: "narrative", detail_level: "detailed" }
);
```

## Implementing Cognitive Programs （实现认知程序）

In practical applications, cognitive programs can be implemented in various ways:
在实际应用中，认知程序可以通过多种方式实现：

### 1. JavaScript/TypeScript Implementation （JavaScript/TypeScript 实现）

```javascript
// In a Node.js or browser environment
// （在 Node.js 或浏览器环境中）
const cognitivePrograms = {
  problemSolver: function(problem, options = {}) {
    // Implementation as shown above
    // （如上所示的实现）
  },
  
  stepByStepReasoning: function(problem, steps = null, options = {}) {
    // Implementation as shown above
    // （如上所示的实现）
  },
  
  // Add more programs as needed
  // （根据需要添加更多程序）
};

// Usage
// （用法）
const prompt = cognitivePrograms.problemSolver("Solve for x: 2x + 5 = 15");
callLLM(prompt).then(response => console.log(response));
```

### 2. Python Implementation （Python 实现）

```python
class CognitivePrograms:
    @staticmethod
    def problem_solver(problem, **options):
        # Implementation converted to Python
        # （转换为 Python 的实现）
        defaults = {
            "show_work": True,
            "verify_solution": True,
            "approach": "auto-detect",
            "detail_level": "standard"
        }
        
        # Merge defaults with provided options
        # （将默认选项与提供的选项合并）
        settings = {**defaults, **options}
        
        # Rest of implementation...
        # （其余实现...）
        return prompt
    
    @staticmethod
    def step_by_step_reasoning(problem, steps=None, **options):
        # Implementation converted to Python
        # （转换为 Python 的实现）
        pass
    
    # Add more programs as needed
    # （根据需要添加更多程序）

# Usage
// （用法）
prompt = CognitivePrograms.problem_solver("Solve for x: 2x + 5 = 15")
response = call_llm(prompt)
print(response)
```

### 3. Prompt String Templates （提示字符串模板）

For simpler implementations without a programming environment:
对于没有编程环境的更简单的实现：

```
PROBLEM SOLVER TEMPLATE

Task: Solve the following problem.

Problem: {{PROBLEM}}

Please show your complete work and reasoning process.

{{APPROACH_INSTRUCTIONS}}

{{DETAIL_INSTRUCTIONS}}

{{VERIFICATION_SECTION}}

Conclusion:
End with a clear, direct answer to the original problem.
```

## Measurement and Optimization （测量与优化）

When using cognitive programs, measure their effectiveness by:
使用认知程序时，通过以下方式衡量其有效性：

1. **Accuracy**: Does the program consistently lead to correct solutions?
   **准确性**：程序是否始终能得出正确的解决方案？
2. **Token Efficiency**: What is the token overhead compared to simpler prompts?
   **令牌效率**：与更简单的提示相比，令牌开销是多少？
3. **Adaptability**: How well does the program handle different variations of problems?
   **适应性**：程序处理不同问题变体的能力如何？
4. **Clarity**: Is the reasoning process clear and easy to follow?
   **清晰度**：推理过程是否清晰易懂？

Optimize your programs by:
通过以下方式优化您的程序：
- Removing unnecessary instructions that don't improve performance
  - 移除不能提高性能的不必要指令
- Adjusting parameters based on empirical testing
  - 根据经验测试调整参数
- Creating specialized variants for different problem domains
  - 为不同的问题领域创建专门的变体

## Next Steps （后续步骤）

- Explore [advanced-programs.md](./advanced-programs.md) for more sophisticated programming patterns
- See [program-library.py](./program-library.py) for a complete implementation library
- Try [program-examples.ipynb](./program-examples.ipynb) for interactive examples and experiments

- 探索 [advanced-programs.md](./advanced-programs.md) 以了解更复杂的编程模式
- 查看 [program-library.py](./program-library.py) 以获取完整的实现库
- 尝试 [program-examples.ipynb](./program-examples.ipynb) 以获取交互式示例和实验

---

## Deeper Dive: Cognitive Program Design Principles （深入探讨：认知程序设计原则）

When designing your own cognitive programs, consider these principles:
在设计自己的认知程序时，请考虑以下原则：

1. **Single Responsibility**: Each program should focus on one type of cognitive operation
   **单一职责**：每个程序应专注于一种类型的认知操作
2. **Clear Parameters**: Make customization options explicit and well-documented
   **清晰的参数**：使自定义选项明确且文档齐全
3. **Sensible Defaults**: Provide reasonable default values for optional parameters
   **合理的默认值**：为可选参数提供合理的默认值
4. **Error Handling**: Consider how the program should behave with unexpected inputs
   **错误处理**：考虑程序在遇到意外输入时应如何表现
5. **Composability**: Design programs that can be easily combined with others
   **可组合性**：设计易于与其他程序组合的程序
6. **Testability**: Make it easy to evaluate the program's effectiveness
   **可测试性**：使其易于评估程序的有效性

These principles help create cognitive programs that are reusable, maintainable, and effective across a wide range of applications.
这些原则有助于创建可复用、可维护且在各种应用中都有效的认知程序。