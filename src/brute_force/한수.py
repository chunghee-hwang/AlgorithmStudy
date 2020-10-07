# https://www.acmicpc.net/problem/1065

def ishansu(num):
    digits = str(num)
    lastdigit = -1
    diff = None
    lastdiff = None
    for digit in digits:
        if lastdigit != -1:
            diff = int(digit) - lastdigit
            if lastdiff != None and lastdiff != diff:
                return False
        lastdigit = int(digit)
        lastdiff = diff
    return True

answer = 0
N = int(input())
for num in range(1, N+1):
    if ishansu(num):
        answer+=1
print(answer)
