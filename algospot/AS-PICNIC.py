# https://algospot.com/judge/problem/read/PICNIC

import sys

input = sys.stdin.readline


def dfs(friend, friends_number):
    if not friends_number:
        return 1

    answer = 0

    for i in range(friend, N):
        if not visited[i]:
            for j in range(i + 1, N):
                if not visited[j] and is_friend[i][j]:
                    visited[i] = True
                    visited[j] = True
                    answer += dfs(i, friends_number - 2)
                    visited[i] = False
                    visited[j] = False

    return answer


C = int(input())

for _ in range(C):
    N, M = map(int, input().split())
    visited = [False] * N
    is_friend = [[False] * N for _ in range(N)]
    friends = list(map(int, input().split()))

    for i in range(0, len(friends), 2):
        is_friend[friends[i]][friends[i+1]] = True
        is_friend[friends[i+1]][friends[i]] = True
    print(dfs(0, N))
