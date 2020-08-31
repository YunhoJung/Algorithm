# https://www.acmicpc.net/problem/5052

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    # make a trie & search prefix
    trie = {}
    answer = 'YES'
    for _ in range(N):
        phone = input().strip()
        head = trie

        for ch in phone:
            if ch not in head:
                if '*' in head: # phone includes prefix
                    answer = 'NO'
                head[ch] = {}
            head = head[ch]
        if head: # phone is prefix
            answer = 'NO'
        head['*'] = phone
    print(answer)
