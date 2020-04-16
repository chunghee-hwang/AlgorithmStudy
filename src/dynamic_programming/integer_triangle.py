# https://programmers.co.kr/learn/courses/30/lessons/43105/solution_groups?language=python3&type=my
def solution(triangle):
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i - 1][0]
        triangle[i][i] += triangle[i - 1][i - 1]
        for j in range(1, i):
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
    return max(triangle[-1])


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
