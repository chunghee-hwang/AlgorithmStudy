def solution(n,m,a,b):
    a.sort()
    for search in b:
        left = 0
        right = n-1
        while left <= right:
            mid = (left + right)//2
            if a[mid] > search:
                right = mid - 1
            else:
                left = mid + 1
        print('1') if a[right] == search else print('0')
        

n = int(input())
a = input().split(' ')
m = int(input())
b = input().split(' ')
solution(n,m,a,b)
