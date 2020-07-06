# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end, min_start, min_end = 0, 0, 0, 0
        min_len = 2**32
        dict_t = {}

        for c in t:
            if c in dict_t:
                dict_t[c] += 1
            else:
                dict_t[c] = 1

        required = len(dict_t)
        flag = 0
        dict_flag = {}

        while end < len(s):
            if s[end] in dict_flag:
                dict_flag[s[end]] += 1
            else:
                dict_flag[s[end]] = 1

            if (s[end] in dict_t) and (dict_flag[s[end]] == dict_t[s[end]]):
                flag += 1

            while start <= end and flag == required:
                if (end - start) < min_len:
                    min_len = end - start
                    min_start = start
                    min_end = end
                dict_flag[s[start]] -= 1

                if (s[start] in dict_t) and (dict_flag[s[start]] < dict_t[s[start]]):
                    flag -= 1

                start += 1
            end += 1

        if min_len != 2**32:
            answer = s[min_start:min_end+1]
        else:
            answer = ""

        return answer
