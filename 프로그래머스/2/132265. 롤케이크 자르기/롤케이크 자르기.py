from collections import Counter
def solution(topping):
    answer = 0
    left = set()
    right = Counter(topping)
    for idx, t in enumerate(topping):
        left.add(t)
        right[t]-=1
        if right[t] == 0:
            right.pop(t)
        if len(left) == len(right):
            answer+=1
        
    return answer