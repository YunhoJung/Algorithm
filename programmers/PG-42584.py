# https://programmers.co.kr/learn/courses/30/lessons/42584

# stack
def solution1(prices):
    stack = [] # [idx, price]
    answer = [0 for _ in range(len(prices))]
    idx = 0
    for price in prices:

        while stack and (stack[-1][1] > price):
            previous_high = stack.pop()
            answer[previous_high[0]] = idx - previous_high[0]

        else:
            stack.append([idx, price])

        idx += 1

    idx -= 1
    while stack:
        previous_high = stack.pop()
        answer[previous_high[0]] = idx - previous_high[0]

    return answer


# two pointers
def solution2(prices):
    answer = []
    for i, price in enumerate(prices):
        count = 0
        pos = i
        while pos < len(prices) and price <= prices[pos]:
            pos += 1
            if pos < len(prices):
                count += 1



        answer.append(count)

    return answer

# queue
from collections import deque
def solution3(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer
