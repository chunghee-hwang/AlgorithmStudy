# 영어 끝말잇기
# https://programmers.co.kr/learn/courses/30/lessons/12981

from collections import defaultdict
def solution(n, words):
    answer = [0,0]
    candidates = [0]*n
    order = 0
    next_start_letter = words[0][0]
    used_words = defaultdict(bool)
    for word in words:
        candidates[order] +=1
        if word[0]!=next_start_letter or used_words[word]:
            answer[0] = order+1; answer[1] = candidates[order]
            break
        next_start_letter = word[-1]
        used_words[word] = True
        order = (order+1)%n
    return answer