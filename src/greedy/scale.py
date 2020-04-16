# https://programmers.co.kr/learn/courses/30/lessons/42886
# https://sihyungyou.github.io/programmers-%EC%A0%80%EC%9A%B8/
def solution(weight):
    weight.sort()
    answer = 1
    for w in weight:
        if answer < w:
            break
        answer+=w
    return answer