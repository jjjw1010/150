# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Initution: Use BFS, compute total values of each level, store the level with the maximal value 
        # after caculate each total value
        dq = collections.deque([root])
        level = 1
        maximal_value = root.val
        maximal = 1
        while dq:
            total = 0
            for _ in range(len(dq)):
                node = dq.popleft()
                total += node.val

                if (node.left):
                    dq.append(node.left)
                if (node.right):
                    dq.append(node.right)
            if maximal_value < total:
                maximal = level
                maximal_value = total
            level += 1
        return maximal
        