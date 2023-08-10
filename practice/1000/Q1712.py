A,B,C = map(int, input().split(" "))

if C-B > 0:
    result = A /(C - B) + 1
    print(int(result))
else:
    print(-1)