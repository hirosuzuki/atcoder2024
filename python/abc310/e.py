# https://atcoder.jp/contests/abc310/tasks/abc310_e

N = int(input())
S = input()

result = 0
t = 0
f = 0

for i in range(N):
    if S[i] == "0":
        t, f = t + f, 1
        result += t
    else:
        t, f = f + 1, t
        result += t

print(result)
