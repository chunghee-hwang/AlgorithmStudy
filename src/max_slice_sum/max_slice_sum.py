# 부분합 알고리즘: 카데인 알고리즘
# https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/
def solution(A):
    n = len(A)
    if n == 1:
        return A[0]
    local_max_sum = global_max_sum = A[0]
    for i in range(1, n):
        local_max_sum = max(A[i], local_max_sum + A[i])
        global_max_sum = max(global_max_sum, local_max_sum)
    return global_max_sum


solution([3, 2, -6, 4, 0])
