# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        left, right, sub_sum, length, answer = 0, 0, 0, 0, float('inf')

        while right < len(nums):
            sub_sum += nums[right]
            length += 1

            while sub_sum >= s:
                answer = min(length, answer)
                sub_sum -= nums[left]
                length -= 1
                left += 1
            right += 1

        if answer == float('inf'):
            return 0
        return answer
