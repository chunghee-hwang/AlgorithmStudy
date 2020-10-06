# 파이썬 입출력 모음
import sys
from collections import defaultdict

def input():
    n = int(sys.stdin.readline())
    lines = sys.stdin.read().splitlines(n)
    lines = [line.rstrip().split(' ') for line in lines]
    return (lines, n)