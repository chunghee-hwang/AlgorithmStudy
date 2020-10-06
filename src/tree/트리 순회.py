# https://www.acmicpc.net/problem/1991
import sys
from collections import defaultdict

answer = []

def input():
    n = int(sys.stdin.readline())
    lines = sys.stdin.read().splitlines(n)
    lines = [line.rstrip().split(' ') for line in lines]
    return (lines, n)

def front(g, name):
    answer.append(name)
    left = g[name][0]
    right = g[name][1]
    if left:
        front(g, left)
    if right:
        front(g, right)
    
def middle(g, name):
    left = g[name][0]
    right = g[name][1]
    if left:
        middle(g, left)
    answer.append(name)
    if right:
        middle(g, right)

def back(g, name):
    left = g[name][0]
    right = g[name][1]
    if left:
        back(g, left)
    if right:
        back(g, right)
    answer.append(name)

def solution(i, n):
    g = defaultdict(list)
    for p, c1, c2 in i:
        g[p] = [None, None]
        if c1 != '.':
            g[p][0] = c1
        if c2 != '.':
            g[p][1] = c2

    front(g, 'A')
    answer.append('\n')
    middle(g, 'A')
    answer.append('\n')
    back(g, 'A')
    print(''.join(answer))
solution(*input())




