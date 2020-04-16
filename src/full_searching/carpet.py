# https://programmers.co.kr/learn/courses/30/lessons/42842
def solution(brown, red):
    red_height = 1
    red_width = red
    while red_height <= red_width:
        if (red_height + red_width) * 2 + 4 == brown:
            return [red_width + 2, red_height + 2]
        red_height += 1
        while red_height <= red and red % red_height != 0:
            red_height += 1
        red_width = red // red_height
    return [red_width + 2, red_height + 2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
