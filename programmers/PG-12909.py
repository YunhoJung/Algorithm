# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    # during for loop, ')' comes and stack is empty -> False
    # after for loop, len(stack) != 0 -> False
    answer = True
    stack = []
    for ch in s:
        if not stack and ch == ')':
            answer = False
            break

        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            stack.pop()

    if len(stack) != 0:
        answer = False
    return answer
