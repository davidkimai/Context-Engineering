# Module 8: Prompt Programming - Writing Code with Words

### Module Summary

Prompt Programming represents the pinnacle of context engineering, where the line between natural language and computer code blurs. This discipline involves applying the structured, logical paradigms of software development—like functional, procedural, and object-oriented programming—to the craft of prompt design. Instead of writing standalone prompts, you begin to design reusable "cognitive functions," compose them into complex workflows, and use logic to guide the AI's reasoning process.

In this module, you will learn to think of prompts not as simple instructions, but as programs written in English. We will explore how to create modular, reusable prompt functions, chain them together to tackle multi-step problems, and even use conditional logic to build prompts that can adapt their own strategy. Mastering Prompt Programming is the final step in transitioning from a prompt user to a sophisticated AI systems architect.

### Key Takeaways

*   **Treat Prompts Like Functions:** The core idea is to define a cognitive task as a function with clear inputs and a predictable output (e.g., `function summarize(text, style, length)`). This makes your prompts modular and reusable.
*   **Compose, Don't Cram:** Solve complex problems by composing simple functions. The output of a `research(topic)` function can be piped directly into an `analyze(research_results)` function, which then feeds a `synthesize(analysis)` function.
*   **Write Procedural Scripts:** For any non-trivial task, explicitly define the sequence of `steps` the AI should follow. This is the most direct way to implement a "program" for the AI to run.
*   **Think in Objects:** When your prompts consistently revolve around a single entity (like analyzing a document), structure your thinking like an "Object." Define its `properties` (e.g., text, author) and the `methods` you can call on it (e.g., `.summarize()`, `.extract_entities()`).
*   **Use Conditional Logic:** Build smarter prompts by including `if/then` logic. For example: "If the user's question is technical, adopt an expert persona. If the question is simple, use a beginner-friendly tone."

> **Pro-Tip:** Create a **"Tool-Builder" meta-prompt**. This is a prompt whose only job is to generate *other* high-quality, specialized prompts for you. For example, you could ask it: `"You are an expert prompt engineer. Create a detailed prompt template for a 'Fact-Checking' agent. The template should include steps for identifying claims, finding primary sources, and flagging contradictions."` By doing this, you leverage the AI to build your own library of powerful, reusable cognitive tools, dramatically accelerating your workflow.

### Your Turn: Mini-Challenge

Your goal is to practice "Functional Composition" by creating a prompt that chains two cognitive tasks together.

**The Task:**
You have a block of text, and you need to first extract the key bullet points and then format those points into a professional email.

**Your "Cognitive Function" Library:**
1.  **`extract_key_points(text)`:** A prompt that takes text and outputs a bulleted list of the most important points.
2.  **`format_as_email(subject, recipient, points)`:** A prompt that takes a subject, recipient, and a bulleted list of points, and formats them into a clean email.

**Your Challenge:**
You are given the following text:
`"The quarterly meeting is confirmed for next Tuesday at 10 AM in Conference Room 3. All department heads are required to attend. Please prepare a 5-minute summary of your team's progress. The main agenda items will be the Q3 budget review and the Q4 product roadmap. A follow-up email with the full agenda will be sent by EOD Friday."`

Write a single, "composed" prompt that instructs the AI to first perform the `extract_key_points` task and then immediately use that output to perform the `format_as_email` task, sending the summary to 'all-heads@company.com' with the subject "Key Info for Upcoming Quarterly Meeting".
