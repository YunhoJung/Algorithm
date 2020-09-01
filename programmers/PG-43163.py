# https://programmers.co.kr/learn/courses/30/lessons/43163

import sys

def solution(begin, target, words):
    stack = [[begin,0]]
    visited_list = [False]*len(words)
    visited = {key:value for key, value in zip(words, visited_list)}
    answer = sys.maxsize

    while stack:
        current, cnt = stack.pop()

        # answer condition
        if current == target and cnt < answer:
            answer = cnt

        for word in words:
            if visited[word] == False:
                match = 0
                for ch1, ch2 in zip(word, current):# all words same length
                    if ch1 == ch2:
                        match +=1

                if match==(len(word)-1):
                    visited[word] = True
                    stack.append([word,cnt+1])

    if answer == sys.maxsize:
        return 0
    return answer

