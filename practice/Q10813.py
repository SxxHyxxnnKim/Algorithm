N, M = map(int, input().split())
box = []
for i in range(N):
   box.append(i+1)

for _ in range(M):
   i,j = map(int, input().split())
   temp = box[i-1]
   box[i-1] = box[j-1]
   box[j-1] = temp

for i in range(N):
   print(box[i], end=' ')