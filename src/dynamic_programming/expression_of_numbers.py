# 숫자의 표현
# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    dp = list(range(0, n+1))
    # 누적합 배열 구하기
    for num in range(1, n+1):
        dp[num] = dp[num-1] + dp[num]

    # 범위 합을 구해서 합이 n 이상이면 break.
    # 합이 n이면 answer += 1
    for idx1 in range(1,n+1):
        for idx2 in range(idx1, n+1):
            dp_sum = dp[idx2] - dp[idx1-1]
            if dp_sum >= n:
                if dp_sum == n:
                    answer+=1
                break
    return answer