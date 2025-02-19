# Chisa Matsumoto

Hi I'm Chisa Matsumoto and my favorite programming language is python because it is easy to learn!

## Example Code

```
import numpy as np
import matplotlib.pyplot as plt
p = np.array([
    [1, 2],
    [1, 3],
    [2, 3],
    [3, 2],
    [3, 1],
    [4, 2],
    [1, 4]
])
colors=["r", "b", "r", "r", "b", "b", "black"]
x = p[:, 0]
y = p[:, 1]
plt.scatter(x, y, color=colors)
plt.show()
```

### Code Explanation

This code uses matplotlib and numpy to display a scatterplot with the points in the array, with some points being red or blue, and one being black.
