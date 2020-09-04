# 비밀지도
# https://programmers.co.kr/learn/courses/30/lessons/17681
def fill_map(n, arr, secret_map):
    for row in range(n):
        num = arr[row]
        for col in range(n-1, -1, -1):
            digit = num % 2
            num //= 2
            if digit == 0:
                if secret_map[row][col] != '#':
                    secret_map[row][col] = ' '
            else:
                secret_map[row][col] = '#'

def solution(n, arr1, arr2):
    secret_map = [['' for x in range(n)] for y in range(n)]
    answer = []
    fill_map(n, arr1, secret_map)
    fill_map(n, arr2, secret_map)
    for row in secret_map:
        answer.append(''.join(row))
    return answer