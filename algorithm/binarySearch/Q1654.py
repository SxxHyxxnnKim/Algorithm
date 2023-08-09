# K, N = map(int, input().split())
# arr = []

# for i in range(K):
#     i = int(input())
#     arr.append(i)

# start, end = 1, max(arr)

# while (start <= end):
#     mid = (start + end) // 2
#     cnt = 0

#     for i in range(K):
#         cnt += arr[i] // mid
#     if cnt >= N:
#         start = mid + 1
#     else:
#         end = mid - 1

# print(end)

# K, N = 5, 10
# lan = [ 100, 2]
K  = 2
N = 4
lan = [100, 50]
# 문제 이해  
# K = 가지고 있는 lan들의 길이 
# N = 일정한 길이로 갖고자하는 lan의 갯수
# K <= N    ->N이 가지고 있는 K보다 크기 때문에 반드시 나눠야함 (같을 때는 모든 lan길이가 같을때만 적용)

#  1. 입력받은 모든 lan들을 모두 사용할 필요 없이 같은 길이(length)의 N개의 lan을 만들면됨(end = max(lan) 하는 이유)
#  2. 만들고자 하는 길이(length)가 길수록 N이 작고, 길이가 짧을 수록 N이 큼 -> 자를 수 있는 길이(length)와 N은 반비례 
#      예를 들어 길이(length)를 더 길게 해서 더 많은 N을 만들 수 없음 (예외가 없음) 
#     ->>> 정렬이 가능하여 이분 탐색 사용 가능 
#  3. 최대 랜선 길이를 구하기 때문에 end를 출력 (total_count >= N 하는 이유)
#    ex) K  = 2, N = 4, lan = [100, 50]일 경우 26~33범위의 길이(length)는 모두 답이 되지만 최대길이는 33 


start, end = 1, max(lan) # 자를 수 있는 최대길이 = max(lan)

while start<=end:
    
    mid = (start + end) // 2

    total_count = 0

    # 총 만들 수 있는 랜선의 개수 합 
    for length in lan:
        total_count += (length // mid)

    if total_count >= N:
        start = mid + 1 # total_count가 N이 되더라도 start의 범위를 올림 -> while문이 끝날떄 end가 최대 
    else:
        end = mid - 1
print('start',start,'mid',mid, 'end', end , 'total_count', total_count)
