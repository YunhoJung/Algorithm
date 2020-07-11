# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    min_start, min_end, start, end, flag = 0, 0, 0, 0, 0
    min_len = float('inf')
    flag = 0
    dict_flag = {}
    gems_set_len = len(set(gems))

    # start two pointers
    while end < len(gems):
        # update dict for the necessary condition
        if gems[end] not in dict_flag:
            dict_flag[gems[end]] = 1
        else:
            dict_flag[gems[end]] += 1

        # update flag for the necessary condition
        if dict_flag[gems[end]] == 1:
            flag += 1

        # the necessary condition for the optimal solution
        while (flag == gems_set_len) and (start <= end):
            # update min_idx & min_len
            if end - start < min_len:
                min_len = end - start
                min_start = start
                min_end = end

            # as already checked gems[start]
            dict_flag[gems[start]] -=1

            # if no gems[start] included in dict
            # -> the necessary condition not satisfied
            if dict_flag[gems[start]] == 0:
                flag -= 1

            start += 1
        end += 1

    answer = [min_start+1, min_end+1]
    return answer
