# https://leetcode.com/problems/largest-rectangle-in-histogram/

import heapq

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = []
        answer = 0

        for i in range(len(heights)+1):
            if i!=len(heights):
                current = heights[i]
            else:
                current = -1

            while stack and current<=heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i-1-stack[-1]
                else:
                    width = i
                answer = max(answer, height*width)
            stack.append(i)

        return answer
