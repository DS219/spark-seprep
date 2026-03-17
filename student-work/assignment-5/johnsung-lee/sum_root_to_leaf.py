class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_root_to_leaf(root: TreeNode) -> int:
    """
    Sum all root-to-leaf paths where each path is treated as a binary number.
    Node values are 0 or 1.
    """
    def dfs(node, current):
        if not node:
            return 0

        # shift left (binary) and add current node value
        current = (current << 1) | node.val

        # if leaf node, return accumulated value
        if not node.left and not node.right:
            return current

        return dfs(node.left, current) + dfs(node.right, current)

    return dfs(root, 0)


# Test case
#      1
#     / \
#    0   1
# Paths: 10 (2) and 11 (3) => sum = 5
root = TreeNode(1, TreeNode(0), TreeNode(1))
print("Sum of root-to-leaf binary numbers:", sum_root_to_leaf(root))