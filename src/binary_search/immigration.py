# 입국 심사
# https://programmers.co.kr/learn/courses/30/lessons/43238
# 참고 사이트: https://woongsin94.tistory.com/185

def solution(n, times):
    left = 1
    right = max(times)*n
    while left <= right:
        mid = (left + right) // 2
        if sum([int(mid/time) for time in times]) >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left