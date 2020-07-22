# https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/start/

def solution(A, B):
    stack = []
    answer = len(A)
    for (a, b) in zip(A, B):
        if b == 1:
            stack.append(a)
        elif b == 0:
            while stack:
                answer -= 1
                if stack[-1] < a:
                    stack.pop()
                else:
                    break
    return answer


solution([4, 3, 2, 1, 5], [0, 1, 1, 0, 0])
