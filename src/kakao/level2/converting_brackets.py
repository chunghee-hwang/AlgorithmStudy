# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058

brackets = {'(': -1, ')':1}

def is_correct_brackets(w):
    if len(w) == 0:
        return True
    stack = []
    for bracket in w:
        if not stack:
            stack.append(bracket)
        else:
            if brackets[stack[-1]] < brackets[bracket]:
                stack.pop()
            else:
                stack.append(bracket)
    return len(stack) == 0

def split_to_balanced_brackets(w):
    balance = 0
    for index in range(len(w)):
        balance += brackets[w[index]]
        if balance == 0:
            break
    return [w[:index+1], w[index+1:]]

def reverse_brackets(w):
    result = ''
    for bracket in w:
        if bracket == '(':
            result+= ')'
        else:
            result+='('
    return result

def solution(w):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if w == '':
        return ''
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v      는 빈 문자열이 될 수 있습니다. 
    u,v = split_to_balanced_brackets(w)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if is_correct_brackets(u):
        v = solution(v)
    #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return u+v
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
    #   4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        new_string = '('
    #   4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        new_string += solution(v)
    #   4-3. ')'를 다시 붙입니다. 
        new_string += ')'
    #   4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        new_string += reverse_brackets(u[1:-1])
    #   4-5. 생성된 문자열을 반환합니다.
        return new_string

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))