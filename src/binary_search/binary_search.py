from sys import stdin


def solution():
    array = list(range(1, 16))

    find_n = int(stdin.readline())
    left = 0
    right = 9
    while left <= right:
        mid = (left + right) // 2
        if array[mid] > find_n:
            right = mid - 1
        elif array[mid] < find_n:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    print('result:', solution())
