# https://programmers.co.kr/learn/courses/30/lessons/42886



def solution1(weight):
    weight.sort()
    answer = weight[0]
    if answer > 1:
        return 1

    for i in range(1, len(weight)):
        if answer + 1 < weight[i]:
            break
        else:
            answer += weight[i]
    return answer + 1


def solution2(weight):
    weight.sort()
    ans = 1
    for e in weight:
        if ans < e:
            break
        ans += e

    return ans

