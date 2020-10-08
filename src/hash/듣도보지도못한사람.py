# https://www.acmicpc.net/problem/1764
import sys
from collections import defaultdict
def readline():
    return sys.stdin.readline().rstrip()

def input():
    N, M = map(int, readline().split(' '))
    a = [readline() for _ in range(N)]
    b = [readline() for _ in range(M)]
    return (a,b)

def solution(a, b):
    dic = defaultdict(int)
    for hear in a:
        dic[hear]+=1
    for see in b:
        dic[see]+=1
    hear_and_see = [key for key in dic.keys() if dic[key]==2]
    hear_and_see.sort()
    print(len(hear_and_see))
    print('\n'.join(hear_and_see))



solution(*input())