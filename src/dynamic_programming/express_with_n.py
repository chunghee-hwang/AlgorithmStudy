# https://programmers.co.kr/learn/courses/30/lessons/42895
min_count_n = 9


def make_expression(n, number, sum_exp, count_n, expression):
    global min_count_n
    if min_count_n <= count_n:
        return
    if sum_exp == number:
        print('count_n:', count_n, 'expression: ', expression)
        min_count_n = count_n
        return
    if count_n > 8:
        return
    count_n += 1
    make_expression(n, number, sum_exp + n, count_n, '(' + expression + ')' + '+' + str(n))
    make_expression(n, number, sum_exp // n, count_n, '(' + expression + ')' + '/' + str(n))
    if sum_exp != 0:
        make_expression(n, number, n // sum_exp, count_n, str(n) + '/' + '(' + expression + ')')
    make_expression(n, number, sum_exp * n, count_n, '(' + expression + ')' + '*' + str(n))
    make_expression(n, number, sum_exp - n, count_n, '(' + expression + ')' + '-' + str(n))
    make_expression(n, number, n - sum_exp, count_n, str(n) + '-' + '(' + expression + ')')

    count_n += 1
    nn = n * 10 + n
    make_expression(n, number, sum_exp + nn, count_n, '(' + expression + ')' + '+' + str(nn))
    make_expression(n, number, sum_exp // nn, count_n, '(' + expression + ')' + '/' + str(nn))
    if sum_exp != 0:
        make_expression(n, number, nn // sum_exp, count_n, str(nn) + '/' + '(' + expression + ')')
    make_expression(n, number, sum_exp * nn, count_n, '(' + expression + ')' + '*' + str(nn))
    make_expression(n, number, nn - sum_exp, count_n, str(nn) + '-' + '(' + expression + ')')
    make_expression(n, number, nn - sum_exp, count_n, str(nn) + '-' + '(' + expression + ')')


def solution(n, number):
    global min_count_n
    make_expression(n, number, n, 1, str(n))
    make_expression(n, number, n * 10 + n, 2, str(n * 10 + n))
    if min_count_n > 8:
        return -1
    return min_count_n


if __name__ == '__main__':
    n = 5
    number = 12
    print('n:', n, 'number:', number)
    solution(n, number)

    min_count_n = 9

    n = 2
    number = 11
    print('\n\nn:', n, 'number:', number)
    solution(n, number)
