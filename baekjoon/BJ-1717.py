# https://www.acmicpc.net/problem/1717

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

    if a==b:
        return True
    else:
        return False


N, M = map(int, input().split())
parent = [i for i in range(N+1)]

for _ in range(M):
    operation, a, b = map(int, input().split())

    if operation == 0:
        union_parent(parent, a, b)

    elif operation == 1:
        if find_parent(parent, a, b):
            print("YES")
        else:
            print("NO")
