# Ian Sabia

I enjoy working with **Python** and **C**. Python is my go-to for data science and machine learning because of its powerful libraries like PyTorch and TensorFlow, which make building and training models straightforward. I also enjoy using C for embedded systems programming, where having direct control over hardware and memory is essential.

## Example code

```python
import numpy as np

def mcmc_sample(target_fn, n_samples=5000, step_size=0.5):
    samples = []
    x = 0.0
    for _ in range(n_samples):
        x_new = x + np.random.normal(0, step_size)
        if np.random.rand() < target_fn(x_new) / target_fn(x):
            x = x_new
        samples.append(x)
    return np.array(samples)

# Sample from a normal distribution using MCMC
target = lambda x: np.exp(-0.5 * x**2)
samples = mcmc_sample(target)

print(f"Mean: {samples.mean():.3f}")
print(f"Std:  {samples.std():.3f}")
```

### Code Explanation

This script implements the Metropolis-Hastings algorithm, a Markov Chain Monte Carlo (MCMC) method used to sample from probability distributions. The function proposes a random step from the current position, then accepts or rejects it based on the ratio of the target density at the new and old points. Here it samples from a standard normal distribution and prints the estimated mean and standard deviation.

To run this code, install NumPy with `pip install numpy`, save the script to a file (e.g., `mcmc.py`), and run it with `python mcmc.py`.
