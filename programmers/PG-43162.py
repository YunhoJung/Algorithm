# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    visited = [False for _ in range(n)]
    q = deque([])
    answer = 0

    for i in range(n):
        if visited[i] == False:
            visited[i] = True
            q.append(i)
            answer += 1

        while q:
            cur = q.popleft()

            for node, connection in enumerate(computers[cur]):
                if node != cur and connection == 1 and visited[node] == False:
                    visited[node] = True
                    q.append(node)

    return answer
