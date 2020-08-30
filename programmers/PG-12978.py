# https://programmers.co.kr/learn/courses/30/lessons/12978

from collections import deque
import heapq
import sys

def solution(N, road, K):
    graph = {}
    for edge in road:
        v1, v2, cost = edge
        if v1 not in graph:
            graph[v1] = [[v2, cost]]
        else:
            graph[v1].append([v2, cost])
        if v2 not in graph:
            graph[v2] = [[v1, cost]]
        else:
            graph[v2].append([v1, cost])
    
    queue = deque([1])
    visited = [False] * (N+1)
    dist = [sys.maxsize] * (N+1)
    dist[1] = 0
    visited[1] = True
    
    while queue:
        cur_node = queue.popleft()

        for edge in graph[cur_node]:
            next_node, next_cost = edge
            # first visit
            if visited[next_node] == False:
                visited[next_node] = True
                dist[next_node] = dist[cur_node] + next_cost
                queue.append(next_node)
            # not first visit, but lower cost
            elif dist[cur_node] + next_cost < dist[next_node]:
                dist[next_node] = dist[cur_node] + next_cost
                queue.append(next_node)

    answer = 0
    for distance in dist:
        if distance <= K:
            answer += 1

    return answer
