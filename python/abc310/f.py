# https://atcoder.jp/contests/abc310/tasks/abc310_f

N = int(input())
A = [int(x) for x in input().split()]

dp: list[list[int]] = [[0] * 2048 for _ in range(N + 1)]

M = 998244353

for i in range(2048):
    dp[0][1] = 1

for i in range(N):
    a = A[i]
    reva = pow(a, -1, M)
    for s in range(2048):
        for j in range(1, a + 1):
            if j >= 11:
                dp[i + 1][s] = (dp[i + 1][s] + dp[i][s] * reva * (a - 10)) % M
                break
            b = (s << j) & 2047
            dp[i + 1][s | b] = (dp[i + 1][s | b] + dp[i][s] * reva) % M

result = 0
for i in range(1024, 2048): # i & (1 << 10) == 1
    result = (result + dp[N][i]) % M

print(result)
