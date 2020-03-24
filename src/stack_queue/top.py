# https://programmers.co.kr/learn/courses/30/lessons/42588
def send_signal(startIdx, idx, heights, answer):
    if idx < 0:
        answer[startIdx] = 0
        if startIdx > 0: send_signal(startIdx - 1, startIdx - 2, heights, answer)
    elif heights[startIdx] < heights[idx]:
        answer[startIdx] = idx + 1
        if startIdx > 0: send_signal(startIdx - 1, startIdx - 2, heights, answer)
    else:
        send_signal(startIdx, idx - 1, heights, answer)


def solution(heights):
    heights_len = len(heights)
    answer = [0] * heights_len
    send_signal(heights_len - 1, heights_len - 2, heights, answer)
    return answer
