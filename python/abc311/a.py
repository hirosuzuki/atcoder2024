# https://atcoder.jp/contests/abc311/tasks/abc311_a

N = int(input())
S = input()

cs: set[str] = set()

result = 0
for c in S:
    cs.add(c)
    result += 1
    if len(cs) >= 3:
        break

print(result)

