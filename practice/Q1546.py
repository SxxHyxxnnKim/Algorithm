n = int(input())
score = list(map(int,input().split(" ")))
new =[]

maxscore = max(score)

#점수 고치기
for i in score : 
    new.append(int(i)/int(maxscore) * 100)

print(sum(new)/n)
