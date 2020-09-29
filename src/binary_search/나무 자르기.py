# https://www.acmicpc.net/problem/2805
def solution(n,m,h):
    left = 0; right=max(h)
    while left <= right:
        mid = (left + right)//2
        sum_of_heights=sum([tree-mid for tree in h if mid < tree])
        if sum_of_heights >= m:
            left = mid+1
        else:
            right = mid -1
    print(right)
n,m = map(int, input().split(' '))
h = list(map(int, input().split(' ')))
solution(n,m,h)