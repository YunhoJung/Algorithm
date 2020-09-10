# https://programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    cache = []
    cities = list(map(lambda x:x.lower(),cities))
    answer = 0

    for city in cities:
        if city not in cache:
            answer += 5
            cache.append(city)

            if len(cache) > cacheSize:
                cache.pop(0)
        else:
            answer += 1
            cache.pop(cache.index(city))
            cache.append(city)

    return answer
