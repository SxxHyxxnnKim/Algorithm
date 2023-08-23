N, M = map(int, input().split())
castle = []

for _ in range(N):
    castle.append(input())

a, b = 0, 0

for i in range(N):
    if "X" not in castle[i]:
        a += 1

for j in range(M):
    if "X" not in [castle[i][j] for i in range(N)]:
        b += 1

print(max(a ,b))
