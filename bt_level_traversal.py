# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# bfs method
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result
        q = deque([root])

        while q:
            size = len(q)
            temp = []
            for i in range(size):  # process the queue level by level
                curr = q.popleft()
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(temp)

        return result


# time complexity is O(n) since we are processing the entire tree nodes once
# space complexity is O(n/2) since we are processing the tree nodes level by level


# dfs method
class Solution:

    def __init__(self):
        self.result = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return self.result
        self.dfs(root, 0)
        return self.result

    def dfs(self, root, level):
        if root is None:
            return

        if len(self.result) == level:
            self.result.append([])

        self.result[level].append(root.val)
        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)
