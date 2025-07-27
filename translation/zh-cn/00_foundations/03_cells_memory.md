# Cells: Adding Memory and State （细胞：添加记忆和状态）

> "We are our memory, we are that chimerical museum of shifting shapes, that pile of broken mirrors." — Jorge Luis Borges

> “我们是我们的记忆，我们是那个由不断变化的形状组成的虚幻博物馆，那堆破碎的镜子。”——豪尔赫·路易斯·博尔赫斯

## From Molecules to Cells （从分子到细胞）

We've explored **atoms** (single instructions) and **molecules** (instructions with examples). Now we ascend to **cells** — context structures with **memory** that persist across multiple interactions.

我们已经探讨了**原子**（单一指令）和**分子**（带示例的指令）。现在我们提升到**细胞**——具有**记忆**的上下文结构，这种记忆在多次交互中持续存在。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  CELL = [INSTRUCTIONS] + [EXAMPLES] + [MEMORY/STATE] + [CURRENT INPUT]      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

Like a biological cell that maintains its internal state while interacting with its environment, our context "cells" preserve information across multiple exchanges with the LLM.

就像生物细胞在与环境互动时保持其内部状态一样，我们的上下文“细胞”在与大型语言模型（LLM）的多次交流中保留信息。

## The Memory Problem （记忆问题）

By default, LLMs have no memory. Each request is processed independently:

默认情况下，大型语言模型（LLM）没有记忆。每个请求都是独立处理的：

```
┌───────────────────────┐      ┌───────────────────────┐
│ Request 1             │      │ Request 2             │
│ （请求 1）              │      │ （请求 2）              │
├───────────────────────┤      ├───────────────────────┤
│ "My name is Alex."    │      │ "What's my name?"     │
│                       │      │                       │
│                       │      │                       │
└───────────────────────┘      └───────────────────────┘
          │                              │
          ▼                              ▼
┌───────────────────────┐      ┌───────────────────────┐
│ Response 1            │      │ Response 2            │
│ （响应 1）              │      │ （响应 2）              │
├───────────────────────┤      ├───────────────────────┤
│ "Hello Alex, nice     │      │ "I don't have access  │
│  to meet you."        │      │  to previous          │
│                       │      │  conversations..."    │
└───────────────────────┘      └───────────────────────┘
```

Without memory, the LLM forgets information from previous interactions, creating a disjointed, frustrating user experience.

没有记忆，大型语言模型（LLM）会忘记之前交互中的信息，从而造成脱节、令人沮丧的用户体验。

## The Cell Solution: Conversation Memory （细胞解决方案：对话记忆）

The simplest cell structure adds conversation history to the context:

最简单的细胞结构是将对话历史添加到上下文中：

```
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  SYSTEM PROMPT: "You are a helpful assistant..."                      │
│  （系统提示：“你是一个乐于助人的助手……”）                               │
│                                                                       │
│  CONVERSATION HISTORY:                                                │
│  （对话历史：）                                                         │
│  User: "My name is Alex."                                             │
│  （用户：“我叫Alex。”）                                                 │
│  Assistant: "Hello Alex, nice to meet you."                           │
│  （助手：“你好Alex，很高兴见到你。”）                                     │
│                                                                       │
│  CURRENT INPUT: "What's my name?"                                     │
│  （当前输入：“我叫什么名字？”）                                           │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

Now the LLM can access previous exchanges and maintain continuity.

现在，大型语言模型（LLM）可以访问以前的交流并保持连续性。

## The Memory Token Budget Problem （记忆令牌预算问题）

As conversations grow, context windows fill up. We need memory management strategies:

随着对话的增长，上下文窗口会填满。我们需要记忆管理策略：

```
          [Context Window Tokens] （上下文窗口令牌）
          ┌─────────────────────────────────────────────┐
          │                                             │
Turn 1    │ System Instructions       User Input 1      │
（回合 1）  │ （系统指令）                （用户输入 1）      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 2    │ System    History 1       User Input 2      │
（回合 2）  │ （系统）    （历史 1）        （用户输入 2）      │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 3    │ Sys  History 1  History 2  User Input 3     │
（回合 3）  │ （系统） （历史 1） （历史 2） （用户输入 3）     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 4    │ S  History 1-3             User Input 4     │
（回合 4）  │ （系统） （历史 1-3）           （用户输入 4）     │
          │                                             │
          ├─────────────────────────────────────────────┤
          │                                             │
Turn 5    │ History 2-4                User Input 5     │
（回合 5）  │ （历史 2-4）                 （用户输入 5）     │
          │                                             │
          └─────────────────────────────────────────────┘
                                       ▲
                                       │
                        Eventually, something has to go （最终，有些东西必须舍弃）
```

## Memory Management Strategies （记忆管理策略）

Several strategies help optimize the use of limited context windows:

有几种策略有助于优化有限上下文窗口的使用：

```
┌───────────────────────────────────────────────────────────────────┐
│ MEMORY MANAGEMENT STRATEGIES                                      │
│ （记忆管理策略）                                                    │
├────────────────────┬──────────────────────────────────────────────┤
│ Windowing          │ Keep only the most recent N turns            │
│ （窗口化）           │ （只保留最近的 N 个回合）                      │
├────────────────────┼──────────────────────────────────────────────┤
│ Summarization      │ Compress older turns into summaries          │
│ （摘要化）           │ （将旧的回合压缩成摘要）                       │
├────────────────────┼──────────────────────────────────────────────┤
│ Key-Value Storage  │ Extract and store important facts separately │
│ （键值存储）         │ （提取并单独存储重要事实）                     │
├────────────────────┼──────────────────────────────────────────────┤
│ Priority Pruning   │ Remove less important turns first            │
│ （优先级修剪）       │ （首先删除不那么重要的回合）                   │
├────────────────────┼──────────────────────────────────────────────┤
│ Semantic Chunking  │ Group related exchanges together             │
│ （语义分块）         │ （将相关的交流分组在一起）                     │
└────────────────────┴──────────────────────────────────────────────┘
```

## Windowing: The Sliding Context （窗口化：滑动上下文）

The simplest memory management approach keeps only the most recent conversation turns:

最简单的记忆管理方法只保留最近的对话回合：

```
                    ┌───────────────────────────┐
Turn 1              │ System + Turn 1           │
（回合 1）            │ （系统 + 回合 1）           │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 2              │ System + Turn 1-2         │
（回合 2）            │ （系统 + 回合 1-2）         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 3              │ System + Turn 1-3         │
（回合 3）            │ （系统 + 回合 1-3）         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 4              │ System + Turn 2-4         │ ← Turn 1 dropped （回合 1 被丢弃）
（回合 4）            │ （系统 + 回合 2-4）         │
                    └───────────────────────────┘
                              │
                              ▼
                    ┌───────────────────────────┐
Turn 5              │ System + Turn 3-5         │ ← Turn 2 dropped （回合 2 被丢弃）
（回合 5）            │ （系统 + 回合 3-5）         │
                    └───────────────────────────┘
```

This approach is simple but forgets information from earlier turns.

这种方法很简单，但会忘记早期回合的信息。

## Summarization: Compressing Memory （摘要化：压缩记忆）

A more sophisticated approach compresses older turns into summaries:

一种更复杂的方法是将旧的回合压缩成摘要：

```
                    ┌────────────────────────────────────────────┐
Turn 1-3            │ System + Turn 1-3                          │
（回合 1-3）          │ （系统 + 回合 1-3）                          │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 4              │ System + Summary(Turn 1-2) + Turn 3-4      │
（回合 4）            │ （系统 + 摘要(回合 1-2) + 回合 3-4）         │
                    └────────────────────────────────────────────┘
                                       │
                                       ▼
                    ┌────────────────────────────────────────────┐
Turn 5              │ System + Summary(Turn 1-3) + Turn 4-5      │
（回合 5）            │ （系统 + 摘要(回合 1-3) + 回合 4-5）         │
                    └────────────────────────────────────────────┘
```

Summarization preserves key information while reducing token count.

摘要化在减少令牌数量的同时保留了关键信息。

## Key-Value Memory: Structured State （键值记忆：结构化状态）

For more control, we can extract and store important facts in a structured format:

为了更好地控制，我们可以将重要事实提取并存储为结构化格式：

```
┌─────────────────────────────────────────────────────────────────────┐
│ CONTEXT WINDOW                                                      │
│ （上下文窗口）                                                        │
│                                                                     │
│  SYSTEM PROMPT: "You are a helpful assistant..."                    │
│  （系统提示：“你是一个乐于助人的助手……”）                            │
│                                                                     │
│  MEMORY:                                                            │
│  （记忆：）                                                           │
│  {                                                                  │
│    "user_name": "Alex",                                             │
│    "favorite_color": "blue",                                        │
│    "location": "Toronto",                                           │
│    "last_topic": "vacation plans"                                   │
│  }                                                                  │
│                                                                     │
│  RECENT CONVERSATION:                                               │
│  （最近对话：）                                                       │
│  User: "What activities would you recommend?"                       │
│  （用户：“你有什么活动推荐吗？”）                                       │
│  Assistant: "Given your location in Toronto and interest in..."     │
│  （助手：“考虑到你在多伦多的位置以及对……的兴趣……”）                     │
│                                                                     │
│  CURRENT INPUT: "How about something indoors? It's cold."           │
│  （当前输入：“室内活动怎么样？天气很冷。”）                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

This structured approach allows precise control over what information is retained.

这种结构化方法可以精确控制保留哪些信息。

## Beyond Conversation: Stateful Applications （超越对话：有状态应用程序）

Cells enable far more than just coherent conversations. They allow stateful applications where the LLM:

细胞不仅仅能实现连贯的对话。它们还允许有状态的应用程序，其中大型语言模型（LLM）：

1. Remembers previous interactions
2. Updates and maintains variables
3. Tracks progress through multi-step processes
4. Builds on previous outputs

1. 记住以前的交互
2. 更新和维护变量
3. 跟踪多步骤过程的进度
4. 基于以前的输出进行构建

Let's explore a simple calculator example:

让我们来看一个简单的计算器示例：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STATEFUL CALCULATOR                                                 │
│ （有状态计算器）                                                      │
│                                                                     │
│ SYSTEM: "You are a calculator assistant that maintains a running    │
│          total. Follow the user's math operations step by step."    │
│ （系统：“你是一个计算器助手，维护一个运行中的总数。请逐步遵循用户的数学运算。”）│
│                                                                     │
│ STATE: { "current_value": 0 }                                       │
│ （状态：{ "current_value": 0 }）                                      │
│                                                                     │
│ User: "Start with 5"                                                │
│ （用户：“从 5 开始”）                                                 │
│ Assistant: "Starting with 5. Current value is 5."                   │
│ （助手：“从 5 开始。当前值为 5。”）                                     │
│ STATE: { "current_value": 5 }                                       │
│ （状态：{ "current_value": 5 }）                                      │
│                                                                     │
│ User: "Multiply by 3"                                               │
│ （用户：“乘以 3”）                                                   │
│ Assistant: "5 × 3 = 15. Current value is 15."                       │
│ （助手：“5 × 3 = 15。当前值为 15。”）                                 │
│ STATE: { "current_value": 15 }                                      │
│ （状态：{ "current_value": 15 }）                                     │
│                                                                     │
│ User: "Add 7"                                                       │
│ （用户：“加 7”）                                                     │
│ Assistant: "15 + 7 = 22. Current value is 22."                      │
│ （助手：“15 + 7 = 22。当前值为 22。”）                                │
│ STATE: { "current_value": 22 }                                      │
│ （状态：{ "current_value": 22 }）                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

The state variable persists across turns, enabling continuous calculations.

状态变量在回合之间持续存在，从而实现连续计算。

## Long-Term Memory: Beyond the Context Window （长期记忆：超越上下文窗口）

For truly persistent memory, we need external storage:

为了实现真正的持久记忆，我们需要外部存储：

```
┌──────────────────────────────────────────────────────────────────────────┐
│                                                                          │
│   User Input （用户输入）                                                  │
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
│   Response （响应）                                                        │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

This architecture enables potentially unlimited memory by:
1. Extracting key information from conversations
2. Storing it in external databases
3. Retrieving relevant context when needed
4. Incorporating that context into the prompt

这种架构通过以下方式实现潜在的无限记忆：
1. 从对话中提取关键信息
2. 将其存储在外部数据库中
3. 在需要时检索相关上下文
4. 将该上下文整合到提示中

## Cell Implementation: A Memory Manager （细胞实现：记忆管理器）

Here's a Python class that implements basic memory management:

这是一个实现基本记忆管理的 Python 类：

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
        """
        Add a conversation exchange to history.
        """
        self.conversation_history.append({
            "user": user_input,
            "assistant": assistant_response
        })
        
        # Apply memory management if needed
        if len(self.conversation_history) > self.max_turns:
            self._manage_memory()
    
    def extract_info(self, key, value):
        """
        Store important information in key-value store.
        """
        self.key_value_store[key] = value
    
    def _manage_memory(self):
        """
        Apply the selected memory management strategy.
        """
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
        """
        Create a summary of conversation exchanges.
        """
        # In practice, this would call an LLM to create the summary
        # For this example, we'll use a placeholder
        return f"Summary of {len(exchanges)} previous exchanges"
    
    def build_context(self, current_input):
        """
        Build the full context for the next LLM call.
        """
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

## Measuring Cell Efficiency （衡量细胞效率）

As with molecules, measuring efficiency is crucial for cells:

与分子一样，衡量细胞的效率至关重要：

```
┌──────────────────────────────────────────────────────────────────┐
│ MEMORY STRATEGY COMPARISON                                       │
│ （记忆策略比较）                                                   │
├──────────────────┬──────────────┬─────────────┬─────────────────┤
│ Strategy         │ Token Usage  │ Information │ Implementation  │
│ （策略）           │ （令牌使用）   │ （信息）      │ （实现）          │
│                  │              │ Retention   │ Complexity      │
│                  │              │ （保留）      │ （复杂性）        │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ No Memory        │ Lowest       │ None        │ Trivial         │
│ （无记忆）         │ （最低）       │ （无）        │ （微不足道）      │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Full History     │ Highest      │ Complete    │ Trivial         │
│ （完整历史）       │ （最高）       │ （完整）      │ （微不足道）      │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Windowing        │ Controlled   │ Recent Only │ Easy            │
│ （窗口化）         │ （受控）       │ （仅最近）    │ （简单）          │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Summarization    │ Moderate     │ Good        │ Moderate        │
│ （摘要化）         │ （适中）       │ （良好）      │ （适中）          │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ Key-Value Store  │ Low          │ Selective   │ Moderate        │
│ （键值存储）       │ （低）         │ （选择性）    │ （适中）          │
├──────────────────┼──────────────┼─────────────┼─────────────────┤
│ External Store   │ Very Low     │ Extensive   │ Complex         │
│ （外部存储）       │ （非常低）     │ （广泛）      │ （复杂）          │
└──────────────────┴──────────────┴─────────────┴─────────────────┘
```

Different strategies optimize for different priorities. Choosing the right approach depends on your specific application needs.

不同的策略针对不同的优先级进行优化。选择正确的方法取决于您的具体应用需求。

## Advanced Techniques: Memory Orchestration （高级技术：记忆编排）

For sophisticated applications, multiple memory systems can work together:

对于复杂的应用程序，多个记忆系统可以协同工作：

```
┌─────────────────────────────────────────────────────────────────────┐
│                      MEMORY ORCHESTRATION                           │
│                      （记忆编排）                                     │
│                                                                     │
│  ┌─────────────────┐    ┌─────────────────┐   ┌─────────────────┐   │
│  │                 │    │                 │   │                 │   │
│  │ Short-term      │    │ Working         │   │ Long-term       │   │
│  │ Memory          │    │ Memory          │   │ Memory          │   │
│  │ （短期记忆）        │    │ （工作记忆）      │   │ （长期记忆）      │
│  │                 │    │                 │   │                 │   │
│  │ • Recent turns  │    │ • Current task  │   │ • User profile  │   │
│  │   （最近回合）    │    │   （当前任务）    │   │   （用户档案）    │
│  │ • Immediate     │    │ • Active        │   │ • Historical    │   │
│  │   context       │    │   variables     │   │   facts         │   │
│  │   （即时上下文）  │    │   （活动变量）    │   │   （历史事实）    │
│  │ • Last few      │    │ • Task progress │   │ • Learned       │   │
│  │   exchanges     │    │   （任务进度）    │   │   preferences   │   │
│  │   （最后几次交流）│    │ • Mid-task      │   │   （学习偏好）    │
│  │                 │    │   state         │   │                 │   │
│  │                 │    │   （任务中间状态）│   │                 │   │
│  └─────────────────┘    └─────────────────┘   └─────────────────┘   │
│         ▲ ▼                   ▲ ▼                   ▲ ▼              │
│         │ │                   │ │                   │ │              │
│  ┌──────┘ └───────────────────┘ └───────────────────┘ └──────┐      │
│  │                                                           │      │
│  │                    Memory Manager                         │      │
│  │                    （记忆管理器）                           │      │
│  └───────────────────────────────┬───────────────────────────┘      │
│                                  │                                   │
│                                  ▼                                   │
│                        ┌─────────────────┐                           │
│                        │                 │                           │
│                        │   Context       │                           │
│                        │   Builder       │                           │
│                        │   （上下文构建器）│                           │
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
- **Short-term memory**: Recent conversation turns
- **Working memory**: Active task state and variables
- **Long-term memory**: Persistent user information and preferences

这种架构模仿了人类的记忆系统，包括：
- **短期记忆**：最近的对话回合
- **工作记忆**：活动任务状态和变量
- **长期记忆**：持久的用户信息和偏好

The memory manager orchestrates these systems, deciding what information to include in each context.

记忆管理器协调这些系统，决定在每个上下文中包含哪些信息。

## Memory and Hallucination Reduction （记忆与幻觉减少）

One of the most valuable benefits of memory cells is reducing hallucinations:

记忆细胞最有价值的好处之一是减少幻觉：

```
┌─────────────────────────────────────────────────────────────────────┐
│ HALLUCINATION REDUCTION STRATEGIES                                  │
│ （幻觉减少策略）                                                      │
├─────────────────────────────────────────────────────────────────────┤
│ 1. Explicitly store facts extracted from previous exchanges         │
│    （明确存储从先前交流中提取的事实）                                   │
│ 2. Tag information with source/certainty levels                     │
│    （用来源/确定性级别标记信息）                                       │
│ 3. Include relevant facts in context when similar topics arise      │
│    （当出现类似主题时，在上下文中包含相关事实）                         │
│ 4. Detect and correct contradictions between memory and responses   │
│    （检测并纠正记忆与响应之间的矛盾）                                   │
│ 5. Periodically verify important facts through user confirmation    │
│    （通过用户确认定期验证重要事实）                                     │
└─────────────────────────────────────────────────────────────────────┘
```

By grounding the LLM in consistent facts from memory, we improve reliability dramatically.

通过将大型语言模型（LLM）基于记忆中一致的事实，我们显著提高了可靠性。

## Beyond Text: Structured State （超越文本：结构化状态）

Advanced cells maintain structured state beyond just text history:

高级细胞不仅维护文本历史，还维护结构化状态：

```
┌─────────────────────────────────────────────────────────────────────┐
│ STRUCTURED STATE EXAMPLES                                           │
│ （结构化状态示例）                                                    │
├─────────────────────────┬───────────────────────────────────────────┤
│ Progression State       │ {"step": 3, "completed_steps": [1, 2],    │
│ （进展状态）              │  "next_action": "validate_input"}         │
├─────────────────────────┼───────────────────────────────────────────┤
│ User Profile            │ {"name": "Alex", "preferences": {         │
│ （用户档案）              │  "communication_style": "concise",        │
│                         │  "expertise_level": "beginner"}}          │
├─────────────────────────┼───────────────────────────────────────────┤
│ Application State       │ {"current_view": "dashboard",             │
│ （应用程序状态）          │  "filters": ["active", "high_priority"],  │
│                         │  "sort_by": "deadline"}                   │
├─────────────────────────┼───────────────────────────────────────────┤
│ Environmental Context   │ {"location": "Toronto",                   │
│ （环境上下文）            │  "weather": "snowing",                    │
│                         │  "time": "evening"}                       │
└─────────────────────────┴───────────────────────────────────────────┘
```

This structured approach allows precise control over the context and enables more sophisticated applications.

这种结构化方法可以精确控制上下文，并实现更复杂的应用程序。

## Memory Feedback Loops （记忆反馈循环）

Sophisticated cells create feedback loops where the LLM helps manage its own memory:

复杂的细胞会创建反馈循环，其中大型语言模型（LLM）帮助管理自己的记忆：

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  User: "I'm planning a trip to Japan next month."                   │
│  （用户：“我下个月计划去日本旅行。”）                                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY EXTRACTION]                                    ││
│  │ （[内部记忆提取]）                                                ││
│  │ Important facts to remember:                                    ││
│  │ （需要记住的重要事实：）                                          ││
│  │ - User is planning a trip to Japan                              ││
│  │   （- 用户计划去日本旅行）                                        │
│  │ - Trip is scheduled for next month                              ││
│  │   （- 旅行安排在下个月）                                          │
│  │ Confidence: High                                                ││
│  │ （置信度：高）                                                    ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
│  Assistant: "That's exciting! Japan is beautiful. Are you           │
│  interested in cities like Tokyo and Kyoto, or more rural areas?"   │
│  （助手：“太棒了！日本很美。你对东京和京都这样的城市感兴趣，还是更喜欢乡村地区？”）│
│                                                                     │
│  User: "Definitely Tokyo, and maybe Osaka too."                     │
│  （用户：“当然是东京，也许还有大阪。”）                               │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────────┐│
│  │ [INTERNAL MEMORY UPDATE]                                        ││
│  │ （[内部记忆更新]）                                                ││
│  │ Updated facts:                                                  ││
│  │ （更新的事实：）                                                  │
│  │ - User is planning a trip to Japan next month                   ││
│  │   （- 用户下个月计划去日本旅行）                                  │
│  │ - User is interested in Tokyo and Osaka                         ││
│  │   （- 用户对东京和大阪感兴趣）                                    │
│  │ - User may not be interested in rural areas (confidence: medium)││
│  │   （- 用户可能对乡村地区不感兴趣（置信度：中））                   │
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

The LLM itself extracts and updates important information to remember, creating a self-improving memory system.

大型语言模型（LLM）本身提取并更新需要记住的重要信息，从而创建一个自我完善的记忆系统。

## Key Takeaways （主要收获）

1. **Memory cells** add state persistence across multiple interactions
2. **Token budget management** is crucial as conversations grow
3. **Memory strategies** include windowing, summarization, and key-value stores
4. **External memory** enables unlimited, persistent storage beyond the context window
5. **Structured state** enables sophisticated applications beyond simple conversations
6. **Memory orchestration** combines multiple memory systems for optimal performance
7. **Self-improving memory** uses the LLM to help manage its own memory

1. **记忆细胞**在多次交互中增加了状态持久性
2. 随着对话的增长，**令牌预算管理**至关重要
3. **记忆策略**包括窗口化、摘要化和键值存储
4. **外部记忆**实现了上下文窗口之外的无限持久存储
5. **结构化状态**使复杂的应用程序超越了简单的对话
6. **记忆编排**结合了多个记忆系统以实现最佳性能
7. **自我完善记忆**利用大型语言模型（LLM）帮助管理其自身的记忆

## Exercises for Practice （练习）

1. Implement a simple conversation memory system with windowing
2. Compare different memory strategies on the same extended conversation
3. Build a key-value store that extracts important facts from conversations
4. Experiment with using an LLM to summarize older conversation turns
5. Create a structured state manager for a specific application domain

1. 实现一个简单的带窗口化的对话记忆系统
2. 在相同的扩展对话中比较不同的记忆策略
3. 构建一个从对话中提取重要事实的键值存储
4. 尝试使用大型语言模型（LLM）来总结旧的对话回合
5. 为特定应用领域创建结构化状态管理器

## Next Steps （下一步）

In the next section, we'll explore **organs** — multi-agent systems where multiple context cells work together to solve complex problems.

在下一节中，我们将探讨**器官**——多智能体系统，其中多个上下文细胞协同工作以解决复杂问题。

[Continue to 04_organs_applications.md →](04_organs_applications.md)

---

## Deeper Dive: Memory Abstractions （深入探讨：记忆抽象）

Memory can be organized in multiple layers of abstraction:

记忆可以组织成多个抽象层：

```
┌────────────────────────────────────────────────────────────────────┐
│ MEMORY ABSTRACTION LAYERS                                          │
│ （记忆抽象层）                                                       │
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

这种分层方法允许系统在具体细节和对交互上下文的高级理解之间取得平衡。