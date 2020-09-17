# 땅따먹기
# https://programmers.co.kr/learn/courses/30/lessons/12913
# https://ssungkang.tistory.com/entry/%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level2

# 자신과 같은 열을 제외한 바로 위에 있는 행 중, 가장 큰 값을 자신의 값과 더해나간다.
# 마지막 행까지 이 작업을 한 뒤, 그 행의 최대값을 구하면 끝
def solution(land):
    for ridx, row in enumerate(land):
        if ridx == 0:
            continue
        for cidx in range(4):
            row[cidx] += max([score for top_cidx, score in enumerate(land[ridx-1]) if top_cidx!=cidx])
    return max(land[-1])

solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]])