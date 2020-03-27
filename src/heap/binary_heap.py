# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
import heapq

mode_min = -1  # 최소 큐 모드
mode_max = 1  # 최대 큐 모드
heap_mode = mode_min


# 최소 큐는 최대 큐로, 최대 큐는 최소 큐로 바꾸는 함수
def switch_heap_to_max_or_min(heap, mode):
    global heap_mode
    if heap_mode == mode:
        return
    for elem in heap:
        elem[0] *= -1
    heapq.heapify(heap)
    heap_mode = mode


def solution(operations):
    global heap_mode, mode_min, mode_max
    binary_heap = []
    for operation in operations:
        c1, c2 = operation.split()
        c2 = int(c2)
        if c1 == 'I':
            if heap_mode == mode_min:
                heapq.heappush(binary_heap, [c2, c2])
            elif heap_mode == mode_max:
                heapq.heappush(binary_heap, [-c2, c2])
        elif c1 == 'D':
            if binary_heap:  # 큐가 차 있을 때
                switch_heap_to_max_or_min(binary_heap, c2)
                heapq.heappop(binary_heap)

    if not binary_heap:  # 큐가 비어있을 때
        return [0, 0]
    else:
        switch_heap_to_max_or_min(binary_heap, mode_max)
        max_value = binary_heap[0][1]
        switch_heap_to_max_or_min(binary_heap, mode_min)
        min_value = binary_heap[0][1]
        return [max_value, min_value]


if __name__ == '__main__':
    print(solution(["I 16", "D 1"]))
    print(solution(["I 7", "I 5", "I -5", "D -1"]))
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
    print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
