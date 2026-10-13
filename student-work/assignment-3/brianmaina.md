# Brian Maina

Hi, my name is Brian and my favorite programming language is Python. It might seem like a cliché pick, but it's incredibly versatile, and I'm good at it because I've drilled so much LeetCode with it!

## Example code

```python
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue

                value = board[r][c]
                square_key = (r//3, c//3)

                if(value in rows[r]
                or value in cols[c]
                or value in squares[square_key]):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[square_key].add(value)

        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]
print(Solution().isValidSudoku(board))
```

### Code Explanation

This is my solution to LeetCode's Valid Sudoku. When I first saw it I had no clue how to approach it, but it taught me a lot, especially using a set for each row, column, and 3x3 square (`(r//3, c//3)`) to catch duplicates in one pass.

To run it, save the code as `sudoku.py` and run `python3 sudoku.py`. It should print `True`.
