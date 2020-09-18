# https://programmers.co.kr/learn/courses/30/lessons/17677

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_tokenized = {}
    str2_tokenized = {}
    for i in range(len(str1)-1):
        token = str1[i:i+2]
        if token.isalpha():
            if token not in str1_tokenized:
                str1_tokenized[token] = 1
            else:
                str1_tokenized[token] += 1
    for i in range(len(str2)-1):
        token = str2[i:i+2]
        if token.isalpha():
            if token not in str2_tokenized:
                str2_tokenized[token] = 1
            else:
                str2_tokenized[token] += 1
    if not str1_tokenized and not str2_tokenized:
        return 1*65536

    union_set = set(str1_tokenized.keys())
    union_set.update(set(str2_tokenized.keys()))

    union = 0
    intersection = 0
    for element in union_set:
        if element in str1_tokenized and element in str2_tokenized:
            union += max(str1_tokenized[element], str2_tokenized[element])
            intersection += min(str1_tokenized[element], str2_tokenized[element])
        elif element not in str1_tokenized and element in str2_tokenized:
            union += str2_tokenized[element]
        elif element not in str2_tokenized and element in str1_tokenized:
            union += str1_tokenized[element]

    answer = int(intersection / union * 65536)
    return answer
