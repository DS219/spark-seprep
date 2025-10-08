### Assignment 6:

**Setup**

Before getting started, fetch new changes from the upstream repo and rebase your main branch.

```
git checkout main
git fetch upstream
git rebase upstream/main
```

Create a new branch for this assignment.

```
git checkout -b assignment-6 upstream/main
```

Check that you are in the correct branch. The assignment-6 branch should be in green and have an asteriks next to it.
```
git branch
```

**Assignment**

1. **Pick any easy category question from [LeetCode](https://leetcode.com/):**
    
   **Example**

   **Problem:** *Two Sum*
   
   **Question:** Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

   - Example Input: `nums = [2,7,11,15]`, `target = 9`
   - Example Output: `[0,1]`
   
   **Constraints:**
   - Each input would have exactly one solution.
   - You may not use the same element twice.

1. **Create a Python script (or any language of your choice) addressing the problem:**

   ```python
   def two_sum(nums, target):
       num_map = {}
       for i, num in enumerate(nums):
           diff = target - num
           if diff in num_map:
               return [num_map[diff], i]
           num_map[num] = i

   # Test case
   nums = [2, 7, 11, 15]
   target = 9
   result = two_sum(nums, target)
   print(f"Indices of the two numbers that add up to {target}: {result}")
   ```

2. **Create a directory in GitHub:**

   - Navigate to: `spark-seprep/student-work/assignment-6`
   - Create a new directory here with your name using `mkdir <firstname-lastname>`
   - Enter this directory for the assignment `cd <firstname-lastname>`
   - You can view the example [here](https://github.com/DS219/spark-seprep/tree/main/student-work/assignment-6/sample-example).

3. **Add the code file to your directory:**
   
   - Save your Python script with a descriptive name, an example for the question above is `two_sum.py`.
   - Add this file to the directory you just created.

4. **Write a detailed commit message:**

   When committing your changes, ensure the commit message is clear and concise. An example commit message could be:

   ```
   Added a solution for LeetCode's 'Two Sum' problem

   - Implemented a Python solution to find indices of two numbers in an array that sum to a target value.
   - Used a dictionary to store previously encountered numbers and their indices for O(n) time complexity.
   - Tested the solution with a sample input [2, 7, 11, 15] and target = 9, returning correct indices [0, 1].
   ```

5. **Create a PR against the DS219/spark-seprep repository like you did in the last two assignments**

**Note: For your assignment, do not use the example already used here to help describe the assignment. Pick any other leetcode question from the easy category.**

**Note: If you mess up after making a commit and want to fix that, DO NOT create a new commit. Amend your existing commit instead and then do a force push**
```
git add [changes]
git commit --amend
git push -f origin [your-branch-name]
```

**Grading Rubric:**
- Descriptive and clear commit message (2 pts)
- Only 1 commit in your PR (2 pts)
- No extra junk files in PR (2 pts)
- Changes should be done on the assignment branch and not on main (2 pts)
- No modifications to any other files in the repo (2 pts)
