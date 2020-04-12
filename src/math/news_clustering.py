# https://programmers.co.kr/learn/courses/30/lessons/17677
from collections import defaultdict
def mk_set(string):
    s_dict = defaultdict(int)
    string = string.lower()
    n = len(string)
    s = set()
    for idx in range(n-1):
        appended = string[idx:idx+2]
        if appended.isalpha():
            s.add((appended, s_dict[appended]))
            s_dict[appended]+=1
            
    return s
        
def solution(str1, str2):
    s1 = mk_set(str1)
    s2 = mk_set(str2)
    intersection = s1 & s2
    union = s1 | s2
    if not intersection and not union:
        return 65536
    answer = int((len(intersection) / len(union)) * 65536)
    return answer