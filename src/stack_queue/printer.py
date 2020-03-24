# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    length = len(priorities)
    q = deque(zip(priorities, range(length)))
    rank = 1
    while q:
        doc = q.popleft()
        pri, loc = doc
        if any(pri < other_pri for other_pri, other_loc in q):
            q.append(doc)
        else:
            if loc == location:
                return rank
            rank += 1
    return -1


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
