from collections import defaultdict, deque
def check(que, mem, nextValue, y, nextCnt):
    if not mem[nextValue] and nextValue <= y:
        mem[nextValue] = True
        que.append((nextValue, nextCnt))
def solution(x, y, n):
    que = deque([(x, 0)])
    answers = []
    mem = defaultdict(bool)
    while que:
        value, cnt = que.popleft()
        if value == y:
            answers.append(cnt)
        else:
            nextCnt = cnt+1
            check(que, mem, value+n, y, nextCnt)
            check(que, mem, value*2, y, nextCnt)
            check(que, mem, value*3, y, nextCnt)
    if answers:
        return min(answers)
    else:
        return -1