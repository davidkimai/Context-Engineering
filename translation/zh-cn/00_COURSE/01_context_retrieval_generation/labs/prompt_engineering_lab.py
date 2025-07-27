#!/usr/bin/env python3
"""
Context Engineering Course - Prompt Engineering Laboratory
==========================================================

A comprehensive, research-backed implementation of advanced prompt engineering techniques
based on "A Survey of Context Engineering for Large Language Models" and formal context
engineering principles.

This laboratory provides practical implementations of:
- Chain-of-Thought (CoT) and variants
- Tree-of-Thought (ToT) reasoning
- ReAct (Reasoning + Acting) frameworks
- Self-consistency techniques
- Role-based prompting
- Meta-cognitive prompting

Usage:
    # Import the module
    from prompt_engineering_lab import *
    
    # Initialize the laboratory
    lab = PromptEngineeringLab()
    
    # Run experiments
    lab.run_chain_of_thought_experiment()
    lab.run_tree_of_thought_experiment()
    lab.run_react_experiment()

Author: Context Engineering Research Team
Version: 1.0.0
License: MIT
"""

import re
import json
import time
import asyncio
import logging
from typing import Dict, List, Optional, Union, Any, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
from datetime import datetime, timedelta

# Configure logging for experimental tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PromptingTechnique(Enum):
    """Enumeration of prompt engineering techniques."""
    CHAIN_OF_THOUGHT = "chain_of_thought"
    TREE_OF_THOUGHT = "tree_of_thought"
    REACT = "react"
    SELF_CONSISTENCY = "self_consistency"
    ROLE_BASED = "role_based"
    META_COGNITIVE = "meta_cognitive"
    FEW_SHOT = "few_shot"
    ZERO_SHOT = "zero_shot"

@dataclass
class PromptExperiment:
    """Data structure for tracking prompt engineering experiments."""
    technique: PromptingTechnique
    prompt_template: str
    test_query: str
    expected_outcome: Optional[str] = None
    execution_time: Optional[float] = None
    quality_score: Optional[float] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class ExperimentResult:
    """Data structure for experiment results."""
    experiment: PromptExperiment
    generated_response: str
    performance_metrics: Dict[str, float]
    success: bool
    error_message: Optional[str] = None

class BasePromptFramework(ABC):
    """Abstract base class for prompt engineering frameworks."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.experiment_history: List[ExperimentResult] = []
    
    @abstractmethod
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a prompt using this framework."""
        pass
    
    @abstractmethod
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse the response to extract structured information."""
        pass
    
    def log_experiment(self, result: ExperimentResult):
        """Log an experiment result."""
        self.experiment_history.append(result)
        logger.info(f"{self.name} experiment completed: {result.success}")

class ChainOfThoughtFramework(BasePromptFramework):
    """
    Implementation of Chain-of-Thought (CoT) prompting framework.
    
    Based on Wei et al. (2022) "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
    """
    
    def __init__(self):
        super().__init__(
            name="Chain-of-Thought",
            description="Sequential step-by-step reasoning framework"
        )
        self.step_indicators = ["Step 1:", "Step 2:", "Step 3:", "Step 4:", "Step 5:"]
        self.conclusion_indicators = ["Therefore:", "Conclusion:", "Final Answer:"]
    
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a Chain-of-Thought prompt."""
        context = context or {}
        
        # Determine reasoning complexity
        complexity = context.get('complexity', 'medium')
        domain = context.get('domain', 'general')
        
        if complexity == 'high':
            cot_template = self._generate_complex_cot_template()
        elif complexity == 'low':
            cot_template = self._generate_simple_cot_template()
        else:
            cot_template = self._generate_standard_cot_template()
        
        # Add domain-specific guidance if provided
        domain_guidance = self._get_domain_guidance(domain)
        
        prompt = f"""
{domain_guidance}

Problem: {query}

{cot_template}
        """.strip()
        
        return prompt
    
    def _generate_standard_cot_template(self) -> str:
        """Generate standard CoT template."""
        return """
Let me work through this step by step:

Step 1: [Understand what is being asked]
Step 2: [Identify the key information and requirements]
Step 3: [Apply relevant knowledge or methods]
Step 4: [Work through the solution systematically]
Step 5: [Verify the answer and check for reasonableness]

Therefore: [State the final answer clearly]
        """.strip()
    
    def _generate_complex_cot_template(self) -> str:
        """Generate complex CoT template for difficult problems."""
        return """
I'll approach this complex problem systematically:

Understanding Phase:
- What exactly is being asked?
- What are the constraints and requirements?
- What domain knowledge is relevant?

Analysis Phase:
- Break down the problem into components
- Identify relationships between components
- Consider multiple approaches

Solution Phase:
- Step 1: [First logical step]
- Step 2: [Second logical step] 
- Step 3: [Third logical step]
- Step 4: [Fourth logical step]
- Step 5: [Additional steps as needed]

Verification Phase:
- Does this answer make sense?
- Have I addressed all parts of the question?
- Are there any edge cases I should consider?

Final Answer: [Complete, verified solution]
        """.strip()
    
    def _generate_simple_cot_template(self) -> str:
        """Generate simple CoT template for straightforward problems."""
        return """
Let me think through this:

1. [Identify the main question]
2. [Apply the relevant method or knowledge]
3. [Calculate or reason through the solution]

Answer: [Clear, direct answer]
        """.strip()
    
    def _get_domain_guidance(self, domain: str) -> str:
        """Get domain-specific guidance for reasoning."""
        domain_guidance = {
            'mathematical': "Use mathematical reasoning and show all calculations clearly.",
            'scientific': "Apply scientific principles and cite relevant laws or theories.",
            'logical': "Use formal logic and clearly state your premises and conclusions.",
            'creative': "Think creatively while maintaining logical structure.",
            'analytical': "Break down the problem analytically and examine each component.",
            'general': "Think systematically and show your reasoning clearly."
        }
        return domain_guidance.get(domain, domain_guidance['general'])
    
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse CoT response to extract reasoning steps and conclusion."""
        parsed = {
            'reasoning_steps': [],
            'conclusion': '',
            'step_count': 0,
            'has_clear_structure': False
        }
        
        # Extract reasoning steps
        step_pattern = r'Step \d+:(.+?)(?=Step \d+:|Therefore:|Conclusion:|Final Answer:|$)'
        steps = re.findall(step_pattern, response, re.DOTALL | re.IGNORECASE)
        parsed['reasoning_steps'] = [step.strip() for step in steps]
        parsed['step_count'] = len(steps)
        
        # Extract conclusion
        conclusion_pattern = r'(?:Therefore:|Conclusion:|Final Answer:|Answer:)(.+?)$'
        conclusion_match = re.search(conclusion_pattern, response, re.DOTALL | re.IGNORECASE)
        if conclusion_match:
            parsed['conclusion'] = conclusion_match.group(1).strip()
        
        # Check for clear structure
        parsed['has_clear_structure'] = (
            parsed['step_count'] > 0 and 
            len(parsed['conclusion']) > 0
        )
        
        return parsed

class TreeOfThoughtFramework(BasePromptFramework):
    """
    Implementation of Tree-of-Thought (ToT) prompting framework.
    
    Based on Yao et al. (2023) "Tree of Thoughts: Deliberate Problem Solving with Large Language Models"
    """
    
    def __init__(self):
        super().__init__(
            name="Tree-of-Thought",
            description="Parallel reasoning exploration with path evaluation"
        )
        self.max_branches = 4
        self.evaluation_criteria = ['feasibility', 'completeness', 'efficiency']
    
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a Tree-of-Thought prompt."""
        context = context or {}
        num_branches = context.get('num_branches', 3)
        evaluation_focus = context.get('evaluation_focus', 'comprehensive')
        
        prompt = f"""
Problem: {query}

I'll explore multiple reasoning paths simultaneously to find the best solution:

🌳 REASONING TREE EXPLORATION:

Branch A: [Approach 1 - {self._get_approach_description(1)}]
├── Step A1: [First step of this approach]
├── Step A2: [Second step of this approach]  
├── Step A3: [Third step of this approach]
└── Evaluation: [Assess this path's viability]
   • Feasibility: [How practical is this approach?]
   • Completeness: [Does this address all aspects?]
   • Efficiency: [How efficient is this solution?]

Branch B: [Approach 2 - {self._get_approach_description(2)}]
├── Step B1: [First step of this approach]
├── Step B2: [Second step of this approach]
├── Step B3: [Third step of this approach]
└── Evaluation: [Assess this path's viability]
   • Feasibility: [How practical is this approach?]
   • Completeness: [Does this address all aspects?]
   • Efficiency: [How efficient is this solution?]

Branch C: [Approach 3 - {self._get_approach_description(3)}]
├── Step C1: [First step of this approach]
├── Step C2: [Second step of this approach]
├── Step C3: [Third step of this approach]
└── Evaluation: [Assess this path's viability]
   • Feasibility: [How practical is this approach?]
   • Completeness: [Does this address all aspects?]
   • Efficiency: [How efficient is this solution?]

PATH COMPARISON AND SELECTION:
• Branch A Analysis: [Strengths and weaknesses]
• Branch B Analysis: [Strengths and weaknesses]
• Branch C Analysis: [Strengths and weaknesses]

OPTIMAL PATH SELECTION:
Selected Branch: [Choose the best branch with clear justification]
Justification: [Explain why this path is optimal]

FINAL SOLUTION:
[Complete solution using the optimal path with full reasoning]
        """.strip()
        
        return prompt
    
    def _get_approach_description(self, branch_number: int) -> str:
        """Get description for different approach types."""
        approaches = {
            1: "Direct/Analytical Approach",
            2: "Alternative/Creative Approach", 
            3: "Systematic/Methodical Approach",
            4: "Hybrid/Combined Approach"
        }
        return approaches.get(branch_number, f"Approach {branch_number}")
    
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse ToT response to extract branches and evaluations."""
        parsed = {
            'branches': [],
            'evaluations': {},
            'selected_branch': '',
            'final_solution': '',
            'comparison_performed': False
        }
        
        # Extract branches
        branch_pattern = r'Branch ([A-Z]):\s*(.+?)(?=Branch [A-Z]:|PATH COMPARISON|$)'
        branches = re.findall(branch_pattern, response, re.DOTALL | re.IGNORECASE)
        
        for branch_id, branch_content in branches:
            # Extract steps for this branch
            step_pattern = f'Step {branch_id}\\d+:(.+?)(?=Step {branch_id}\\d+:|Evaluation:|Branch [A-Z]:|$)'
            steps = re.findall(step_pattern, branch_content, re.DOTALL)
            
            # Extract evaluation for this branch
            eval_pattern = f'Evaluation:(.+?)(?=Branch [A-Z]:|PATH COMPARISON|$)'
            eval_match = re.search(eval_pattern, branch_content, re.DOTALL | re.IGNORECASE)
            evaluation = eval_match.group(1).strip() if eval_match else ""
            
            parsed['branches'].append({
                'id': branch_id,
                'steps': [step.strip() for step in steps],
                'evaluation': evaluation
            })
        
        # Extract selected branch
        selected_pattern = r'Selected Branch:\s*(.+?)(?=Justification:|FINAL SOLUTION:|$)'
        selected_match = re.search(selected_pattern, response, re.IGNORECASE)
        if selected_match:
            parsed['selected_branch'] = selected_match.group(1).strip()
        
        # Extract final solution
        solution_pattern = r'FINAL SOLUTION:\s*(.+?)$'
        solution_match = re.search(solution_pattern, response, re.DOTALL | re.IGNORECASE)
        if solution_match:
            parsed['final_solution'] = solution_match.group(1).strip()
        
        # Check if comparison was performed
        parsed['comparison_performed'] = 'PATH COMPARISON' in response.upper()
        
        return parsed

class ReActFramework(BasePromptFramework):
    """
    Implementation of ReAct (Reasoning + Acting) framework.
    
    Based on Yao et al. (2022) "ReAct: Synergizing Reasoning and Acting in Language Models"
    """
    
    def __init__(self):
        super().__init__(
            name="ReAct",
            description="Reasoning and Acting integration framework"
        )
        self.available_actions = [
            'search', 'calculate', 'analyze', 'verify', 'synthesize'
        ]
    
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a ReAct prompt."""
        context = context or {}
        available_tools = context.get('tools', self.available_actions)
        max_iterations = context.get('max_iterations', 5)
        
        tools_description = self._format_tools_description(available_tools)
        
        prompt = f"""
Task: {query}

Available Actions: {', '.join(available_tools)}

{tools_description}

I'll solve this using Reasoning + Acting cycles:

Thought 1: [Initial analysis of what I need to do]
Action 1: [Specific action to take - must be one of: {', '.join(available_tools)}]
Observation 1: [Result of the action or information gathered]

Thought 2: [Reasoning based on the observation]
Action 2: [Next action based on my reasoning]
Observation 2: [Result of the second action]

Thought 3: [Updated analysis incorporating all information]
Action 3: [Final action or conclusion]
Observation 3: [Final result or synthesis]

Final Answer: [Complete solution based on the reasoning-action cycle]

Note: Continue the Thought-Action-Observation cycle until you have sufficient information to provide a comprehensive answer.
        """.strip()
        
        return prompt
    
    def _format_tools_description(self, tools: List[str]) -> str:
        """Format description of available tools."""
        tool_descriptions = {
            'search': "Search for relevant information",
            'calculate': "Perform mathematical calculations", 
            'analyze': "Analyze data or information",
            'verify': "Verify facts or check accuracy",
            'synthesize': "Combine information from multiple sources"
        }
        
        descriptions = []
        for tool in tools:
            desc = tool_descriptions.get(tool, f"Use {tool} functionality")
            descriptions.append(f"- {tool}: {desc}")
        
        return "Tool Descriptions:\n" + "\n".join(descriptions)
    
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse ReAct response to extract thought-action cycles."""
        parsed = {
            'cycles': [],
            'final_answer': '',
            'total_cycles': 0,
            'actions_used': []
        }
        
        # Extract thought-action-observation cycles
        cycle_pattern = r'Thought (\d+):\s*(.+?)Action \1:\s*(.+?)Observation \1:\s*(.+?)(?=Thought \d+:|Final Answer:|$)'
        cycles = re.findall(cycle_pattern, response, re.DOTALL | re.IGNORECASE)
        
        for cycle_num, thought, action, observation in cycles:
            cycle_data = {
                'cycle_number': int(cycle_num),
                'thought': thought.strip(),
                'action': action.strip(),
                'observation': observation.strip()
            }
            parsed['cycles'].append(cycle_data)
            
            # Track actions used
            action_clean = action.strip().lower()
            for available_action in self.available_actions:
                if available_action in action_clean:
                    parsed['actions_used'].append(available_action)
                    break
        
        parsed['total_cycles'] = len(cycles)
        
        # Extract final answer
        final_pattern = r'Final Answer:\s*(.+?)$'
        final_match = re.search(final_pattern, response, re.DOTALL | re.IGNORECASE)
        if final_match:
            parsed['final_answer'] = final_match.group(1).strip()
        
        return parsed

class SelfConsistencyFramework(BasePromptFramework):
    """
    Implementation of Self-Consistency prompting framework.
    
    Based on Wang et al. (2022) "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
    """
    
    def __init__(self):
        super().__init__(
            name="Self-Consistency",
            description="Multiple reasoning paths with consistency validation"
        )
        self.num_paths = 3
        self.confidence_threshold = 0.7
    
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a Self-Consistency prompt."""
        context = context or {}
        num_paths = context.get('num_paths', self.num_paths)
        
        prompt = f"""
Problem: {query}

I'll solve this problem multiple ways to ensure consistency and reliability:

🔄 SOLUTION PATH 1:
[Solve the problem using your first approach - show all reasoning steps]

Answer 1: [State your answer clearly]

🔄 SOLUTION PATH 2:
[Solve the same problem using a different approach or perspective]

Answer 2: [State your answer clearly]

🔄 SOLUTION PATH 3:
[Solve the problem using a third approach for verification]

Answer 3: [State your answer clearly]

CONSISTENCY ANALYSIS:
• Agreement Check: [Do the answers agree? Which ones match?]
• Disagreement Analysis: [If answers differ, why might that be?]
• Reasoning Quality: [Which reasoning path seems most robust?]
• Confidence Assessment: [How confident are you in each approach?]

FINAL VALIDATED ANSWER:
Answer: [The most consistent and well-reasoned result]
Confidence Level: [High/Medium/Low with justification]
Reasoning: [Explanation of why this answer is most reliable]
        """.strip()
        
        return prompt
    
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse Self-Consistency response to extract multiple solutions."""
        parsed = {
            'solution_paths': [],
            'answers': [],
            'consistency_analysis': '',
            'final_answer': '',
            'confidence_level': '',
            'agreement_score': 0.0
        }
        
        # Extract solution paths and answers
        path_pattern = r'SOLUTION PATH (\d+):\s*(.+?)Answer \1:\s*(.+?)(?=SOLUTION PATH \d+:|CONSISTENCY ANALYSIS:|$)'
        paths = re.findall(path_pattern, response, re.DOTALL | re.IGNORECASE)
        
        for path_num, reasoning, answer in paths:
            parsed['solution_paths'].append({
                'path_number': int(path_num),
                'reasoning': reasoning.strip(),
                'answer': answer.strip()
            })
            parsed['answers'].append(answer.strip())
        
        # Extract consistency analysis
        analysis_pattern = r'CONSISTENCY ANALYSIS:\s*(.+?)(?=FINAL VALIDATED ANSWER:|$)'
        analysis_match = re.search(analysis_pattern, response, re.DOTALL | re.IGNORECASE)
        if analysis_match:
            parsed['consistency_analysis'] = analysis_match.group(1).strip()
        
        # Extract final answer and confidence
        final_pattern = r'Answer:\s*(.+?)Confidence Level:\s*(.+?)(?=Reasoning:|$)'
        final_match = re.search(final_pattern, response, re.DOTALL | re.IGNORECASE)
        if final_match:
            parsed['final_answer'] = final_match.group(1).strip()
            parsed['confidence_level'] = final_match.group(2).strip()
        
        # Calculate agreement score
        if len(parsed['answers']) > 1:
            unique_answers = len(set(parsed['answers']))
            total_answers = len(parsed['answers'])
            parsed['agreement_score'] = 1.0 - (unique_answers - 1) / max(1, total_answers - 1)
        
        return parsed

class RoleBasedPromptingFramework(BasePromptFramework):
    """
    Implementation of Role-Based prompting framework.
    
    Leverages persona instantiation for specialized expertise access.
    """
    
    def __init__(self):
        super().__init__(
            name="Role-Based Prompting",
            description="Expert persona instantiation framework"
        )
        self.expert_roles = {
            'scientist': {
                'expertise': ['research methodology', 'data analysis', 'hypothesis testing'],
                'approach': 'evidence-based, systematic, peer-review oriented',
                'communication': 'precise, technical, well-cited'
            },
            'analyst': {
                'expertise': ['pattern recognition', 'data interpretation', 'strategic thinking'],
                'approach': 'analytical, data-driven, objective',
                'communication': 'clear, structured, insight-focused'
            },
            'engineer': {
                'expertise': ['problem-solving', 'system design', 'optimization'],
                'approach': 'pragmatic, efficient, solution-oriented',
                'communication': 'practical, detailed, implementation-focused'
            },
            'teacher': {
                'expertise': ['explanation', 'curriculum design', 'learning psychology'],
                'approach': 'pedagogical, progressive, adaptive',
                'communication': 'clear, engaging, scaffolded'
            }
        }
    
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a role-based prompt."""
        context = context or {}
        role = context.get('role', 'analyst')
        experience_level = context.get('experience_level', 'senior')
        
        if role not in self.expert_roles:
            role = 'analyst'
        
        role_config = self.expert_roles[role]
        
        prompt = f"""
EXPERT ROLE ACTIVATION:

You are a {experience_level} {role} with extensive professional experience.

Your Expertise Includes:
{self._format_expertise(role_config['expertise'])}

Your Professional Approach:
{role_config['approach']}

Your Communication Style:
{role_config['communication']}

Professional Methodology:
When facing complex problems, you:
1. Apply domain-specific frameworks and best practices
2. Draw upon extensive professional experience
3. Consider multiple perspectives and potential solutions
4. Validate approaches against industry standards
5. Communicate findings clearly and actionably

TASK: {query}

Please approach this task with your full professional expertise and experience. Structure your response in a way that reflects your professional standards and methodology.

PROFESSIONAL RESPONSE:
        """.strip()
        
        return prompt
    
    def _format_expertise(self, expertise_list: List[str]) -> str:
        """Format expertise list for prompt."""
        return '\n'.join(f"• {expertise}" for expertise in expertise_list)
    
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse role-based response to extract professional elements."""
        parsed = {
            'professional_structure': False,
            'domain_expertise_evident': False,
            'methodology_applied': False,
            'communication_quality': 'unknown',
            'expertise_indicators': []
        }
        
        # Check for professional structure
        structure_indicators = ['analysis:', 'methodology:', 'recommendation:', 'conclusion:']
        parsed['professional_structure'] = any(
            indicator in response.lower() for indicator in structure_indicators
        )
        
        # Check for domain expertise indicators
        expertise_indicators = ['based on experience', 'industry standard', 'best practice', 
                              'professional judgment', 'methodology', 'framework']
        found_indicators = [ind for ind in expertise_indicators if ind in response.lower()]
        parsed['expertise_indicators'] = found_indicators
        parsed['domain_expertise_evident'] = len(found_indicators) > 0
        
        # Check for methodology application
        methodology_indicators = ['step 1', 'first', 'analysis', 'evaluation', 'assessment']
        parsed['methodology_applied'] = any(
            indicator in response.lower() for indicator in methodology_indicators
        )
        
        return parsed

class MetaCognitivePromptingFramework(BasePromptFramework):
    """
    Implementation of Meta-Cognitive prompting framework.
    
    Enables self-reflection, error correction, and iterative improvement.
    """
    
    def __init__(self):
        super().__init__(
            name="Meta-Cognitive Prompting",
            description="Self-reflective reasoning and improvement framework"
        )
        self.reflection_aspects = [
            'completeness', 'accuracy', 'clarity', 'relevance', 'methodology'
        ]
    
    def generate_prompt(self, query: str, context: Optional[Dict] = None) -> str:
        """Generate a meta-cognitive prompt."""
        context = context or {}
        reflection_depth = context.get('reflection_depth', 'standard')
        
        if reflection_depth == 'deep':
            return self._generate_deep_metacognitive_prompt(query)
        else:
            return self._generate_standard_metacognitive_prompt(query)
    
    def _generate_standard_metacognitive_prompt(self, query: str) -> str:
        """Generate standard meta-cognitive prompt."""
        return f"""
Task: {query}

I'll approach this with meta-cognitive awareness, monitoring and improving my reasoning:

INITIAL RESPONSE:
[Provide your initial response to the task]

META-COGNITIVE REFLECTION:
Now let me reflect on my response:

Quality Assessment:
• Completeness: Did I address all aspects of the task?
• Accuracy: Are my facts and reasoning correct? 
• Clarity: Is my explanation clear and well-structured?
• Relevance: Does everything relate directly to the task?
• Methodology: Did I use appropriate reasoning methods?

Self-Critique:
• What might I have missed or overlooked?
• Are there alternative perspectives I should consider?
• Could I provide better examples or explanations?
• Are there any weaknesses in my reasoning?

IMPROVED RESPONSE:
Based on my reflection, here's my enhanced response:
[Provide an improved version that addresses identified gaps]

FINAL REFLECTION:
[Brief assessment of the improvement process and remaining limitations]
        """.strip()
    
    def _generate_deep_metacognitive_prompt(self, query: str) -> str:
        """Generate deep meta-cognitive prompt with multiple reflection layers."""
        return f"""
Task: {query}

I'll use deep meta-cognitive reflection with multiple improvement cycles:

CYCLE 1 - INITIAL RESPONSE:
[Provide initial response]

CYCLE 1 - META-ANALYSIS:
• Cognitive processes used: [What thinking strategies did I employ?]
• Assumptions made: [What did I assume without verification?]
• Knowledge gaps: [What information do I lack?]
• Reasoning quality: [How sound is my logic?]

CYCLE 2 - REFINED RESPONSE:
[Improved response addressing cycle 1 analysis]

CYCLE 2 - DEEPER REFLECTION:
• Alternative approaches: [What other methods could I use?]
• Perspective diversity: [Have I considered multiple viewpoints?]
• Error potential: [Where might I be wrong?]
• Confidence calibration: [How confident should I be?]

CYCLE 3 - OPTIMIZED RESPONSE:
[Final optimized response incorporating all reflections]

META-LEARNING:
• What did I learn about my thinking process?
• How can I improve my approach to similar problems?
• What patterns do I notice in my reasoning?
        """.strip()
    
    def parse_response(self, response: str) -> Dict[str, Any]:
        """Parse meta-cognitive response to extract reflection elements."""
        parsed = {
            'initial_response': '',
            'reflections': [],
            'improvements': [],
            'meta_learning': '',
            'reflection_depth': 0,
            'self_awareness_indicators': []
        }
        
        # Extract initial response
        initial_pattern = r'INITIAL RESPONSE:\s*(.+?)(?=META-COGNITIVE REFLECTION:|CYCLE 1|$)'
        initial_match = re.search(initial_pattern, response, re.DOTALL | re.IGNORECASE)
        if initial_match:
            parsed['initial_response'] = initial_match.group(1).strip()
        
        # Extract reflection cycles
        reflection_pattern = r'(?:META-COGNITIVE REFLECTION:|CYCLE \d+ - META-ANALYSIS:|CYCLE \d+ - DEEPER REFLECTION:)\s*(.+?)(?=IMPROVED RESPONSE:|CYCLE \d+|FINAL REFLECTION:|META-LEARNING:|$)'
        reflections = re.findall(reflection_pattern, response, re.DOTALL | re.IGNORECASE)
        parsed['reflections'] = [ref.strip() for ref in reflections]
        parsed['reflection_depth'] = len(reflections)
        
        # Extract improvements
        improvement_pattern = r'(?:IMPROVED RESPONSE:|CYCLE \d+ - REFINED RESPONSE:|CYCLE \d+ - OPTIMIZED RESPONSE:)\s*(.+?)(?=FINAL REFLECTION:|META-COGNITIVE REFLECTION:|CYCLE \d+|META-LEARNING:|$)'
        improvements = re.findall(improvement_pattern, response, re.DOTALL | re.IGNORECASE)
        parsed['improvements'] = [imp.strip() for imp in improvements]
        
        # Extract meta-learning
        learning_pattern = r'(?:FINAL REFLECTION:|META-LEARNING:)\s*(.+?)$'
        learning_match = re.search(learning_pattern, response, re.DOTALL | re.IGNORECASE)
        if learning_match:
            parsed['meta_learning'] = learning_match.group(1).strip()
        
        # Identify self-awareness indicators
        awareness_indicators = [
            'i realize', 'i notice', 'i should consider', 'i missed', 'i assumed',
            'upon reflection', 'thinking about it', 'i could improve'
        ]
        
        found_indicators = []
        response_lower = response.lower()
        for indicator in awareness_indicators:
            if indicator in response_lower:
                found_indicators.append(indicator)
        
        parsed['self_awareness_indicators'] = found_indicators
        
        return parsed

class PromptEngineeringLab:
    """
    Comprehensive laboratory for prompt engineering research and experimentation.
    
    Provides structured experimentation environment for testing and validating
    prompt engineering techniques based on formal research methodologies.
    """
    
    def __init__(self):
        self.frameworks = {
            PromptingTechnique.CHAIN_OF_THOUGHT: ChainOfThoughtFramework(),
            PromptingTechnique.TREE_OF_THOUGHT: TreeOfThoughtFramework(),
            PromptingTechnique.REACT: ReActFramework(),
            PromptingTechnique.SELF_CONSISTENCY: SelfConsistencyFramework(),
            PromptingTechnique.ROLE_BASED: RoleBasedPromptingFramework(),
            PromptingTechnique.META_COGNITIVE: MetaCognitivePromptingFramework()
        }
        
        self.experiment_results: List[ExperimentResult] = []
        self.test_cases = self._initialize_test_cases()
        
        logger.info("Prompt Engineering Laboratory initialized with 6 frameworks")
    
    def _initialize_test_cases(self) -> Dict[str, Dict]:
        """Initialize standardized test cases for systematic evaluation."""
        return {
            'mathematical_reasoning': {
                'query': 'A train leaves Station A at 2:00 PM traveling at 60 mph. Another train leaves Station B (180 miles away) at 2:30 PM traveling toward Station A at 80 mph. At what time will they meet?',
                'expected_elements': ['distance calculation', 'relative speed', 'time calculation'],
                'domain': 'mathematical',
                'complexity': 'medium'
            },
            'logical_reasoning': {
                'query': 'All birds can fly. Penguins are birds. Penguins cannot fly. How do you resolve this logical contradiction?',
                'expected_elements': ['identify contradiction', 'examine premises', 'logical resolution'],
                'domain': 'logical',
                'complexity': 'medium'
            },
            'creative_problem_solving': {
                'query': 'Design a creative solution for reducing food waste in restaurants while maintaining profitability.',
                'expected_elements': ['problem analysis', 'creative ideas', 'feasibility assessment'],
                'domain': 'creative',
                'complexity': 'high'
            },
            'analytical_reasoning': {
                'query': 'Analyze the potential long-term economic impacts of remote work becoming permanent for 50% of knowledge workers.',
                'expected_elements': ['multiple perspectives', 'economic factors', 'systematic analysis'],
                'domain': 'analytical',
                'complexity': 'high'
            },
            'factual_retrieval': {
                'query': 'What are the key differences between mitosis and meiosis in cell division?',
                'expected_elements': ['accurate definitions', 'clear comparisons', 'scientific terminology'],
                'domain': 'scientific',
                'complexity': 'low'
            }
        }
    
    def run_systematic_experiment(self, 
                                test_case_name: str, 
                                techniques: Optional[List[PromptingTechnique]] = None,
                                custom_context: Optional[Dict] = None) -> Dict[str, ExperimentResult]:
        """
        Run systematic experiment comparing multiple prompting techniques.
        
        Args:
            test_case_name: Name of test case from self.test_cases
            techniques: List of techniques to test (default: all)
            custom_context: Additional context for prompt generation
            
        Returns:
            Dictionary mapping technique names to experiment results
        """
        if test_case_name not in self.test_cases:
            raise ValueError(f"Unknown test case: {test_case_name}")
        
        test_case = self.test_cases[test_case_name]
        techniques = techniques or list(self.frameworks.keys())
        
        results = {}
        
        logger.info(f"Starting systematic experiment: {test_case_name}")
        logger.info(f"Testing techniques: {[t.value for t in techniques]}")
        
        for technique in techniques:
            if technique not in self.frameworks:
                logger.warning(f"Unknown technique: {technique}")
                continue
            
            try:
                result = self._run_single_experiment(
                    technique=technique,
                    query=test_case['query'],
                    context={
                        'domain': test_case['domain'],
                        'complexity': test_case['complexity'],
                        **(custom_context or {})
                    },
                    expected_elements=test_case['expected_elements']
                )
                
                results[technique.value] = result
                self.experiment_results.append(result)
                
                logger.info(f"Completed {technique.value}: Success={result.success}")
                
            except Exception as e:
                logger.error(f"Experiment failed for {technique.value}: {e}")
                results[technique.value] = ExperimentResult(
                    experiment=PromptExperiment(
                        technique=technique,
                        prompt_template="Failed to generate",
                        test_query=test_case['query']
                    ),
                    generated_response="",
                    performance_metrics={},
                    success=False,
                    error_message=str(e)
                )
        
        return results
    
    def _run_single_experiment(self, 
                              technique: PromptingTechnique,
                              query: str,
                              context: Dict,
                              expected_elements: List[str]) -> ExperimentResult:
        """Run a single prompt engineering experiment."""
        framework = self.frameworks[technique]
        
        # Generate prompt
        start_time = time.time()
        prompt = framework.generate_prompt(query, context)
        generation_time = time.time() - start_time
        
        # Simulate response (in real implementation, this would call an LLM)
        simulated_response = self._simulate_llm_response(technique, prompt, query)
        
        # Parse response
        parsed_response = framework.parse_response(simulated_response)
        
        # Calculate performance metrics
        performance_metrics = self._calculate_performance_metrics(
            parsed_response, expected_elements, technique
        )
        
        # Create experiment record
        experiment = PromptExperiment(
            technique=technique,
            prompt_template=prompt,
            test_query=query,
            execution_time=generation_time,
            metadata={
                'context': context,
                'expected_elements': expected_elements,
                'parsed_response': parsed_response
            }
        )
        
        # Determine success
        success = performance_metrics.get('overall_score', 0.0) > 0.6
        
        return ExperimentResult(
            experiment=experiment,
            generated_response=simulated_response,
            performance_metrics=performance_metrics,
            success=success
        )
    
    def _simulate_llm_response(self, technique: PromptingTechnique, prompt: str, query: str) -> str:
        """
        Simulate LLM response for testing purposes.
        
        In production, this would be replaced with actual LLM API calls.
        """
        # Generate technique-specific simulated responses
        if technique == PromptingTechnique.CHAIN_OF_THOUGHT:
            return self._simulate_cot_response(query)
        elif technique == PromptingTechnique.TREE_OF_THOUGHT:
            return self._simulate_tot_response(query)
        elif technique == PromptingTechnique.REACT:
            return self._simulate_react_response(query)
        elif technique == PromptingTechnique.SELF_CONSISTENCY:
            return self._simulate_self_consistency_response(query)
        elif technique == PromptingTechnique.ROLE_BASED:
            return self._simulate_role_based_response(query)
        elif technique == PromptingTechnique.META_COGNITIVE:
            return self._simulate_metacognitive_response(query)
        else:
            return f"Simulated response for {technique.value}: {query}"
    
    def _simulate_cot_response(self, query: str) -> str:
        """Simulate Chain-of-Thought response."""
        return f"""
Step 1: I need to understand what this problem is asking.
The question involves {query[:50]}...

Step 2: Let me identify the key information and what I need to find.
Key information: [relevant details from query]
Need to find: [goal of the query]

Step 3: I'll apply the appropriate method or formula.
Using [relevant approach], I can work through this systematically.

Step 4: Let me work through the solution step by step.
[Detailed calculation or reasoning process]

Step 5: I should verify this answer makes sense.
Checking: [verification process]

Therefore: [Final answer with clear conclusion]
        """.strip()
    
    def _simulate_tot_response(self, query: str) -> str:
        """Simulate Tree-of-Thought response."""
        return f"""
🌳 REASONING TREE EXPLORATION:

Branch A: Direct Analytical Approach
├── Step A1: Break down the problem into components
├── Step A2: Apply standard methodology 
├── Step A3: Calculate or reason through systematically
└── Evaluation: This approach is straightforward and reliable
   • Feasibility: High - uses established methods
   • Completeness: Good - addresses main aspects
   • Efficiency: High - direct path to solution

Branch B: Alternative Creative Approach  
├── Step B1: Consider unconventional angles
├── Step B2: Explore creative possibilities
├── Step B3: Synthesize novel solution
└── Evaluation: This approach offers fresh perspective
   • Feasibility: Medium - requires validation
   • Completeness: Good - comprehensive view
   • Efficiency: Medium - more exploratory

Branch C: Systematic Methodical Approach
├── Step C1: Establish comprehensive framework
├── Step C2: Apply rigorous analysis
├── Step C3: Validate through multiple checks
└── Evaluation: This approach is thorough and reliable
   • Feasibility: High - well-established process
   • Completeness: Excellent - very thorough
   • Efficiency: Medium - takes more time

PATH COMPARISON AND SELECTION:
• Branch A Analysis: Fast and reliable, good for straightforward problems
• Branch B Analysis: Innovative but needs more validation
• Branch C Analysis: Most thorough but time-intensive

OPTIMAL PATH SELECTION:
Selected Branch: A (Direct Analytical Approach)
Justification: Provides the best balance of reliability, efficiency, and completeness for this type of problem.

FINAL SOLUTION:
[Complete solution using Branch A methodology with systematic reasoning]
        """.strip()
    
    def _simulate_react_response(self, query: str) -> str:
        """Simulate ReAct response."""
        return f"""
Thought 1: I need to break down this problem and determine what information I need to gather.
Action 1: analyze
Observation 1: The problem requires [specific type of analysis] and I should gather [specific information].

Thought 2: Now I have a clearer understanding. I should search for relevant information or perform calculations.
Action 2: search
Observation 2: Found relevant information: [key facts or data relevant to the query].

Thought 3: With this information, I can now synthesize a comprehensive answer.
Action 3: synthesize  
Observation 3: Combining all the information, I can provide a well-reasoned solution.

Final Answer: [Comprehensive answer based on the reasoning-action cycle, incorporating all gathered information and analysis]
        """.strip()
    
    def _simulate_self_consistency_response(self, query: str) -> str:
        """Simulate Self-Consistency response."""
        return f"""
🔄 SOLUTION PATH 1:
Let me approach this systematically by [first approach method].
[Detailed reasoning for first path]
Answer 1: [First answer]

🔄 SOLUTION PATH 2:  
Now let me try a different approach by [second approach method].
[Detailed reasoning for second path]
Answer 2: [Second answer - should be consistent]

🔄 SOLUTION PATH 3:
For verification, let me use [third approach method].
[Detailed reasoning for third path] 
Answer 3: [Third answer - should be consistent]

CONSISTENCY ANALYSIS:
• Agreement Check: All three approaches yield the same/similar answers
• Disagreement Analysis: Minor variations in [specific aspects] but core answer consistent
• Reasoning Quality: Path 1 most direct, Path 2 most thorough, Path 3 good verification
• Confidence Assessment: High confidence due to consistent results across methods

FINAL VALIDATED ANSWER:
Answer: [Consistent answer from all paths]
Confidence Level: High - confirmed through multiple independent reasoning paths
Reasoning: The consistency across different approaches strongly supports this conclusion.
        """.strip()
    
    def _simulate_role_based_response(self, query: str) -> str:
        """Simulate Role-Based response."""
        return f"""
As a senior analyst with extensive experience in this domain, I'll approach this systematically:

Professional Assessment:
Based on my years of experience, this type of problem requires [specific professional approach]. Industry best practices suggest [relevant methodology].

Analytical Framework:
1. Situational Analysis: [Professional analysis of the context]
2. Stakeholder Considerations: [Who is affected and how]
3. Risk Assessment: [Potential challenges and mitigation strategies]
4. Solution Development: [Professional recommendation based on expertise]

Methodology Applied:
Drawing upon established frameworks in my field, I'm applying [specific professional methodology] which has proven effective in similar situations.

Professional Recommendation:
[Detailed professional response with industry-specific insights and recommendations]

Quality Assurance:
This recommendation aligns with industry standards and has been validated against best practices in my professional experience.
        """.strip()
    
    def _simulate_metacognitive_response(self, query: str) -> str:
        """Simulate Meta-Cognitive response."""
        return f"""
INITIAL RESPONSE:
[Initial answer to the query]

META-COGNITIVE REFLECTION:
Quality Assessment:
• Completeness: I addressed the main aspects but may have missed [specific area]
• Accuracy: The factual content appears correct, but I should verify [specific claim]
• Clarity: The explanation is reasonably clear, though I could improve [specific aspect]
• Relevance: Everything relates to the task, though some details might be excessive
• Methodology: I used appropriate reasoning, but could consider alternative approaches

Self-Critique:
• I may have overlooked the importance of [specific consideration]
• Could provide more concrete examples to illustrate key points
• Should consider potential counterarguments or alternative perspectives
• My reasoning assumes [specific assumption] which may not always hold

IMPROVED RESPONSE:
Based on my reflection, here's an enhanced response that addresses the identified gaps:
[Improved response incorporating the self-identified improvements]

FINAL REFLECTION:
The improvement process helped me recognize that I initially focused too heavily on [specific aspect] while underemphasizing [other aspect]. This meta-cognitive approach leads to more balanced and thorough responses.
        """.strip()
    
    def _calculate_performance_metrics(self, 
                                     parsed_response: Dict[str, Any],
                                     expected_elements: List[str],
                                     technique: PromptingTechnique) -> Dict[str, float]:
        """Calculate performance metrics for experiment evaluation."""
        metrics = {
            'structure_score': 0.0,
            'completeness_score': 0.0,
            'technique_adherence_score': 0.0,
            'overall_score': 0.0
        }
        
        # Technique-specific scoring
        if technique == PromptingTechnique.CHAIN_OF_THOUGHT:
            metrics['structure_score'] = 1.0 if parsed_response.get('has_clear_structure') else 0.5
            metrics['completeness_score'] = min(1.0, parsed_response.get('step_count', 0) / 3.0)
            
        elif technique == PromptingTechnique.TREE_OF_THOUGHT:
            metrics['structure_score'] = 1.0 if parsed_response.get('comparison_performed') else 0.5
            metrics['completeness_score'] = min(1.0, len(parsed_response.get('branches', [])) / 3.0)
            
        elif technique == PromptingTechnique.REACT:
            metrics['structure_score'] = 1.0 if parsed_response.get('total_cycles', 0) > 0 else 0.0
            metrics['completeness_score'] = min(1.0, parsed_response.get('total_cycles', 0) / 3.0)
            
        elif technique == PromptingTechnique.SELF_CONSISTENCY:
            metrics['structure_score'] = 1.0 if len(parsed_response.get('answers', [])) >= 2 else 0.5
            metrics['completeness_score'] = parsed_response.get('agreement_score', 0.0)
            
        elif technique == PromptingTechnique.ROLE_BASED:
            metrics['structure_score'] = 1.0 if parsed_response.get('professional_structure') else 0.5
            metrics['completeness_score'] = 1.0 if parsed_response.get('domain_expertise_evident') else 0.5
            
        elif technique == PromptingTechnique.META_COGNITIVE:
            metrics['structure_score'] = min(1.0, parsed_response.get('reflection_depth', 0) / 2.0)
            metrics['completeness_score'] = 1.0 if len(parsed_response.get('improvements', [])) > 0 else 0.5
        
        # Technique adherence scoring
        technique_indicators = {
            PromptingTechnique.CHAIN_OF_THOUGHT: ['step', 'therefore', 'conclusion'],
            PromptingTechnique.TREE_OF_THOUGHT: ['branch', 'path', 'evaluation'],
            PromptingTechnique.REACT: ['thought', 'action', 'observation'],
            PromptingTechnique.SELF_CONSISTENCY: ['solution path', 'consistency', 'agreement'],
            PromptingTechnique.ROLE_BASED: ['professional', 'experience', 'expertise'],
            PromptingTechnique.META_COGNITIVE: ['reflection', 'critique', 'improvement']
        }
        
        # This would be implemented with actual response text analysis
        metrics['technique_adherence_score'] = 0.8  # Simulated score
        
        # Calculate overall score
        metrics['overall_score'] = (
            0.3 * metrics['structure_score'] +
            0.4 * metrics['completeness_score'] +
            0.3 * metrics['technique_adherence_score']
        )
        
        return metrics
    
    def analyze_experiment_results(self, results: Dict[str, ExperimentResult]) -> Dict[str, Any]:
        """
        Analyze experiment results to generate insights and recommendations.
        
        Args:
            results: Dictionary of experiment results by technique
            
        Returns:
            Analysis report with comparative insights
        """
        analysis = {
            'technique_rankings': [],
            'performance_comparison': {},
            'strengths_weaknesses': {},
            'recommendations': [],
            'statistical_summary': {}
        }
        
        # Extract performance scores
        technique_scores = {}
        for technique_name, result in results.items():
            if result.success:
                overall_score = result.performance_metrics.get('overall_score', 0.0)
                technique_scores[technique_name] = overall_score
        
        # Rank techniques by performance
        analysis['technique_rankings'] = sorted(
            technique_scores.items(), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        # Performance comparison
        analysis['performance_comparison'] = technique_scores
        
        # Statistical summary
        if technique_scores:
            scores = list(technique_scores.values())
            analysis['statistical_summary'] = {
                'mean_score': np.mean(scores),
                'std_score': np.std(scores),
                'min_score': np.min(scores),
                'max_score': np.max(scores),
                'score_range': np.max(scores) - np.min(scores)
            }
        
        # Generate recommendations
        if analysis['technique_rankings']:
            best_technique = analysis['technique_rankings'][0][0]
            best_score = analysis['technique_rankings'][0][1]
            
            analysis['recommendations'].append(
                f"Best performing technique: {best_technique} (score: {best_score:.3f})"
            )
            
            if best_score < 0.7:
                analysis['recommendations'].append(
                    "All techniques showed moderate performance - consider prompt refinement"
                )
            
            if len(analysis['technique_rankings']) > 1:
                score_gap = (analysis['technique_rankings'][0][1] - 
                           analysis['technique_rankings'][1][1])
                if score_gap < 0.1:
                    analysis['recommendations'].append(
                        "Performance differences are minimal - consider task-specific optimization"
                    )
        
        return analysis
    
    def generate_experiment_report(self, 
                                 test_case_name: str,
                                 results: Dict[str, ExperimentResult],
                                 analysis: Dict[str, Any]) -> str:
        """Generate comprehensive experiment report."""
        report_sections = []
        
        # Header
        report_sections.append("=" * 80)
        report_sections.append(f"PROMPT ENGINEERING EXPERIMENT REPORT")
        report_sections.append(f"Test Case: {test_case_name}")
        report_sections.append(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_sections.append("=" * 80)
        
        # Executive Summary
        report_sections.append("\nEXECUTIVE SUMMARY")
        report_sections.append("-" * 40)
        if analysis['technique_rankings']:
            best_technique = analysis['technique_rankings'][0][0]
            best_score = analysis['technique_rankings'][0][1]
            report_sections.append(f"Best Performing Technique: {best_technique}")
            report_sections.append(f"Performance Score: {best_score:.3f}")
        
        report_sections.append(f"Techniques Tested: {len(results)}")
        successful_tests = sum(1 for r in results.values() if r.success)
        report_sections.append(f"Successful Tests: {successful_tests}/{len(results)}")
        
        # Performance Rankings
        if analysis['technique_rankings']:
            report_sections.append("\nPERFORMANCE RANKINGS")
            report_sections.append("-" * 40)
            for i, (technique, score) in enumerate(analysis['technique_rankings'], 1):
                report_sections.append(f"{i}. {technique}: {score:.3f}")
        
        # Statistical Summary
        if analysis['statistical_summary']:
            stats = analysis['statistical_summary']
            report_sections.append("\nSTATISTICAL SUMMARY")
            report_sections.append("-" * 40)
            report_sections.append(f"Mean Score: {stats['mean_score']:.3f}")
            report_sections.append(f"Standard Deviation: {stats['std_score']:.3f}")
            report_sections.append(f"Score Range: {stats['min_score']:.3f} - {stats['max_score']:.3f}")
        
        # Detailed Results
        report_sections.append("\nDETAILED RESULTS")
        report_sections.append("-" * 40)
        for technique_name, result in results.items():
            report_sections.append(f"\n{technique_name}:")
            report_sections.append(f"  Success: {result.success}")
            if result.success:
                metrics = result.performance_metrics
                report_sections.append(f"  Overall Score: {metrics.get('overall_score', 0.0):.3f}")
                report_sections.append(f"  Structure Score: {metrics.get('structure_score', 0.0):.3f}")
                report_sections.append(f"  Completeness Score: {metrics.get('completeness_score', 0.0):.3f}")
            else:
                report_sections.append(f"  Error: {result.error_message}")
        
        # Recommendations
        if analysis['recommendations']:
            report_sections.append("\nRECOMMENDATIONS")
            report_sections.append("-" * 40)
            for rec in analysis['recommendations']:
                report_sections.append(f"• {rec}")
        
        return "\n".join(report_sections)
    
    def run_comparative_study(self, 
                            techniques: Optional[List[PromptingTechnique]] = None) -> Dict[str, Any]:
        """
        Run comprehensive comparative study across all test cases.
        
        Args:
            techniques: List of techniques to compare (default: all)
            
        Returns:
            Comprehensive study results with cross-case analysis
        """
        techniques = techniques or list(self.frameworks.keys())
        
        study_results = {
            'test_case_results': {},
            'technique_performance_summary': {},
            'cross_case_analysis': {},
            'overall_rankings': [],
            'study_metadata': {
                'start_time': datetime.now(),
                'techniques_tested': [t.value for t in techniques],
                'test_cases_count': len(self.test_cases)
            }
        }
        
        logger.info(f"Starting comparative study with {len(techniques)} techniques across {len(self.test_cases)} test cases")
        
        # Run experiments for each test case
        for test_case_name in self.test_cases:
            logger.info(f"Running test case: {test_case_name}")
            
            case_results = self.run_systematic_experiment(
                test_case_name=test_case_name,
                techniques=techniques
            )
            
            case_analysis = self.analyze_experiment_results(case_results)
            
            study_results['test_case_results'][test_case_name] = {
                'results': case_results,
                'analysis': case_analysis
            }
        
        # Aggregate performance across test cases
        technique_aggregate_scores = {t.value: [] for t in techniques}
        
        for test_case_data in study_results['test_case_results'].values():
            for technique_name, result in test_case_data['results'].items():
                if result.success:
                    score = result.performance_metrics.get('overall_score', 0.0)
                    technique_aggregate_scores[technique_name].append(score)
        
        # Calculate aggregate statistics
        for technique_name, scores in technique_aggregate_scores.items():
            if scores:
                study_results['technique_performance_summary'][technique_name] = {
                    'mean_score': np.mean(scores),
                    'std_score': np.std(scores),
                    'min_score': np.min(scores),
                    'max_score': np.max(scores),
                    'test_cases_completed': len(scores),
                    'consistency_score': 1.0 - (np.std(scores) / max(np.mean(scores), 0.001))
                }
        
        # Overall rankings
        study_results['overall_rankings'] = sorted(
            study_results['technique_performance_summary'].items(),
            key=lambda x: x[1]['mean_score'],
            reverse=True
        )
        
        # Cross-case analysis
        study_results['cross_case_analysis'] = self._perform_cross_case_analysis(
            study_results['test_case_results']
        )
        
        study_results['study_metadata']['end_time'] = datetime.now()
        study_results['study_metadata']['duration'] = (
            study_results['study_metadata']['end_time'] - 
            study_results['study_metadata']['start_time']
        ).total_seconds()
        
        logger.info(f"Comparative study completed in {study_results['study_metadata']['duration']:.2f} seconds")
        
        return study_results
    
    def _perform_cross_case_analysis(self, test_case_results: Dict) -> Dict[str, Any]:
        """Perform cross-case analysis to identify patterns."""
        analysis = {
            'technique_strengths': {},
            'domain_preferences': {},
            'complexity_performance': {},
            'consistency_rankings': []
        }
        
        # Analyze technique strengths across different domains
        domain_performance = {}
        complexity_performance = {}
        
        for case_name, case_data in test_case_results.items():
            test_case = self.test_cases[case_name]
            domain = test_case['domain']
            complexity = test_case['complexity']
            
            for technique_name, result in case_data['results'].items():
                if result.success:
                    score = result.performance_metrics.get('overall_score', 0.0)
                    
                    # Domain analysis
                    if domain not in domain_performance:
                        domain_performance[domain] = {}
                    if technique_name not in domain_performance[domain]:
                        domain_performance[domain][technique_name] = []
                    domain_performance[domain][technique_name].append(score)
                    
                    # Complexity analysis
                    if complexity not in complexity_performance:
                        complexity_performance[complexity] = {}
                    if technique_name not in complexity_performance[complexity]:
                        complexity_performance[complexity][technique_name] = []
                    complexity_performance[complexity][technique_name].append(score)
        
        # Summarize domain preferences
        for domain, techniques in domain_performance.items():
            domain_scores = {}
            for technique, scores in techniques.items():
                domain_scores[technique] = np.mean(scores)
            
            best_technique = max(domain_scores.keys(), key=lambda k: domain_scores[k])
            analysis['domain_preferences'][domain] = {
                'best_technique': best_technique,
                'best_score': domain_scores[best_technique],
                'all_scores': domain_scores
            }
        
        # Summarize complexity performance
        for complexity, techniques in complexity_performance.items():
            complexity_scores = {}
            for technique, scores in techniques.items():
                complexity_scores[technique] = np.mean(scores)
            
            analysis['complexity_performance'][complexity] = complexity_scores
        
        return analysis

# Main execution and demo functions
def demo_individual_techniques():
    """Demonstrate individual prompting techniques."""
    lab = PromptEngineeringLab()
    
    print("=== PROMPT ENGINEERING TECHNIQUES DEMONSTRATION ===\n")
    
    # Demo query
    demo_query = "How can artificial intelligence be used to improve education while addressing ethical concerns?"
    
    techniques_to_demo = [
        PromptingTechnique.CHAIN_OF_THOUGHT,
        PromptingTechnique.TREE_OF_THOUGHT,
        PromptingTechnique.REACT
    ]
    
    for technique in techniques_to_demo:
        print(f"\n{'='*60}")
        print(f"TECHNIQUE: {technique.value.upper()}")
        print(f"{'='*60}")
        
        framework = lab.frameworks[technique]
        
        # Generate prompt
        prompt = framework.generate_prompt(
            demo_query, 
            {'domain': 'analytical', 'complexity': 'high'}
        )
        
        print("GENERATED PROMPT:")
        print("-" * 40)
        print(prompt)
        print("\n" + "="*60)

def demo_systematic_experiment():
    """Demonstrate systematic experimental methodology."""
    lab = PromptEngineeringLab()
    
    print("=== SYSTEMATIC EXPERIMENT DEMONSTRATION ===\n")
    
    # Run experiment on mathematical reasoning
    print("Running experiment: Mathematical Reasoning")
    print("-" * 50)
    
    results = lab.run_systematic_experiment(
        test_case_name='mathematical_reasoning',
        techniques=[
            PromptingTechnique.CHAIN_OF_THOUGHT,
            PromptingTechnique.TREE_OF_THOUGHT,
            PromptingTechnique.SELF_CONSISTENCY
        ]
    )
    
    # Analyze results
    analysis = lab.analyze_experiment_results(results)
    
    # Generate report
    report = lab.generate_experiment_report(
        'mathematical_reasoning', 
        results, 
        analysis
    )
    
    print(report)

def demo_comparative_study():
    """Demonstrate comprehensive comparative study."""
    lab = PromptEngineeringLab()
    
    print("=== COMPREHENSIVE COMPARATIVE STUDY ===\n")
    
    # Run comparative study
    study_results = lab.run_comparative_study(
        techniques=[
            PromptingTechnique.CHAIN_OF_THOUGHT,
            PromptingTechnique.TREE_OF_THOUGHT,
            PromptingTechnique.REACT,
            PromptingTechnique.SELF_CONSISTENCY
        ]
    )
    
    # Display summary results
    print("OVERALL TECHNIQUE RANKINGS:")
    print("-" * 40)
    for i, (technique, stats) in enumerate(study_results['overall_rankings'], 1):
        mean_score = stats['mean_score']
        consistency = stats['consistency_score']
        print(f"{i}. {technique}")
        print(f"   Mean Score: {mean_score:.3f}")
        print(f"   Consistency: {consistency:.3f}")
        print(f"   Test Cases: {stats['test_cases_completed']}")
        print()
    
    # Domain-specific insights
    print("DOMAIN-SPECIFIC PERFORMANCE:")
    print("-" * 40)
    cross_analysis = study_results['cross_case_analysis']
    
    for domain, data in cross_analysis['domain_preferences'].items():
        best_technique = data['best_technique']
        best_score = data['best_score']
        print(f"{domain.title()}: {best_technique} ({best_score:.3f})")
    
    print()
    
    # Complexity analysis
    print("COMPLEXITY-BASED PERFORMANCE:")
    print("-" * 40)
    for complexity, scores in cross_analysis['complexity_performance'].items():
        best_technique = max(scores.keys(), key=lambda k: scores[k])
        best_score = scores[best_technique]
        print(f"{complexity.title()} complexity: {best_technique} ({best_score:.3f})")

class PromptOptimizer:
    """
    Advanced prompt optimization utilities for research and development.
    
    Provides methods for systematic prompt improvement through iterative
    refinement and performance-based optimization.
    """
    
    def __init__(self, lab: PromptEngineeringLab):
        self.lab = lab
        self.optimization_history = []
        
    def optimize_prompt_iteratively(self, 
                                  base_prompt: str,
                                  test_query: str,
                                  optimization_rounds: int = 3,
                                  improvement_threshold: float = 0.05) -> Dict[str, Any]:
        """
        Iteratively optimize a prompt through systematic refinement.
        
        Args:
            base_prompt: Starting prompt template
            test_query: Query to test optimization against
            optimization_rounds: Number of optimization iterations
            improvement_threshold: Minimum improvement required to continue
            
        Returns:
            Optimization results with best prompt and performance history
        """
        optimization_log = {
            'base_prompt': base_prompt,
            'test_query': test_query,
            'rounds': [],
            'best_prompt': base_prompt,
            'best_score': 0.0,
            'total_improvement': 0.0
        }
        
        current_prompt = base_prompt
        current_score = self._evaluate_prompt_performance(current_prompt, test_query)
        optimization_log['best_score'] = current_score
        
        logger.info(f"Starting prompt optimization - Initial score: {current_score:.3f}")
        
        for round_num in range(optimization_rounds):
            round_data = {
                'round': round_num + 1,
                'input_prompt': current_prompt,
                'input_score': current_score,
                'optimizations_tried': [],
                'best_optimization': None,
                'output_prompt': current_prompt,
                'output_score': current_score,
                'improvement': 0.0
            }
            
            # Generate optimization candidates
            optimization_candidates = self._generate_optimization_candidates(
                current_prompt, test_query
            )
            
            best_candidate = None
            best_candidate_score = current_score
            
            # Test each optimization candidate
            for candidate_name, candidate_prompt in optimization_candidates.items():
                candidate_score = self._evaluate_prompt_performance(
                    candidate_prompt, test_query
                )
                
                round_data['optimizations_tried'].append({
                    'name': candidate_name,
                    'prompt': candidate_prompt,
                    'score': candidate_score,
                    'improvement': candidate_score - current_score
                })
                
                if candidate_score > best_candidate_score:
                    best_candidate = candidate_name
                    best_candidate_score = candidate_score
            
            # Apply best optimization if improvement exceeds threshold
            improvement = best_candidate_score - current_score
            if improvement > improvement_threshold:
                # Find the best candidate details
                best_candidate_data = next(
                    opt for opt in round_data['optimizations_tried'] 
                    if opt['name'] == best_candidate
                )
                
                current_prompt = best_candidate_data['prompt']
                current_score = best_candidate_score
                
                round_data['best_optimization'] = best_candidate
                round_data['output_prompt'] = current_prompt
                round_data['output_score'] = current_score
                round_data['improvement'] = improvement
                
                # Update global best
                if current_score > optimization_log['best_score']:
                    optimization_log['best_prompt'] = current_prompt
                    optimization_log['best_score'] = current_score
                
                logger.info(f"Round {round_num + 1}: Improvement of {improvement:.3f} with {best_candidate}")
            else:
                logger.info(f"Round {round_num + 1}: No significant improvement found")
                round_data['improvement'] = 0.0
            
            optimization_log['rounds'].append(round_data)
            
            # Early stopping if no improvement
            if improvement <= improvement_threshold:
                logger.info("Optimization converged - stopping early")
                break
        
        optimization_log['total_improvement'] = (
            optimization_log['best_score'] - 
            optimization_log['rounds'][0]['input_score']
        )
        
        self.optimization_history.append(optimization_log)
        
        return optimization_log
    
    def _evaluate_prompt_performance(self, prompt: str, test_query: str) -> float:
        """Evaluate prompt performance using simulated metrics."""
        # In real implementation, this would involve actual LLM testing
        # For simulation, we use heuristic scoring based on prompt characteristics
        
        score = 0.5  # Base score
        
        # Reward clear structure
        if any(indicator in prompt.lower() for indicator in ['step', 'analysis', 'evaluation']):
            score += 0.1
        
        # Reward specific instructions
        if any(indicator in prompt.lower() for indicator in ['specifically', 'clearly', 'systematically']):
            score += 0.1
        
        # Reward domain context
        if 'domain' in prompt.lower() or 'context' in prompt.lower():
            score += 0.05
        
        # Reward output format specification
        if any(indicator in prompt.lower() for indicator in ['format', 'structure', 'organize']):
            score += 0.05
        
        # Penalize excessive length (over 1000 characters)
        if len(prompt) > 1000:
            score -= min(0.2, (len(prompt) - 1000) / 2000)
        
        # Add some randomness to simulate real-world variation
        import random
        score += random.uniform(-0.05, 0.05)
        
        return max(0.0, min(1.0, score))
    
    def _generate_optimization_candidates(self, 
                                        current_prompt: str, 
                                        test_query: str) -> Dict[str, str]:
        """Generate candidate optimizations for the current prompt."""
        candidates = {}
        
        # Structure enhancement
        if 'step' not in current_prompt.lower():
            candidates['add_step_structure'] = self._add_step_structure(current_prompt)
        
        # Clarity improvement
        candidates['enhance_clarity'] = self._enhance_clarity(current_prompt)
        
        # Context enrichment
        candidates['add_context'] = self._add_contextual_guidance(current_prompt, test_query)
        
        # Output specification
        if 'format' not in current_prompt.lower():
            candidates['specify_output_format'] = self._specify_output_format(current_prompt)
        
        # Verification addition
        if 'verify' not in current_prompt.lower() and 'check' not in current_prompt.lower():
            candidates['add_verification'] = self._add_verification_step(current_prompt)
        
        return candidates
    
    def _add_step_structure(self, prompt: str) -> str:
        """Add step-by-step structure to prompt."""
        return prompt + "\n\nPlease approach this systematically:\n1. Analyze the problem\n2. Develop your solution\n3. Verify your answer"
    
    def _enhance_clarity(self, prompt: str) -> str:
        """Enhance prompt clarity with specific instructions."""
        clarity_addition = "\n\nPlease be specific and clear in your response, providing detailed explanations for your reasoning."
        return prompt + clarity_addition
    
    def _add_contextual_guidance(self, prompt: str, test_query: str) -> str:
        """Add contextual guidance based on query analysis."""
        context_addition = "\n\nConsider the broader context and implications of this problem when formulating your response."
        return prompt + context_addition
    
    def _specify_output_format(self, prompt: str) -> str:
        """Add output format specifications."""
        format_addition = "\n\nStructure your response with clear headings and organize your thoughts logically."
        return prompt + format_addition
    
    def _add_verification_step(self, prompt: str) -> str:
        """Add verification and validation step."""
        verification_addition = "\n\nAfter providing your answer, please verify its correctness and reasonableness."
        return prompt + verification_addition

class ExperimentTracker:
    """
    Comprehensive experiment tracking and analysis system.
    
    Provides utilities for longitudinal studies and meta-analysis
    of prompt engineering experiments.
    """
    
    def __init__(self):
        self.experiments_database = []
        self.meta_analysis_cache = {}
        
    def track_experiment(self, experiment_data: Dict[str, Any]):
        """Track a completed experiment in the database."""
        experiment_record = {
            'timestamp': datetime.now(),
            'experiment_id': len(self.experiments_database),
            'data': experiment_data
        }
        
        self.experiments_database.append(experiment_record)
        logger.info(f"Tracked experiment {experiment_record['experiment_id']}")
    
    def analyze_longitudinal_trends(self, 
                                  time_window_days: int = 30) -> Dict[str, Any]:
        """Analyze trends in experiment performance over time."""
        cutoff_date = datetime.now() - timedelta(days=time_window_days)
        
        recent_experiments = [
            exp for exp in self.experiments_database
            if exp['timestamp'] > cutoff_date
        ]
        
        if not recent_experiments:
            return {'error': 'No recent experiments found'}
        
        # Analyze technique performance trends
        technique_trends = {}
        
        for exp in recent_experiments:
            if 'technique_performance_summary' in exp['data']:
                for technique, stats in exp['data']['technique_performance_summary'].items():
                    if technique not in technique_trends:
                        technique_trends[technique] = []
                    
                    technique_trends[technique].append({
                        'timestamp': exp['timestamp'],
                        'mean_score': stats['mean_score'],
                        'consistency': stats['consistency_score']
                    })
        
        # Calculate trend statistics
        trend_analysis = {}
        for technique, data_points in technique_trends.items():
            if len(data_points) >= 2:
                scores = [dp['mean_score'] for dp in data_points]
                timestamps = [dp['timestamp'] for dp in data_points]
                
                # Simple linear trend calculation
                score_trend = (scores[-1] - scores[0]) / max(1, len(scores) - 1)
                
                trend_analysis[technique] = {
                    'data_points': len(data_points),
                    'score_trend': score_trend,
                    'latest_score': scores[-1],
                    'score_volatility': np.std(scores) if len(scores) > 1 else 0.0,
                    'improvement': 'improving' if score_trend > 0.01 else 'stable' if abs(score_trend) <= 0.01 else 'declining'
                }
        
        return {
            'analysis_period_days': time_window_days,
            'experiments_analyzed': len(recent_experiments),
            'technique_trends': trend_analysis,
            'summary': self._generate_trend_summary(trend_analysis)
        }
    
    def _generate_trend_summary(self, trend_analysis: Dict) -> Dict[str, Any]:
        """Generate summary insights from trend analysis."""
        if not trend_analysis:
            return {'insight': 'Insufficient data for trend analysis'}
        
        improving_techniques = [
            tech for tech, data in trend_analysis.items()
            if data['improvement'] == 'improving'
        ]
        
        declining_techniques = [
            tech for tech, data in trend_analysis.items()
            if data['improvement'] == 'declining'
        ]
        
        most_volatile = max(
            trend_analysis.keys(),
            key=lambda k: trend_analysis[k]['score_volatility']
        ) if trend_analysis else None
        
        return {
            'improving_techniques': improving_techniques,
            'declining_techniques': declining_techniques,
            'most_volatile_technique': most_volatile,
            'total_techniques_tracked': len(trend_analysis),
            'overall_trend': 'positive' if len(improving_techniques) > len(declining_techniques) else 'negative' if len(declining_techniques) > len(improving_techniques) else 'mixed'
        }
    
    def export_experiment_data(self, format_type: str = 'json') -> str:
        """Export experiment data for external analysis."""
        if format_type == 'json':
            # Convert datetime objects to strings for JSON serialization
            exportable_data = []
            for exp in self.experiments_database:
                exp_copy = exp.copy()
                exp_copy['timestamp'] = exp_copy['timestamp'].isoformat()
                exportable_data.append(exp_copy)
            
            return json.dumps(exportable_data, indent=2)
        
        elif format_type == 'csv':
            # Flatten data for CSV export
            csv_rows = []
            for exp in self.experiments_database:
                base_row = {
                    'experiment_id': exp['experiment_id'],
                    'timestamp': exp['timestamp'].isoformat()
                }
                
                # Add technique performance data if available
                if 'technique_performance_summary' in exp['data']:
                    for technique, stats in exp['data']['technique_performance_summary'].items():
                        row = base_row.copy()
                        row['technique'] = technique
                        row['mean_score'] = stats.get('mean_score', 0)
                        row['consistency_score'] = stats.get('consistency_score', 0)
                        row['test_cases_completed'] = stats.get('test_cases_completed', 0)
                        csv_rows.append(row)
                
            # Convert to CSV string
            if csv_rows:
                import csv
                import io
                
                output = io.StringIO()
                writer = csv.DictWriter(output, fieldnames=csv_rows[0].keys())
                writer.writeheader()
                writer.writerows(csv_rows)
                return output.getvalue()
        
        return "Unsupported format"

# Utility functions for easy lab usage
def quick_technique_comparison(query: str, 
                             techniques: Optional[List[PromptingTechnique]] = None) -> None:
    """Quick comparison of techniques for a given query."""
    lab = PromptEngineeringLab()
    
    if techniques is None:
        techniques = [
            PromptingTechnique.CHAIN_OF_THOUGHT,
            PromptingTechnique.TREE_OF_THOUGHT,
            PromptingTechnique.REACT
        ]
    
    print(f"QUICK TECHNIQUE COMPARISON")
    print(f"Query: {query}")
    print("=" * 80)
    
    for technique in techniques:
        framework = lab.frameworks[technique]
        prompt = framework.generate_prompt(query)
        
        print(f"\n{technique.value.upper()}:")
        print("-" * 40)
        print(prompt[:300] + "..." if len(prompt) > 300 else prompt)

def benchmark_technique_performance() -> None:
    """Run standardized benchmark across all techniques."""
    lab = PromptEngineeringLab()
    
    print("RUNNING STANDARDIZED BENCHMARK...")
    print("=" * 50)
    
    study_results = lab.run_comparative_study()
    
    print("\nBENCHMARK RESULTS:")
    print("-" * 30)
    
    for i, (technique, stats) in enumerate(study_results['overall_rankings'], 1):
        print(f"{i}. {technique}")
        print(f"   Score: {stats['mean_score']:.3f} ± {stats['std_score']:.3f}")
        print(f"   Consistency: {stats['consistency_score']:.3f}")

# Main execution block
if __name__ == "__main__":
    print("Context Engineering Course - Prompt Engineering Laboratory")
    print("=" * 60)
    print()
    
    # Initialize lab
    lab = PromptEngineeringLab()
    optimizer = PromptOptimizer(lab)
    tracker = ExperimentTracker()
    
    print("Available demonstrations:")
    print("1. Individual Techniques Demo")
    print("2. Systematic Experiment Demo") 
    print("3. Comparative Study Demo")
    print("4. Quick Technique Comparison")
    print("5. Benchmark Performance Test")
    print()
    
    # Example usage
    try:
        # Demo individual techniques
        print("Running Individual Techniques Demo...")
        demo_individual_techniques()
        print("\n" + "="*80 + "\n")
        
        # Demo systematic experiment
        print("Running Systematic Experiment Demo...")
        demo_systematic_experiment()
        print("\n" + "="*80 + "\n")
        
        # Quick comparison example
        print("Running Quick Comparison Demo...")
        quick_technique_comparison(
            "Explain the potential impacts of artificial intelligence on future employment.",
            [PromptingTechnique.CHAIN_OF_THOUGHT, PromptingTechnique.TREE_OF_THOUGHT]
        )
        
    except Exception as e:
        logger.error(f"Demo execution failed: {e}")
        print(f"Error during demonstration: {e}")
    
    print("\nLaboratory session complete. Use the provided classes and functions")
    print("to conduct your own prompt engineering research and experiments.")
    print("\nFor research-grade usage:")
    print("- Use PromptEngineeringLab for systematic experiments")
    print("- Use PromptOptimizer for iterative prompt improvement")
    print("- Use ExperimentTracker for longitudinal studies")
    print("- Extend BasePromptFramework for custom techniques")

# Research and academic utilities
class ResearchUtilities:
    """
    Utilities specifically designed for academic research and publication.
    
    Provides statistical analysis, significance testing, and research
    methodology compliance for prompt engineering studies.
    """
    
    @staticmethod
    def calculate_statistical_significance(scores_a: List[float], 
                                         scores_b: List[float],
                                         alpha: float = 0.05) -> Dict[str, Any]:
        """Calculate statistical significance between two technique performance sets."""
        from scipy import stats
        
        if len(scores_a) < 2 or len(scores_b) < 2:
            return {'error': 'Insufficient data for statistical testing'}
        
        # Perform t-test
        t_stat, p_value = stats.ttest_ind(scores_a, scores_b)
        
        # Effect size (Cohen's d)
        pooled_std = np.sqrt(((len(scores_a) - 1) * np.var(scores_a, ddof=1) + 
                             (len(scores_b) - 1) * np.var(scores_b, ddof=1)) / 
                            (len(scores_a) + len(scores_b) - 2))
        
        cohens_d = (np.mean(scores_a) - np.mean(scores_b)) / pooled_std
        
        return {
            't_statistic': t_stat,
            'p_value': p_value,
            'significant': p_value < alpha,
            'alpha': alpha,
            'cohens_d': cohens_d,
            'effect_size': 'small' if abs(cohens_d) < 0.2 else 'medium' if abs(cohens_d) < 0.8 else 'large',
            'interpretation': 'statistically significant' if p_value < alpha else 'not statistically significant'
        }
    
    @staticmethod
    def generate_research_report(study_results: Dict[str, Any],
                               research_questions: List[str]) -> str:
        """Generate academic-style research report."""
        report_sections = []
        
        # Abstract
        report_sections.append("ABSTRACT")
        report_sections.append("=" * 40)
        report_sections.append(
            f"This study investigates the comparative effectiveness of {len(study_results['overall_rankings'])} "
            f"prompt engineering techniques across {study_results['study_metadata']['test_cases_count']} "
            f"standardized test cases. Results indicate..."
        )
        report_sections.append("")
        
        # Research Questions
        report_sections.append("RESEARCH QUESTIONS")
        report_sections.append("=" * 40)
        for i, rq in enumerate(research_questions, 1):
            report_sections.append(f"RQ{i}: {rq}")
        report_sections.append("")
        
        # Methodology
        report_sections.append("METHODOLOGY")
        report_sections.append("=" * 40)
        report_sections.append(f"Techniques tested: {len(study_results['overall_rankings'])}")
        report_sections.append(f"Test cases: {study_results['study_metadata']['test_cases_count']}")
        report_sections.append(f"Study duration: {study_results['study_metadata']['duration']:.2f} seconds")
        report_sections.append("")
        
        # Results
        report_sections.append("RESULTS")
        report_sections.append("=" * 40)
        for i, (technique, stats) in enumerate(study_results['overall_rankings'], 1):
            report_sections.append(
                f"{i}. {technique}: M={stats['mean_score']:.3f}, "
                f"SD={stats['std_score']:.3f}, N={stats['test_cases_completed']}"
            )
        report_sections.append("")
        
        # Discussion and limitations would be added here
        report_sections.append("LIMITATIONS")
        report_sections.append("=" * 40)
        report_sections.append("- Simulated responses limit ecological validity")
        report_sections.append("- Limited test case diversity") 
        report_sections.append("- Absence of human evaluation")
        
        return "\n".join(report_sections)

# Export all main classes and functions for easy importing
__all__ = [
    'PromptingTechnique',
    'PromptExperiment', 
    'ExperimentResult',
    'BasePromptFramework',
    'ChainOfThoughtFramework',
    'TreeOfThoughtFramework', 
    'ReActFramework',
    'SelfConsistencyFramework',
    'RoleBasedPromptingFramework',
    'MetaCognitivePromptingFramework',
    'PromptEngineeringLab',
    'PromptOptimizer',
    'ExperimentTracker',
    'ResearchUtilities',
    'demo_individual_techniques',
    'demo_systematic_experiment',
    'demo_comparative_study',
    'quick_technique_comparison',
    'benchmark_technique_performance'
]
