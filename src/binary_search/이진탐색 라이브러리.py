# https://programmers.co.kr/learn/courses/10336/lessons/66365
from bisect import bisect_left, bisect_right

# 수행하기전 리스트 정렬 필수!

# "정렬된" 리스트에서 범위가 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(li, left_value, right_value):
    right_index = bisect_right(li,right_value)
    left_index = bisect_left(li, left_value)
    return right_index-left_index

# print(count_by_range([1,3,5,7,9,11], 3,8)) # 3,5,7로 3개 반환

# 정확히 값이 x인 데이터의 인덱스 반환
def index_of_x(a, x):
    i = bisect_left(a,x)
    if i != len(a) and a[i] == x:
        return i
    return None

# print(index_of_x([1,3,5,7,9,11], 3))

# x보다 작은 데이터 중에서, 가장 큰 값의 인덱스를 반환
def index_of_less_than_x(a, x):
    i = bisect_left(a,x)
    # x보다 작은 데이터가 존재하는 경우
    if i:
        return i-1 # 그 중에서 가장 큰 값의 인덱스 반환
    # x가 모든 데이터의 값 이하인 경우 None 반환
    return None

# print(index_of_less_than_x([1,3,5,7,9,11], 9))

# x 이하인 데이터 중에서, 가장 큰 값의 인덱스 반환
def index_of_less_or_equal_than_x(a,x):
    i = bisect_right(a,x)
    # x보다 작거나 같은 데이터가 존재하는 경우
    if i:
        return i-1 # 그 중에서 가장 큰 값의 인덱스 반환
    # x가 모든 데이터의 값보다 작은 경우 None 반환
    return None

# print(index_of_less_or_equal_than_x([1,3,5,7,9,11], 9))

# x 보다 큰 데이터 중에서, 가장 작은 값의 인덱스를 반환
def index_of_greater_than_x(a,x):
    i = bisect_right(a,x)
    # x보다 큰 데이터가 존재하는 경우
    if i != len(a):
        return i # 그 중에서 가장 작은 값의 인덱스 반환
    # x가 모든 데이터의 값 이상인 경우 None 반환
    return None

# print(index_of_greater_than_x([1,3,5,7,9,11], 9))

# x 이상의 데이터 중에서, 가장 작은 값의 인덱스 반환
def index_of_greater_equal_than_x(a,x):
    i = bisect_left(a,x)
    # x보다 크거나 같은 데이터가 존재하는 경우
    if i != len(a):
        return i # 그 중에서 가장 작은 값의 인덱스 반환
    # x가 모든 데이터의 값보다 큰 경우 None 반환
    return None

print(index_of_greater_equal_than_x([1,3,5,7,9,11], 9))