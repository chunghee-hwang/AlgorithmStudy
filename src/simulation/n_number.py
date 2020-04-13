# https://programmers.co.kr/learn/courses/30/lessons/17687
def plus_one(n, nums, idx, result):
    nums[idx] += 1
    if nums[idx] >= n:
        nums[idx] = 0
        if idx == 0:
            nums.insert(0, 1)
            result.extend(nums)
        else:
            plus_one(n, nums, idx - 1, result)
    else:
        result.extend(nums)


def write_my_turn_num(n, m, p, t, result):
    output = []
    num_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    idx = p - 1
    print(result)
    for _ in range(t):
        appended = result[idx]
        if appended > 9 and n > 10:
            appended = num_dict[appended]
        output.append(str(appended))
        idx += m
    return ''.join(output)


def solution(n, t, m, p):
    result = [0]
    nums = [0]
    while len(result) < t * m:
        plus_one(n, nums, len(nums) - 1, result)
    return write_my_turn_num(n, m, p, t, result)


if __name__ == '__main__':
    print(solution(2, 4, 2, 1))
    print(solution(16, 16, 2, 1))
    print(solution(16, 16, 2, 2))
