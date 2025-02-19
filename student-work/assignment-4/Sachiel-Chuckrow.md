# Sachiel Chuckrow
Hello! My fav language is python because I cannot work with object oriented languages. Python is fun and intuitive to me (plus good for data sci)
## Example code
```{python}
    import numpy as np

class GridWorld:
    def __init__(self, grid, gamma=0.9):
        self.grid = grid
        self.gamma = gamma
        self.n_rows, self.n_cols = grid.shape
        self.n_actions = 4
        
    def __str__(self):
        grid_str = ""
        for row in self.grid:
            grid_str += ' '.join(f'{cell:2}' for cell in row) + "\n"
        return grid_str
        
    def get_neighbors(self, point_in_grid):    
        neighbors = []
        for action in range(self.n_actions):
            new_row = point_in_grid[0] + (action == 0) - (action == 1)
            new_col = point_in_grid[1] + (action == 2) - (action == 3)
            if 0 <= new_row < self.n_rows and 0 <= new_col < self.n_cols:
                neighbors.append((new_row, new_col))
        return neighbors

    def value_iteration(self, max_iterations=1000):
        value_grid = np.zeros_like(self.grid, dtype=float)
        iteration = 0
        while iteration < max_iterations:
            new_value_grid = np.copy(value_grid)
            for row in range(self.n_rows):
                for col in range(self.n_cols):
                    neighbors = self.get_neighbors((row, col))
                    max_value = float('-inf')
                    for new_row, new_col in neighbors:
                        reward = self.grid[new_row, new_col]
                        value = reward + self.gamma * value_grid[new_row, new_col]
                        if value > max_value:
                            max_value = value
                    new_value_grid[row, col] = max_value
            if np.allclose(value_grid, new_value_grid):
                break
            value_grid = new_value_grid
            iteration += 1  
        return value_grid
```
### Code Explination     
This code was written for my rienforcment learning class, which finds optimal values in a grid via value iteration.
