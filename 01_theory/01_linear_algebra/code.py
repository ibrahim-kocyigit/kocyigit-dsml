####################################
### INTRODUCTION TO NUMPY ARRAYS ###
####################################

# Importing numpy
import numpy as np

# Create a NumPy array 'a' containing the elements 1, 2, 3.
a = np.array([1, 2, 3])
print(a)  # Output: [1 2 3]

# Create an array with 3 integers, starting from the default integer 0.
b = np.arange(3)
print(b)  # Output: [0 1 2]

# Create an array that starts from the integer 1, ends at 20, incremented by 3.
c = np.arange(1, 20, 3)
print(c)  # Output: [ 1  4  7 10 13 16 19]

# Create an array that starts from the float 1.0, ends at 20.0, incremented by 3.
c_float = np.arange(1, 20, 3, dtype=float)
print(c_float)  # Output: [ 1.  4.  7. 10. 13. 16. 19.]

# Create an array with five evenly spaced values in the interval from 0 to 100
lin_spaced_arr = np.linspace(0, 100, 5)
print(lin_spaced_arr)  # Output: [  0.  25.  50.  75. 100.]

# Create an array of integers with five evenly spaced values in the interval from 0 to 100
lin_spaced_arr_int = np.linspace(0, 100, 5, dtype=int)
print(lin_spaced_arr_int)  # Output: [  0  25  50  75 100]
