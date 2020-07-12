# https://programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    tmp = sorted(numbers)
    if (tmp[0]) == 0 and (tmp[-1] == 0):
        return '0'

    answer = []

    for number in numbers:
        original = str(number)
        compare_number = list(str(number))
        digit_len = len(original)

        idx = 0
        while len(compare_number) <= 4:
            compare_number.append(original[idx%digit_len])
            idx += 1

        compare_number = int(''.join(compare_number))
        answer.append([compare_number, original])

    answer = sorted(answer, key=lambda x:x[0], reverse=True)


    return ''.join([item[1] for item in answer])
