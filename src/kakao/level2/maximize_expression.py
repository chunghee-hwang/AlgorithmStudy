# 수식 최대화
# https://programmers.co.kr/learn/courses/30/lessons/67257

import re
from itertools import permutations

def calculate_expression(expression, operator_priority):
    new_expression = expression[:]
    operator_index = 0
    len_operator_priority = len(operator_priority)
    while operator_index < len_operator_priority:
        operator = operator_priority[operator_index]
        try:
            found_index = new_expression.index(operator)
            operand1 = int(new_expression[found_index-1])
            operand2 = int(new_expression[found_index+1])
            if operator == '*':
                result = operand1 * operand2
            elif operator == '-':
                result = operand1 - operand2
            else:
                result = operand1 + operand2
            del new_expression[found_index:found_index+2]
            new_expression[found_index-1] = result
        except:
            operator_index +=1
            
    return abs(new_expression[0])

def solution(expression):
    answer = 0
    # \D: 숫자가 아닌 것.
    operators = list(set(re.findall('\D', expression)))
    # regex에 괄호를 치게되면 그것까지 포함해서 split한다.
    expression = re.split('(\D)',expression)
    priorities = list(permutations(operators,len(operators)))
    for operator_priority in priorities:
        answer = max(calculate_expression(expression, operator_priority), answer)
    return answer