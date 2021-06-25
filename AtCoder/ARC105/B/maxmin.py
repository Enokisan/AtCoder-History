import math

N = int(input())
a = list(map(int, input().split()))

ans = a[0]
for i in range(0, N-1):
    ans = math.gcd(ans, a[i+1])
print(ans)