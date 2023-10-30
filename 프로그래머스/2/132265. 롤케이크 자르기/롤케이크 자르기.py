from collections import defaultdict
def solution(topping):
    answer = 0
    left = defaultdict(int)
    leftKeysSize = 0
    right = defaultdict(int)
    for idx, t in enumerate(topping):
        right[t]+=1
    rightKeysSize = len(right.keys())
    for idx, t in enumerate(topping):
        left[t]+=1
        if left[t] == 1:
            leftKeysSize +=1
        right[t]-=1
        if right[t] == 0:
            rightKeysSize-=1
        if leftKeysSize == rightKeysSize:
            answer+=1
        
    return answer