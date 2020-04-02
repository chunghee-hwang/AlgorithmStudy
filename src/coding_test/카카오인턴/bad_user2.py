# 다른 유저가 짠 코드
# https://programmers.co.kr/learn/courses/30/lessons/64064
from itertools import product


def check(str1, str2):
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        if str1[i] == "*":
            continue
        if str1[i] != str2[i]:
            return False
    return True


def solution(user_id, banned_id):
    answer = set()
    result = [[] for i in range(len(banned_id))]

    for i in range(len(banned_id)):
        for u in user_id:
            if check(banned_id[i], u):
                result[i].append(u)
    print(result)
    result = list(product(*result))  # product: 벡터곱 --> (a, b) x (c, d) --> (a, c), (a, d), (b, c), (b, d)
    print(result)
    for r in result:
        if len(set(r)) == len(banned_id):
            answer.add("".join(sorted(set(r))))
    print(answer)
    return len(answer)


if __name__ == '__main__':
    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))

    # print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
