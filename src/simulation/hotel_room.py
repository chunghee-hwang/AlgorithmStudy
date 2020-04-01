# https://programmers.co.kr/learn/courses/30/lessons/64063?language=cpp
def solution(k, room_number):
    next_empty = list(range(k + 1))
    ans_idx = 0
    n = len(room_number)
    for num in room_number:
        prev_room_num = room_number[ans_idx] = next_empty[num]
        if prev_room_num != k:
            new_room_num = next_empty[prev_room_num + 1]
            num2 = prev_room_num
            if ans_idx != n - 1:
                while 0 < num2 and prev_room_num == next_empty[num2]:
                    next_empty[num2] = new_room_num
                    num2 -= 1
        ans_idx += 1
    return room_number


if __name__ == '__main__':
    print(solution(10, [1,3,4,1,3,1]))
