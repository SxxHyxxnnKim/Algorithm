from math import sqrt

T = int(input())

string_list = []
for i in range(T):
    message = input()

    sqrt_num = int(sqrt(len(message)))

    original_msg = ''
    for j in range(sqrt_num-1, -1, -1):
        for index in range(0, len(message), sqrt_num):
            word = message[index: index+sqrt_num]
            original_msg += word[j]
    
    print(original_msg)

# 다른 풀이
# a = int(input())
# for i in range(a):

#     text = input()
#     n = int(len(text)**0.5)
#     arr = [[0 for x in range(n)] for x in range(n)] # 초기화

#     # 입력
#     cnt = 0
#     for j in range(n):
#         for k in range(n):
#             arr[n-k-1][j] = text[cnt]
#             cnt += 1

#     for j in range(n):
#         for k in range(n):
#             print(arr[j][k], end='')
#     print("")