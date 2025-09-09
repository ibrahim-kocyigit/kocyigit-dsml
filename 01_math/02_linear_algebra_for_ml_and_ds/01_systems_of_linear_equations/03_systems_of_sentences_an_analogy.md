# Systems of Sentences - An Analogy

Before we dive deep into the algebra of linear equations, let's start with a more intuitive idea: thinking of equations as sentences.

A single sentence (or equation) provides a piece of information. A **system of sentences** (or equations) combines multiple pieces of information. The way these sentences interact to build a complete picture is very similar to how equations work together. The goal is always to get as much clear information as possible.

## Simple Systems: What's the Animal's Color?

Let's start with a simple scenario. Assume you have one dog and one cat, and each animal has only one color. Your goal is to figure out their colors based on the information provided.

### System 1: A Complete System
* **Sentence 1:** "The dog is black."
* **Sentence 2:** "The cat is orange."

**Analysis:** We have 2 sentences and they give us 2 distinct pieces of information. This is a **complete** system. We know everything we need to.

### System 2: A Redundant System
* **Sentence 1:** "The dog is black."
* **Sentence 2:** "The dog is black."

**Analysis:** We have 2 sentences, but the second one adds no new information. It just repeats the first. This system only provides 1 unique piece of information. It is **redundant**.

### System 3: A Contradictory System
* **Sentence 1:** "The dog is black."
* **Sentence 2:** "The dog is white."

**Analysis:** The two sentences conflict with each other. Since we know the dog can only have one color, this information is impossible to resolve. The system is **contradictory**.

## New Terminology: Singular vs. Non-Singular

The amount of information a system carries is critical. This leads us to two very important terms that you will use throughout your study of linear algebra.

* **Non-singular System** ✅
    A system that is **complete**. It carries as many unique pieces of information as it has sentences (or equations). It's the most informative and useful type of system.

* **Singular System** ⚠️
    A system that is either **redundant** or **contradictory**. It is less informative than a non-singular system because information is either repeated or nonsensical.

Based on these definitions:
* System 1 ("The dog is black.", "The cat is orange.") is **non-singular**.
* System 2 ("The dog is black.", "The dog is black.") is **singular**.
* System 3 ("The dog is black.", "The dog is white.") is **singular**.

## Systems with More Sentences

This concept scales up to any number of sentences. Let's consider a new scenario with three animals: a dog, a cat, and a bird.

* **System 1:**
    1.  "The dog is black."
    2.  "The cat is orange."
    3.  "The bird is red."
    *  **Result:** 3 sentences, 3 pieces of info. This is **complete** and **non-singular**.  

* **System 2:**
    1.  "The dog is black."
    2.  "The dog is black."
    3.  "The bird is red."
    * **Result:** 3 sentences, but only 2 pieces of info. This is **redundant** and **singular**.  

* **System 3:**
    1.  "The dog is black."
    2.  "The dog is black."
    3.  "The dog is black."
    * **Result:** 3 sentences, but only 1 piece of info. This is highly **redundant** and **singular**.  

* **System 4:**
    1.  "The dog is black."
    2.  "The dog is white."
    3.  "The bird is red."
    * **Result:** The first two sentences conflict. This is **contradictory** and **singular**.  
 
> **Future Concept:** Notice that System 3 is "more redundant" than System 2. There is a mathematical measure for this called **rank**, which you will learn about later.

## A Logic Puzzle 🧩

Systems aren't always straightforward. Sometimes you need to deduce the information. Consider this system:

* **Sentence 1:** "Between the dog, the cat, and the bird, one of them is red."
* **Sentence 2:** "Between the dog and the cat, one of them is orange."
* **Sentence 3:** "The dog is black."

Based on these sentences, can you answer these two questions?
1.  What color is the bird?
2.  Is this system singular or non-singular?

## Solution to the Logic Puzzle

Let's solve this step-by-step:

1.  **Start with the most direct fact.** Sentence 3 tells us plainly: **The dog is black**.

2.  **Use that information in the next sentence.** Sentence 2 says one of the dog or cat is orange. Since we now know the dog is black, it logically follows that **the cat must be orange**.

3.  **Use both facts in the final sentence.** Sentence 1 says one of the three animals is red. We've established the dog is black and the cat is orange. Therefore, **the bird must be red**.

#### Answering the Questions

1.  **What color is the bird?** The bird is **red**.
2.  **Is the system singular or non-singular?** We started with 3 sentences and were able to determine 3 unique pieces of information (the color of each of the three animals). The system contains no redundancies or contradictions. Therefore, it is a **complete** system and is **non-singular**.

---

[Next: Systems of Linear Equations](./04_systems_of_linear_equations.md)