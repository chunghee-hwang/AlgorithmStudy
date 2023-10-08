def solution(s):
    splitted = s.split(' ')
    splitted.sort(key=lambda x: int(x))
    return splitted[0]+' '+splitted[-1]