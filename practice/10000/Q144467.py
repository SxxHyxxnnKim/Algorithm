N = int(input())

cow_arr = {}
cross = 0
for i in range(N):
    cow_num, cow_loc = map(int, input().split())
    if cow_num not in cow_arr:
        cow_arr[cow_num] = cow_loc
    else:
        if cow_arr[cow_num] != cow_loc:
            cross += 1
            cow_arr[cow_num] = cow_loc

print(cross)