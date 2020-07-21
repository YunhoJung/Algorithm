# https://leetcode.com/problems/validate-binary-tree-nodes/

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        path = set()
        queue = []
        root = float('inf')

        # create indegrees for root search -> root properties : indegree == 0
        indegrees = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                indegrees[leftChild[i]] += 1
            if rightChild[i] != -1:
                indegrees[rightChild[i]] += 1

        # find out the root node by using indegrees and comparison
        for i in range(n):
            if indegrees[i] == 0:
                root = min(i, root) # just in case(multiple roots - Example 4)
                queue.append(root)

        # if queue empty -> root node tree with n == 1 or False(Example 3)
        if not queue:
            return n == 1

        # traversal
        while queue:
            node = queue.pop(0)
            if node in path:
                return False # Example 2

            path.add(node)
            if leftChild[node] != -1: # not leaf node
                queue.append(leftChild[node])

            if rightChild[node] != -1: # not leaf node
                queue.append(rightChild[node])

        return len(path) == n # Example 4
