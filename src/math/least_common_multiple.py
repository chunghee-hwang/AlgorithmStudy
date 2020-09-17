# n개의 최소공배수
# https://programmers.co.kr/learn/courses/30/lessons/12953
# https://mathbang.net/204

from collections import Counter
# 소수 목록 구하는 함수(에라토스테네스의 체)
def init_eratos(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    i = 2
    while i * i <= n:
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
        i += 1
    primes = [number for number, prime in enumerate(primes) if prime]
    return primes

# 소인수 분해 함수, 리턴 예시: 2^3 * 3^2 == Counter(2:3, 3:2)
def soinsubunhae(number, primes):
    insu_list = []
    while number != 1:
        for prime in primes:
            if number % prime == 0:
                number //= prime
                insu_list.append(prime)
                break
    return Counter(insu_list)

def solution(arr):
    answer = 1
    primes = init_eratos(max(arr))
    
    # 배열의 요소의 소인수들의 합집합 구하기
    insus_sum = Counter()
    for number in arr:
        insus_sum |= soinsubunhae(number, primes)
        
    # 소인수의 합 구하기
    for key in insus_sum.keys():
        # print(key,'^',insus_sum[key])
        answer*=key**insus_sum[key]
    return answer