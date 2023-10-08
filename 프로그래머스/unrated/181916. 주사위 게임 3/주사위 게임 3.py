def solution(a, b, c, d):
    if len(set([a,b,c,d])) == 1:
        return 1111*a
    if len(set([a,b,c,d])) == 4:
        return min([a,b,c,d])
    mem = [0] * 7
    for elem in [a,b,c,d]:
        mem[elem] += 1
    counter = [(num, cnt) for num, cnt in enumerate(mem) if cnt > 0]
    if len(counter) == 3:
        q, r = map(lambda y: y[0], filter(lambda x: x[1] != 2, counter))
        return q * r
    if len(counter) == 2:
        if counter[0][1] == counter[1][1]:
            p = counter[0][0]; q = counter[1][0]
            return (p + q) * abs(p - q)
        if counter[0][1] == 1 and counter[1][1] == 3:
            p = counter[1][0]; q = counter[0][0]
        elif counter[0][1] == 3 and counter[1][1] == 1:
            p = counter[0][0]; q = counter[1][0]
        return (10 * p + q) ** 2
        