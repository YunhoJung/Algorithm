# https://www.acmicpc.net/problem/14425

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# make a trie
trie = {}
for _ in range(N):
    string = input().strip()
    head = trie

    for ch in string:
        if ch not in head:
            head[ch] = {}
        head = head[ch]
    head['*'] = string

# match
cnt = 0
for _ in range(M):
    pattern = input().strip()
    head = trie

    for ch in pattern:
        if ch not in head:
            break
        head = head[ch]

    if '*' in head and head['*'] == pattern:
        cnt += 1
print(cnt)
