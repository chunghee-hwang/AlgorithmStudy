from collections import defaultdict


def solution(m, n, board):
    answer = 0

    deleted = defaultdict(set)
    new_board = defaultdict(list)
    for x in range(n):
        for b in board:
            new_board[x].append(b[x])
    while True:
        y = 0
        while y < m - 1:
            x = 0
            while x < n - 1:
                if ' ' != new_board[x][y] == new_board[x][y + 1] == new_board[x + 1][y] == new_board[x + 1][y + 1]:
                    deleted[x] |= {y, y + 1}
                    deleted[x + 1] |= {y, y + 1}
                x += 1
            y += 1
        # print(deleted)
        if not deleted:
            break
        for x in range(n):
            ys = deleted[x]
            len_ys = len(ys)
            answer += len_ys
            for y in ys:
                new_board[x][y] = '?'
            new_board[x] = list(filter(lambda k: k != '?', new_board[x]))
            for _ in range(len_ys):
                new_board[x].insert(0, ' ')
        # print(new_board)
        deleted.clear()
    return answer


if __name__ == '__main__':
    print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
    print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
    print(solution(4, 4, ["ABCD", "BACE", "BCDD", "BCDD"]))  # 8
