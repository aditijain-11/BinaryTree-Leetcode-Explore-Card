# recursice solution
# TC O(n)
# SC O(n)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels


# Iterative Solution
# TC O(n)
# SC O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        q = deque(
            [
                root,
            ]
        )

        while q:
            levels.append([])
            levlen = len(q)
            for i in range(levlen):
                node = q.popleft()
                levels[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return levels
