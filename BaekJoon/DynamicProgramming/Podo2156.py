import sys
n = int(sys.stdin.readline())
s = [0 for i in range(n+2)]
dp = [0 for i in range(n+2)]
for i in range(n):
    s[i] = int(sys.stdin.readline())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(dp[1], s[0] + s[2], s[1] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 1], (dp[i - 2] + s[i]), (dp[i - 3] + s[i - 1] + s[i]))
print(dp[n-1])