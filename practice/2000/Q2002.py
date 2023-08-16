from collections import deque

cnt = 0 # 추월한 차량의 개수

N = int(input())
q = deque()

# 터널 들어가는 차량 입력
for i in range(N):
    q.append(input())
    
# 터널 나오는 차량을 입력받고 처리
for i in range(N):
    out = input()
    
    # 추월한 차량
    if out != q[0]:
        q.remove(out)
        cnt += 1
        
    else:
        q.popleft()
        
print(cnt)
    