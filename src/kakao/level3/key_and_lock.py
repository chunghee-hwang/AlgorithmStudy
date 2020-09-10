# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotate_key_right(key):
    row_index = 0
    column_size = len(key[0])
    row_size = len(key)
    return [[key[row_index][column_index] for row_index in range(row_size-1, -1, -1)] for column_index in range(column_size)]

def solution(key, lock):
    answer = True
    m = len(key)
    n = len(lock)
    k = n + (m-1)*2
    new_lock = [[0 for x in range(k)] for y in range(k)]
    for y in range(m-1, k-m+1):
        for x in range(m-1, k-m+1):
            new_lock[y][x] = lock[y-m+1][x-m+1]
    y = 0; x = 0
    while True:
        print('y:',y, 'x:',x)
        for row_idx in range(y, y+m):
            key_matched = True
            for column_idx in range(x, x+m):
                if key[row_idx%m][column_idx%m] != new_lock[row_idx][column_idx%m]:
                    key_matched = False
                    break
            if key_matched:
                return True
        x +=1
        if x > k - m:
            x = 0
            y+=1
        if y > k - m:
            break
        
        
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))