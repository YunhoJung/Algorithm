# https://programmers.co.kr/learn/courses/30/lessons/17678

def solution(n, t, m, timetable):
    timetable_int = list(map(lambda time: int(''.join(time.split(':'))), timetable))
    timetable_int.sort()

    bus_timetable = []
    bus = 900
    for i in range(n):
        bus_timetable.append([bus, m])
        next_bus = t if t // 60 == 0 else 100
        bus += next_bus

    idx = 0
    crews = len(timetable)
    for bus_item in bus_timetable:
        while idx < crews and bus_item[0] >= timetable_int[idx]:
            if timetable_int[idx] <= bus_item[0] and bus_item[1] > 0:
                idx += 1
                bus_item[1] -= 1
            else:
                break
        if bus_item[1] > 0:
            answer = bus_item[0]
        else:
            if timetable_int[idx-1] % 100 == 0:
                answer = timetable_int[idx-1] - 41
            else:
                answer = timetable_int[idx-1] - 1

    answer = str(answer)
    if len(answer) == 3:
        answer = '0' + answer[0] + ':' + answer[1:]
    elif len(answer) == 4:
        answer = answer[:2] + ':' + answer[2:]
    else:
        answer = '00:00'

    return answer
