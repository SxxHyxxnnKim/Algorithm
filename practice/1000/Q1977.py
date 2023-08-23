M = int(input())
N = int(input())


def is_square(n):
    if int(n ** 0.5) ** 2 == n:
        return True
    else:
        return False

sum_list = []
for i in range(M, N+1):
    sum = 0
    if is_square(i):
        sum += i
        sum_list.append(sum)

total = 0
for i in range(len(sum_list)):
    total += sum_list[i]
if total == 0:
    print('-1')
else:
    print(total)
    print(min(sum_list))
    


