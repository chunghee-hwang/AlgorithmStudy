# n진수 게임
# https://programmers.co.kr/learn/courses/30/lessons/17687

from collections import deque
over_ten_dict = {10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
def convert_to_notation(n, number):
    if n == 10:
        return number
    result = deque()
    while True:
        remains = number % n
        number = number// n
        if remains > 9:
            remains = over_ten_dict[remains]
        else:
            remains = str(remains)
        result.appendleft(remains)
        if number == 0:
            break
    return result
def solution(n, t, m, p):
    answer = []
    values = deque()
    number = 0
    while len(values) < t*m: # 게임에 대답하기 위해 필요한 최소 values 길이 이상 될때까지 계속 추가
        values.extend(convert_to_notation(n, number))
        number+=1
    value_index = p-1
    for _ in range(t):
        answer.append(values[value_index])
        value_index+=m
    return ''.join(answer)