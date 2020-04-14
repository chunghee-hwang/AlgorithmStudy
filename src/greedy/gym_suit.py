# https://programmers.co.kr/learn/courses/30/lessons/42862
from collections import defaultdict
def default_clothe():
    return 1
def solution(n, lost, reserve):
    answer = 0
    clothes = defaultdict(default_clothe)
    for re in reserve:
        clothes[re]+=1
    for lo in lost:
        clothes[lo]-=1
    for lo in lost:
        if clothes[lo]> 0:
            continue
        if lo > 1 and clothes[lo-1] > 1:
            clothes[lo-1]=1
            clothes[lo]=1
        elif lo < n and clothes[lo+1] > 1:
            clothes[lo+1]=1
            clothes[lo]=1
    for idx in range(1, n+1):
        if clothes[idx] > 0:
            answer+=1
    return answer