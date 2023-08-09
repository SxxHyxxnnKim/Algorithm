import sys

n =  int(sys.stdin.readline())

if n == 1:
    dp = [0] * 3
else:
    dp = [0] * (n+1)
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])