str = input()
list = list(str)
result = ""

for i in list:
    if i.islower():
        result += i.upper()
    else :
        result += i.lower()

print(result)

