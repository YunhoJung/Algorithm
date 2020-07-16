# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort()
    max_h_idx = len(citations)

    for idx, q in enumerate(citations):

        if q >= max_h_idx - idx:
            return max_h_idx - idx

    return 0
