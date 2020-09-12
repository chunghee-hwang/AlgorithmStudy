# 징검 다리
# https://programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    n = len(stones)
    # 1 에서 stone 요소의 최대값 까지의 값들을 모두 뺀 뒤, 연속되는 0이 k 이상일 때를 찾아야한다.
    # 1~최대값까지 모두 빼기에는 시간이 많이 소모되므로
    # 이분탐색을 활용한다.
    # 이분탐색 시 빼는 값을 범위(left, right, mid)로 정한다.
    left = 1; right = max(stones)
    while left<=right:
        mid = (left + right) // 2
        zero_combo = 0
        is_over_k = False
        for stone in stones:
            if stone - mid <= 0:
                zero_combo+=1
            else:
                zero_combo=0
            if zero_combo >= k:
                is_over_k = True
                break
        if is_over_k:
            right = mid - 1
        else:
            left = mid + 1
    return left

print(solution([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 5))