# 등굣길
# https://programmers.co.kr/learn/courses/30/lessons/42898
# 참고 사이트: https://velog.io/@ajufresh/%EB%93%B1%EA%B5%A3%EA%B8%B8

from collections import defaultdict
def iterateidx(y,x, m):
    x+=1
    if x == m:
        x = 0
        y += 1
    return (y,x)

def solution(m, n, puddles):
    answer = 0
    puddledict = defaultdict(bool)
    dp = [[0 for x in range(m)] for y in range(n)]
    dp[0][0]=1 
    for puddle in puddles:
        puddledict[(puddle[1]-1,puddle[0]-1)] = True
    x = y = 0
    while y != n:
        if x == y == 0:
            y,x = iterateidx(y,x,m)
            continue
        if not puddledict[(y,x)]:
            if y-1<0 or puddledict[(y-1,x)]:
                top = 0
            else:
                top = dp[y-1][x]
            if x-1<0 or puddledict[(y, x-1)]:
                left = 0
            else:
                left = dp[y][x-1]
            dp[y][x] = (top+left)%1000000007
        y,x = iterateidx(y,x,m)
    return dp[n-1][m-1]%1000000007

solution(4,3,[[2,2]])