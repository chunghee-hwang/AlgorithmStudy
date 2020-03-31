# https://programmers.co.kr/learn/courses/30/lessons/64064
import re
from functools import reduce

banned_list = []
answer_set = set()


def plus_idxs(idxs, ns, i):
    if i < 0:
        return
    if idxs[i] + 1 > ns[i] - 1:
        idxs[i] = 0
        plus_idxs(idxs, ns, i - 1)
    else:
        idxs[i] += 1


def find_comb(n, ns):
    idxs = [0 for _ in range(n)]
    case = reduce(lambda x, y: x * y, ns)
    for _ in range(case):
        visit = {}
        valid_comb = True
        comb_tuple = []
        for i in range(n):
            comb = banned_list[i][idxs[i]]
            comb_tuple.append(comb)
            if comb not in visit:
                visit[comb] = True
            else:
                valid_comb = False
                break
        if valid_comb:
            answer_set.add(tuple(sorted(comb_tuple)))
        plus_idxs(idxs, ns, n - 1)


def solution(user_id, banned_id):
    global banned_list, answer_set
    n = len(banned_id)
    banned_list = [[] for _ in range(n)]
    ns = [0 for _ in range(n)]
    b_idx = 0
    for b_id in banned_id:
        regex = '^{}$'.format(b_id.replace('*', '.'))
        p = re.compile(regex)
        u_idx = 0
        for u_id in user_id:
            m = p.match(u_id)
            if m:
                banned_list[b_idx].append(u_idx)
                ns[b_idx] += 1
            u_idx += 1
        b_idx += 1
    if len(banned_id) == len(user_id):
        return 1
    find_comb(n, ns)
    return len(answer_set)


if __name__ == '__main__':
    print(solution(["frodo", "abcde", "bcdef", "cfgea", "defga"], ["f****", "a****", "b****", "c****", "d****"]))
    banned_list.clear()
    answer_set.clear()

    print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
    banned_list.clear()
    answer_set.clear()

    print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
    banned_list.clear()
    answer_set.clear()