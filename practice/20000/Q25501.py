def recursion(s,l,r):
    if l >= r :
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
    
def isPalidrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())

for i in range(T):
    s = input()
    print(isPalidrome(s))

