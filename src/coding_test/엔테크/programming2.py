import timeit


def solution(n):
    n_str = str(n)
    n_str_len = len(n_str)
    dividers = set(int(n_str[i]) for i in range(n_str_len))
    divide_available_count = 0
    for divider in dividers:
        if divider != 0:
            if n % divider == 0:
                divide_available_count += 1
    return divide_available_count


if __name__ == '__main__':
    start = timeit.default_timer()
    print(solution(2322))
    print('time elapsed:', (timeit.default_timer() - start)*1e03, 'ms')

    start = timeit.default_timer()
    print(solution(1234))
    print('time elapsed:', (timeit.default_timer() - start)*1e03, 'ms')
