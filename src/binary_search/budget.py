# https://programmers.co.kr/learn/courses/30/lessons/43237
max_budget_sum = 0


def get_budget_sum(budgets, limit, M):
    budget_sum = 0
    for budget in budgets:
        budget_sum += min(budget, limit)
        if budget_sum > M:
            return 0
    return budget_sum


def solution(budgets, M):
    global max_budget_sum
    low = 0
    high = max(budgets)
    budget_sum = sum(budgets)
    mid = -1
    if budget_sum <= M:
        return high
    while low < high:
        mid = (low + high) // 2
        budget_sum = get_budget_sum(budgets, mid, M)
        if max_budget_sum < budget_sum:
            low = mid
            max_budget_sum = budget_sum
        else:
            high = mid
    return mid


if __name__ == '__main__':
    print(solution([120, 110, 140, 150], 485))
