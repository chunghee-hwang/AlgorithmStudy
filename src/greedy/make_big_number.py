# https://programmers.co.kr/learn/courses/30/lessons/42883
from collections import deque
def solution(number, k):
    stack = deque()
    delete_cnt = 0
    for num in number:
        if not stack:
            stack.append(num)
        else:
            while stack and stack[-1] < num and delete_cnt < k:
                stack.pop()
                delete_cnt+=1
            stack.append(num)
    if delete_cnt < k:
        for _ in range(k - delete_cnt):
            stack.pop()
    return ''.join(stack)