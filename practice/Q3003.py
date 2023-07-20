white = list(map(int, input().split(" ")))

chess = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(len(chess)):
    
    if chess[i] == white[i]:
        answer.append(0)
    else : 
        answer.append(chess[i] - white[i])
    
for i in answer:
    print(i, end=" ")
