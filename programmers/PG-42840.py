# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    scores = {1:0, 2:0, 3:0}

    for i, ans in enumerate(answers):
        if student1[i%(len(student1))] == ans: scores[1]+=1
        if student2[i%(len(student2))] == ans: scores[2]+=1
        if student3[i%(len(student3))] == ans: scores[3]+=1
    MAX = max(scores.values())
    answer = []

    for i, score in scores.items():
        if score == MAX:
            answer.append(i)

    return answer
