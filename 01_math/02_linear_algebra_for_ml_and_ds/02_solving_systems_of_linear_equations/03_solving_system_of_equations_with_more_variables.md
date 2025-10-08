# Solving Systems of Equations with More Variables

The method of elimination we learned for 2x2 systems can be extended to solve larger systems, such as three equations with three variables. The overall strategy is to systematically eliminate variables until we can solve for one, then work backward to find the others.

The goal is to transform a complex system like this:

1.  $a + b + 2c = 12$
2.  $3a - 3b - c = 3$
3.  $2a - b + 6c = 24$

...into a simple, "solved" system where each equation gives us the value of one variable.

## The Algorithm: A Step-by-Step Guide

The process involves:
1.  **Eliminating the first variable** (`a`) from the second and third equations. This leaves a smaller 2x2 system for the remaining variables.
2.  **Solving the new 2x2 system** to find the value of one variable (e.g., `c`).
3.  **Back-substituting** the known values to find the remaining variables (`b` and then `a`).

## Worked Example

Let's apply this algorithm to our system.

### Step 1: Eliminate 'a' from Equations 2 and 3

Our first objective is to make the `a` variable disappear from the second and third equations. We can use the first equation to do this.

- **To eliminate `a` from Equation 2:** We can multiply Equation 1 by 3 and subtract it from Equation 2.
    - $(3a - 3b - c) - 3(a + b + 2c) = 3 - 3(12)$
    - $(3a - 3a) + (-3b - 3b) + (-c - 6c) = 3 - 36$
    - **New Equation 2:** $-6b - 7c = -33$  

- **To eliminate `a` from Equation 3:** We can multiply Equation 1 by 2 and subtract it from Equation 3.
    - $(2a - b + 6c) - 2(a + b + 2c) = 24 - 2(12)$
    - $(2a - 2a) + (-b - 2b) + (6c - 4c) = 24 - 24$
    - **New Equation 3:** $-3b + 2c = 0$

Our system has now been simplified. The bottom two equations form their own 2x2 system involving only `b` and `c`:

**Simplified System:**
1.  $a + b + 2c = 12$
2.  $-6b - 7c = -33$
3.  $-3b + 2c = 0$

### Step 2: Solve the 2x2 System for 'c'

Now, we focus only on the two new equations. Let's eliminate `b`.

- **New Equation 2:** $-6b - 7c = -33$
- **New Equation 3:** $-3b + 2c = 0$

To eliminate `b`, we can multiply the New Equation 3 by 2 and subtract it from the New Equation 2:
- $(-6b - 7c) - 2(-3b + 2c) = -33 - 2(0)$
- $(-6b + 6b) + (-7c - 4c) = -33$
- $-11c = -33$

Solving this gives us our first known value:
$$ c = 3 $$

---

### Step 3: Back-Substitution

Now that we have the value of `c`, we work our way back up.

1.  **Find `b`:** We plug `c=3` back into one of the 2x2 equations (let's use `-3b + 2c = 0` as it's simpler).
    - $-3b + 2(3) = 0$
    - $-3b + 6 = 0$
    - $-3b = -6$
    - $b = 2$  

2.  **Find `a`:** Now that we know `b=2` and `c=3`, we plug both values back into the very first original equation.
    - $a + b + 2c = 12$
    - $a + (2) + 2(3) = 12$
    - $a + 2 + 6 = 12$
    - $a + 8 = 12$
    - $a = 4$

### The Solved System

We have successfully transformed our original system into the solved system:
1.  $a = 4$
2.  $b = 2$
3.  $c = 3$