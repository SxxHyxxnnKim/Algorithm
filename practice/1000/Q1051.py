import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int ,sys.stdin.readline().strip())) for _ in range(n)]

area = []

for i in range(n):
    for j in range(m):
        number = graph[i][j]
        for k in range(j, m):
            if graph[i][k] == number and i + k - j < n:
                if graph[i+k-j][j] == number and graph[i+k-j][k] == number:
                    area.append((k-j+1)**2)

print(max(area))