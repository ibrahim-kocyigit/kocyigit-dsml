### **Summary: Week 1 - Introduction to Linear Algebra & Systems of Linear Equations**  

#### **Key Concepts:**  
1. **Linear Algebra in Machine Learning (ML):**  
   - Fundamental for ML models (e.g., linear regression, neural networks).  
   - Deals with **systems of linear equations**, matrices, and vector spaces.  

2. **Linear Regression Example:**  
   - **Single feature:** Modeled as \( y = wx + b \) (a line in 2D).  
   - **Multiple features:** \( y = w_1x_1 + w_2x_2 + \dots + w_nx_n + b \) (a hyperplane in \( n \)-D).  
   - Goal: Find optimal weights (\( w \)) and bias (\( b \)) to minimize prediction error.  

3. **Systems of Linear Equations:**  
   - Represented as:  
     \[
     \begin{cases}
     y^{(1)} = w_1x_1^{(1)} + \dots + w_nx_n^{(1)} + b \\
     \vdots \\
     y^{(m)} = w_1x_1^{(m)} + \dots + w_nx_n^{(m)} + b
     \end{cases}
     \]  
   - **Objective:** Solve for \( w \) and \( b \) that best fit all equations.  

4. **Geometric Interpretations:**  
   - **2D (1 feature):** Line fitting data points.  
   - **3D (2 features):** Plane in space.  
   - **Higher dimensions:** Hyperplanes.  

5. **Singular vs. Non-Singular Systems:**  
   - **Non-singular:** Unique solution.  
   - **Singular:** No solution or infinitely many solutions.  

6. **Applications in ML:**  
   - Linear regression, neural networks, PCA, SVMs.  

#### **Next Steps:**  
- Matrix representations of linear systems.  
- Solution methods (e.g., Gaussian elimination).  

**Takeaway:** Linear algebra is the backbone of ML, enabling modeling and optimization of complex systems.  

---

**LaTeX Cheat Sheet:**  
- Single-variable regression: `\( y = wx + b \)`  
- Multivariable regression: `\( y = w_1x_1 + \dots + w_nx_n + b \)`  
- System of equations: Use `\begin{cases} ... \end{cases}`.