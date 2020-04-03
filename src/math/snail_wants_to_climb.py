from sys import stdin
import math
if __name__ == '__main__':
    a, b, v = map(int, stdin.readline().split())
    print(math.ceil(((v-a) / (a-b)) + 1))
