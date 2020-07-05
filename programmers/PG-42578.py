# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution1(clothes):
    clothes_dict = {}
    for c in clothes:
        if c[1] in clothes_dict:
            clothes_dict[c[1]] += 1
        else:
            clothes_dict[c[1]] = 1
    answer = 1
    for cnt in clothes_dict.values():
        answer *= cnt+1
    return answer-1

def solution2(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1

    cnt = 1
    for i in answer.values():
        cnt *= (i+1)
    return cnt - 1
