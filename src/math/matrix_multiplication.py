# 행렬의 곱셈
# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    rlen1, clen1= len(arr1), len(arr1[0])
    rlen2, clen2 = len(arr2), len(arr2[0])
    rlen, clen = rlen1, clen2
    answer = [[0 for x in range(clen)] for y in range(rlen)]
    for y in range(rlen):
        for x in range(clen):
            karo = arr1[y]
            sero = [arr2[ridx][x] for ridx in range(rlen2) ]
            # print(karo,'x',sero)
            answer[y][x] = sum([k*s for k,s in zip(karo, sero)])
    return answer