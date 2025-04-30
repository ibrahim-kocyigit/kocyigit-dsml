import numpy as np
import torch

X = np.array([[25, 2], [5, 26], [3, 7]])
X_pt = torch.tensor([[25, 2], [5, 26], [3, 7]])

### WHAT IS A TENSOR TRANSPOSITION?
X.T
X_pt.T
"""
[[25,  5,  3],
 2, 26,  7]]
"""

### BASIC TENSOR ARITHMETIC
X * 2  # type: ignore
X + 2  # type: ignore
X * 2 + 2  # type: ignore

# with PyTorch:
X_pt * 2 + 2  # type: ignore
torch.add(torch.mul(X_pt, 2), 2)
