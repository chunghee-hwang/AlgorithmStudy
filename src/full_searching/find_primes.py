# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations


def init_eratos(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    return primes


def solution(numbers):
    answer = 0
    n = int(''.join(sorted(list(numbers), reverse=True)))
    if n <= 1:
        return 0
    primes = init_eratos(n)
    visit = [False] * (n+1)
    for i in range(1, len(numbers) + 1):
        perms = list(permutations(numbers, i))
        for perm in perms:
            num = int(''.join(perm))
            if not visit[num]:
                visit[num] = True
                if primes[num]:
                    answer+=1
    return answer


if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))
    print(solution("71113"))
