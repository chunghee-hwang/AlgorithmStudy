# 다트 게임
# https://programmers.co.kr/learn/courses/30/lessons/17682

import re
def solution(dart_result):
    valid_result = re.match('^(\d|S|D|T|\*|#)+$', dart_result)
    if not valid_result:
        return 0
    tokens = re.findall('\d+|S|D|T|\*|#', dart_result)
    stack = []
    for token in tokens:
        if token == 'S':
            pass
        elif token == 'D':
            stack[-1] = stack[-1]**2
        elif token == 'T':
            stack[-1] = stack[-1]**3
        elif token == '#':
            stack[-1] = -stack[-1]
        elif token == '*':
            stack_size = len(stack)
            if stack_size>=2:
                stack[stack_size-2] *= 2
            stack[stack_size-1] *= 2      
        else:
            stack.append(int(token))
    return sum(stack)