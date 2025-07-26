# Cells: Adding Memory and State  
单元：添加记忆和状态

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#cells-adding-memory-and-state)

> "We are our memory, we are that chimerical museum of shifting shapes, that pile of broken mirrors." — Jorge Luis Borges  
> “我们就是我们的记忆，我们就是那个不断变换形状的空想博物馆，就是那堆破碎的镜子。”——豪尔赫·路易斯·博尔赫斯

## From Molecules to Cells  从分子到细胞

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#from-molecules-to-cells)

We've explored **atoms** (single instructions) and **molecules** (instructions with examples). Now we ascend to **cells** — context structures with **memory** that persist across multiple interactions.  
我们已经探索了**原子** （单个指令）和**分子** （包含示例的指令）。现在我们进一步探讨**细胞** ——一种具有**记忆**的上下文结构，能够在多次交互中持续存在。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  CELL = [INSTRUCTIONS] + [EXAMPLES] + [MEMORY/STATE] + [CURRENT INPUT]      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Like a biological cell that maintains its internal state while interacting with its environment, our context "cells" preserve information across multiple exchanges with the LLM.  
就像生物细胞在与环境相互作用的同时保持其内部状态一样，我们的上下文“细胞”在与 LLM 的多次交换中保存信息。

## The Memory Problem  记忆问题

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#the-memory-problem)

By default, LLMs have no memory. Each request is processed independently:  
默认情况下，LLM 没有记忆。每个请求都会被独立处理：

```
┌───────────────────────┐      ┌───────────────────────┐
│ Request 1             │      │ Request 2             │
├───────────────────────┤      ├───────────────────────┤
│ "My name is Alex."    │      │ "What's my name?"     │
│                       │      │                       │
│                       │      │                       │
└───────────────────────┘      └───────────────────────┘
          │                              │
          ▼                              ▼
┌───────────────────────┐      ┌───────────────────────┐
│ Response 1            │      │ Response 2            │
├───────────────────────┤      ├───────────────────────┤
│ "Hello Alex, nice     │      │ "I don't have access  │
│  to meet you."        │      │  to previous          │
│                       │      │  conversations..."    │
└───────────────────────┘      └───────────────────────┘
```

Without memory, the LLM forgets information from previous interactions, creating a disjointed, frustrating user experience.  
如果没有记忆，LLM 就会忘记以前交互中的信息，从而造成脱节、令人沮丧的用户体验。

## The Cell Solution: Conversation Memory  
单元解决方案：对话记忆

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#the-cell-solution-conversation-memory)

The simplest cell structure adds conversation history to the context:  
最简单的单元结构将对话历史记录添加到上下文中：

```
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  SYSTEM PROMPT: "You are a helpful assistant..."                      │
│                                                                       │
│  CONVERSATION HISTORY:                                                │
│  User: "My name is Alex."                                             │
│  Assistant: "Hello Alex, nice to meet you."                           │
│                                                                       │
│  CURRENT INPUT: "What's my name?"                                     │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

Now the LLM can access previous exchanges and maintain continuity.  
现在，法学硕士可以访问以前的交流并保持连续性。

## The Memory Token Budget Problem  
记忆代币预算问题

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#the-memory-token-budget-problem)

As conversations grow, context windows fill up. We need memory management strategies:  
随着对话的增长，上下文窗口会被填满。我们需要记忆管理策略：

```
          [Context Window Tokens]
          ┌─────────────────────────────────────────────┐
          │                                             │
Turn 1    │ System Instructions       User Input 1      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 2    │ System    History 1       User Input 2      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 3    │ Sys  History 1  History 2  User Input 3     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 4    │ S  History 1-3             User Input 4     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 5    │ History 2-4                User Input 5     │
          │                                             │
          └─────────────────────────────────────────────┘
                                       ▲
                                       │
                        Eventually, something has to go
```

## Memory Management Strategies  
记忆管理策略

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#memory-management-strategies)

Several strategies help optimize the use of limited context windows:  
有几种策略有助于优化有限上下文窗口的使用：

```
┌───────────────────────────────────────────────────────────────────┐
│ MEMORY MANAGEMENT STRATEGIES                                      │
├────────────────────┬──────────────────────────────────────────────┤
│ Windowing          │ Keep only the most recent N turns            │
├────────────────────┼──────────────────────────────────────────────┤
│ Summarization      │ Compress older turns into summaries          │
├────────────────────┼──────────────────────────────────────────────┤
│ Key-Value Storage  │ Extract and store important facts separately │
├────────────────────┼──────────────────────────────────────────────┤
│ Priority Pruning   │ Remove less important turns first            │
├────────────────────┼──────────────────────────────────────────────┤
│ Semantic Chunking  │ Group related exchanges together             │
└────────────────────┴──────────────────────────────────────────────┘
```

## Windowing: The Sliding Context  
窗口：滑动上下文

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#windowing-the-sliding-context)

The simplest memory management approach keeps only the most recent conversation turns:  
最简单的记忆管理方法仅保留最近的对话轮次：

```
                    ┌───────────────────────────┐
Turn 1              │ System + Turn 1           │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 2              │ System + Turn 1-2         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 3              │ System + Turn 1-3         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 4              │ System + Turn 2-4         │ ← Turn 1 dropped
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 5              │ System + Turn 3-5         │ ← Turn 2 dropped
                    └───────────────────────────┘
```

This approach is simple but forgets information from earlier turns.  
这种方法很简单，但会忘记之前的信息。

## Summarization: Compressing Memory  
总结：压缩记忆

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#summarization-compressing-memory)

A more sophisticated approach compresses older turns into summaries:  
一种更复杂的方法是将旧的转变压缩成摘要：

```
                    ┌────────────────────────────────────────────┐
Turn 1-3            │ System + Turn 1-3                          │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 4              │ System + Summary(Turn 1-2) + Turn 3-4      │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 5              │ System + Summary(Turn 1-3) + Turn 4-5      │
                    └────────────────────────────────────────────┘
```

Summarization preserves key information while reducing token count.  
摘要保留了关键信息，同时减少了标记数。

## Key-Value Memory: Structured State  
键值记忆：结构化状态

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#key-value-memory-structured-state)

For more control, we can extract and store important facts in a structured format:  
为了更好地控制，我们可以以结构化格式提取和存储重要事实：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT WINDOW                                                      │
│                                                                     │
│  SYSTEM PROMPT: "You are a helpful assistant..."                    │
│                                                                     │
│  MEMORY:                                                            │
│  {                                                                  │
│    "user_name": "Alex",                                             │
│    "favorite_color": "blue",                                        │
│    "location": "Toronto",                                           │
│    "last_topic": "vacation plans"                                   │
│  }                                                                  │
│                                                                     │
│  RECENT CONVERSATION:                                               │
│  User: "What activities would you recommend?"                       │
│  Assistant: "Given your location in Toronto and interest in..."     │
│                                                                     │
│  CURRENT INPUT: "How about something indoors? It's cold."           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

This structured approach allows precise control over what information is retained.  
这种结构化方法可以精确控制保留的信息。

## Beyond Conversation: Stateful Applications  
超越对话：有状态的应用程序

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#beyond-conversation-stateful-applications)

Cells enable far more than just coherent conversations. They allow stateful applications where the LLM:  
单元格的功能远不止于实现连贯的对话。它们允许有状态的应用程序，其中 LLM：

1. Remembers previous interactions  
    记住之前的互动
2. Updates and maintains variables  
    更新并维护变量
3. Tracks progress through multi-step processes  
    通过多步骤流程跟踪进度
4. Builds on previous outputs  
    建立在先前成果的基础上

Let's explore a simple calculator example:  
让我们探索一个简单的计算器示例：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STATEFUL CALCULATOR                                                 │
│                                                                     │
│ SYSTEM: "You are a calculator assistant that maintains a running    │
│          total. Follow the user's math operations step by step."    │
│                                                                     │
│ STATE: { "current_value": 0 }                                       │
│                                                                     │
│ User: "Start with 5"                                                │
│ Assistant: "Starting with 5. Current value is 5."                   │
│ STATE: { "current_value": 5 }                                       │
│                                                                     │
│ User: "Multiply by 3"                                               │
│ Assistant: "5 × 3 = 15. Current value is 15."                       │
│ STATE: { "current_value": 15 }                                      │
│                                                                     │
│ User: "Add 7"                                                       │
│ Assistant: "15 + 7 = 22. Current value is 22."                      │
│ STATE: { "current_value": 22 }                                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

The state variable persists across turns, enabling continuous calculations.  
状态变量在各个回合中持续存在，从而实现连续计算。

## Long-Term Memory: Beyond the Context Window  
长期记忆：超越上下文窗口

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#long-term-memory-beyond-the-context-window)

For truly persistent memory, we need external storage:  
对于真正的持久记忆，我们需要外部存储：

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   User Input                                                             │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐                                                         │
│  │ Extract     │                                                         │
│  │ Key Info    │                                                         │
│  └─────────────┘                                                         │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐      ┌────────────────────┐                            │
│  │ Update      │◄─────┤ External Memory    │                            │
│  │ Memory      │      │ (Vector DB,        │                            │
│  │             │─────►│  Document DB, etc) │                            │
│  └─────────────┘      └────────────────────┘                            │
│       │                        ▲                                         │
│       │                        │                                         │
│       ▼                        │                                         │
│  ┌─────────────┐      ┌────────────────────┐                            │
│  │ Construct   │      │ Retrieve Relevant  │                            │
│  │ Context     │◄─────┤ Memory             │                            │
│  │             │      │                    │                            │
│  └─────────────┘      └────────────────────┘                            │
│       │                                                                  │
│       ▼                                                                  │
│  ┌─────────────┐                                                         │
│  │             │                                                         │
│  │ LLM         │                                                         │
│  │             │                                                         │
│  └─────────────┘                                                         │
│       │                                                                  │
│       ▼                                                                  │
│   Response                                                               │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

This architecture enables potentially unlimited memory by:  
该架构通过以下方式实现了无限的记忆：

1. Extracting key information from conversations  
    从对话中提取关键信息
2. Storing it in external databases  
    将其存储在外部数据库中
3. Retrieving relevant context when needed  
    在需要时检索相关上下文
4. Incorporating that context into the prompt  
    将该上下文纳入提示中

## Cell Implementation: A Memory Manager  
单元实现：记忆管理器

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#cell-implementation-a-memory-manager)

Here's a Python class that implements basic memory management:  
下面是实现基本记忆管理的 Python 类：

```python
class ContextCell:
    """A context cell that maintains memory across interactions."""
    
    def __init__(self, system_prompt, max_turns=10, memory_strategy="window"):
        """
        Initialize the context cell.
        
        Args:
            system_prompt (str): The system instructions
            max_turns (int): Maximum conversation turns to keep
            memory_strategy (str): 'window', 'summarize', or 'key_value'
        """
        self.system_prompt = system_prompt
        self.max_turns = max_turns
        self.memory_strategy = memory_strategy
        self.conversation_history = []
        self.key_value_store = {}
        
    def add_exchange(self, user_input, assistant_response):
        """Add a conversation exchange to history."""
        self.conversation_history.append({
            "user": user_input,
            "assistant": assistant_response
        })
        
        # Apply memory management if needed
        if len(self.conversation_history) > self.max_turns:
            self._manage_memory()
    
    def extract_info(self, key, value):
        """Store important information in key-value store."""
        self.key_value_store[key] = value
    
    def _manage_memory(self):
        """Apply the selected memory management strategy."""
        if self.memory_strategy == "window":
            # Keep only the most recent turns
            self.conversation_history = self.conversation_history[-self.max_turns:]
        
        elif self.memory_strategy == "summarize":
            # Summarize older turns (would use an LLM in practice)
            to_summarize = self.conversation_history[:-self.max_turns + 1]
            summary = self._create_summary(to_summarize)
            
            # Replace old turns with summary
            self.conversation_history = [{"summary": summary}] + \
                                       self.conversation_history[-(self.max_turns-1):]
    
    def _create_summary(self, exchanges):
        """Create a summary of conversation exchanges."""
        # In practice, this would call an LLM to create the summary
        # For this example, we'll use a placeholder
        return f"Summary of {len(exchanges)} previous exchanges"
    
    def build_context(self, current_input):
        """Build the full context for the next LLM call."""
        context = f"{self.system_prompt}\n\n"
        
        # Add key-value memory if we have any
        if self.key_value_store:
            context += "MEMORY:\n"
            for key, value in self.key_value_store.items():
                context += f"{key}: {value}\n"
            context += "\n"
        
        # Add conversation history
        if self.conversation_history:
            context += "CONVERSATION HISTORY:\n"
            for exchange in self.conversation_history:
                if "summary" in exchange:
                    context += f"[Previous exchanges: {exchange['summary']}]\n\n"
                else:
                    context += f"User: {exchange['user']}\n"
                    context += f"Assistant: {exchange['assistant']}\n\n"
        
        # Add current input
        context += f"User: {current_input}\nAssistant:"
        
        return context
```

## Measuring Cell Efficiency  
测量电池效率

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#measuring-cell-efficiency)

As with molecules, measuring efficiency is crucial for cells:  
与分子一样，测量效率对于细胞来说至关重要：

```
┌──────────────────────────────────────────────────────────────────┐
│ MEMORY STRATEGY COMPARISON                                       │
├──────────────────┬──────────────┬─────────────┬─────────────────┤
│ Strategy         │ Token Usage  │ Information │ Implementation  │
│                  │              │ Retention   │ Complexity      │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ No Memory        │ Lowest       │ None        │ Trivial         │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Full History     │ Highest      │ Complete    │ Trivial         │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Windowing        │ Controlled   │ Recent Only │ Easy            │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Summarization    │ Moderate     │ Good        │ Moderate        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Key-Value Store  │ Low          │ Selective   │ Moderate        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ External Store   │ Very Low     │ Extensive   │ Complex         │
└──────────────────┴──────────────┴─────────────┴─────────────────┘
```

Different strategies optimize for different priorities. Choosing the right approach depends on your specific application needs.  
不同的策略针对不同的优先级进行优化。选择正确的方法取决于您的具体应用需求。

## Advanced Techniques: Memory Orchestration  
高级技术：记忆编排

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#advanced-techniques-memory-orchestration)

For sophisticated applications, multiple memory systems can work together:  
对于复杂的应用程序，多个记忆系统可以协同工作：

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MEMORY ORCHESTRATION                           │
│                                                                     │
│  ┌─────────────────┐    ┌─────────────────┐   ┌─────────────────┐   │
│  │                 │    │                 │   │                 │   │
│  │ Short-term      │    │ Working         │   │ Long-term       │   │
│  │ Memory          │    │ Memory          │   │ Memory          │   │
│  │                 │    │                 │   │                 │   │
│  │ • Recent turns  │    │ • Current task  │   │ • User profile  │   │
│  │ • Immediate     │    │ • Active        │   │ • Historical    │   │
│  │   context       │    │   variables     │   │   facts         │   │
│  │ • Last few      │    │ • Task progress │   │ • Learned       │   │
│  │   exchanges     │    │ • Mid-task      │   │   preferences   │   │
│  │                 │    │   state         │   │                 │   │
│  └─────────────────┘    └─────────────────┘   └─────────────────┘   │
│         ▲ ▼                   ▲ ▼                   ▲ ▼              │
│         │ │                   │ │                   │ │              │
│  ┌──────┘ └───────────────────┘ └───────────────────┘ └──────┐      │
│  │                                                           │      │
│  │                    Memory Manager                         │      │
│  │                                                           │      │
│  └───────────────────────────────┬───────────────────────────┘      │
│                                  │                                   │
│                                  ▼                                   │
│                        ┌─────────────────┐                           │
│                        │                 │                           │
│                        │   Context       │                           │
│                        │   Builder       │                           │
│                        │                 │                           │
│                        └─────────────────┘                           │
│                                  │                                   │
│                                  ▼                                   │
│                        ┌─────────────────┐                           │
│                        │                 │                           │
│                        │      LLM        │                           │
│                        │                 │                           │
│                        └─────────────────┘                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

This architecture mirrors human memory systems, with:  
该架构反映了人类的记忆系统，具有：

- **Short-term memory**: Recent conversation turns  
    **短期记忆** ：最近的对话
- **Working memory**: Active task state and variables  
    **工作记忆** ：活动任务状态和变量
- **Long-term memory**: Persistent user information and preferences  
    **长期记忆** ：持久的用户信息和偏好

The memory manager orchestrates these systems, deciding what information to include in each context.  
记忆管理器协调这些系统，决定在每个上下文中包含哪些信息。

## Memory and Hallucination Reduction  
记忆力和幻觉减少

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#memory-and-hallucination-reduction)

One of the most valuable benefits of memory cells is reducing hallucinations:  
记忆细胞最有价值的好处之一是减少幻觉：

```
┌─────────────────────────────────────────────────────────────────────┐
│ HALLUCINATION REDUCTION STRATEGIES                                  │
├─────────────────────────────────────────────────────────────────────┤
│ 1. Explicitly store facts extracted from previous exchanges         │
│ 2. Tag information with source/certainty levels                     │
│ 3. Include relevant facts in context when similar topics arise      │
│ 4. Detect and correct contradictions between memory and responses   │
│ 5. Periodically verify important facts through user confirmation    │
└─────────────────────────────────────────────────────────────────────┘
```

By grounding the LLM in consistent facts from memory, we improve reliability dramatically.  
通过将法学硕士建立在记忆中的一致事实之上，我们大大提高了可靠性。

## Beyond Text: Structured State  
超越文本：结构化状态

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#beyond-text-structured-state)

Advanced cells maintain structured state beyond just text history:  
高级单元格除了文本历史记录之外，还维护结构化状态：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STRUCTURED STATE EXAMPLES                                           │
├─────────────────────────┬───────────────────────────────────────────┤
│ Progression State       │ {"step": 3, "completed_steps": [1, 2],    │
│                         │  "next_action": "validate_input"}         │
├─────────────────────────┼───────────────────────────────────────────┤
│ User Profile            │ {"name": "Alex", "preferences": {         │
│                         │  "communication_style": "concise",        │
│                         │  "expertise_level": "beginner"}}          │
├─────────────────────────┼───────────────────────────────────────────┤
│ Application State       │ {"current_view": "dashboard",             │
│                         │  "filters": ["active", "high_priority"],  │
│                         │  "sort_by": "deadline"}                   │
├─────────────────────────┼───────────────────────────────────────────┤
│ Environmental Context   │ {"location": "Toronto",                   │
│                         │  "weather": "snowing",                    │
│                         │  "time": "evening"}                       │
└─────────────────────────┴───────────────────────────────────────────┘
```

This structured approach allows precise control over the context and enables more sophisticated applications.  
这种结构化方法可以精确控制上下文并支持更复杂的应用。

## Memory Feedback Loops  记忆反馈回路

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#memory-feedback-loops)

Sophisticated cells create feedback loops where the LLM helps manage its own memory:  
复杂的细胞会创建反馈回路，其中 LLM 会帮助管理自己的记忆：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  User: "I'm planning a trip to Japan next month."                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY EXTRACTION]                                    ││
│  │ Important facts to remember:                                    ││
│  │ - User is planning a trip to Japan                              ││
│  │ - Trip is scheduled for next month                              ││
│  │ Confidence: High                                                ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  Assistant: "That's exciting! Japan is beautiful. Are you           │
│  interested in cities like Tokyo and Kyoto, or more rural areas?"   │
│                                                                     │
│  User: "Definitely Tokyo, and maybe Osaka too."                     │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY UPDATE]                                        ││
│  │ Updated facts:                                                  ││
│  │ - User is planning a trip to Japan next month                   ││
│  │ - User is interested in Tokyo and Osaka                         ││
│  │ - User may not be interested in rural areas (confidence: medium)││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

The LLM itself extracts and updates important information to remember, creating a self-improving memory system.  
LLM 本身会提取并更新需要记住的重要信息，从而创建一个自我完善的记忆系统。

## Key Takeaways  关键要点

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#key-takeaways)

1. **Memory cells** add state persistence across multiple interactions  
    **记忆细胞**在多次交互中增加状态持久性
2. **Token budget management** is crucial as conversations grow  
    随着对话的增多， **代币预算管理**至关重要
3. **Memory strategies** include windowing, summarization, and key-value stores  
    **记忆策略**包括窗口化、汇总和键值存储
4. **External memory** enables unlimited, persistent storage beyond the context window  
    **外部存储器**可实现超出上下文窗口的无限持久存储
5. **Structured state** enables sophisticated applications beyond simple conversations  
    **结构化状态**使复杂的应用程序超越简单的对话
6. **Memory orchestration** combines multiple memory systems for optimal performance  
    **记忆编排**结合多个记忆系统以实现最佳性能
7. **Self-improving memory** uses the LLM to help manage its own memory  
    **自我提升记忆**利用 LLM 来帮助管理自己的记忆

## Exercises for Practice  练习

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#exercises-for-practice)

1. Implement a simple conversation memory system with windowing  
    用窗口实现简单的对话记忆系统
2. Compare different memory strategies on the same extended conversation  
    比较同一段扩展对话中的不同记忆策略
3. Build a key-value store that extracts important facts from conversations  
    构建一个键值存储，从对话中提取重要事实
4. Experiment with using an LLM to summarize older conversation turns  
    尝试使用 LLM 来总结旧的对话转折
5. Create a structured state manager for a specific application domain  
    为特定应用程序域创建结构化状态管理器

## Next Steps  后续步骤

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#next-steps)

In the next section, we'll explore **organs** — multi-agent systems where multiple context cells work together to solve complex problems.  
在下一节中，我们将探索**器官** ——多智能体系统，其中多个上下文单元协同工作以解决复杂问题。

[Continue to 04_organs_applications.md →  
继续 04_organs_applications.md →](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/04_organs_applications.md)

---

## Deeper Dive: Memory Abstractions  
深入探究：记忆抽象

[](https://github.com/KashiwaByte/Context-Engineering-Chinese-Bilingual/blob/main/Chinese-Bilingual/00_foundations/03_cells_memory.md#deeper-dive-memory-abstractions)

Memory can be organized in multiple layers of abstraction:  
记忆可以按多个抽象层进行组织：

```
┌────────────────────────────────────────────────────────────────────┐
│ MEMORY ABSTRACTION LAYERS                                          │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│   ┌─────────────────┐                                              │
│   │ Episodic Memory │  Specific conversation exchanges and events  │
│   └─────────────────┘                                              │
│           ▲                                                        │
│           │                                                        │
│   ┌─────────────────┐                                              │
│   │ Semantic Memory │  Facts, concepts, and structured knowledge   │
│   └─────────────────┘                                              │
│           ▲                                                        │
│           │                                                        │
│   ┌─────────────────┐                                              │
│   │ Conceptual      │  High-level patterns, preferences, goals     │
│   │ Memory          │                                              │
│   └─────────────────┘                                              │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

This layered approach allows the system to balance concrete details with high-level understanding of the interaction context.  
这种分层方法使系统能够平衡具体细节和对交互环境的高级理解。