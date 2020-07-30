# https://programmers.co.kr/learn/courses/30/lessons/12979

from collections import deque

def solution1(n, stations, w): # only 13 test case failed
    if n == 1 and len(stations) > 0:
        return 0
    q = deque([]) # [[start, end]]
    for station in stations:
        start = station - w
        end = station + w
        q.append([start, end])

    apt = 1
    answer = 0
    while apt < n and q:
        if apt < q[0][0]:
            station_needed = (q[0][0] - apt) // (2*w + 1)
            station_needed = station_needed if (q[0][0] - apt) % (2*w + 1) == 0 else station_needed + 1
            answer += station_needed
            apt = q[0][1] + 1
            q.popleft()
        else:
            apt = q[0][1] + 1
            q.popleft()

    if apt <= n and not q:
        station_needed = (n+1 - apt) // (2*w + 1)
        station_needed = station_needed if (n+1 - apt) % (2*w + 1) == 0 else station_needed + 1
        answer += station_needed

    return answer

def solution2(n, stations, w):
    answer = 0
    start = 1
    for station in stations:
        left = station - w - 1
        right = station + w + 1

        if start <= left:
            not_covered = left - start + 1
            station_needed = not_covered // (2*w + 1)
            station_needed = station_needed if not_covered % (2*w + 1) == 0 else station_needed + 1
            answer += station_needed
        start = right

    if start <= n:
        not_covered = n + 1 - start
        station_needed = not_covered // (2*w + 1)
        station_needed = station_needed if not_covered % (2*w + 1) == 0 else station_needed + 1
        answer += station_needed

    return answer
