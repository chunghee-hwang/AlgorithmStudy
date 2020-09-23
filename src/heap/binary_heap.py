# https://programmers.co.kr/learn/courses/30/lessons/42628?language=python3
# 이중우선순위큐
import heapq
def solution(operations):
    answer = []
    q = []
    for operation in operations:
        oper, operand = operation.split(' ')
        operand = int(operand)
        if oper == 'I':
            heapq.heappush(q, operand)
        else:
            if not q:
                continue
            if operand == -1:
                heapq.heappop(q)
            else:
                q.remove(max(q))
    if q:
        return [max(q), min(q)]
    else:
        return [0,0]
    return answer


if __name__ == '__main__':
    print(solution(["I 16", "D 1"]))
    print(solution(["I 7", "I 5", "I -5", "D -1"]))
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
    print(solution(["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]))
