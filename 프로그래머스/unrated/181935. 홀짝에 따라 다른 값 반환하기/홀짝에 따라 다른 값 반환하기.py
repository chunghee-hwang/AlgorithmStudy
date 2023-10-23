def solution(n):
    if n % 2 != 0:
        return sum(filter(lambda x: x % 2 != 0, range(n+1)))
    return sum(map(lambda y: y**2, filter(lambda x: x % 2 == 0, range(n+1))))