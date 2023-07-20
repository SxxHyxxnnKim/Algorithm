n = int(input())
byte = n // 4
result = ""

if n%4 != 0 :
    byte += 1

for i in range(1, byte+1) :
    result += "long "
    
print(result + "int")