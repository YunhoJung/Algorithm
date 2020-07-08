# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    students = [0] * n

    for idx in lost:
        students[idx-1] -= 1
    for idx in reserve:
        students[idx-1] += 1

    for i in range(n):
        if (i-1>=0) and (i+2<=n) and students[i] == 1:
            if students[i-1] == -1:
                students[i-1] += 1
                students[i] -= 1
            elif students[i+1] == -1:
                students[i+1] += 1
                students[i] -= 1
        elif i==0 and students[i] == 1:
            if students[i+1] == -1:
                students[i+1] += 1
                students[i] -= 1
        elif i==n-1 and students[i] == 1:
            if students[i-1] == -1:
                students[i-1] +=1
                students[i] -= 1

    answer = 0
    for status in students:
        if status >= 0:
            answer += 1
    return answer
