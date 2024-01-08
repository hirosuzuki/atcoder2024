# https://atcoder.jp/contests/abc310/tasks/abc310_a

N, P, Q = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

result = min(P, Q + min(D))
print(result)
