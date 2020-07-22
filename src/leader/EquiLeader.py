# https://app.codility.com/programmers/lessons/8-leader/equi_leader/

from collections import defaultdict


def solution(A):
    left = defaultdict(int)
    right = defaultdict(int)
    len_left = 0
    len_right = len(A)
    answer = 0
    leader = 0
    left_leader_count = 0
    right_leader_count = 0
    for value in A:
        right[value] += 1

    for value in A:
        left[value] += 1
        right[value] -= 1
        len_left += 1
        len_right -= 1

        if left[value] > left_leader_count:
            leader = value
            left_leader_count = left[value]

        if left_leader_count > len_left/2 and right[leader] > len_right / 2:
            answer += 1
    return answer
