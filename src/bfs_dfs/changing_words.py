# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from collections import defaultdict, Counter, deque
def is_changeable(word1, word2):
    return len(Counter(word1)- Counter(word2))==1
def solution(begin, target, words):
    cand = []
    if target not in words:
        return 0
    n = len(words)
    nextwords=defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if is_changeable(words[i], words[j]):
                nextwords[words[i]].append(words[j])
                nextwords[words[j]].append(words[i])
    q = deque()
    for word in words:
        if is_changeable(begin, word):
            q.append([word, defaultdict(bool), 0])
    while q:
        qsize = len(q)
        for _ in range(qsize):
            w, visit, cnt = q.popleft()
            cnt+=1
            visit[w]=True
            if w == target:
                cand.append(cnt)
                continue
            for nw in nextwords[w]:
                if not visit[nw]:
                    q.append([nw, visit, cnt])
    return min(cand)

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])