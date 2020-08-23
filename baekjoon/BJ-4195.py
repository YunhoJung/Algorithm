# https://www.acmicpc.net/problem/4195

import sys

input = sys.stdin.readline

def get_parent(parent, friend):
    if parent[friend][0] == friend:
        return friend
    return get_parent(parent, parent[friend][0])

def union_parent(parent, friend1, friend2):
    a = get_parent(parent, friend1)
    b = get_parent(parent, friend2)

    if a < b:
        parent[a][1] += parent[b][1]
        parent[b][0] = a

    elif b < a:
        parent[b][1] += parent[a][1]
        parent[a][0] = b

T = int(input())

for _ in range(T):
    F = int(input())
    friendship = {}
    for _ in range(F):
        friend1, friend2 = input().strip().split()
    
        if friend1 not in friendship:
                friendship[friend1] = [friend1,1]
        if friend2 not in friendship:
                friendship[friend2] = [friend2,1]

        union_parent(friendship, friend1, friend2)
        if friend1 < friend2:
            parent_friend = get_parent(friendship, friend1)
        else:
            parent_friend = get_parent(friendship, friend2)
        print(friendship[parent_friend][1])

