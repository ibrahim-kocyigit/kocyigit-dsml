# The Rank of a Matrix in General

Just as with 2x2 matrices, the **rank** is a measure of how non-singular a larger matrix is. The concept is the same: the rank measures how much unique, non-redundant information the matrix (or its corresponding system of linear equations) is carrying.

The number of **linearly independent** equations in a system determines its rank. An equation is considered dependent if it can be constructed from a linear combination of the other equations in the system.

Let's analyze 4 different 3x3 systems to define the rank for larger matrices.

### System 1 (Non-Singular)
* **Equations:**
    1.  $a + b + c = 0$
    2.  $a + 2b + c = 0$
    3.  $a + b + 2c = 0$
* **Analysis:** In this system, it's impossible to obtain any one equation from a combination of the other two. All three equations are linearly independent.
* **Information:** 3 equations, 3 unique pieces of information.
* **Result:** The system has **Rank = 3**. The corresponding matrix also has **Rank = 3**.

### System 2 (Singular)
* **Equations:**
    1.  $a + b + c = 0$
    2.  $a + b + 2c = 0$
    3.  $a + b + 3c = 0$
* **Analysis:** In this system, the third equation is a linear combination of the first two (specifically, `Eq3 = 2 \times Eq2 - Eq1`). It provides no new information.
* **Information:** 3 equations, but only 2 unique pieces of information.
* **Result:** The system has **Rank = 2**. The corresponding matrix also has **Rank = 2**.

### System 3 (Singular)
* **Equations:**
    1.  $a + b + c = 0$
    2.  $2a + 2b + 2c = 0$
    3.  $3a + 3b + 3c = 0$
* **Analysis:** The second equation is twice the first, and the third is three times the first. Both are linearly dependent on the first equation.
* **Information:** 3 equations, but only 1 unique piece of information.
* **Result:** The system has **Rank = 1**. The corresponding matrix also has **Rank = 1**.

### System 4 (Singular, Trivial)
* **Equations:**
    1.  $0a + 0b + 0c = 0$
    2.  $0a + 0b + 0c = 0$
    3.  $0a + 0b + 0c = 0$
* **Analysis:** All equations are $0=0$. No equation provides any information about the variables.
* **Information:** 3 equations, 0 pieces of information.
* **Result:** The system has **Rank = 0**. The corresponding matrix also has **Rank = 0**.

## The Next Step: A Simpler Way to Calculate Rank

A question naturally arises: checking for linear dependence by hand seems difficult and time-consuming. Is there a simpler, more algorithmic way to calculate the rank of any matrix?

The answer is **yes**, and it involves using the **row echelon form** of the matrix, which we will explore next.

---

**Next:** [Row Echelon Form](./08_row_echelon_form.md)