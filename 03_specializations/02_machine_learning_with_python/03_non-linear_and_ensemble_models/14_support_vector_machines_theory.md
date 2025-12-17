# Support Vector Machines (SVM)

## 1. The Core Idea: A Maximum-Margin Separator

Support Vector Machines (SVM) are supervised learning algorithms for classification and regression. Their goal is to find a decision boundary (a hyperplane) that separates classes with the largest possible margin - the distance to the closest points from each class.

- In 2D, the decision boundary is a line; in 3D, a plane; in higher dimensions, a hyperplane.
- The closest points that "pin" the boundary are called support vectors. Moving a support vector changes the boundary; most other points are irrelevant to the final decision function.

<img src="./images/1401.png" alt="SVM Margin and Support Vectors" width="500"/>

Maximizing margin typically improves generalization: a wider margin tends to yield a boundary that performs better on unseen data.

## 2. The Mathematics: Hard vs. Soft Margin

### 2.1. Hard-Margin SVM (Perfectly Separable Data)
If data is linearly separable, SVM fins the separating hyperplane with the largest margin:

#### Decision Function:

$$
f(x) = w^\top x + b
$$  

> "Multiply each input feature by its learned weight, add them up, then add a bias. If the result is positive, predict the positive class; if negative, predict the negative class." The sign of $f(x)$ determines the class.

#### Optimization:

$$
\min_{w,b}\ \frac{1}{2}\lVert w\rVert^2
\quad\text{s.t.}\quad
y_i\big(w^\top x_i + b\big)\ \ge\ 1\ \ \forall i
$$

> "Choose the weights and bias to make the weights as small as possible (which widens the margin), while forcing every training point to be on the correct side of the boundary and at least '1 unit' away from it." This enforces perfect separation with a safety buffer.

### 2.2. Soft-Margin SVM (Real Data with Overlap/Noise)

Real-world data is rarely perfectly separable. Introduce slack variables $\xi_i \ge 0$ to allow margin violations:

#### Optimization:

$$
\min_{w,b,\xi}\ \frac{1}{2}\lVert w\rVert^2 + C\sum_{i=1}^n \xi_i
\quad\text{s.t.}\quad
y_i\big(w^\top x_i + b\big)\ \ge\ 1 - \xi_i,\ \ \xi_i \ge 0
$$

> "Still try to keep the weights small (for a wide margin), but now also pay a penalty for any point that is inside the margin or misclassified." The term $C\sum \xi_i$ adds up how badly points violate the margin. A larger $C$ means we punish violations more; a smaller $C$ means we tolerate more violations for a simpler boundary.

What the slack $\xi_i$ means in practice:  

- $\xi_i = 0$: correctly classified and outside the margin.  
- $0 < \xi_i \le 1$: on the correct side but inside the margin (intruding into the “street” between the classes).  
- $\xi_i > 1$: misclassified (on the wrong side of the boundary).

Role of $C$ (regularization):  
- Larger $C$: fit training data closely → narrower margin, fewer violations (risk of overfitting).  
- Smaller $C$: allow more violations → wider margin, simpler boundary (risk of underfitting).

### 2.3. Hinge Loss View
Soft-margin SVM can be expressed via the hinge loss. Hinge loss per example:

$$
\max\big(0,\ 1 - y_i f(x_i)\big)
$$  

Objective:

$$
\frac{1}{2}\lVert w\rVert^2\ +\ C \sum_i \max\big(0,\ 1 - y_i f(x_i)\big)
$$

> "Keep the model simple (small weights) and minimize the total margin violations across all points, with $C$ deciding how harshly to penalize those violations.

## 3. Non-Linear Boundaries: The Kernel Trick

When classes are not separable by a straight hyperplane, SVM uses the kernel trick to implicitly map inputs into a higher-dimensional space where a linear separator exists-without explicitly computing the mapping.

#### Kernel Function:

$$
K(x, x') = \langle \phi(x), \phi(x') \rangle
$$

> The kernel returns a similarity score between two points as if they had been transformed into a higher-dimensonal feature space. You never compute $\phi(\cdot)$ directly; the kernel gives you the dot product there 'for free'.

#### Common Kernels:

1. **Linear:** $K(x, x') = x^\top x'$  
    “Ordinary dot product” — straight-line similarity; equivalent to no feature mapping.
2. **Polynomial:** $K(x, x') = (\gamma\, x^\top x' + r)^d$  
    “Dot product plus a shift, then raised to a power” — adds curved boundaries; $\gamma$ scales similarity, $r$ offsets it, $d$ controls curvature.
3. **RBF (Gaussian):** $K(x, x') = \exp\big(-\gamma \lVert x - x' \rVert^2\big)$  
    “Exponentially decaying similarity based on squared distance” — nearby points have similarity near 1; far points near 0. $\gamma$ controls how quickly similarity decays with distance.
4. **Sigmoid:** $K(x, x') = \tanh(\gamma\, x^\top x' + r)$  
    “Apply a squashing tanh to a scaled dot product plus offset” — historically linked to neural nets; used less often than RBF/linear.

<img src="./images/1402.png" alt="SVM Kernel Trick" width="600"/>