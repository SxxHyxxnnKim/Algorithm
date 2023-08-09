my_string = input()
alp = input()
answer = ''

list = list(my_string)

for i in list:
    if i == alp :
        answer += i.upper()
    else :
        answer += i

print(answer)
