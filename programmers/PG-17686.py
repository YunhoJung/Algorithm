# https://programmers.co.kr/learn/courses/30/lessons/17686
import re

def solution1(files):
    tmp = [re.split(r"([0-9]+)", s) for s in files]

    sort = sorted(tmp, key=lambda x:(x[0].lower(),int(x[1])))

    return ["".join(s) for s in sort]

def solution2(files):    
    files_sort = []

    for file in files:
        HEAD, NUMBER , TAIL, integer_str = '', 0, '', ''
        int_cnt, nonzero_cnt, tail_cnt = 0, 0, 0
        
        for ch in file:
            try:
                integer = int(ch)
                int_cnt += 1
                
                if integer > 0:
                    nonzero_cnt += 1
                
                if tail_cnt == 0:
                    if nonzero_cnt == 0:
                        continue
                    elif nonzero_cnt > 0:
                        integer_str += ch
                else:
                    TAIL += ch
            except:
                if int_cnt == 0:
                    HEAD += ch.lower()
                else:
                    tail_cnt += 1
                    TAIL += ch
        if integer_str == '':
            integer_str = '0'
        NUMBER = int(integer_str)
        files_sort.append((HEAD, NUMBER, TAIL, file))
        
    files_sort.sort(key=lambda x:(x[0], x[1]))
    answer = [file[3] for file in files_sort]
    
    return answer
