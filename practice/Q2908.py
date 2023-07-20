a, b = input().split()

print(a)
print(b)

ra = int(a[::-1])
rb = int(b[::-1])

if ra > rb:
    print(ra)
else :
     print(rb)