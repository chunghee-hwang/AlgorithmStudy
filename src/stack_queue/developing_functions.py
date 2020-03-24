# https://programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    idx = 0
    length = len(progresses)
    while idx < length:
        for i in range(idx, length):
            progresses[i] += speeds[i]
        func_cnt = 0
        while idx < length and progresses[idx] >= 100:
            idx += 1
            func_cnt += 1
        if func_cnt != 0:
            answer.append(func_cnt)
    return answer


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))
