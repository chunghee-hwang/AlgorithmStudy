def solution(input_line):
    input_list = list(input_line)
    brackets = {'[': 3, ']': -3, '{': 2, '}': -2, '(': 1, ')': -1}
    stack = []
    for inp in input_list:
        if inp not in brackets:
            continue
        bracket = brackets[inp]
        if stack:
            last_elem = stack[-1]
            if 0 < last_elem <= bracket:
                return False
            elif 0 > bracket >= last_elem:
                return False
            elif last_elem + bracket == 0:
                stack.pop()
            else:
                stack.append(bracket)
        else:
            stack.append(bracket)

    return not stack


if __name__ == '__main__':
    answer1 = solution('3+[(5+1)-1]')
    answer2 = solution('3+([5+1])')
    answer3 = solution('3+{(5+1}')
    answer4 = solution('3+[{(5+1)-1}+3]')
    answer5 = solution('{{()()}}')
    print(answer1)
    print(answer2)
    print(answer3)
    print(answer4)
    print(answer5)
