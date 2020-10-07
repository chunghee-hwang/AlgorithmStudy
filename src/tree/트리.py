# https://www.acmicpc.net/problem/1068
import sys
from collections import defaultdict
answer = 0

def input():
    n = int(sys.stdin.readline())
    nodes = map(int, sys.stdin.readline().rstrip().split(' '))
    d = int(sys.stdin.readline())
    return (n, nodes, d)

def findleaf(tree, node):
    global answer
    if len(tree[node]) == 0:
        answer+=1
    else:
        for child in tree[node]:
            findleaf(tree, child)

def solution(n, nodes, d):
    tree = defaultdict(list)
    root = None
    for num, parent in enumerate(nodes):
        if num == d or parent == d:
            continue
        if parent == -1:
            root = num
        else:
            tree[parent].append(num)
    if root!=None:
        findleaf(tree, root)
    
    print(answer)

solution(*input())