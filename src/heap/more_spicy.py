# https://programmers.co.kr/learn/courses/30/lessons/42626?language=python3
import heapq


def solution(scoville, K):
    mix_count = 0
    heapq.heapify(scoville)
    while scoville[0] < K and len(scoville) > 1:
        sco1 = heapq.heappop(scoville)
        sco2 = heapq.heappop(scoville)
        heapq.heappush(scoville, sco1 + (sco2 * 2))
        mix_count += 1

    if scoville[0] < K:
        return -1
    return mix_count


if __name__ == '__main__':
    print(solution([12, 10, 3, 1, 2, 9], 7))
