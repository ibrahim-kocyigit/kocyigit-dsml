# Solving Non-Singular Systems of Linear Equations

We are now ready to learn a formal algorithm for finding the solution to a system of linear equations. This method will allow us to solve any non-singular system and will also help us identify if a system is singular.

Let's start by revisiting the apple and banana problem:

1. $a + b = 10$
2. $a + 2b = 12$

Our logical deduction led us to the **solved system**:

1. $a = 8$
2. $b = 2$

## Allowed Equation Manipulations

There are two primary ways we can manipulate linear equations to create new, equally true equations.

1. **Multiplying by a Constant:**  
   If an equation is true, multiplying both sides by the same non-zero constant results in an equation that is also true and carries the same information.  

   *Example:* If $a + b = 10$, then $7(a+b) = 7(10)$, which gives $7a + 7b = 70$.

2. **Adding Two Equations:**  
   If two separate equations are true, their sum is also a true equation.  

   *Example:* If $a + b = 10$ and $2a + 3b = 26$ are both true, then adding them together gives $(a+2a) + (b+3b) = 10+26$, which simplifies to $3a + 4b = 36$.

## Solving a System: A Step-by-Step Example

Let's use these manipulations to solve a slightly harder system of equations. Our goal is to eliminate one variable from one of the equations.

**System:**
1. $5a + b = 17$
2. $4a - 3b = 6$

### Step 1: Normalize the 'a' Coefficient

To make subtraction easier, let's make the coefficient of $a$ equal to 1 in both equations. We do this by dividing each equation by its $a$ coefficient.

- **Equation 1:** Divide by 5 ➔ $a + 0.2b = 3.4$
- **Equation 2:** Divide by 4 ➔ $a - 0.75b = 1.5$

Our new, equivalent system is:
1. $a + 0.2b = 3.4$
2. $a - 0.75b = 1.5$

### Step 2: Eliminate 'a' from the Second Equation

Now we can subtract the first new equation from the second new equation to eliminate $a$.

$$
(a - a) + (-0.75b - 0.2b) = (1.5 - 3.4) \\
0a - 0.95b = -1.9 \\
-0.95b = -1.9
$$

### Step 3: Solve for 'b'

Now that $a$ is gone, we have a simple equation with only one unknown.

$$
-0.95b = -1.9 \\
b = \frac{-1.9}{-0.95} = 2
$$

We have found the first part of our solution!

### Step 4: Substitute to Find 'a'

Now that we know $b = 2$, we can substitute this value back into one of our simplified original equations (let's use the first one).

$$
a + 0.2b = 3.4 \\
a + 0.2(2) = 3.4 \\
a + 0.4 = 3.4 \\
a = 3.4 - 0.4 = 3
$$

### The Solved System

We have successfully transformed our original system into the solved system:
1. $a = 3$
2. $b = 2$

## A Special Case: Zero Coefficients

What if the variable you want to eliminate is already missing from an equation?

**New System:**
1. $5a + b = 17$
2. $3b = 6$

Here, the coefficient of $a$ in the second equation is 0. This is good news! The variable $a$ is already eliminated for us. We can immediately solve the second equation:

$$
3b = 6 \implies b = 2
$$

We can then proceed with Step 4 as usual, substituting $b=2$ into the first equation to find that $a=3$.

---

**Next:** [Solving Systems of Equations with More Variables](./03_solving_system_of_equations_with_more_variables.md)