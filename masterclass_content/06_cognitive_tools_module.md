# Module 6: Cognitive Tools - Engineering the AI's Thought Process

### Module Summary

This module marks a major shift in our approach. We move beyond providing context to actively engineering the AI's reasoning process itself. "Cognitive Tools" are advanced, structured methods that mimic human mental shortcuts (heuristics) to make an AI's thinking more robust, reusable, and transparent.

We will explore three key tools. First, **Prompt Programs** (or Protocol Shells), which transform our prompts from one-off commands into reusable, programmable templates. Second, **Context Schemas**, which structure the information we provide to the AI, much like a database schema organizes data. Finally, **Recursive Prompting**, a powerful technique that creates a feedback loop, forcing the AI to reflect on and improve its own work. By mastering these tools, you evolve from being a prompt writer into a true "cognitive architect," designing the very systems the AI uses to think.

### Key Takeaways

*   **Program Your Prompts:** A "Prompt Program" is a reusable prompt template with defined parameters, a clear process, and a specified output format. It turns prompting from an art into an engineering discipline.
*   **Structure is Not Optional:** A "Context Schema" (e.g., using JSON or YAML) defines the shape of your context, making it predictable and easier for the AI to understand. This reduces ambiguity and improves reliability.
*   **Force Self-Correction:** "Recursive Prompting" is a loop where you ask the AI to critique its own previous answer. This simple feedback mechanism can dramatically improve the quality and accuracy of complex outputs.
*   **Protocol Shells for Clarity:** A "Protocol Shell" is a simple, text-based way to implement a Prompt Program without code, using a clear `/protocol.name{}` syntax to define intent, inputs, process, and outputs.
*   **Become a Cognitive Architect:** The goal of these tools is to elevate your work from writing individual prompts to designing scalable, reusable, and transparent reasoning systems for the AI to use.

> **Pro-Tip:** Go back to one of your most complex and successful prompts—the one you're most proud of. Analyze it and try to reverse-engineer it into a "Prompt Program." Formalize the core `task`, identify the implicit `process` steps you were guiding the AI through, and define the `output format` you expected. This act of deconstructing your own intuitive success is a huge step toward making your prompting skills more systematic and scalable.

### Your Turn: Mini-Challenge

Your goal is to apply the "Prompt Program" concept to a standard, ad-hoc prompt, making it more structured and reusable.

**The Task:**
You have the following simple, "atomic" prompt:
`"Explain the concept of photosynthesis to a 10-year-old in two paragraphs."`

**Your Challenge:**
Rewrite this ad-hoc prompt into a structured **Prompt Program** using the template below. Your program should have clear parameters for the `concept`, `target_audience`, and `length`.

**Template to Fill In:**
```
program ExplainConcept(concept, target_audience, length) {
  // Define the task
  task = `...`;

  // Define the process
  process = ```
    1. ...
    2. ...
    3. ...
  ```;

  // Define the output format
  format = `...`;

  // Construct the complete prompt
  return `${task}\n\nProcess:\n${process}\n\nFormat:\n${format}\n\nConcept to explain: ${concept}`;
}
```
This exercise will give you hands-on practice in thinking about prompts not as single commands, but as reusable, structured components.
