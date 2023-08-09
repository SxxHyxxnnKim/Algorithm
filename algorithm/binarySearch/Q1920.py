N =  int(input())
a = list(map(int, input().split()))
M =  int(input())
b = list(map(int, input().split()))

a.sort()

for i in b:
    start, end = 0, N-1
    exist = False

    while start <= end:
        mid = (start + end)//2

        if i == a[mid]:
            exist = True
            print(1)
            break
        elif i > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
        
    if not exist:
        print(0) 