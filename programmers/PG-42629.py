# https://programmers.co.kr/learn/courses/30/lessons/42629

import heapq

def solution(stock, dates, supplies, k):    
    h = []
    dates_len = len(dates)
    idx = 0
    answer = 0
    
    # if stock >= k, supply completed successfully
    while stock < k:
        for i in range(idx, dates_len):
            # push supplies to Heap until stocks run out
            if stock >= dates[i]:
                heapq.heappush(h, (-supplies[i], supplies[i]))
                idx = i+1
            # out of stock expected on the date
            else:
                break
        # supply as needed
        stock += heapq.heappop(h)[1]
        answer += 1
    
    return answer
