import math

P = int(input())
s = 0

for j in range(10, 0, -1):
    while P >= math.factorial(j):
        P -= math.factorial(j)
        s += 1

print(s)