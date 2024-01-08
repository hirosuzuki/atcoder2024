# https://atcoder.jp/contests/abc310/tasks/abc310_b

N, M = [int(x) for x in input().split()]
P: list[int] = []
C: list[int] = []
F: list[set[int]] = []
for i in range(N):
    xs = [int(x) for x in input().split()]
    P.append(xs[0])
    C.append(xs[1])
    F.append(set(xs[2:]))

result = False

for i in range(N):
    for j in range(N):
        if i != j and P[i] >= P[j] and not (F[i] - F[j]):
            if P[i] > P[j] or F[j] - F[i]:
                result = True

if result:
    print("Yes")
else:
    print("No")

