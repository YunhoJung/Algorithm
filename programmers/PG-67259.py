# https://programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

def solution(board):
    N = len(board) # constant
    dx, dy = [-1,0,1,0], [0,-1,0,1] # for directions
    q = deque([(0,0,-1,0)]) # (x_index, y_index, direction, cost)
    distance = [[float('inf')]*N for _ in range(N)] # keep updating distance
    distance[0][0] = 0 # init

    while q:
        x, y, d, cost = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # if able to go
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0:
                new_cost = cost
                if d == -1: # for init
                    new_cost += 100
                elif (d+i)%2 == 0: # for straight roads
                    new_cost += 100
                else: # for corners
                    new_cost += 600

                # if find out the cheaper path
                if new_cost <= distance[nx][ny]: # enough condition - no variables such as visited needed
                    distance[nx][ny] = new_cost
                    q.append((nx,ny,i,new_cost))

    answer = distance[N-1][N-1]
    return answer
