import math

N = int(input())
C = list(map(int, input().split()))
mod = 1000000007

C.sort()
r = 1

for i in range(N):
    r = (r * (C[i]-i)) % mod
print(r)