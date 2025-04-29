import torch
import tenso

######## 01. Scalars ########
# in base Python
x = 25
type(x)  # Out: int

# in PyTorch
x_pt = torch.tensor(25)
x_float_pt = torch.tensor(25, dtype=torch.float)

x_pt.shape  # Out: torch.Size([])

######## 02. Vectors ########
