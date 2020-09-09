# 압축
# https://programmers.co.kr/learn/courses/30/lessons/17684?language=python3

def solution(msg):
    answer = []
    lzw_dict = {}
    len_msg = len(msg)
    for index, alphabet in enumerate(map(chr,range(65, 91))):
        lzw_dict[alphabet] = index+1
    msg_idx = 0
    while True:
        longest_word = ''
        len_word = 1
        while msg_idx+len_word <= len_msg:
            new_longest_word = msg[msg_idx: msg_idx+len_word]
            if new_longest_word in lzw_dict:
                longest_word = new_longest_word
                len_word+=1
            else:
                break
        answer.append(lzw_dict[longest_word])
        next_msg_idx = msg_idx + len_word - 1
        if next_msg_idx < len_msg:
            lzw_dict[longest_word+msg[next_msg_idx]] = len(lzw_dict)+1
            msg_idx = next_msg_idx
        else:
            break
    return answer

print(solution("KAKAO"))