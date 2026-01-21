# Software Engineering Practicum

Welcome to DS219 - Spark Software Engineering Practicum

This repository contains resources and assignments for DS219: Spark Software Engineering Practicum. Please read this document carefully to get started and follow best practices throughout the course.

## Overview

- **Resources** for the class are found in the [`resources`](resources/) directory.
- **Assignments and practice code** are organized in subdirectories (e.g., `class-practice/`).

## Getting Started

Please complete the following before the first class:
1. **Update your laptop** to the latest operating system.
2. **Create a GitHub account** if you don’t have one.
3. **Create a [Docker Hub](https://www.docker.com/) account**.
4. **Install [Homebrew](https://brew.sh/)** (Mac users only).
5. **Set up a text editor** (VSCode and vi/vim are preferred).

## Project Practices

To ensure smooth collaboration and code quality, please follow these guidelines:

### 1. Use CodeRabbit for Pull Requests

- CodeRabbit is enabled for this repository to help review your code and provide automated feedback.
- Make sure you address CodeRabbit's comments before the assignment deadline.

### 2. Write Clear Commit Messages

- Every commit should have a concise and descriptive message explaining **what** and **why**.
- Example:  
  `Fix: handle edge case in input parsing for chatbot assignment`
- Avoid generic messages like "update" or "fix".

### 3. Always Create a New Branch per Assignment

- Never commit directly to the `main` branch.
- For each assignment, create a new branch:
  ```bash
  git checkout -b assignment-<name>
  ```
- Open a Pull Request (PR) from your assignment branch to `main` when ready for review.

### 4. Always Fetch Upstream Before Starting Work

- Keep your local repository up-to-date with the latest changes from the upstream repository:
  ```bash
  git fetch upstream
  git checkout main
  git rebase upstream/main
  ```
- This helps prevent merge conflicts and ensures you are working on the latest code.

## Need Help?

- Ask questions using piazza or email to contact the instructors.
- Check the `resources` directory for guides and troubleshooting tips.

---

Happy coding and good luck in the practicum!
