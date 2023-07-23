nums = []
check = []

for i in range(9) :
    i = int(input())
    nums.append(i)

max = max(nums)

for i in range(9) :
    if nums[i] == max :
        print(max)
        print(i+1)
        break;