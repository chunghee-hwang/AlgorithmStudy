# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3
def dfs(idx, numbers, target, number):
    if idx == len(numbers):
        if number == target:
            return 1
        else:
            return 0
    plus_result = dfs(idx+1, numbers, target, number + numbers[idx])
    minus_result = dfs(idx+1, numbers, target, number - numbers[idx])
    return plus_result + minus_result


def solution(numbers, target):
    return dfs(0, numbers, target, 0)


print(solution([1, 1, 1, 1, 1], 3))
