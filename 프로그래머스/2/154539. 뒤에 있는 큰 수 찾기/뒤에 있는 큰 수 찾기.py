def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, num in enumerate(numbers):
        stack.append((num, idx))
        while len(stack) > 1:
            left, right = stack[-2], stack[-1]
            num1, idx1 = left
            num2, idx2 = right
            if num1 < num2:
                answer[idx1] = num2
                stack.pop(-2)
            else:
                break

    return answer