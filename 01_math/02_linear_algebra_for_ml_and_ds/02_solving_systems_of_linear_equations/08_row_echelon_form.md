# Row Echelon Form

In the previous lessons, we learned about a simplified matrix form called **row echelon form**. We can obtain this form from any matrix by applying the simple row operations we've just studied. This process is a powerful, algorithmic way to analyze a matrix.

Let's walk through the process for our 2x2 examples.

## Example 1: A Non-Singular Matrix

**Original Matrix:**  

$$
A = 
\begin{bmatrix} 
5 & 1 \\ 
4 & -3 
\end{bmatrix}
$$

The goal is to get a 1 as the first non-zero entry in each row (a "leading 1") and zeros below each leading 1.

### Step 1: Normalize the First Row

Divide the first row by its leading coefficient (5) to get a leading 1.

$$
\begin{bmatrix} 
1 & 0.2 \\ 
4 & -3 
\end{bmatrix}
$$

### Step 2: Eliminate the Entry Below the First Leading 1

To get a zero in the bottom-left corner, we subtract 4 times the first row from the second row.

_New Row 2 = `[4, -3] - 4 * [1, 0.2]` = `[4-4, -3 - 0.8]` = `[0, -3.8]`_

$$
\begin{bmatrix} 
1 & 0.2 \\ 
0 & -3.8 
\end{bmatrix}
$$

### Step 3: Normalize the Second Row

Divide the second row by its leading non-zero coefficient (-3.8) to get its leading 1.

$$
\begin{bmatrix} 
1 & 0.2 \\ 
0 & 1 
\end{bmatrix}
$$

This matrix is now in **row echelon form**.

## Example 2: A Singular Matrix

**Original Matrix:**  

$$
B = 
\begin{bmatrix} 
5 & 1 \\ 
10 & 2 
\end{bmatrix}
$$

### Step 1: Normalize the First Row

Divide the first row by 5.

$$
\begin{bmatrix} 
1 & 0.2 \\ 
10 & 2 
\end{bmatrix}
$$

### Step 2: Eliminate the Entry Below the First Leading 1

Subtract 10 times the first row from the second row.

_New Row 2 = `[10, 2] - 10 * [1, 0.2]` = `[10-10, 2 - 2]` = `[0, 0]`_

$$
\begin{bmatrix} 
1 & 0.2 \\ 
0 & 0 
\end{bmatrix}
$$

### Step 3: Normalize the Second Row

We can't! The leading coefficient is 0, and we cannot divide by zero. The process stops here. This resulting matrix is the **row echelon form** for our singular matrix.

## The Connection Between Row Echelon Form and Rank

This algorithmic process gives us the easiest way to calculate the rank of a matrix.

> **The rank of a matrix is the number of non-zero rows in its row echelon form.**

Let's check our examples:

#### Matrix A (Non-Singular):

* Row Echelon Form: 

$$
\begin{bmatrix} 
1 & 0.2 \\ 
0 & 1 
\end{bmatrix}
$$

* It has **two** non-zero rows. ➔ **Rank = 2**  

#### Matrix B (Singular):**
* Row Echelon Form: 

$$
\begin{bmatrix} 
1 & 0.2 \\ 
0 & 0 
\end{bmatrix}
$$

* It has **one** non-zero row. ➔ **Rank = 1**  

#### The Zero Matrix:**
* Row Echelon Form: 

$$
\begin{bmatrix} 
0 & 0 \\ 
0 & 0 
\end{bmatrix}
$$

* It has **zero** non-zero rows. ➔ **Rank = 0**

This confirms what we learned before and gives us a powerful tool. It also leads to a final, clear definition of non-singularity:

> A square matrix is **non-singular** if and only if its row echelon form has a leading 1 in every row (i.e., no rows of all zeros).

---

**Next:** []