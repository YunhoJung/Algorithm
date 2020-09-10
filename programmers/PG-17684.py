# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    word_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    word_dict = {word:i for word, i in zip(word_list, range(1,len(word_list)+1))}

    answer = []
    cnt = 26
    current_input = msg[0]
    idx = 1
    while idx < len(msg):
        if current_input + msg[idx] not in word_dict:
            answer.append(word_dict[current_input])

            cnt += 1
            word_dict[current_input + msg[idx]] = cnt

            current_input = msg[idx]

            idx += 1
            continue
        current_input += msg[idx]
        idx += 1

    answer.append(word_dict[current_input])
    return answer
