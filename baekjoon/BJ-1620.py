# https://www.acmicpc.net/problem/1620

import sys

input = sys.stdin.readline

if __name__ == '__main__':
    N, M = map(int, input().split())
    
    pokemons = []
    name_to_number = {}
    number_to_name = {}
    
    for n in range(1,N+1):
        pokemon = input().strip()
        name_to_number[pokemon] = n
        number_to_name[n] = pokemon
        
    for _ in range(M):
        question = input().strip()            
        asc = ord(question[0])

        if asc >= 65 and asc <= 90:
            answer = name_to_number[question]
        else:
            answer = number_to_name[int(question)]
        print(answer)
