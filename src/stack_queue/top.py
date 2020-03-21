# https://programmers.co.kr/learn/courses/30/lessons/42588
def sendSignal(startIdx, idx, heights, answer):
    if idx < 0:
        answer[startIdx] = 0
        if startIdx > 0: sendSignal(startIdx-1, startIdx-2, heights, answer)
    elif heights[startIdx] < heights[idx]:
        answer[startIdx] = idx+1
        if startIdx > 0: sendSignal(startIdx-1, startIdx-2, heights, answer)
    else: sendSignal(startIdx, idx-1, heights, answer)
def solution(heights):
    heightsLen = len(heights)
    answer = [0]*heightsLen
    sendSignal(heightsLen-1, heightsLen-2, heights, answer)
    return answer