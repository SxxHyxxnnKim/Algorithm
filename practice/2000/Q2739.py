N, M = map(int, input().split())
matrix =[]
matrix2 = []
for _ in range(N):
   line = list (map (int,input() .split ()))
   matrix.append(line)

for _ in range(N):
   line = list(map (int,input() .split ()))
   matrix2.append(line)

for i in range(N):
   for j in range(M):
      print(matrix[i][j]+matrix2[i][j], end=" ")
   print()