# https://programmers.co.kr/learn/courses/30/lessons/12987

import heapq

def solution(A, B):
    B.sort()
    heapq.heapify(A)
    answer = 0

    for i, b in enumerate(B):
        if b > A[0]:
            heapq.heappop(A)
            answer += 1


    return answer
