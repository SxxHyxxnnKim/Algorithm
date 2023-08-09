from itertools import combinations

N, M = map(int, input().split())
#각 치킨에 대한 선호도를 list로 저장
chicken = [list(map(int, input().split())) for i in range(N)]
#결과값 계산
cnt = 0

#3가지 치킨에 대한 가능한 모든 조합
for i, j, k in combinations(range(M), 3):
   #각 선호도 점수를 저장
   sum = 0
   #각각의 회원들의 치킨 선호도 최대값 구하기
   for a in range(N):
      sum += max(chicken[a][i], chicken[a][j], chicken[a][k])
   cnt = max(cnt, sum)

print(cnt)