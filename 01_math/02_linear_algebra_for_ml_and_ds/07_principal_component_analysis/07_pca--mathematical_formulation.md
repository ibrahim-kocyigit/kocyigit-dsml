# PCA - The Mathematical Formulation

Now that we have the intuition behind PCA, let's formalize the step-by-step algorithm using the mathematical concepts we've studied.

This process can be applied to a dataset of any size. For this example, let's assume we start with a dataset of *n* observations and 5 features, and our goal is to reduce it to 2 dimensions.

### Step 1: Construct and Center the Data Matrix
First, we arrange our data into a matrix `X` with *n* rows (observations) and 5 columns (features). Then, we center the data by calculating the mean of each column ($\mu$) and subtracting it from the data.

$$
X_{centered} = X - \mu 
$$

### Step 2: Calculate the Covariance Matrix
Next, we calculate the 5x5 covariance matrix `C` of our centered data. As we learned, this can be done with a single matrix operation:

$$
C = \frac{1}{n-1} X_{centered}^T \cdot X_{centered} 
$$

### Step 3: Find and Sort Eigenvalues and Eigenvectors
We then find the eigenvalues and eigenvectors of the covariance matrix `C`. Since `C` is a 5x5 matrix, we will find 5 eigenvalues ($\lambda_1, \dots, \lambda_5$) and 5 corresponding eigenvectors ($v_1, \dots, v_5$).

We sort these pairs in descending order based on the value of the eigenvalues.

### Step 4: Select Principal Components
Since our goal is to reduce the data to 2 dimensions, we select the **two eigenvectors** that correspond to the **two largest eigenvalues**. These are our principal components.

$ \text{Principal Components} = \{v_1, v_2\} $

### Step 5: Create the Projection Matrix
We create our projection matrix, `V`, by first **normalizing** our chosen eigenvectors to have a length of 1, and then combining them into a single matrix where each normalized vector is a column.

Let $\hat{v}_1 = \frac{v_1}{||v_1||_2}$ and $\hat{v}_2 = \frac{v_2}{||v_2||_2}$ be the normalized eigenvectors.

$ V = \begin{bmatrix} \hat{v}_1 & \hat{v}_2 \end{bmatrix} $

### Step 6: Project the Data
Finally, we project our original centered data onto the new space defined by our principal components. This is done with a final matrix multiplication:

$ X_{PCA} = X_{centered} \cdot V $

The resulting matrix, `X_PCA`, will have *n* rows but now only **2 columns**. We have successfully reduced the dimensionality of our data from 5 to 2 while preserving the maximum possible variance.