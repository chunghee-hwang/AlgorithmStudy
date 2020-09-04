# 키패드 누르기
# https://programmers.co.kr/learn/courses/30/lessons/67256

def get_distance(position1, position2):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

def solution(numbers, hand):
    answer = []
    left_position = [0,3]
    right_position = [2,3]
    num_positions = [(1,3),(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2),(1,2),(2,2)]
    for num in numbers:
        num_position =  num_positions[num]
        x,y = num_position
        left_moved = False
        if x == 0:
            left_moved = True
        elif x == 2:
            left_moved = False
        else:
            left_distance = get_distance(left_position, num_position)
            right_distance = get_distance(right_position, num_position)
            if left_distance > right_distance:
                left_moved = False
            elif left_distance < right_distance:
                left_moved = True
            else:
                left_moved = hand == 'left'
        
        if left_moved:
            left_position = num_position
            answer.append('L')
        else:
            right_position = num_position
            answer.append('R')
    
    return ''.join(answer)