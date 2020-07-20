# https://programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    idx_list = []
    answer = 0

    # count up & down
    for i, ch in enumerate(name):
        if ch != 'A':
            idx_list.append(i+1)
        min_cnt = min(26 + ord('A') - ord(ch), -(ord('A') - ord(ch)))
        answer += min_cnt

    length = len(name)
    flag = 0
    min_answer = float('inf')

    # count left & right
    for i in range(len(idx_list) - 1):

        if idx_list[-1] - idx_list[i] > idx_list[i] + length - idx_list[i+1]:
            # if direction changed
            flag = 1
            min_answer = min(min_answer,idx_list[i] -1 + idx_list[i] + length - idx_list[i+1])

    # if direction not changed
    if flag == 0:
        answer = answer + idx_list[-1] - idx_list[0]
    else:
        answer += min_answer

    return answer
