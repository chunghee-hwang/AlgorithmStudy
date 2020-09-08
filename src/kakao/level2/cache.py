# 캐시
# https://programmers.co.kr/learn/courses/30/lessons/17680
# https://jins-dev.tistory.com/entry/LRU-Cache-Algorithm-%EC%A0%95%EB%A6%AC
from collections import defaultdict

def solution(cache_size, cities):
    answer = 0
    cache_hit_time = 1
    cache_miss_time = 5
    cache_map = defaultdict(bool)
    cache = []
    for city in cities:
        city = city.lower()
        if not cache_map[city]:
            if cache_size != 0:
                if len(cache) == cache_size:
                    cache_map[cache.pop(0)] = False
                cache.append(city)
                cache_map[city] = True
            answer+=cache_miss_time
        else:
            cache.append(cache.pop(cache.index(city)))
            answer+=cache_hit_time
    return answer