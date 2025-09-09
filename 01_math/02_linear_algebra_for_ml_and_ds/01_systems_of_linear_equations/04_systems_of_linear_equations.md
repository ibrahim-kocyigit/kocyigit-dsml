# Systems of Linear Equations

We've seen how systems of sentences can provide information. Now, we'll focus on sentences that carry numerical information and translate them into formal **linear equations**.

For example, the sentence:
> "The price of an apple and a banana is $10."

Can be turned into an equation by assigning variables:
* Let `a` = the price of an apple.
* Let `b` = the price of a banana.

The resulting equation is:
$ a + b = 10 $

In this section, we'll solve a few systems using logic and see how they can result in one unique solution, infinite solutions, or no solution at all.

## Problem 1: A Complete System (Unique Solution)

You go to a peculiar grocery store where individual items aren't priced. You only see the total at checkout. You want to figure out the individual prices.

* **Day 1:** You buy 1 apple and 1 banana. The total is **10 dollars**.
* **Day 2:** You buy 1 apple and 2 bananas. The total is **12 dollars**.

How much does each fruit cost?

This scenario gives us a system of two equations with two unknown variables:
1.  $a + b = 10$
2.  $a + 2b = 12$

Let's solve this with logic. The only difference between your purchase on Day 1 and Day 2 is **one extra banana**. The price difference is **2 dollars** (12 dollars - 10 dollars).

Therefore, that one extra banana must cost 2 dollars. So, **b = 2**.

Now that we know a banana costs 2 dollars, we can substitute this value back into the first day's equation:
$ a + 2 = 10 $

Solving for `a`, we find that an apple must cost 8 dollars. So, **a = 8**.

This system has one **unique solution**: apples cost 8 dollars and bananas cost 2 dollars. Because it provides just enough information to solve it completely, it's a **complete** and **non-singular** system.

## Problem 2: A Redundant System (Infinite Solutions)

Let's consider a different scenario at the same store.

* **Day 1:** You buy 1 apple and 1 banana. The total is **10 dollars**.
* **Day 2:** You buy 2 apples and 2 bananas. The total is **20 dollars**.

How much does each fruit cost now? The system of equations is:

1.  $a + b = 10$
2.  $2a + 2b = 20$

If we analyze the second equation, we can see it's just the first equation multiplied by 2. If one apple and one banana cost 10 dollars, it's logical that two of each would cost 20 dollars. The second day's information is **redundant**—it adds nothing new to what we already knew from the first day.

Because we only have one unique piece of information but two unknowns, we cannot find a single solution. This system has **infinitely many solutions**. Any two prices that add up to 10 are valid.

* Could apples be 8 dollars and bananas 2 dollars? Yes. ($8+2=10$)
* Could apples be 5 dollars and bananas 5 dollars? Yes. ($5+5=10$)
* Could apples be 1.50 dollars and bananas 8.50 dollars? Yes. ($1.5+8.5=10$)

This is a **redundant** and **singular** system.

## Problem 3: A Contradictory System (No Solution)

One last trip to the store.

* **Day 1:** You buy 1 apple and 1 banana. The total is **10 dollars**.
* **Day 2:** You buy 2 apples and 2 bananas. The total is **24 dollars**.

This gives us the system:

1.  $a + b = 10$
2.  $2a + 2b = 24$

Here we have a problem. The first day's information tells us that one "set" of (apple + banana) costs 10 dollars. Logic dictates that two "sets" must cost 20 dollars. But the second day's information says the cost is 24 dollars. This is a **contradiction**. The two equations cannot both be true at the same time.

There is a mistake in the information. This system has **no solution**. It is **contradictory** and **singular**.

## What Makes an Equation "Linear"?

We've been using the term **linear equation**. What exactly does it mean? An equation is linear if it follows a simple rule: variables can only be multiplied by constants (scalars) and added or subtracted together.

### ✅ Allowed in Linear Equations:
* $a + b = 10$
* $2a + 3b = 15$
* $3.4a - 48.99b + 2c = 122.5$

### ❌ Not Allowed in Linear Equations (These are Non-Linear):
* Variables raised to a power: $a^2 + b = 10$
* Multiplying or dividing variables: $a \cdot b = 10$ or $b/a = 10$
* Variables inside functions: $sin(a) + b = 10$ or $log(a) = b$
* Variables as exponents: $2^a + b = 10$

**Linear Algebra** is the study of these simpler, "linear" systems. Their straightforward structure allows us to manipulate them and extract information in powerful ways.