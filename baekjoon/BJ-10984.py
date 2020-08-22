# https://www.acmicpc.net/problem/10984
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    
    for _ in range(T):
        N = int(input())
        
        total_c = 0
        total_g = 0
        for _ in range(N):
            C, G = map(float, input().split())
            total_c += C
            total_g += C*G
        GPA = round(total_g/total_c,1)
        print(int(total_c), GPA)
