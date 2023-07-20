x = int(input())
n = int(input())
chk = 0

for i in range(1, n+1) :
    a,b = map(int, input().split(" "))
    chk += a*b

if x == chk :
    print("Yes")
else :
    print("No")
    
    