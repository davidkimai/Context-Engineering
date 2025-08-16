# Module 4: Cells of Context - Giving Your AI a Memory

### Module Summary

By default, an AI has the memory of a goldfish; it forgets everything the moment a conversation turn is over. A "Cell" of context solves this problem by giving the AI a memory. This is done by feeding the history of the conversation back to the model with each new turn. This creates a stateful, continuous interaction, allowing the AI to remember what you've said, refer to past points, and build on previous information.

However, this solution creates a new, critical challenge: the AI's context window (its short-term memory) is finite. As the conversation gets longer, you'll run out of space. The art of building context cells lies in effective memory management—choosing a strategy to decide what the AI "forgets" and what it "remembers." Mastering this is the key to building everything from coherent chatbots to complex, stateful applications that can track information and progress over time.

### Key Takeaways

*   **Memory is Not Automatic:** You must manually add memory to an AI's context, typically by including the past conversation history in the prompt.
*   **The Token Budget Problem:** Every piece of memory you add consumes valuable tokens from the limited context window. The central challenge of memory is managing this budget.
*   **Windowing Memory (The Simplest):** This strategy keeps only the last N conversation turns. It's easy to implement but will always forget the beginning of a long conversation.
*   **Summarization Memory (The Smartest):** This involves using another AI call to summarize older parts of the conversation. It preserves information more effectively but costs more in tokens and time.
*   **Key-Value Memory (The Most Precise):** This method involves extracting specific facts (e.g., `user_name: "Alex"`) and storing them as structured data. It's highly efficient for remembering critical details but requires more complex logic.
*   **Memory Enables Applications:** Stateful memory is for more than just chatbots. It's the foundation for any application that needs to track progress, update variables, or build on previous outputs, like a calculator with a running total.

> **Pro-Tip:** Start with the simplest memory strategy that works for your use case. Don't build a complex summarization or key-value system if a simple "sliding window" of the last 5 turns is good enough. A good progression is:
> 1.  Start with **Windowing**.
> 2.  If the AI forgets key facts from early in the conversation, upgrade to **Summarization**.
> 3.  If you need to remember specific, structured data across many sessions (like user preferences), implement a **Key-Value Store**.

### Your Turn: Mini-Challenge

Your goal is to design the context for a simple, stateful application that demonstrates memory.

**The Task:**
You are building an AI assistant that acts as a "running total" calculator. It needs to remember the current value and update it based on the user's commands.

**Your Challenge:**
Design the "context cell" that would be sent to the AI for the **third turn** of the conversation below. You don't need to write code, just the full text of the prompt.

*   **Turn 1 User Input:** "Start with the number 10."
    *   *(AI Responds: "Got it. The current total is 10.")*
*   **Turn 2 User Input:** "Add 5 to that."
    *   *(AI Responds: "Okay. 10 + 5 = 15. The current total is 15.")*
*   **Turn 3 User Input:** "Now, subtract 3."

Your designed context should include:
1.  A clear **System Prompt** explaining the AI's role.
2.  A structured way to represent the application's **State** (the current total).
3.  The **Current User Input**.

This exercise forces you to think about memory not just as a log of conversation, but as a structured "state" that enables an application to function.
