# https://www.acmicpc.net/problem/2470

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    solution_list = list(map(int,input().split()))
    solution_list.sort()
    min_value = sys.maxsize
    left = 0
    right = N-1
    
    while(left<right):
        tmp = solution_list[left]+solution_list[right]
        if abs(tmp) < min_value:
            min_value = abs(tmp)
            min_pair = (solution_list[left], solution_list[right])
        if tmp >= 0:
            right -= 1
        else:
            left += 1
    
    print(min_pair[0], min_pair[1])
