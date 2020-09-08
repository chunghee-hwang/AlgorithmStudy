# 후보키
# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations
from collections import defaultdict

def is_minimalized(column_index, candidations):
    for candidation in candidations:
        if all(index in column_index for index in candidation):
            return False
    return True

def solution(relation):
    candidations = []
    column_count = len(relation[0])
    for comb_count in range(1,column_count+1):
        column_indexes = (list(combinations(range(column_count), comb_count)))
        for column_index in column_indexes:
            if not is_minimalized(column_index, candidations):
                continue
            duplicate_check_map = defaultdict(bool)
            is_candidation = True
            for row in relation:
                selected_column_values = tuple([row[index] for index in column_index])
                if not duplicate_check_map[selected_column_values]:
                    duplicate_check_map[selected_column_values] = True
                else:
                    is_candidation = False
                    break
            if is_candidation:
                candidations.append(column_index)
    return len(candidations)