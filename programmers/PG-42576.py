# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution1(participant, completion):
    answer = ''
    p_dict = {}
    for p in participant:
        if p not in p_dict:
            p_dict[p]=1
        else:
            p_dict[p]+=1
    c_dict = {}
    for c in completion:
        if c not in c_dict:
            c_dict[c]=1
        else:
            c_dict[c]+=1
    for key, value in p_dict.items():
        if (key not in c_dict) or (c_dict[key]!=value):
            answer = key

    return answer

def solution2(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
