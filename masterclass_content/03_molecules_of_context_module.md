# Module 3: Molecules of Context - Teaching with Examples

### Module Summary

If "atomic" prompts are single commands, "molecular" prompts are complete recipes. A molecule combines a core **Instruction** with high-quality **Examples**, teaching the AI how to perform a task rather than just telling it. This method, known as **few-shot learning**, is one of the most effective ways to improve an AI's accuracy and reliability without needing complex programming.

By providing the AI with a few examples of the desired input-output pattern, you are giving it a blueprint to follow. This dramatically reduces ambiguity and inconsistency, especially for tasks like classification, structured data extraction, or following a specific format. The key to success is not just providing examples, but choosing the *right* examples and structuring them effectively. Moving from atoms to molecules is your first big leap from simply *using* an AI to *engineering* its context.

### Key Takeaways

*   **Go Beyond Instruction:** A molecular prompt is more than a command; it's a lesson. The basic formula is `INSTRUCTION + EXAMPLES + NEW INPUT`.
*   **Structure is Everything:** How you format your examples matters. Simple `Input: / Output:` pairs work well for many tasks, but using a `Chain-of-Thought` structure within your examples can teach the model more complex reasoning.
*   **Curate Your Examples Wisely:** The quality of your examples is paramount. Include a diverse range of cases, especially tricky edge cases, to clearly define the boundaries of the task for the AI.
*   **Beware Diminishing Returns:** The biggest performance jump often comes from the very first example. Each additional example provides less and less benefit while still costing tokens. Find the "sweet spot" of 2-5 examples for most tasks.
*   **Dynamic Selection is Advanced Practice:** The most sophisticated systems don't use a fixed set of examples. They dynamically retrieve the most relevant examples from a large database based on the user's specific query.

> **Pro-Tip:** You can supercharge a simple prompt by using a "Chain of Thought" example, even if you don't need the final output to show its reasoning. By showing the AI an example where you've reasoned step-by-step, you "prime" it to think more logically and carefully when it processes your new input. This can significantly improve accuracy on tricky tasks without cluttering the final response.

### Your Turn: Mini-Challenge

Your goal is to directly measure the impact of few-shot learning on a sentiment classification task.

**The Task:**
You need to classify the sentiment of customer reviews as "Positive", "Negative", or "Neutral". Here is the new review you need to classify:
`"The checkout process was smooth, but the item arrived a week late."`

**Your Challenge:**
Create three different prompts to classify this review, starting with zero examples and progressively adding more.

1.  **Prompt A (Zero-Shot):** Use a simple "atomic" prompt with only an instruction.
2.  **Prompt B (One-Shot):** Add one clear example of a "Positive" review to your prompt.
3.  **Prompt C (Few-Shot):** Add three diverse examples to your prompt (one Positive, one Negative, one Neutral) before asking the AI to classify the new review.

**Example structure for Prompt C:**
```
Classify the sentiment of the following reviews as Positive, Negative, or Neutral.

Review: 'The product is fantastic, I love it!'
Sentiment: Positive

Review: 'The item broke after one use.'
Sentiment: Negative

Review: 'The packaging was standard.'
Sentiment: Neutral

Review: 'The checkout process was smooth, but the item arrived a week late.'
Sentiment:
```

Observe how the AI's answer might change from "Negative" (in Prompt A) to the more nuanced and correct "Neutral" as you provide more context in Prompt C. This demonstrates the power of molecular prompting.
