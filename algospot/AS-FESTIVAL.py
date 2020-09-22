# https://algospot.com/judge/problem/read/FESTIVAL

import sys

input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N, L = map(int, input().split())
    cost = list(map(int, input().split()))
    avg = sys.maxsize
    for i in range(N-L+1):
        sub_sum = sum(cost[i:i+L])
        if (sub_sum / L) < avg:
            avg = sub_sum / L

        for j in range(N-L-i):
            sub_sum += cost[i+L+j]
            if (sub_sum / (L+j+1)) < avg:
                avg = (sub_sum / (L+j+1))
    print("%.11f"%avg)
