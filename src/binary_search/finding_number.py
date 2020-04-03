# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때,
# 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N(1≤N≤100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
# 다음 줄에는 M(1≤M≤100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데,
# 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

from sys import stdin
def read_line():
    return stdin.readline()
def read_array():
    return list(map(int, read_line().rstrip().split(' ')))
def find_number(match, arr, n):
    low = 0
    high = n-1
    while low <= high:
        mid = (low + high) // 2
        found = arr[mid]
        if found < match:
            low = mid + 1
        elif found > match:
            high = mid - 1
        else:
            return mid
    return -1
if __name__ == '__main__':
    n = int(read_line())
    arr = sorted(read_array())
    m = int(read_line())
    match_arr2 = read_array()
    output = []
    for match in match_arr2:
        found_idx = find_number(match, arr, n)
        if found_idx != -1:
            output.append('1')
        else:
            output.append('0')
    print('\n'.join(output))

