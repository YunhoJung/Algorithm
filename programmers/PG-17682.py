# https://programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    stack = []
    result = []

    for ch in dartResult:
        if ch.isdigit():
            stack.append(int(ch))
        elif ch == 'S':
            value = stack.pop()
            if stack and stack[-1] == 1:
                stack.pop()
                value = 10
            result.append(value**1)
        elif ch == 'D':
            value = stack.pop()
            if stack and stack[-1] == 1:
                stack.pop()
                value = 10
            result.append(value**2)
        elif ch == 'T':
            value = stack.pop()
            if stack and stack[-1] == 1:
                stack.pop()
                value = 10
            result.append(value**3)
        elif ch == '*':
            if len(result) >= 2:
                result[-2] *= 2
            result[-1] *= 2
        elif ch == '#':
            result[-1] *= -1

    answer = sum(result)
    return answer
