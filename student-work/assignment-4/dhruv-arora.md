
# Dhruv Arora

Hi! My favorite programming language is **Python** because the ecosystem (NumPy, pandas, PyTorch) lets me move fast and iterate quickly.

## Example code
```python
def top_k(nums, k):
    """Return the k largest numbers from the list."""
    return sorted(nums, reverse=True)[:k]

print(top_k([3, 10, 1, 7, 4], 3))
### Code Explanation
The function sorts the list in descending order and takes the first `k`.  
For larger inputs, using `heapq.nlargest(k, nums)` is more efficient (`O(n log k)`).
