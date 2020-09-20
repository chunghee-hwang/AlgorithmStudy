# 예상 대진표
# https://programmers.co.kr/learn/courses/30/lessons/12985
def solution(n,a,b):
    answer = 0
    while a!=b:
        if a == (a >> 1 << 1):
            a>>=1
        else:
            a = (a+1)>>1
        if b == (b >> 1 << 1):
            b>>=1
        else:
            b = (b+1)>>1
        answer+=1
    return answer