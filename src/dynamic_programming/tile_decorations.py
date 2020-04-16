# https://programmers.co.kr/learn/courses/30/lessons/43104
side_lens = []
rounds = []


def get_side_lens(n):
    if side_lens[n] == 0:
        if n <= 2:
            side_lens[n] = 1
        else:
            side_lens[n] = get_side_lens(n - 1) + get_side_lens(n - 2)
    return side_lens[n]


def get_round(n):
    if rounds[n] == 0:
        if n == 1:
            rounds[n] = 4
        else:
            rounds[n] = get_round(n - 1) + get_side_lens(n) * 2
    return rounds[n]


def solution(n):
    global side_lens, rounds
    side_lens = [0] * (n + 1)
    rounds = [0] * (n + 1)
    return get_round(n)


if __name__ == '__main__':
    print(solution(5))
    print(solution(6))
