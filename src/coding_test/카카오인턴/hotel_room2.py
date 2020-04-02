# 다른 유저가 품
# https://programmers.co.kr/learn/courses/30/lessons/64063?language=cpp
def solution(k, room_number):
    answer = []
    rooms = {}
    # k = 0
    for num in room_number:
        answer.append(getRoom(rooms, num))

    return answer


def getRoom(rooms, num):
    target = num
    sub = []
    while rooms.get(target) is not None:
        sub.append(target)
        target = rooms[target]
    for s in sub:
        rooms[s] = target + 1
    rooms[target] = target + 1
    return target


if __name__ == '__main__':
    print(solution(10, [1, 3, 4, 1, 3, 1]))
