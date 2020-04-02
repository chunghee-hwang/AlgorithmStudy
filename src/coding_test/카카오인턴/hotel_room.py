# https://programmers.co.kr/learn/courses/30/lessons/64063
from collections import defaultdict
def solution(k, room_number):
    answer = []
    rooms = defaultdict(int)
    for target in room_number:
        full = []
        while rooms[target] != 0:
            full.append(target)
            target = rooms[target]
        for f in full:
            rooms[f] = target+1
        rooms[target] = target+1
        answer.append(target)
    return room_number


if __name__ == '__main__':
    print(solution(10, [1, 3, 4, 1, 3, 1]))
