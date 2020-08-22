# https://www.acmicpc.net/problem/1927

import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
    # min heap
    N = int(input())
    min_heap = []
    for _ in range(N):
        operation = int(input())
        
        if operation == 0:
            if min_heap:
                print(heapq.heappop(min_heap))
            else:
                print(0)
        elif operation > 0:
            heapq.heappush(min_heap, operation)
