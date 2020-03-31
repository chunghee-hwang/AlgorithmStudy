import re
from itertools import combinations
def solution(user_id, banned_id):
    banned_set = []
    b_idx = 0
    for b_id in banned_id:
        regex = '^{}$'.format(b_id.replace('*','.'))
        p = re.compile(regex)
        tup = []
        u_idx = 0
        for u_id in user_id:
            m = p.match(u_id)
            if m:
                tup.append((u_idx, b_idx))
                banned_set.append((u_idx, b_idx))
            u_idx+=1
        b_idx+=1
    answer_set = set()
    n = len(banned_id)
    combination = list(combinations(banned_set, n))
    for comb in combination:
        banned_num_visit = {}
        u_id_visit = {}
        valid_comb = True
        for (u_id, banned_num) in comb:
            if u_id not in u_id_visit:
                u_id_visit[u_id] = True
            else:
                valid_comb = False
                break
            if banned_num not in banned_num_visit:
                banned_num_visit[banned_num] = True
            else:
                valid_comb = False
                break
        if valid_comb:
            b_id, b_num = zip(*comb)
            answer_set.add(tuple(sorted(list(b_id))))
    return len(answer_set)