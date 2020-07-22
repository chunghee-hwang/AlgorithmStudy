# https://codility.com/media/train/4-Sorting.pdf
def solution(A, k):
    n = len(A)
    count = [0] * (k+1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    for i in range(k+1):
        for j in range(count[i]):
            A[p] = i
            p += 1
    return A


solution([9, 7, 5, 1, 4], 9)
