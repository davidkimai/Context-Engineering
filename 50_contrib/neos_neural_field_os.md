# NEOS: From Context Engineering to Cognitive Computing

> *"The last operating system will not manage files. It will manage meaning."*

## What This Is

NEOS (Neural Field Operating System) is a proof of concept that takes the theoretical vocabulary of context engineering — fields, attractors, resonance, symbolic residue — and builds a working operating system around it. Where this repository provides the *conceptual framework* for field-level context design, NEOS provides the *virtual machine model*, the *OS architecture*, and *empirical evidence* that field dynamics produce emergent structure no prompt could.

This contribution documents the system, the theory behind it, and a complete case study.

- **Paper**: [samuele95.github.io/neos/neos-paper.pdf](https://samuele95.github.io/neos/neos-paper.pdf)
- **Interactive Web Version**: [samuele95.github.io/neos](https://samuele95.github.io/neos/NEOS-BREAKTHROUGH.html)
- **Repository**: [github.com/Samuele95/neos](https://github.com/Samuele95/neos)

---

## 1. The Core Thesis: LLMs Are Virtual Machines

The Java Virtual Machine executes bytecode without caring whether it came from Java or Kotlin. An LLM executes token sequences without caring whether they came from a chat, a RAG pipeline, or an agent framework.

```
┌─────────────────────────────────────────────────────────────────┐
│                     THE PARALLEL                                │
├─────────────────────┬───────────────────────────────────────────┤
│  Hardware Age       │  Intelligence Age                        │
├─────────────────────┼───────────────────────────────────────────┤
│  CPU                │  LLM                                     │
│  Machine code       │  Token sequences                         │
│  Unix (bare HW OS)  │  NEOS (bare LLM OS)                     │
│  Files & processes  │  Patterns & resonance                    │
│  Heap memory        │  Field state                             │
│  Garbage collection │  Decay (λ)                               │
│  Stack trace        │  Cycle trace                             │
│  Threads            │  Multi-field orchestration               │
│  JIT compilation    │  Adaptive resonance                      │
└─────────────────────┴───────────────────────────────────────────┘
```

And just as bare hardware needed Unix and the JVM needed an ecosystem of build tools, debuggers, and package managers, the LLM-as-VM needs an operating system. That is what NEOS is: the OS layer between the raw LLM and the applications people build on top of it.

**Socratic Question**: If an LLM is a virtual machine, what is its instruction set? What is its memory model? What does "debugging" mean when the computation is *reasoning*?

---

## 2. The Master Equation

All NEOS dynamics flow from a single PDE:

```
∂A/∂t = -λA(x) + α∫K(x,y)A(y)dy + ι(x,t)
         decay    +    resonance      +   injection
```

Three forces in perpetual tension:

| Force | Parameter | What It Does |
|-------|-----------|--------------|
| **Decay** | λ = 0.05 | Ideas fade unless reinforced. Garbage collection for thought. |
| **Resonance** | α = 0.30 | Related ideas amplify each other through a semantic kernel K(x,y). |
| **Injection** | ι(x,t) | You inject new meaning. The user is the I/O device. |

Two more parameters govern the field's character:

| Parameter | Default | What It Does |
|-----------|---------|--------------|
| **τ (threshold)** | 0.40 | Activation floor — patterns below this go dormant. |
| **σ (bandwidth)** | 0.50 | Semantic reach of each pattern's influence. |

```
┌────────────────────────────────────────────────────────────────┐
│                   ONE DYNAMICS CYCLE                           │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  1. DECAY      All patterns lose activation: A ← A × (1 − λ) │
│  2. RESONATE   Compute pairwise semantic resonance R(i,j)      │
│  3. AMPLIFY    Resonant patterns gain: A ← A + α·Σ(R·A)       │
│  4. THRESHOLD  Below τ → dormant                               │
│  5. COHERENCE  Measure field: C = μ_R / (1 + σ²_R)            │
│  6. ATTRACTOR  Test: coherence > 0.6 ∧ stability > 0.7?       │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

This is not metaphorical. These dynamics run on every `nf cycle` command. The LLM *computes* the resonance, *updates* the activations, and *reports* the field state — all within its context window.

---

## 3. Connection to Context Engineering

This repository's progression from atoms to neural fields maps directly onto NEOS's architecture:

```
Context Engineering Layer    →    NEOS Equivalent
─────────────────────────────────────────────────
Atoms (prompts)              →    nf inject (single pattern)
Molecules (context chunks)   →    Field state (pattern collection)
Cells (memory)               →    Persistence layer (commit/branch)
Organs (applications)        →    Multi-field routing (nf field, nf route)
Neural Systems               →    Dynamics engine (cycle, evolve, collapse)
Neural Fields                →    The master PDE itself
```

The key insight: context engineering at the field level is not about *crafting better prompts* — it is about creating a **continuous activation landscape** where meaning self-organizes through resonance. This is precisely what NEOS implements.

**Socratic Question**: What if context is not a *window* to be filled, but a *field* to be shaped? What changes when you stop *loading* context and start *evolving* it?

---

## 4. Case Study: Software Quality Discipline

To validate the approach, a complete session was run: 69 software engineering patterns were injected into a NEOS field and allowed to self-organize over 52 dynamics cycles.

### What Went In

69 patterns from across software engineering: SOLID principles, GoF design patterns, testing disciplines, refactoring heuristics, API design rules, performance principles.

### What Came Out

**None of the following was encoded in the inputs.** The field discovered it through resonance dynamics:

**Five eigenvectors** (principal components explaining 100% of variance):

| # | Axis | Variance | The Question It Asks |
|---|------|----------|----------------------|
| λ₁ | Meaning ↔ Mechanism | 34.2% | Am I coupling to *what* this does or *how*? |
| λ₂ | Principle ↔ Technique | 22.7% | Do I understand *why* before choosing *how*? |
| λ₃ | Production ↔ Verification | 18.1% | Can I *prove* this works as well as I can *build* it? |
| λ₄ | Restraint ↔ Generalization | 14.3% | Is this abstraction *earned* or *speculative*? |
| λ₅ | Class ↔ System | 10.7% | Does this principle hold at *every scale*? |

**Seven attractor basins** in a nested hierarchy:

```
                         Ψ (Universal Attractor)
                  "What it MEANS > how it WORKS"
                    /          |           \
                   /           |            \
            α₁ SOLID      α₂ Verify      α₃ Craft
           (10 patterns)  (13 patterns)  (12 GoF)
              |               |              |
           α₄ Reuse    ┌─────┼─────┐        |
           (protocol)  α₅   α₆   α₇    singleton
                      Guard Model Optimize  EXPELLED
```

**One universal invariant** (Ψ):

> **"What something MEANS persists; how it WORKS changes."**

Expressed as a field equation:

```
Q(x) = Ψ · [0.342·SOLID + 0.227·F + 0.181·Protocol + 0.143·Simplex + 0.107·Scale]
```

### The Singleton Expulsion

The most striking emergent behavior: the Singleton pattern was *expelled from the field*. Injected at cycle 31 with strength 0.65, it was driven below threshold (0.341 < τ) by cycle 52 through sustained lateral inhibition from four independent sources — test isolation, dependency inversion, composition preference, and single responsibility.

No rule said "expel Singleton." The field's topology made it structurally incompatible with the attractor landscape. This is the kind of emergent structure that an OS-level abstraction enables and that prompt-level thinking cannot achieve.

---

## 5. The Shell: `nf`

NEOS provides ~40 commands organized in 8 categories:

```
┌────────────────────────────────────────────────────────────┐
│                    NEOS COMMAND ALGEBRA                     │
├────────────────┬───────────────────────────────────────────┤
│ Field Ops      │ inject, amplify, attenuate, collapse      │
│ Dynamics       │ cycle, evolve, step, reset                │
│ Measurement    │ measure, attractor, basin, state          │
│ Visualization  │ plot, animate, export                     │
│ Versioning     │ commit, branch, checkout, diff, merge     │
│ Multi-Field    │ field, route, couple                      │
│ Autonomy       │ mode, checkpoint, proceed, task           │
│ Interface      │ config, ask, compute, help                │
└────────────────┴───────────────────────────────────────────┘
```

**A typical workflow:**

```bash
nf session new "analysis"
nf inject "concept_a" --strength 0.8
nf inject "concept_b" --strength 0.7
nf cycle 10                          # Run 10 dynamics cycles
nf attractor list                    # What emerged?
nf collapse --strategy attractor     # Resolve to concrete output
nf commit "first collapse"           # Version the reasoning state
```

The versioning commands deserve special attention: `commit`, `branch`, `checkout`, `diff`, `merge` — this is **git for thought**. You can fork a line of reasoning, explore alternatives, diff two cognitive states, and merge insights. Debugging an agent becomes inspecting its cycle trace.

---

## 6. Why This Matters for Context Engineering

Context engineering as presented in this repository is the *theoretical foundation*. NEOS is one answer to the question: **what does a system look like that takes field-level context design seriously?**

The connection runs deeper than analogy:

- **Attractor dynamics** (`40_reference/attractor_dynamics.md`) describe *what happens* in a context field. NEOS makes those dynamics *executable*.
- **Symbolic mechanisms** (`40_reference/symbolic_mechanisms.md`) describe *how* meaning emerges from tokens. NEOS provides the *observation tools* — cycle traces, resonance maps, coherence metrics.
- **The biological progression** (atoms → fields) describes *complexity levels*. NEOS implements the *full stack* from injection to multi-field orchestration.

The goal: use NEOS as a kernel for a true Agentic OS — one where agents don't just *act* on context but *reason* through it, with every step observable, debuggable, and reproducible.

---

## Links

| Resource | URL |
|----------|-----|
| Repository | [github.com/Samuele95/neos](https://github.com/Samuele95/neos) |
| Paper (PDF) | [samuele95.github.io/neos/neos-paper.pdf](https://samuele95.github.io/neos/neos-paper.pdf) |
| Interactive Paper | [samuele95.github.io/neos](https://samuele95.github.io/neos/NEOS-BREAKTHROUGH.html) |
| Presentation | [samuele95.github.io/neos/presentation](https://samuele95.github.io/neos/NEOS-PRESENTATION.html) |

---

*Contributed by [Samuele Arioli](https://github.com/Samuele95) — NEOS v1.0*
