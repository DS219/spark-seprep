# Kaiyi Liu
My favorite programming language is Python because its clean syntax, massive ecosystem (NumPy, Pandas, PyTorch), and great tooling make it fast to prototype ideas—especially for deep learning and data science.

## Example Code
```
from math import sqrt

def rms(values):
    """Root-mean-square of a list of numbers."""
    n = len(values)
    return sqrt(sum(x*x for x in values) / n)

if __name__ == "__main__":
    xs = [1, 2, 3, 4, 5]
    print("RMS:", rms(xs))
```
### Code Explanation
The code defines a small rms function to compute the root-mean-square of a list, then runs it on [1,2,3,4,5]. Saving the code as rms.py, and run python rms.py in terminal. You must have python environment set up.
