# https://atcoder.jp/contests/abc310/tasks/abc310_c

N = int(input())
S = [input() for _ in range(N)]

xs: set[str] = set()

for s in S:
    rs = s[::-1]
    if rs < s:
        xs.add(rs)
    else:
        xs.add(s)

print(len(xs))
