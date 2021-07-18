import math
a = list(map(int, input().split()))

x = 2*a[1] - a[0] - a[2]
k = math.ceil((-1) * x / 2)
k = max(0, k)

print(x+3*k)