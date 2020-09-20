# 점프와 순간이동
# https://programmers.co.kr/learn/courses/30/lessons/12980
def solution(n):
    ans = 0
    while n > 0:
        divided_by_two = n>>1
        if n == divided_by_two<<1: # 짝수면 n = n/2
            n = divided_by_two
        else: # 홀수면 n = n-1, answer+=1
            n-=1
            ans+=1
    return ans