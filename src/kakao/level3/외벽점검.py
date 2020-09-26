# https://programmers.co.kr/learn/courses/30/lessons/60062
from itertools import permutations
def solution(n, weak, dist):
    weak_count = len(weak)
    friend_count = len(dist)
    answer = friend_count+1
    for i in range(weak_count):
        weak.append(weak[i]+n)
    print(weak)
    friends_perm = list(permutations(dist, friend_count))
    for idx in range(weak_count+1):
        for friends in friends_perm:
            fcount = 1
            flimit = friends[fcount-1]+weak[idx]
            for idx2 in range(idx, idx+weak_count):
                if flimit < weak[idx2]:
                    fcount+=1
                    if fcount > friend_count:
                        break
                    flimit = friends[fcount-1]+weak[idx2]
        answer = min(answer, fcount)
    if answer > friend_count:
        return -1
    return answer

solution(12, [1, 5, 6, 10], [1, 2, 3, 4])