# 가장 큰 정사각형
# https://programmers.co.kr/learn/courses/30/lessons/12905?language=python3
# https://minnnne.tistory.com/16

def solution(board):
    dp = [row for row in board]
    max_length = 0
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if x ==0 or y == 0:
                if col == 1:
                    max_length = max(max_length, 1)
                continue
            if col == 1:
                min_length_buffer = []
                if y-1>-1 and x-1>-1:
                    min_length_buffer.append(dp[y-1][x-1])
                if y-1>-1:
                    min_length_buffer.append(dp[y-1][x])
                if x-1>-1:
                    min_length_buffer.append(dp[y][x-1])
                dp[y][x] = min(min_length_buffer)+1
                max_length = max(dp[y][x], max_length)
    return max_length**2


solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]])