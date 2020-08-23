# https://www.acmicpc.net/problem/1976

import sys

input = sys.stdin.readline

def get_parent(parent, num):
    if parent[num] == num:
        return num
    return get_parent(parent, parent[num])

def union_parent(parent, num1, num2):
    a = get_parent(parent, num1)
    b = get_parent(parent, num2)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find_parent(parent, num1, num2):
    a = get_parent(parent, num1)
    b = get_parent(parent, num2)

    if a == b:
        return True
    else:
        return False


N = int(input()) 
M = int(input()) 

cities = []
parent = [i for i in range(N+1)]

for _ in range(N):
    connection = list(map(int,input().split()))
    cities.append(connection)


path = list(map(int,input().split()))

# union
for i in range(N):
    for j in range(i,N):
        if cities[i][j]==1:
            union_parent(parent, i+1, j+1)

mask = False
for i in range(M-1):
    if find_parent(parent, path[i], path[i+1]):
        mask = True
    else:
        mask = False
        break
if mask:
    print("YES")
else:
    print("NO")
