arr = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
mrow = 0
mcol = 0
for row in range(9):
    for col in range(9):
        if max_num <= arr[row][col]:
            max_num = arr[row][col]
            mrow = row + 1
            mcol = col + 1

print(max_num)
print(mrow, mcol)