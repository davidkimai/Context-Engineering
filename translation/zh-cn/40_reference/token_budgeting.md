# Token Budgeting: Strategic Context Management （Token 预算：战略性上下文管理）

> "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away."
>
>
> **— Antoine de Saint-Exupéry**

> "完美不是在没有什么可添加的时候实现的，而是在没有什么可拿走的时候实现的。"
>
>
> **— 安托万·德·圣埃克苏佩里**

## 1. Introduction: The Economy of Context （1. 引言：上下文的经济性）
Imagine your context window as a precious, finite resource - like memory on an old computer or water in a desert. Every token you use is a drop of water or a byte of memory. Spend too many on the wrong things, and you'll run dry exactly when you need it most.

想象一下您的上下文窗口是一个宝贵的、有限的资源——就像旧电脑上的内存或沙漠中的水。您使用的每个 token 都是一滴水或一个字节的内存。在错误的事情上花费太多，您就会在最需要它的时候耗尽。

Token budgeting is the art and science of making the most of this finite resource. It's about maximizing the value of every token while ensuring your most critical information gets through.

Token 预算是充分利用这一有限资源的艺术和科学。它旨在最大限度地提高每个 token 的价值，同时确保您最关键的信息能够传达。

**Socratic Question**: What happens when you run out of context space in the middle of a complex task?

**苏格拉底式问题**：当您在复杂任务中途耗尽上下文空间时会发生什么？

In this guide, we'll explore several perspectives on token budgeting:

在本指南中，我们将探讨 token 预算的几个视角：

- **Practical**: Concrete techniques to optimize token usage
- **Economic**: Cost-benefit frameworks for token allocation
- **Information-theoretic**: Entropy, compression, and signal-to-noise optimization
- **Field-theoretic**: Managing token distribution in neural fields

- **实用**：优化 token 使用的具体技术
- **经济**：token 分配的成本效益框架
- **信息论**：熵、压缩和信噪比优化
- **场论**：管理神经网络中的 token 分布

## 2. The Token Budget Lifecycle （2. Token 预算生命周期）

### 2.1. Budget Planning （2.1. 预算规划）

Before you begin working with an LLM, understanding your token constraints is crucial:

在开始使用 LLM 之前，了解您的 token 约束至关重要：

```
Model           | Context Window | Typical Usage Pattern
----------------|----------------|----------------------
GPT-3.5 Turbo   | 16K tokens     | Quick tasks, drafting, simple reasoning
GPT-4           | 128K tokens    | Complex reasoning, large document processing
Claude 3 Opus   | 200K tokens    | Long-form content, multiple document analysis
Claude 3 Sonnet | 200K tokens    | Balanced performance for most tasks
Claude 3 Haiku  | 200K tokens    | Fast responses, lower complexity
```

For our examples, we'll work with a standard 16K token context window, though the principles apply across all models and window sizes.

对于我们的示例，我们将使用标准的 16K token 上下文窗口，尽管这些原则适用于所有模型和窗口大小。

### 2.2. The Token Budget Equation （2.2. Token 预算方程）

At its simplest, your token budget can be expressed as:

最简单地说，您的 token 预算可以表示为：

```
Available Tokens = Context Window Size - (System Prompt + Chat History + Current Input)
```

Let's break this down further:

让我们进一步分解：

```
System Prompt Tokens    = Base Instructions + Context Engineering + Examples
Chat History Tokens     = Previous User Messages + Previous Assistant Responses
Current Input Tokens    = User's Current Message + Supporting Documents
```

**Socratic Question**: If your total budget is 16K tokens and your system prompt uses 2K tokens, how should you allocate the remaining 14K tokens for optimal performance?

**苏格拉底式问题**：如果您的总预算是 16K token，并且您的系统提示使用了 2K token，您应该如何分配剩余的 14K token 以获得最佳性能？

### 2.3. Cost-Benefit Analysis （2.3. 成本效益分析）

Not all tokens are created equal. Consider this framework for evaluating token value:

并非所有 token 都生而平等。考虑以下用于评估 token 价值的框架：

```
Token Value = Information Content / Token Count
```

Or more specifically:

或者更具体地说：

```
Value = (Relevance × Specificity × Uniqueness) / Token Count
```

Where:
- **Relevance**: How directly the information relates to the task
- **Specificity**: How precise and detailed the information is
- **Uniqueness**: How difficult the information would be for the model to infer

其中：
- **相关性**：信息与任务的直接关联程度
- **特异性**：信息的精确和详细程度
- **独特性**：模型推断信息的难度

## 3. Practical Token Budgeting Techniques （3. 实用 Token 预算技术）

### 3.1. System Prompt Optimization （3.1. 系统提示优化）

Your system prompt is like the foundation of a building - it needs to be solid but not excessive. Here are techniques to optimize it:

您的系统提示就像建筑的基础——它需要坚固但不能过度。以下是优化它的技术：

#### 3.1.1. Progressive Reduction （3.1.1. 渐进式缩减）

Start with a comprehensive prompt, then iteratively remove elements while testing performance:

从一个全面的提示开始，然后迭代地删除元素，同时测试性能：

```
Original (350 tokens):
You are a financial analyst with expertise in market trends, stock valuation, and investment strategies. You have a PhD in Finance from Stanford University and 15 years of experience working at top investment firms including Goldman Sachs and Morgan Stanley. You specialize in technology sector analysis with deep knowledge of SaaS business models, semiconductor industry dynamics, and emerging tech trends. When analyzing stocks, you consider fundamentals like P/E ratios, growth rates, and competitive positioning. You also incorporate macroeconomic factors such as interest rates, inflation, and regulatory environments. Your responses should be detailed, nuanced, and reflect both quantitative analysis and qualitative strategic thinking...

Optimized (89 tokens):
You are a senior financial analyst specializing in tech stocks. Provide nuanced analysis incorporating:
1. Fundamentals (P/E, growth, competition)
2. Industry context (tech trends, business models)
3. Macroeconomic factors (rates, regulation)
Balance quantitative data with strategic insights.
```

#### 3.1.2. Explicit Role vs. Implicit Guidance （3.1.2. 显式角色与隐式指导）

Rather than using tokens to specify elaborate personas, focus on task-specific guidance:

与其使用 token 来指定复杂的角色，不如专注于任务特定的指导：

```
Instead of (89 tokens):
You are a Python programming expert with 20 years of experience. You've worked at Google, Microsoft, and Amazon. You specialize in machine learning algorithms, data structures, and optimization.

Use (31 tokens):
Provide efficient, production-ready Python code with comments explaining key decisions.
```

#### 3.1.3. Minimal Scaffolding （3.1.3. 最小脚手架）

Use the minimal structure needed to guide the response format:

使用指导响应格式所需的最小结构：

```
Instead of (118 tokens):
Please provide your analysis in the following format:
1. Executive Summary: A 3-5 sentence overview of the key findings
2. Background: Detailed context about the situation
3. Analysis: Step-by-step breakdown of the problem
4. Considerations: Potential challenges and limitations
5. Recommendations: Specific actions to take
6. Timeline: Suggested implementation schedule
7. Additional Resources: Relevant references

Use (35 tokens):
Analyze this problem with:
1. Summary (3-5 sentences)
2. Analysis (step-by-step)
3. Recommendations
```

### 3.2. Chat History Management （3.2. 聊天历史管理）

Chat history can quickly consume your token budget. Here are strategies to manage it:

聊天历史会迅速消耗您的 token 预算。以下是管理它的策略：

#### 3.2.1. Windowing （3.2.1. 窗口化）

Keep only the most recent N messages in context:

仅保留上下文中最新的 N 条消息：

```python
def apply_window(messages, window_size=10):
    """Keep only the most recent window_size messages."""
    if len(messages) <= window_size:
        return messages
    # Always keep the system message (first message)
    return [messages[0]] + messages[-(window_size-1):]
```

#### 3.2.2. Summarization （3.2.2. 摘要）

Periodically summarize the conversation to compress history:

定期总结对话以压缩历史记录：

```python
def summarize_history(messages, summarization_prompt):
    """Summarize chat history to compress token usage."""
    # Extract message content
    history_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages[1:]])
    
    # Create a summarization request
    summary_request = {
        "role": "user",
        "content": f"{summarization_prompt}\n\nChat history to summarize:\n{history_text}"
    }
    
    # Get summary from model
    summary = get_model_response([messages[0], summary_request])
    
    # Replace history with summarized version
    return [
        messages[0],  # Keep system message
        {"role": "system", "content": f"Previous conversation summary: {summary}"}
    ]
```

#### 3.2.3. Key-Value Memory （3.2.3. 键值内存）

Store only the most important information from the conversation:

仅存储对话中最重要的信息：

```python
def update_kv_memory(messages, memory):
    """Extract and store key information from the conversation."""
    for msg in messages:
        if msg['role'] == 'assistant' and 'key_information' in msg.get('metadata', {}):
            for key, value in msg['metadata']['key_information'].items():
                memory[key] = value
    
    # Convert memory to a message
    memory_content = "\n".join([f"{k}: {v}" for k, v in memory.items()])
    memory_message = {"role": "system", "content": f"Important information:\n{memory_content}"}
    
    return memory_message
```

### 3.3. Input Optimization （3.3. 输入优化）

Optimize how you present information to the model:

优化您向模型呈现信息的方式：

#### 3.3.1. Progressive Loading （3.3.1. 渐进式加载）

For large documents, load them in chunks as needed:

对于大型文档，根据需要分块加载：

```python
def progressive_loading(document, chunk_size=1000, overlap=100):
    """Split document into chunks with overlap."""
    chunks = []
    for i in range(0, len(document), chunk_size - overlap):
        chunk = document[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

def process_document_progressively(document, initial_prompt):
    chunks = progressive_loading(document)
    context = initial_prompt
    results = []
    
    for chunk in chunks:
        prompt = f"{context}\n\nProcess this section of the document:\n{chunk}"
        response = get_model_response(prompt)
        results.append(response)
        
        # Update context with key information
        context = f"{initial_prompt}\n\nKey information so far: {summarize(results)}"
    
    return combine_results(results)
```

#### 3.3.2. Information Extraction and Filtering （3.3.2. 信息提取和过滤）

Pre-process documents to extract only relevant information:

预处理文档以仅提取相关信息：

```python
def extract_relevant_information(document, query):
    """Extract only information relevant to the query."""
    sentences = split_into_sentences(document)
    
    # Calculate relevance scores
    relevance_scores = []
    for sentence in sentences:
        relevance = calculate_relevance(sentence, query)
        relevance_scores.append((sentence, relevance))
    
    # Sort by relevance and take top results
    relevance_scores.sort(key=lambda x: x[1], reverse=True)
    
    # Take top 50% of relevant sentences or until we hit a threshold
    extracted = []
    cumulative_relevance = 0
    target_relevance = sum([score for _, score in relevance_scores]) * 0.8
    
    for sentence, score in relevance_scores:
        extracted.append(sentence)
        cumulative_relevance += score
        if cumulative_relevance >= target_relevance:
            break
    
    return " ".join(extracted)
```

#### 3.3.3. Structured Input （3.3.3. 结构化输入）

Use structured formats to reduce token usage:

使用结构化格式以减少 token 使用：

```
Instead of (127 tokens):
The customer's name is John Smith. He is 45 years old. He has been a customer for 5 years. His account number is AC-12345. His email is john.smith@example.com. His phone number is 555-123-4567. He has a premium subscription. His last purchase was on March 15, 2023. He has spent a total of $3,450 with us. His customer satisfaction score is 4.8/5.

Use (91 tokens):
Customer:
- Name: John Smith
- Age: 45
- Tenure: 5 years
- ID: AC-12345
- Email: john.smith@example.com
- Phone: 555-123-4567
- Tier: Premium
- Last purchase: 2023-03-15
- Total spend: $3,450
- CSAT: 4.8/5
```

## 4. Information Theory Perspective （4. 信息论视角）

### 4.1. Entropy and Information Density （4.1. 熵和信息密度）

From an information theory perspective, we want to maximize the information content per token:

从信息论的角度来看，我们希望最大化每个 token 的信息内容：

```
Information Density = Information Content (bits) / Token Count
```

Claude Shannon's information theory tells us that the information content of a message depends on its unpredictability or surprise value. In the context of LLMs:

克劳德·香农的信息论告诉我们，消息的信息内容取决于其不可预测性或惊喜值。在 LLM 的上下文中：

- High-entropy content: Unique information the model couldn't easily predict
- Low-entropy content: Common knowledge or predictable patterns

- 高熵内容：模型不易预测的独特信息
- 低熵内容：常识或可预测模式

**Socratic Question**: Which contains more information per token: a list of common English words or a sequence of random alphanumeric characters?

**苏格拉底式问题**：每 token 包含更多信息的是：常见英语单词列表还是随机字母数字字符序列？

### 4.2. Compression Strategies （4.2. 压缩策略）

Compression works by removing redundancy. Here are some approaches:

压缩通过消除冗余来实现。以下是一些方法：

#### 4.2.1. Semantic Compression （4.2.1. 语义压缩）

Reduce text while preserving core meaning:

在保留核心意义的同时缩减文本：

```
Original (55 tokens):
The meeting is scheduled to take place on Tuesday, April 15th, 2025, at 2:30 PM Eastern Standard Time. The meeting will be held in Conference Room B on the 3rd floor of the headquarters building.

Compressed (28 tokens):
Meeting: Tue 4/15/25, 2:30PM EST
Location: HQ, 3rd floor, Conf Room B
```

#### 4.2.2. Abstraction Levels （4.2.2. 抽象级别）

Move to higher levels of abstraction to compress information:

转移到更高的抽象级别以压缩信息：

```
Low abstraction (84 tokens):
The user clicked on the "Add to Cart" button. Then they navigated to the shopping cart page. They entered their shipping information, including street address, city, state, and zip code. They selected "Standard Shipping" as their shipping method. They entered their credit card information. They clicked on "Place Order".

High abstraction (23 tokens):
User completed standard e-commerce purchase flow from item selection through checkout.
```

#### 4.2.3. Information Chunking （4.2.3. 信息分块）

Group related information into logical chunks:

将相关信息分组为逻辑块：

```
Unstructured (58 tokens):
The API rate limit is 100 requests per minute. Authentication uses OAuth 2.0. The endpoint for user data is /api/v1/users. The endpoint for product data is /api/v1/products. The data format is JSON. Responses include pagination information.

Chunked (51 tokens):
API Specs:
- Rate limit: 100 req/min
- Auth: OAuth 2.0
- Endpoints: /api/v1/users, /api/v1/products
- Format: JSON with pagination
```

## 5. Field Theory Approach to Token Budgeting （5. Token 预算的场论方法）

From a field theory perspective, we can think of the context window as a semantic field where tokens form patterns, attractors, and resonances.

从场论的角度来看，我们可以将上下文窗口视为一个语义场，其中 token 形成模式、吸引子和共振。

### 5.1. Attractor Formation （5.1. 吸引子形成）

Strategic token placement can create semantic attractors that influence the model's interpretation:

战略性 token 放置可以创建语义吸引子，从而影响模型的解释：

```
Weak attractor (diffuse focus):
"Please discuss the importance of renewable energy."

Strong attractor (focused basin):
"Analyze the economic impact of solar panel manufacturing scaling on rural employment specifically."
```

The second prompt creates a much stronger attractor basin, guiding the model toward a specific region of its semantic space.

第二个提示创建了一个更强的吸引盆，引导模型走向其语义空间的特定区域。

### 5.2. Field Resonance and Token Efficiency （5.2. 场共振和 Token 效率）

Tokens that resonate with each other create stronger field patterns:

相互共振的 token 会产生更强的场模式：

```python
def measure_token_resonance(tokens, embeddings_model):
    """Measure semantic resonance between tokens."""
    embeddings = [embeddings_model.embed(token) for token in tokens]
    
    # Calculate pairwise cosine similarity
    resonance_matrix = np.zeros((len(tokens), len(tokens)))
    for i in range(len(tokens)):
        for j in range(len(tokens)):
            resonance_matrix[i][j] = cosine_similarity(embeddings[i], embeddings[j])
    
    # Average resonance
    overall_resonance = (resonance_matrix.sum() - len(tokens)) / (len(tokens) * (len(tokens) - 1))
    
    return overall_resonance, resonance_matrix
```

Higher resonance can achieve stronger field effects with fewer tokens, making your context more efficient.

更高的共振可以用更少的 token 实现更强的场效应，使您的上下文更高效。

### 5.3. Boundary Dynamics （5.3. 边界动力学）

Control information flow through your context window's boundaries:

通过上下文窗口的边界控制信息流：

```python
def apply_boundary_control(new_input, current_context, model_embeddings, threshold=0.7):
    """Control what information enters the context based on relevance."""
    # Embed the current context
    context_embedding = model_embeddings.embed(current_context)
    
    # Process input in chunks
    input_chunks = chunk_text(new_input, chunk_size=50)
    filtered_chunks = []
    
    for chunk in input_chunks:
        # Embed the chunk
        chunk_embedding = model_embeddings.embed(chunk)
        
        # Calculate relevance to current context
        relevance = cosine_similarity(context_embedding, chunk_embedding)
        
        # Apply boundary filter
        if relevance > threshold:
            filtered_chunks.append(chunk)
    
    # Reconstruct filtered input
    filtered_input = " ".join(filtered_chunks)
    
    return filtered_input
```

This creates a semi-permeable boundary around your context, allowing only the most relevant information to enter.

这会在您的上下文周围创建一个半渗透边界，只允许最相关的信息进入。

## 6. Strategic Budget Allocation （6. 战略预算分配）

Now that we understand various perspectives on token budgeting, let's explore strategic allocation frameworks:

现在我们了解了 token 预算的各种视角，接下来让我们探讨战略分配框架：

### 6.1. The 40-40-20 Framework （6.1. 40-40-20 框架）

A general-purpose allocation for complex tasks:

复杂任务的通用分配：

```
40% - Task-specific context and examples
40% - Active working memory (chat history and evolving state)
20% - Reserve for unexpected complexity
```

### 6.2. The Pyramid Model （6.2. 金字塔模型）

Allocate tokens based on a hierarchy of needs:

根据需求层次分配 token：

```
Level 1 (Base): Core instructions and constraints (20%)
Level 2: Critical context and examples (30%)
Level 3: Recent interaction history (30%)
Level 4: Auxiliary information and enhancements (15%)
Level 5 (Top): Reserve buffer (5%)
```

### 6.3. Dynamic Allocation （6.3. 动态分配）

Adapt your budget based on task complexity:

根据任务复杂性调整预算：

```python
def allocate_token_budget(task_type, context_window_size):
    """Dynamically allocate token budget based on task type."""
    if task_type == "simple_qa":
        return {
            "system_prompt": 0.1,  # 10% for system prompt
            "examples": 0.0,       # No examples needed
            "history": 0.7,        # 70% for conversation history
            "user_input": 0.15,    # 15% for user input
            "reserve": 0.05        # 5% reserve
        }
    elif task_type == "creative_writing":
        return {
            "system_prompt": 0.15,  # 15% for system prompt
            "examples": 0.2,        # 20% for examples
            "history": 0.4,         # 40% for conversation history
            "user_input": 0.15,     # 15% for user input
            "reserve": 0.1          # 10% reserve
        }
    elif task_type == "complex_reasoning":
        return {
            "system_prompt": 0.15,  # 15% for system prompt
            "examples": 0.25,       # 25% for examples
            "history": 0.3,         # 30% for conversation history
            "user_input": 0.2,      # 20% for user input
            "reserve": 0.1          # 10% reserve
        }
    # Default allocation
    return {
        "system_prompt": 0.15,
        "examples": 0.15,
        "history": 0.4,
        "user_input": 0.2,
        "reserve": 0.1
    }
```

## 7. Measuring and Optimizing Token Efficiency （7. 测量和优化 Token 效率）

### 7.1. Token Efficiency Metrics （7.1. Token 效率指标）

To optimize, we need to measure. Here are key metrics:

为了优化，我们需要测量。以下是关键指标：

#### 7.1.1. Task Completion Rate (TCR) （7.1.1. 任务完成率 (TCR)）

```
TCR = (Tasks Successfully Completed) / (Total Tokens Used)
```

Higher is better - more completed tasks per token spent.

越高越好——每个 token 完成的任务越多。

#### 7.1.2. Information Retention Ratio (IRR) （7.1.2. 信息保留率 (IRR)）

```
IRR = (Key Information Points Retained) / (Total Information Points)
```

Measures how well your token budget preserves critical information.

衡量您的 token 预算保留关键信息的程度。

#### 7.1.3. Response Quality per Token (RQT) （7.1.3. 每 Token 响应质量 (RQT)）

```
RQT = (Response Quality Score) / (Total Tokens Used)
```

Measures value delivered per token invested.

衡量每投入一个 token 所产生的价值。

### 7.2. Token Efficiency Experiments （7.2. Token 效率实验）

Here's a framework for running token efficiency experiments:

以下是运行 token 效率实验的框架：

```python
def run_token_efficiency_experiment(prompt_variants, task, evaluation_function):
    """Run experiment to measure token efficiency of different prompt variants."""
    results = []
    
    for variant in prompt_variants:
        # Count tokens
        token_count = count_tokens(variant)
        
        # Get model response
        response = get_model_response(variant, task)
        
        # Evaluate response
        quality_score = evaluation_function(response, task)
        
        # Calculate efficiency
        efficiency = quality_score / token_count
        
        results.append({
            "variant": variant,
            "token_count": token_count,
            "quality_score": quality_score,
            "efficiency": efficiency
        })
    
    # Sort by efficiency (highest first)
    results.sort(key=lambda x: x["efficiency"], reverse=True)
    
    return results
```

## 8. Practical Implementation Guide （8. 实用实施指南）

Let's put these concepts into practice with a step-by-step implementation guide:

让我们通过分步实施指南将这些概念付诸实践：

### 8.1. Token Budget Planner （8.1. Token 预算规划器）

```python
class TokenBudgetPlanner:
    def __init__(self, context_window_size, tokenizer):
        self.context_window_size = context_window_size
        self.tokenizer = tokenizer
        self.allocations = {}
        self.used_tokens = {}
    
    def set_allocation(self, component, percentage):
        """Set allocation percentage for a component."""
        self.allocations[component] = percentage
        self.used_tokens[component] = 0
    
    def get_budget(self, component):
        """Get token budget for a component."""
        return int(self.context_window_size * self.allocations[component])
    
    def track_usage(self, component, content):
        """Track token usage for a component."""
        token_count = len(self.tokenizer.encode(content))
        self.used_tokens[component] = token_count
        return token_count
    
    def get_remaining(self):
        """Get remaining tokens in the budget."""
        used = sum(self.used_tokens.values())
        return self.context_window_size - used
    
    def is_within_budget(self, component, content):
        """Check if content fits within component budget."""
        token_count = len(self.tokenizer.encode(content))
        return token_count <= self.get_budget(component)
    
    def optimize_to_fit(self, component, content, optimizer_function):
        """Optimize content to fit within budget."""
        if self.is_within_budget(component, content):
            return content
        
        budget = self.get_budget(component)
        optimized = optimizer_function(content, budget)
        
        # Verify optimized content fits
        if not self.is_within_budget(component, optimized):
            raise ValueError(f"Optimizer failed to fit content within budget of {budget} tokens")
        
        return optimized
    
    def get_status_report(self):
        """Get budget status report."""
        report = {}
        for component in self.allocations:
            budget = self.get_budget(component)
            used = self.used_tokens.get(component, 0)
            report[component] = {
                "budget": budget,
                "used": used,
                "remaining": budget - used,
                "utilization": used / budget if budget > 0 else 0
            }
        
        report["overall"] = {
            "budget": self.context_window_size,
            "used": sum(self.used_tokens.values()),
            "remaining": self.get_remaining(),
            "utilization": sum(self.used_tokens.values()) / self.context_window_size
        }
        
        return report
```

### 8.2. Memory Manager （8.2. 内存管理器）

```python
class ContextMemoryManager:
    def __init__(self, budget_planner, summarization_model=None):
        self.budget_planner = budget_planner
        self.summarization_model = summarization_model
        self.messages = []
        self.memory = {}
    
    def add_message(self, role, content):
        """Add a message to the conversation history."""
        message = {"role": role, "content": content}
        self.messages.append(message)
        
        # Check if we're exceeding our history budget
        history_content = "\n".join([f"{msg['role']}: {msg['content']}" for msg in self.messages])
        history_tokens = self.budget_planner.track_usage("history", history_content)
        history_budget = self.budget_planner.get_budget("history")
        
        # If we're over budget, compress the history
        if history_tokens > history_budget:
            self.compress_history()
    
    def extract_key_information(self, message):
        """Extract key information from a message to store in memory."""
        if self.summarization_model:
            extraction_prompt = "Extract key facts and information from this message as key-value pairs:"
            extraction_input = f"{extraction_prompt}\n\n{message['content']}"
            extraction_result = self.summarization_model(extraction_input)
            
            # Parse key-value pairs
            for line in extraction_result.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    self.memory[key.strip()] = value.strip()
    
    def compress_history(self):
        """Compress history when it exceeds the budget."""
        if not self.summarization_model:
            # If no summarization model, use windowing
            # Always keep the first message (system prompt) and last 5 messages
            self.messages = [self.messages[0]] + self.messages[-5:]
        else:
            # Use summarization
            history_to_summarize = self.messages[1:-3]  # Skip system prompt and keep last 3 messages
            
            if not history_to_summarize:
                return  # Nothing to summarize
                
            # Extract content to summarize
            content_to_summarize = "\n".join([
                f"{msg['role']}: {msg['content']}" 
                for msg in history_to_summarize
            ])
            
            # Create summarization prompt
            summarization_prompt = (
                "Summarize the following conversation history concisely, "
                "preserving key information, decisions, and context:"
            )
            
            # Get summary
            summary = self.summarization_model(
                f"{summarization_prompt}\n\n{content_to_summarize}"
            )
            
            # Replace the messages with a summary
            summary_message = {
                "role": "system",
                "content": f"Summary of previous conversation: {summary}"
            }
            
            # New messages list: system prompt + summary + recent messages
            self.messages = [self.messages[0], summary_message] + self.messages[-3:]
    
    def get_formatted_memory(self):
        """Get memory formatted as a string."""
        if not self.memory:
            return ""
            
        memory_lines = [f"{key}: {value}" for key, value in self.memory.items()]
        return "Key information from conversation:\n" + "\n".join(memory_lines)
    
    def get_context(self):
        """Get the full context for the next interaction."""
        # Combine messages and memory
        memory_content = self.get_formatted_memory()
        
        # If we have memory, insert it after the system prompt
        if memory_content and len(self.messages) > 1:
            memory_message = {"role": "system", "content": memory_content}
            context = [self.messages[0], memory_message] + self.messages[1:]
        else:
            context = self.messages.copy()
            
        return context
```

```
┌─────────────────────────────────────────────────────────────┐
│                     MEMORY MANAGER                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌───────────────┐          ┌───────────────────────────┐   │
│  │ Budget Planner│◄─────────┤ Token Usage Monitoring    │   │
│  └───────┬───────┘          └───────────────────────────┘   │
│          │                                                  │
│          ▼                                                  │
│  ┌───────────────┐   Over    ┌───────────────────────────┐  │
│  │ Message History├─Budget?──►│ Compression Strategies    │  │
│  └───────┬───────┘          ┌┴──────────────────────────┐│  │
│          │                  │1. Windowing               ││  │
│          │                  │2. Summarization           ││  │
│          │                  │3. Key-Value Extraction    ││  │
│          │                  └───────────────────────────┘│  │
│          ▼                                               │  │
│  ┌───────────────┐          ┌───────────────────────────┐│  │
│  │ Context Builder│◄─────────┤ Memory Storage            ││  │
│  └───────┬───────┘          └───────────────────────────┘│  │
│          │                                                  │
│          ▼                                                  │
│  ┌───────────────────────────────────────────────────────┐  │
│  │               Final Context for LLM                    │  │
│  └───────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.3. Dynamic Token Optimizer （8.3. 动态 Token 优化器）

```python
class DynamicTokenOptimizer:
    def __init__(self, tokenizer, optimization_strategies=None):
        self.tokenizer = tokenizer
        self.strategies = optimization_strategies or {
            "summarize": self.summarize_text,
            "extract_key_points": self.extract_key_points,
            "restructure": self.restructure_text,
            "compress_format": self.compress_format
        }
    
    def count_tokens(self, text):
        """Count tokens in text."""
        return len(self.tokenizer.encode(text))
    
    def optimize(self, text, target_tokens, strategy=None):
        """Optimize text to fit within target token count."""
        current_tokens = self.count_tokens(text)
        
        if current_tokens <= target_tokens:
            return text  # Already within budget
        
        # Calculate compression ratio needed
        compression_ratio = target_tokens / current_tokens
        
        # If no strategy specified, select based on compression ratio
        if not strategy:
            if compression_ratio > 0.8:
                strategy = "compress_format"  # Light compression
            elif compression_ratio > 0.5:
                strategy = "restructure"  # Medium compression
            elif compression_ratio > 0.3:
                strategy = "extract_key_points"  # Heavy compression
            else:
                strategy = "summarize"  # Extreme compression
        
        # Apply selected strategy
        if strategy in self.strategies:
            return self.strategies[strategy](text, target_tokens)
        else:
            raise ValueError(f"Unknown optimization strategy: {strategy}")
    
    def summarize_text(self, text, target_tokens):
        """Summarize text to target token count."""
        # This would typically call an LLM for summarization
        # For this example, we'll just truncate with a note
        ratio = target_tokens / self.count_tokens(text)
        truncated = self.truncate_to_ratio(text, ratio * 0.9)  # Leave room for the note
        return f"{truncated}\n[Note: Content has been summarized to fit token budget.]"
    
    def extract_key_points(self, text, target_tokens):
        """Extract key points from text."""
        # This would typically call an LLM to extract key points
        # For this example, we'll create a simple bullet point extraction
        lines = text.split("\n")
        result = "Key points:\n"
        
        for line in lines:
            line = line.strip()
            if line and self.count_tokens(result + f"• {line}\n") <= target_tokens * 0.95:
                result += f"• {line}\n"
        
        return result
    
    def restructure_text(self, text, target_tokens):
        """Restructure text to be more token-efficient."""
        # Remove redundancies, use abbreviations, etc.
        # This is a simplified example
        text = re.sub(r"([A-Za-z]+) \1", r"\1", text)  # Remove repeated words
        text = text.replace("for example", "e.g.")
        text = text.replace("that is", "i.e.")
        text = text.replace("and so on", "etc.")
        
        if self.count_tokens(text) <= target_tokens:
            return text
        
        # If still too long, combine with extraction
        return self.extract_key_points(text, target_tokens)
    
    def compress_format(self, text, target_tokens):
        """Compress by changing formatting without losing content."""
        # Remove extra whitespace
        text = re.sub(r"\s+", " ", text)
        
        # Convert paragraphs to bullet points if appropriate
        if ":" in text and "\n" in text:
            lines = text.split("\n")
            result = ""
            for line in lines:
                if ":" in line:
                    key, value = line.split(":", 1)
                    result += f"• {key}: {value.strip()}\n"
                else:
                    result += line + "\n"
            text = result
        
        if self.count_tokens(text) <= target_tokens:
            return text
        
        # If still too long, try more aggressive restructuring
        return self.restructure_text(text, target_tokens)
    
    def truncate_to_ratio(self, text, ratio):
        """Truncate text to a ratio of its original length."""
        words = text.split()
        target_words = int(len(words) * ratio)
        return " ".join(words[:target_words])
```

```
┌──────────────────────────────────────────────────────────────────┐
│                 DYNAMIC TOKEN OPTIMIZATION                       │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌────────────────────────────────────────────────────────┐     │
│   │                 Compression Ratio                      │     │
│   └────────────────────────────────────────────────────────┘     │
│                           │                                      │
│                           ▼                                      │
│   ┌─────────────┬─────────┴───────────┬──────────────┐          │
│   │             │                     │              │          │
│   ▼             ▼                     ▼              ▼          │
│ 0.8-1.0       0.5-0.8              0.3-0.5        0.0-0.3       │
│ Light         Medium               Heavy          Extreme       │
│                                                                  │
│   ┌─────────────┬─────────────────────┬──────────────┐          │
│   │             │                     │              │          │
│   ▼             ▼                     ▼              ▼          │
│┌─────────┐  ┌─────────┐         ┌──────────┐    ┌─────────┐    │
││ Format  │  │Structure│         │ Extract  │    │Summarize│    │
││Compress │  │Reformat │         │Key Points│    │  Text   │    │
│└─────────┘  └─────────┘         └─────────┘    └─────────┘    │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 8.4. Field-Aware Context Management （8.4. 场感知上下文管理）

Implementing field theory concepts for token budgeting:

为 token 预算实施场论概念：

```python
class FieldAwareContextManager:
    def __init__(self, embedding_model, tokenizer, budget_planner):
        self.embedding_model = embedding_model
        self.tokenizer = tokenizer
        self.budget_planner = budget_planner
        self.field_state = {
            "attractors": [],
            "boundaries": {
                "permeability": 0.7,  # Default permeability threshold
                "gradient": 0.2       # How quickly permeability changes
            },
            "resonance": 0.0,
            "residue": []
        }
    
    def embed_text(self, text):
        """Generate embeddings for text."""
        return self.embedding_model.embed(text)
    
    def detect_attractors(self, text, threshold=0.8):
        """Detect semantic attractors in text."""
        # Split into paragraphs or sections
        sections = text.split("\n\n")
        
        # Get embeddings for each section
        embeddings = [self.embed_text(section) for section in sections]
        
        # Calculate centroid
        centroid = np.mean(embeddings, axis=0);
        
        # Find sections that form attractors (high similarity to many others)
        attractors = []
        for i, (section, embedding) in enumerate(zip(sections, embeddings)):
            # Calculate average similarity to other sections
            similarities = [cosine_similarity(embedding, other_emb) 
                           for j, other_emb in enumerate(embeddings) if i != j]
            avg_similarity = np.mean(similarities) if similarities else 0
            
            # If similarity is above threshold, it's an attractor
            if avg_similarity > threshold:
                tokens = self.tokenizer.encode(section)
                attractors.append({
                    "text": section,
                    "embedding": embedding,
                    "strength": avg_similarity,
                    "token_count": len(tokens)
                })
        
        return attractors
    
    def calculate_resonance(self, text):
        """Calculate field resonance for text."""
        # Split into paragraphs or sections
        sections = text.split("\n\n")
        
        if len(sections) <= 1:
            return 0.0  # Not enough sections to calculate resonance
        
        # Get embeddings for each section
        embeddings = [self.embed_text(section) for section in sections]
        
        # Calculate pairwise similarities
        similarities = []
        for i in range(len(embeddings)):
            for j in range(i+1, len(embeddings)):
                similarities.append(cosine_similarity(embeddings[i], embeddings[j]))
        
        # Resonance is the average similarity
        return np.mean(similarities)
    
    def update_field_state(self, new_text):
        """Update field state with new text."""
        # Update attractors
        new_attractors = self.detect_attractors(new_text)
        self.field_state["attractors"].extend(new_attractors)
        
        # Update resonance
        new_resonance = self.calculate_resonance(new_text)
        self.field_state["resonance"] = (
            self.field_state["resonance"] * 0.7 + new_resonance * 0.3
        )  # Weighted average
        
        # Update permeability based on resonance
        if new_resonance > self.field_state["resonance"]:
            # If resonance is increasing, increase permeability
            self.field_state["boundaries"]["permeability"] += self.field_state["boundaries"]["gradient"]
        else:
            # If resonance is decreasing, decrease permeability
            self.field_state["boundaries"]["permeability"] -= self.field_state["boundaries"]["gradient"]
        
        # Keep permeability in [0.1, 0.9] range
        self.field_state["boundaries"]["permeability"] = max(
            0.1, min(0.9, self.field_state["boundaries"]["permeability"])
        )
    
    def filter_by_attractor_relevance(self, text, top_n_attractors=3, threshold=0.6):
        """Filter text based on relevance to top attractors."""
        if not self.field_state["attractors"]:
            return text  # No attractors to filter by
        
        # Sort attractors by strength
        sorted_attractors = sorted(
            self.field_state["attractors"], 
            key=lambda x: x["strength"], 
            reverse=True
        )
        
        # Take top N attractors
        top_attractors = sorted_attractors[:top_n_attractors]
        top_embeddings = [attractor["embedding"] for attractor in top_attractors]
        
        # Split text into paragraphs
        paragraphs = text.split("\n\n")
        
        # Calculate relevance of each paragraph to top attractors
        filtered_paragraphs = []
        for paragraph in paragraphs:
            # Skip empty paragraphs
            if not paragraph.strip():
                continue
                
            # Get embedding
            embedding = self.embed_text(paragraph)
            
            # Calculate max similarity to any attractor
            similarities = [cosine_similarity(embedding, attractor_emb) 
                           for attractor_emb in top_embeddings]
            max_similarity = max(similarities)
            
            # If similarity is above threshold or permeability allows it
            if (max_similarity > threshold or 
                random.random() < self.field_state["boundaries"]["permeability"]):
                filtered_paragraphs.append(paragraph)
        
        # Join filtered paragraphs
        return "\n\n".join(filtered_paragraphs)
    
    def optimize_context_for_budget(self, context, target_tokens):
        """Optimize context to fit token budget using field-aware methods."""
        # Count current tokens
        current_tokens = len(self.tokenizer.encode(context))
        
        if current_tokens <= target_tokens:
            return context  # Already within budget
        
        # If we have attractors, use them to filter
        if self.field_state["attractors"]:
            context = self.filter_by_attractor_relevance(context)
            
            # Check if we're now within budget
            current_tokens = len(self.tokenizer.encode(context))
            if current_tokens <= target_tokens:
                return context
        
        # If still over budget, use more aggressive techniques
        # First, try to preserve the most important parts based on field analysis
        
        # Extract residue (symbolic fragments that should persist)
        paragraphs = context.split("\n\n")
        residue = []
        
        for paragraph in paragraphs:
            # Check if paragraph contains key information worth preserving
            # This could be based on resonance with attractors, presence of key terms, etc.
            if any(attractor["text"] in paragraph for attractor in self.field_state["attractors"]):
                residue.append(paragraph)
        
        # Update residue in field state
        self.field_state["residue"] = residue
        
        # Combine residue with most important attractors
        preserved_content = "\n\n".join(residue)
        preserved_tokens = len(self.tokenizer.encode(preserved_content))
        
        # If preserved content already exceeds budget, summarize it
        if preserved_tokens > target_tokens:
            # This would typically call an LLM for summarization
            # For this example, we'll just truncate
            return context[:int(len(context) * (target_tokens / current_tokens))]
        
        # If we have room left, add the most relevant remaining content
        remaining_budget = target_tokens - preserved_tokens
        
        # Sort remaining paragraphs by relevance to field state
        remaining_paragraphs = [p for p in paragraphs if p not in residue]
        
        if not remaining_paragraphs:
            return preserved_content
            
        # Calculate relevance scores
        relevance_scores = []
        for paragraph in remaining_paragraphs:
            embedding = self.embed_text(paragraph)
            # Calculate average similarity to attractors
            similarities = [cosine_similarity(embedding, attractor["embedding"]) 
                           for attractor_emb in self.field_state["attractors"]]
            avg_similarity = np.mean(similarities) if similarities else 0
            tokens = len(self.tokenizer.encode(paragraph))
            relevance_scores.append((paragraph, avg_similarity, tokens))
        
        # Sort by relevance
        relevance_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Add paragraphs until we hit the budget
        additional_content = []
        for paragraph, _, tokens in relevance_scores:
            if tokens <= remaining_budget:
                additional_content.append(paragraph)
                remaining_budget -= tokens
            
            if remaining_budget <= 0:
                break
        
        # Combine preserved content with additional content
        return preserved_content + "\n\n" + "\n\n".join(additional_content)
```

```
┌─────────────────────────────────────────────────────────────────┐
│                FIELD-AWARE CONTEXT MANAGEMENT                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌────────────────────┐      ┌────────────────────────────┐     │
│  │   Field State      │      │       Attractor Map        │     │
│  │                    │      │                            │     │
│  │  • Attractors      │      │   Strong      Medium       │     │
│  │  • Boundaries      │      │ ╭────╮       ╭────╮       │     │
│  │  • Resonance       │      │ │ A1 │       │ A2 │       │     │
│  │  • Residue         │      │ ╰────╯       ╰────╯       │     │
│  └────────┬───────────┘      │                            │     │
│           │                  │               Weak         │     │
│           │                  │              ╭────╮        │     │
│           │                  │              │ A3 │        │     │
│           │                  │              ╰────╯        │     │
│           │                  └────────────────────────────┘     │
│           │                                                     │
│           ▼                                                     │
│  ┌────────────────────┐      ┌────────────────────────────┐     │
│  │  Context Filtering │      │     Boundary Dynamics      │     │
│  │                    │      │                            │     │
│  │  • Attractor       │      │  Permeability: 0.7         │     │
│  │    Relevance       │      │  ┌─────────────────────┐   │     │
│  │  • Resonance       │      │  │█████████░░░░░░░░░░░░│   │     │
│  │    Amplification   │      │  └─────────────────────┘   │     │
│  │  • Residue         │      │                            │     │
│  │    Preservation    │      │  Gradient: 0.2             │     │
│  └────────┬───────────┘      └────────────────────────────┘     │
│           │                                                     │
│           ▼                                                     │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                 Optimized Context                        │   │
│  │                                                          │   │
│  │  • Preserved high-resonance content                      │   │
│  │  • Retained symbolic residue                             │   │
│  │  • Filtered by attractor relevance                       │   │
│  │  • Dynamically balanced by field state                   │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 9. No Code: Protocol Shells for Token Optimization （9. 无代码：用于 Token 优化的协议外壳）

You don't need to be a programmer to leverage advanced token budgeting techniques. Here we'll explore how to use protocol shells, pareto-lang, and fractal.json patterns to optimize your context without writing any code.

您无需成为程序员即可利用高级 token 预算技术。在这里，我们将探讨如何使用协议外壳、pareto-lang 和 fractal.json 模式来优化您的上下文，而无需编写任何代码。

### 9.1. Introduction to Protocol Shells （9.1. 协议外壳简介）

Protocol shells are structured, human-readable templates that help organize context and control token usage. They follow a consistent pattern that both humans and AI models can easily understand.

协议外壳是结构化的、人类可读的模板，有助于组织上下文和控制 token 使用。它们遵循人类和 AI 模型都能轻松理解的一致模式。

#### Basic Protocol Shell Structure （基本协议外壳结构）

```
/protocol.name{
    intent="What this protocol aims to achieve",
    input={
        key1="value1",
        key2="value2"
    },
    process=[
        /step1{action="do something"},
        /step2{action="do something else"}
    ],
    output={
        result1="expected output 1",
        result2="expected output 2"
    }
}
```

This structure creates a clear, token-efficient way to express complex instructions.

这种结构创建了一种清晰、token 高效的方式来表达复杂指令。

### 9.2. Using Pareto-lang for Token Management （9.2. 使用 Pareto-lang 进行 Token 管理）

Pareto-lang is a simple but powerful notation for defining context operations. Here's how to use it for token optimization:

Pareto-lang 是一种简单但功能强大的符号，用于定义上下文操作。以下是如何使用它进行 token 优化：

#### 9.2.1. Basic Syntax （9.2.1. 基本语法）

```
/action.modifier{parameters}
```

For example:

例如：

```
/context.compress{target="history", method="summarize", threshold=0.7}
```

This tells the model to compress the conversation history using summarization when it exceeds 70% of the allocated budget.

这告诉模型，当对话历史超过分配预算的 70% 时，使用摘要功能压缩对话历史。

#### 9.2.2. Token Budget Protocol Example （9.2.2. Token 预算协议示例）

```
/token.budget{
    intent="Manage token usage efficiently throughout conversation",
    allocations={
        system_prompt=0.15,   // 15% for system instructions
        history=0.40,         // 40% for conversation history
        current_input=0.30,   // 30% for current user input
        reserve=0.15          // 15% reserve capacity
    },
    management_rules=[
        /history.summarize{when="history > 0.8*allocation", method="key_points"},
        /system.prune{when="system > allocation", keep="essential_instructions"},
        /input.prioritize{method="relevance_to_context"}
    ],
    monitoring={
        track_usage=true,
        alert_threshold=0.9,  // Alert when 90% of total budget is used
        optimize_automatically=true
    }
}
```

### 9.3. Token-Efficient Field Management （9.3. Token 高效场管理）

Let's see how to use protocol shells to implement field theory concepts without code:

让我们看看如何使用协议外壳在不编写代码的情况下实现场论概念：

```
/field.manage{
    intent="Create and maintain semantic field structure for optimal token usage",
    
    attractors=[
        {name="core_concept_1", strength=0.8, keywords=["key1", "key2", "key3"]},
        {name="core_concept_2", strength=0.7, keywords=["key4", "key5", "key6"]}
    ],
    
    boundaries={
        permeability=0.7,  // How easily new content enters the field
        gradient=0.2,      // How quickly permeability changes
        rules=[
            /boundary.adapt{trigger="resonance_change", threshold=0.1},
            /boundary.filter{method="attractor_relevance", min_score=0.6}
        ]
    },
    
    residue_handling={
        tracking=true,
        preservation_strategy="compress_and_retain",
        priority="high"  // Residue gets token priority
    },
    
    token_optimization=[
        /optimize.by_attractor{keep="strongest", top_n=3},
        /optimize.preserve_residue{min_strength=0.5},
        /optimize.amplify_resonance{target=0.8}
    ]
}
```

### 9.4. Fractal.json for Structured Token Management （9.4. Fractal.json 用于结构化 Token 管理）

Fractal.json provides a structured way to define recursive, self-similar patterns for context management:

Fractal.json 提供了一种结构化的方式来定义用于上下文管理的递归、自相似模式：

```json
{
  "fractalTokenManager": {
    "version": "1.0.0",
    "description": "Recursive token optimization framework",
    "allocation": {
      "system": 0.15,
      "history": 0.40,
      "input": 0.30,
      "reserve": 0.15
    },
    "strategies": {
      "system": {
        "compression": "minimal",
        "priority": "high"
      },
      "history": {
        "compression": "progressive",
        "strategies": ["window", "summarize", "key_value"],
        "recursion": true
      },
      "input": {
        "filtering": "relevance",
        "threshold": 0.6
      }
    },
    "field": {
      "attractors": {
        "detection": true,
        "influence": 0.8
      },
      "resonance": {
        "target": 0.7,
        "amplification": true
      },
      "boundaries": {
        "adaptive": true,
        "permeability": 0.6
      }
    },
    "recursion": {
      "depth": 3,
      "self_optimization": true
    }
  }
}
```

### 9.5. Practical Applications Without Code （9.5. 无代码实际应用）

Here are some practical ways to use these approaches without programming:

以下是一些无需编程即可使用这些方法的实用方法：

#### 9.5.1. Manual Token Budget Tracking （9.5.1. 手动 Token 预算跟踪）

Keep a simple tracking system in your prompts:

在您的提示中保留一个简单的跟踪系统：

```
TOKEN BUDGET (16K total):
- System Instructions: 2K (12.5%)
- Examples: 3K (18.75%)
- Conversation History: 6K (37.5%)
- Current Input: 4K (25%)
- Reserve: 1K (6.25%)

OPTIMIZATION RULES:
1. When history exceeds 6K tokens, summarize oldest parts
2. Prioritize examples most relevant to current query
3. Keep system instructions concise and focused
```

#### 9.5.2. Field-Aware Prompting Template （9.5.2. 场感知提示模板）

```
FIELD MANAGEMENT:

CORE ATTRACTORS:
1. [Primary Topic] - maintain focus on this concept
2. [Secondary Topic] - include when relevant to primary
3. [Tertiary Topic] - include only when explicitly mentioned

BOUNDARY RULES:
- Include new information only when relevance > 7/10
- Maintain coherence with previous context
- Filter tangential content

RESIDUE PRESERVATION:
- Key definitions must persist across context
- Core principles should be reinforced
- Critical decisions/conclusions must be retained

OPTIMIZATION DIRECTIVES:
- Summarize history when exceeding 40% of context
- Prioritize content with highest relevance to core attractors
- Compress format but preserve meaning
```

#### 9.5.3. Protocol Shell Prompt Example （9.5.3. 协议外壳提示示例）

Here's a complete example you can copy and paste to implement token budgeting:

以下是一个完整的示例，您可以复制粘贴以实现 token 预算：

```
I want you to act as a context management system using the following protocol:

/context.manage{
    intent="Optimize token usage while preserving key information",
    
    budget={
        total_tokens=8000,
        system=1000,
        history=3000,
        current=3000,
        reserve=1000
    },
    
    optimization=[
        /system.compress{method="minimal_instructions"},
        /history.manage{
            method="summarize_when_exceeds_budget",

```