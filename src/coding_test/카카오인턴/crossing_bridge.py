# https://programmers.co.kr/learn/courses/30/lessons/64062
# 다른 사람이 품
# 이분 탐색 적용?
def can_pass(stones, k, h):
    zero_count = 0
    for i in range(len(stones)):
        y = max(0, stones[i] - h + 1)
        if y == 0:
            zero_count += 1
        else:
            zero_count = 0

        if zero_count >= k:
            return False

    return True

def solution(stones, k):
    low, high = 0, 200_000_001

    while low + 1 < high:
        mid = (low + high) // 2
        if can_pass(stones, k, mid):
            low = mid
        else:
            high = mid

    return low
if __name__ == '__main__':
    print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
    print(solution([0, 0, 0, 0, 0, 0, 0], 3))
