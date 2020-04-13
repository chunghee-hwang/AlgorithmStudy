# def solution(cacheSize, cities):
#     answer = 0
#     cache = {}
#     time = 0
#     if cacheSize == 0:
#         return len(cities) * 5
#     for city in cities:
#         city = city.lower()
#         if city in cache:
#             answer += 1
#             cache[city] = time
#         else:
#             if cache and len(cache) == cacheSize:
#                 items = cache.items()
#                 min_item = min(items, key=lambda x: x[1])
#                 del cache[min_item[0]]
#             cache[city] = time
#             answer += 5
#         time += 1
#     return answer

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque(maxlen=cacheSize)  # maxlen 지정: 큐가 꽉 차면 자동으로 맨 앞의 원소에 append 한다.
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            cache.append(city)
            answer += 5
    return answer


if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
