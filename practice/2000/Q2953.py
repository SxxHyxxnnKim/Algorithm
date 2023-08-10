score = []
for i in range(1, 5+1):
    score_line = list(map(int, input().split(" ")))
    score.append(score_line)

# sum_list = [sum(score[i] for i in range(5))]
sum_list = []
for i in range(5):
    sum_list.append(sum(score[i]))

max_score = max(sum_list)

print(sum_list.index(max_score)+1, max_score)
    
    