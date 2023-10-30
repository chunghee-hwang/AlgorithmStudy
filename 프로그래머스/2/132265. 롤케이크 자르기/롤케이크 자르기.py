from collections import Counter
def solution(topping):
    answer = 0
    left = Counter()
    leftKeysSize = 0
    right = Counter(topping)
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