# 파일명 정렬
# https://programmers.co.kr/learn/courses/30/lessons/17686?language=python3

from functools import cmp_to_key
import re
def get_file_info(file, input_order):
    m = re.compile('^\D+').match(file)
    head = m.group().lower()
    next_index = m.end()
    number_and_tail = file[next_index:]
    m = re.compile('^\d{1,5}').match(number_and_tail)
    number = int(m.group())
    next_index = m.end()
    tail = number_and_tail[next_index:]
    return (head, number, tail, input_order, file)

def compare_str(str1, str2):
    if str1 == str2:
        return 0
    elif str1 > str2:
        return 1
    elif str1 < str2:
        return -1

def compare_file_infos(file_info1, file_info2):
    head1, number1, tail1, input_order1, file1 = file_info1
    head2, number2, tail2, input_order2, file2 = file_info2
    if head1 == head2:
        if number1 == number2:
            return input_order1 - input_order2
        else:
            return number1 - number2
    else:
        return compare_str(head1, head2)

def solution(files):
    file_infos = []
    for index, file in enumerate(files):
        file_infos.append(get_file_info(file, index))
    file_infos.sort(key=cmp_to_key(compare_file_infos))
    answer= [file_info[-1] for file_info in file_infos]
    return answer