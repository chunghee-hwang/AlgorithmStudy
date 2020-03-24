# https://programmers.co.kr/learn/courses/30/lessons/42585
def solution(arrangement):
    stack = []
    length = len(arrangement)
    left = '('
    right = ')'
    cut_count = 0
    bar_count = 0
    for i in range(length):
        if arrangement[i] == right:
            if i > 0 and arrangement[i - 1] == right:
                bar_count += 1
            stack.pop()
            if stack and arrangement[stack[-1]] == left:
                if i > 0 and arrangement[i - 1] != right:
                    cut_count += len(stack)
        else:
            stack.append(i)
    return cut_count + bar_count


if __name__ == '__main__':
    print(solution('()(((()())(())()))(())'))
