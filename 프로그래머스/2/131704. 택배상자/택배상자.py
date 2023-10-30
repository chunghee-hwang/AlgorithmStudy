from collections import deque
def solution(order):
    answer = 0
    que = deque(range(1, len(order) + 1))
    order = deque(order)
    stack = []
    while True:
        a, b = False, False
        while stack and stack[-1] == order[0]:
            answer += 1
            stack.pop()
            order.popleft()
            a = True
        while que and order[0] != que[0]:
            stack.append(que.popleft())
        if que and que[0] == order[0]:
            answer += 1
            que.popleft()
            order.popleft()
            b = True
        if not a and not b:
            break
    return answer