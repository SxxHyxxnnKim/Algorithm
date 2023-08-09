N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time.sort(key=lambda x: (x[1], x[0]))

last = 0
conut = 0

for i, j in time:
  if i >= last:
    conut += 1
    last = j

print(conut)