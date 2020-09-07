# 뉴스 클러스터링
# https://programmers.co.kr/learn/courses/30/lessons/17677

import re
from collections import Counter
def solution(str1, str2):
    set1 = [str1[index:index+2].lower() for index in range(len(str1)) if re.match('[a-zA-Z]{2}', str1[index:index+2])]
    set2 = [str2[index:index+2].lower() for index in range(len(str2)) if re.match('[a-zA-Z]{2}', str2[index:index+2])]
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    intersection_count = sum((counter1 & counter2).values())
    union_count = sum((counter1|counter2).values())
    if (intersection_count == 0 and union_count == 0) or union_count == 0:
        similarity = 1
    else:
        similarity = intersection_count / union_count
    return int(similarity*65536)
