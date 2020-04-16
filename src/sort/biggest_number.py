# https://programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key
def compare(num1, num2):
    new_num1 = num1+num2
    new_num2 = num2+num1
    if  new_num1> new_num2:
        return 1
    elif new_num1 < new_num2:
        return -1
    return 0
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare), reverse=True)
    return str(int(''.join(map(str, numbers))))