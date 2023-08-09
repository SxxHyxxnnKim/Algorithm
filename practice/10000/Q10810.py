N, M = map(int, input().split())
box = [0]*N #N개만큼 바구니 생성

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i, j+1):
        #바구니 번호는 1부터 시작, 배열은 0부터 시작
        box[index-1] = k

for i in range(N):
    print(box[i], end=' ')