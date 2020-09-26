# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right
# 리스트에서 범위가 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(li, left_value, right_value):
    right_index = bisect_right(li,right_value)
    left_index = bisect_left(li, left_value)
    return right_index-left_index

def solution(words, queries):
    answer = []
    wdict = [[] for _ in range(100001)] # 접미어 쿼리를 위한 사전
    wrevdict = [[] for _ in range(100001)] # 접두어 쿼리를 위한 사전
    
    for word in words:
        wdict[len(word)].append(word)
        wrevdict[len(word)].append(word[::-1])
    for i in range(100001):
        wdict[i].sort()
        wrevdict[i].sort()
    for query in queries:
        start = query.replace('?','a')
        end = query.replace('?','z')
        if query[0] == '?': # 접두어 쿼리
            start = start[::-1]
            end = end[::-1]
            answer.append(count_by_range(wrevdict[len(query)], start, end))
        else: # 접미사 쿼리
            answer.append(count_by_range(wdict[len(query)], start, end))
            
    return answer