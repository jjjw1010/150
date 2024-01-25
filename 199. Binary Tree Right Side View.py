# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Initution: Use BFS, append the right most node of the level, add each node by level,
        dq = collections.deque([root])
        ans = []
        if not root: return ans
        while dq:
            ans.append(dq[0].val)
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.right:
                    dq.append(node.right)
                if node.left:
                    dq.append(node.left)
        return ans
        