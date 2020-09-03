# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        left, right, cnt, answer = 0, 0, 0, 0
        word_dict = {}

        while right < len(s):
            if s[right] not in word_dict:
                word_dict[s[right]] = 1
            else:
                word_dict[s[right]] += 1
                answer = max(answer, cnt)
            cnt += 1

            while word_dict[s[right]] > 1 and left < right:
                word_dict[s[left]] -= 1
                cnt -= 1
                left += 1

            right += 1
        return max(answer,cnt)
