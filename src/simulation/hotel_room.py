# https://programmers.co.kr/learn/courses/30/lessons/64063?language=cpp
from collections import defaultdict


def solution(k, room_number):
    next_empty = defaultdict(int)
    ans_idx = 0
    for num in room_number:
        tmp_num = num
        while next_empty[tmp_num] != 0:
            tmp_num = next_empty[tmp_num]
        room_number[ans_idx] = tmp_num
        if tmp_num < k:
            nex = next_empty[tmp_num + 1]
            if nex == 0:
                nex = tmp_num+1
            next_empty[tmp_num] = nex
        ans_idx += 1
    return room_number


if __name__ == '__main__':
    print(solution(10, [1, 3, 4, 1, 3, 1]))
