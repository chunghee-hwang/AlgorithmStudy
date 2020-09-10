# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059
# 참고 사이트: https://medium.com/@dltkddud4403/2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EB%B8%94%EB%9D%BC%EC%9D%B8%EB%93%9C-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%AC%BC%EC%87%A0%EC%99%80-%EC%97%B4%EC%87%A0-47c2846da576

import copy

# 키를 오른쪽으로 90도 회전
def rotate_key_right(key):
    row_index = 0
    column_size = len(key[0])
    row_size = len(key)
    return [[key[row_index][column_index] for row_index in range(row_size-1, -1, -1)] for column_index in range(column_size)]

# 키와 자물쇠를 더한 배열의 padding을 제외한 값들이 모두 1인지 확인 ==> 자물쇠 열림
def is_open(lock_with_key, m, k):
    for y in range(m-1, k-m+1):
        for x in range(m-1, k-m+1):
            if lock_with_key[y][x] != 1:
                return False
    return True

def solution(key, lock):
    answer = True
    m = len(key) # 키 가로 세로 길이
    n = len(lock) # 원본 자물쇠 가로 세로 길이
    k = n + (m-1)*2 # padding을 추가한 자물쇠의 가로 세로 길이

    # 자물쇠의 모든 변에 m-1만큼 padding 추가(원할한 윈도우 탐색을 위해)
    new_lock = [[0 for x in range(k)] for y in range(k)]
    for y in range(m-1, k-m+1):
        for x in range(m-1, k-m+1):
            new_lock[y][x] = lock[y-m+1][x-m+1]
    lock = new_lock

    y = 0; x = 0
    rotate_count = 0 # 자물쇠 오른쪽으로 돌린 횟수

    # 0도, 90도, 180도, 270도로 돌린 열쇠를 가지고 열쇠가 자물쇠에 맞는지 완전탐색
    while rotate_count < 4:
        key_row_idx = 0
        lock_with_key = copy.deepcopy(lock)
        for row_idx in range(y, y+m):
            key_column_idx=0
            for column_idx in range(x, x+m):
                # 열쇠와 자물쇠의 값을 더함. 더한 값이 1이면 홈에 맞는 거
                lock_with_key[row_idx][column_idx] = lock_with_key[row_idx][column_idx] + key[key_row_idx][key_column_idx]
                key_column_idx+=1
            key_row_idx+=1
        if is_open(lock_with_key, m, k):
            return True
        x +=1

        # 맨 오른쪽 탐색을 완료하면, 키 맨 왼쪽으로 다시 이동하고 아래로 한 칸 이동
        if x > k - m:
            x = 0
            y+=1
        
        # 오른쪽 대각선 끝까지 탐색을 완료하면 키를 왼쪽 대각선 끝으로 이동하고 키 오른쪽으로 회전.
        if y > k - m:
            x = 0
            y = 0
            key = rotate_key_right(key)
            rotate_count+=1
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))