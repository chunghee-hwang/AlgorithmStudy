# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

def len_compress_string(s, unit):
    n = len(s)
    prev_part = ''
    results = []
    for index in range(0,n,unit):
        part = s[index:index+unit]
        if prev_part == part:
            results[-1][0]+=1
        else:
            results.append([1, part])
        prev_part = part
    len_result = 0
    for result in results:
        part_count, part = result
        if part_count != 1:
            len_result+=len(str(part_count))
        len_result+=len(part)
    return len_result
            
        
def solution(s):
    min_len = len(s)
    for unit in range(1, min_len//2 + 1):
        min_len = min(min_len, len_compress_string(s, unit))
    return min_len