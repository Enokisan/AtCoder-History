import math
A = list(map(int, input().split()))
"""
if A[1]==max(A):
    A.sort()
"""

totyu = (A[0] + A[2]) / 2

c = A[1] - totyu

if c > 0:
    print(int(c*2))

else:
    if (A[0]+A[2]) % 2 == 0:
        print(int((-1) * c))
    else:
        c = math.ceil(totyu) - A[1]
        print(c)
