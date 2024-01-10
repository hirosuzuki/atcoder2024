# https://atcoder.jp/contests/abc311/tasks/abc311_b

N, D = [int(x) for x in input().split()]
S = [input() for _ in range(N)]

result = 0
r = 0
for row in zip(*S):
    if row.count('o') == N:
        r += 1
    else:
        r = 0
    result = max(result, r)

print(result)
