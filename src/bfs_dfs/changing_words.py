# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

from collections import defaultdict, Counter, deque
def is_changeable(word1, word2):
    return len(Counter(word1)- Counter(word2))==1
def solution(begin, target, words):
    answer = len(words)
    if target not in words:
        return 0
    n = len(words)
    nextwords=defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if is_changeable(words[i], words[j]):
                nextwords[words[i]].append(words[j])
                nextwords[words[j]].append(words[i])
    for word in words:
        if is_changeable(begin, word):
            nextwords[begin].append(word)
    visit=defaultdict(bool)
    q = deque([[begin,0]])
    visit[begin] = True
    while q:
        start,count = q.popleft()
        if start == target:
            answer = min(answer, count)
        for nextword in nextwords[start]:
            if not visit[nextword]:
                q.append([nextword, count+1])
                visit[nextword]=True
    return answer

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])