N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_max = max(A)
B_min = min(B)
r = 0

for _ in range(A_max, B_min + 1):
    r += 1

print(r)