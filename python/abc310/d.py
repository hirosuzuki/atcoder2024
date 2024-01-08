# https://atcoder.jp/contests/abc310/tasks/abc310_d

N, T, M = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]

vab: dict[int, int] = dict((i + 1, 0) for i in range(N))

for a, b in AB:
    vab[a] |= 1 << (b-1)
    vab[b] |= 1 << (a-1)

dp: list[list[list[int]]] = [[[] for _ in range(N + 1)] for _ in range(T + 1)]

x = 0

for i in range(1, N + 1):
    if x & vab[i]:
        break
    x |= 1 << (i - 1)
    dp[1][i] = [[x]]

for i in range(2, T + 1):
    for j in range(i, N + 1):
        x = [xs + [1 << (j - 1)] for xs in dp[i - 1][j - 1]]
        for xs in dp[i][j - 1]:
            for k in range(len(xs)):
                if not (xs[k] & vab[j]):
                    x.append(xs[:k] + [xs[k] | 1 << (j - 1)] + xs[k + 1:])
        dp[i][j] = x

print(len(dp[T][N]))
