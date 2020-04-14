from collections import defaultdict


def default_str():
    return 'A'


# 위, 아래로 커서 움직였을 때 조작횟수가 더 적은 방향으로 알파벳 변경
def move_cursor_up_down(cursor, string, dest_str):
    dest_chr = ord(dest_str)
    delta = min(dest_chr - 65, 90 - dest_chr + 1)
    string[cursor] = dest_str
    return delta


# 왼쪽, 오른쪽으로 커서를 string과 name 배열의 알파벳이 다를 때 까지 이동해본다.
# 왼쪽, 오른쪽 중 조작 횟수가 더 적은 곳으로 커서 이동
def find_next_left_right_cursor(cursor, string, name, n):
    left_cursor = right_cursor = cursor
    # 왼쪽으로 움직일 경우
    left_move_count = right_move_count = 0
    while True:
        left_cursor = (n + left_cursor - 1) % n
        left_move_count += 1
        if string[left_cursor] != name[left_cursor]:
            break
        if left_cursor == cursor:
            break
    # 오른쪽으로 움직일 경우
    while True:
        right_cursor = (right_cursor + 1) % n
        right_move_count += 1
        if string[right_cursor] != name[right_cursor]:
            break
        if right_cursor == cursor:
            break
    moves = []
    if cursor != left_cursor:
        moves.append((left_move_count, left_cursor))
    if cursor != right_cursor:
        moves.append((right_move_count, right_cursor))
    if not moves:
        return None
    return min(moves)  # return (최소 조작횟수, 다음에 위치할 커서)


def solution(name):
    answer = 0
    string = defaultdict(default_str)
    n = len(name)
    cursor = 0
    while True:
        answer += move_cursor_up_down(cursor, string, name[cursor])
        min_move = find_next_left_right_cursor(cursor, string, name, n)
        if not min_move:
            break
        move_diff, cursor = min_move
        answer += move_diff
    return answer


if __name__ == '__main__':
    print(solution("JEROEN"))
    print(solution("JAN"))
    print(solution("JAZ"))
