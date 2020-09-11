# 불량 사용자
# https://programmers.co.kr/learn/courses/30/lessons/64064
# 참고 사이트: https://covenant.tistory.com/158
import re
from itertools import permutations

def is_match(cands, ban_regexes):
    return all([re.match(ban_regexes[idx], cands[idx])for idx in range(len(cands))])

def solution(user_ids, banned_ids):
    banned_user_lists = set()
    ban_regexes = ['^'+banned_id.replace('*','.')+'$' for banned_id in banned_ids]
    for cands in permutations(user_ids, len(banned_ids)):
        if is_match(cands, ban_regexes):
            banned_user_lists.add(tuple(sorted(cands)))
    return len(banned_user_lists)