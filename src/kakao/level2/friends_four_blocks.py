# 프렌즈4블록
# https://programmers.co.kr/learn/courses/30/lessons/17679

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
        deleted.clear()
    return answer


print(solution(2,2,["AA", "AA"])) #답 : 4
print(solution(2,2, ["AA", "AB"])) #답 : 0
print(solution(3,2, ["AA", "AA", "AB"])) #답 : 4
print(solution(4,2, ["CC", "AA", "AA", "CC"])) #답 : 8

print(solution(6,2, ["DD", "CC", "AA", "AA", "CC", "DD"])) #답 : 12
print(solution(8,2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"])) #답 : 8
print(solution(6,2, ["AA", "AA", "CC", "AA", "AA", "DD"])) #답 : 8
print(solution(4,5,["AAAAA","AUUUA","AUUAA","AAAAA"])) #14
