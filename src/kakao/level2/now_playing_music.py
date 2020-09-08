# 방금 그곡
# https://programmers.co.kr/learn/courses/30/lessons/17683
import re
from functools import cmp_to_key
def get_interval_time_in_minutes(start_time, end_time):
    h1, m1 = map(int, start_time.split(':'))
    h2, m2 = map(int, end_time.split(':'))
    min_interval = m2 - m1
    if min_interval < 0:
        h2 -= 1
        min_interval+=60
    hour_interval = h2 - h1
    return hour_interval*60 + min_interval

def get_played_scale(original_scale, interval_time):
    index = 0
    len_origianl_scale = len(original_scale)
    played_scale = []
    for _ in range(interval_time):
        played_scale.append(original_scale[index])
        index = (index + 1) % len_origianl_scale
    return played_scale

def split_scale(scale):
    return [s for s in re.split('([A-G]#?)', scale) if s]

def is_scale_matched(heard_scale, played_scale):
    first_heard_scale = heard_scale[0]
    found_indexes = [index for index, ps in enumerate(played_scale) if first_heard_scale == ps]
    for found_index in found_indexes:
        if heard_scale == played_scale[found_index:found_index+len(heard_scale)]:
            return True
    return False
    
def compare_musics(music1, music2):
    interval_time1, input_order1, musicname1 = music1
    interval_time2, input_order2, musicname2 = music2
    if interval_time1 == interval_time2:
        return input_order2 - input_order1
    else:
        return interval_time1 - interval_time2

def solution(m, musicinfos):
    matched_musics = []
    input_order = 1
    for musicinfo in musicinfos:
        start_time, end_time, musicname, original_scale = musicinfo.split(',')
        interval_time= get_interval_time_in_minutes(start_time, end_time)
        original_scale = split_scale(original_scale)
        played_scale = get_played_scale(original_scale, interval_time)
        if is_scale_matched(split_scale(m), played_scale):
            matched_musics.append((interval_time, input_order, musicname))
        input_order+=1
    if not matched_musics:
        return '(None)'
    else:
        return max(matched_musics, key=cmp_to_key(compare_musics))[2]

print(solution("CCB", ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"])) #FOO