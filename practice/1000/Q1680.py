T = int(input())

for _ in range(T):
   W, N = map(int, input().split())
   x = [0] * N  # 지점 거리
   w = [0] * N  # 지점의 쓰레기의 양
   distance = 0  # 쓰레기차의 움직인 거리
   W_load = W  # 쓰레기차의 남은 용량

   # 쓰레기 지점의 개수만큼 입력
   for i in range(N):
      x[i], w[i] = map(int, input().split())

   i = 0
   while i < N:
   # 용량이 같을때
      if W_load == w[i]:
         distance += 2 * x[i]
         i += 1
         W_load = W
   # 용량이 여유가 있을때
      elif W_load > w[i]:
         W_load -= w[i]  # i지점에 있는 쓰레기를 채웠다
         i += 1
   # 용량이 넘칠때
      else:
         distance += 2 * x[i]
         W_load = W

   # 용량이 여유가 있는 상태로 맨 마지막 지점에 도착하게 된다면
   if W_load < W:
      distance += 2 * x[i]

   print(distance)