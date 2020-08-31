# https://www.acmicpc.net/problem/5670

import sys

input = sys.stdin.readline

while True:
    try:
        N = int(input())
    except:
        break

    # make a trie
    trie = {}
    word_list = []
    for _ in range(N):
        word = input().strip()
        word_list.append(word)
        head = trie

        for ch in word:
            if ch not in head:
                head[ch] = {}
            head = head[ch]
        head['*'] = word

    # the count number of pressed button
    cnt = 0
    for wrd in word_list:
        head = trie
        cnt += 1 # init count
        idx = 0
        length = len(wrd)
        for ch in wrd:
            idx += 1
            if idx != length and len(head[ch]) > 1:
                cnt += 1
            head = head[ch]

    # the averge of the count number
    average = cnt/N
    print("{0:0.2f}".format(average))
