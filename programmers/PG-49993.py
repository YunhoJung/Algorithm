# https://programmers.co.kr/learn/courses/30/lessons/49993

def solution1(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        flag = 0
        idx = 0

        for s in skill_tree:
            if s in skill:
                if s == skill[idx]:
                    idx += 1
                else:
                    flag = 1
                    break

        if flag == 0:
            answer += 1

def solution2(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx =0

        for s in skill_tree:
            if s in skill:
                if s == skill[idx]:
                    idx += 1
                else:
                    break
        else:
            answer += 1

    return answer

from collections import deque()


def solution3(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_list = deque(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.popleft():
                    break
        else:
            answer += 1

    return answer
