T = int(input())

for i in range(T):
    mul ,word = input().split()
    
    for x in word:
        print(x* int(mul), end="")
    print()
