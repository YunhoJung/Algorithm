# https://programmers.co.kr/learn/courses/30/lessons/42585

def solution1(arrangement):
    # stack = [[idx, '(']]
    stack = []
    stack_len = 0
    answer = 0
    flag = 0
    # flag = 1 and c_i == ')' -> razor
    # flag = 0 and c_i == ')' -> end
    for idx_i, c_i in enumerate(arrangement):
        if c_i == '(':
            stack.append([idx_i, c_i])
            flag = 1
            stack_len += 1
        elif c_i == ')' and flag == 0:
            stack.pop()
            stack_len -= 1
            answer += 1
        else:
            stack.pop()
            stack_len -= 1
            answer += stack_len
            flag = 0

    return answer

def solution2(arrangement):
    answer = 0
    sticks = 0
    rasor_to_zero = arrangement.replace('()','0')

    for i in rasor_to_zero:
        if i == '(':
            sticks += 1
        elif i =='0' :
            answer += sticks
        else :
            sticks -= 1
            answer += 1

    return answer
