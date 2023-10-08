def solution(arr, queries):
    for idx, pivot in enumerate(queries):
        if idx % 2 == 0:
            arr = arr[:pivot+1]
        else:
            arr = arr[pivot:]
    return arr
        