# 다음 큰 숫자
# https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    n_count_one = bin(n).count('1')
    next_n = n
    while True:
        next_n+=1
        binary = bin(next_n)
        if n_count_one == binary.count('1'):
            return next_n