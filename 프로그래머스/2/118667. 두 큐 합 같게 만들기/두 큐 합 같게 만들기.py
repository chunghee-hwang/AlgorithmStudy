from collections import deque
def moveOne(source, dest, sourceSum, destSum):
    moved = source.popleft()
    dest.append(moved)
    sourceSum -= moved
    destSum += moved
    return sourceSum, destSum
def solution(queue1, queue2):
    totalLen = (len(queue1) + len(queue2))*2
    que1 = deque(queue1)
    que2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    answer = 0
    while sum1 != sum2 and answer < totalLen:
        if sum1 > sum2:
            sum1, sum2 = moveOne(que1, que2, sum1, sum2)
        else:
            sum2, sum1 = moveOne(que2, que1, sum2, sum1)
        answer += 1
    if sum1 == sum2:
        return answer
    return -1