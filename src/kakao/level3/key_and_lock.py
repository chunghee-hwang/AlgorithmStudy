# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

# 2차원 배열을 시계방향으로 90도 회전
def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = matrix[i][j]
    return result

# 길이가 3배로 늘어난 자물쇠 배열의 정 중앙이 모두 1인지 확인
def is_open(new_lock, n, m):
    for y in range(n):
        for x in range(m):
            if new_lock[y+n][x+m] != 1:
                return False
    return True
        
def solution(key, lock):
    n = len(lock) # 자물쇠 가로 길이
    m = len(lock[0]) # 자물쇠 세로 길이
    new_lock = [[0]*(m*3) for _ in range(n*3)] # 키를 옮기기 싶게 자물쇠 배열을 3배(padding)로 늘림
    for y in range(n):
        for x in range(m):
            new_lock[y+n][x+m] = lock[y][x]
    for _ in range(4): # 0, 90, 180, 270도 회전
        kn = len(key) # 키 가로 길이
        km = len(key[0]) # 키 세로 길이
        # 키 배열를 움직이는 원점 기준 offset
        for yoffset in range(n*2+1):
            for xoffset in range(m*2+1):
                # 먼저 키를 자물쇠 배열에 모두 더함
                for y in range(kn):
                    for x in range(km):
                        new_lock[y+yoffset][x+xoffset]+=key[y][x]
                # 정 중앙에 있는 자물쇠 부분이 모두 1이면 열림 처리
                if is_open(new_lock, n, m):
                    return True
                # 자물쇠에서 키를 뺌
                for y in range(kn):
                    for x in range(km):
                        new_lock[y+yoffset][x+xoffset]-=key[y][x]
        # 키 시계방향으로 90도 회전
        key= rotate_matrix(key)
    
    # 모든 경우의 수를 해봐도 안 열리면 False 반환
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))