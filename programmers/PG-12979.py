# https://programmers.co.kr/learn/courses/30/lessons/12979

from collections import deque

def solution(n, stations, w):
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
