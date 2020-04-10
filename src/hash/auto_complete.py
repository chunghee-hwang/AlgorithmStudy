# https://programmers.co.kr/learn/courses/30/lessons/17685
from collections import defaultdict

def make_search_list(search_list, search_dict, search):
    for word in search_list:
        if word.startswith(search):
            search_dict[search].append(word)

def solution(words):
    answer = 0
    search_dict = defaultdict(list)
    search_dict[''] = words
    for word in words:
        search = ''
        prev_search = ''
        for idx in range(len(word)):
            search = search+word[idx]
            if search not in search_dict:
                make_search_list(search_dict[prev_search], search_dict, search)
            answer+=1
            if len(search_dict[search]) == 1:
                break
            prev_search = search
            
    return answer