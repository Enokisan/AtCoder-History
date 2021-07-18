import math
A = list(map(int, input().split()))
r = []
totyu = (A[0] + A[2]) / 2
c = A[1] - totyu

if c > 0:
    r.append(int(c*2))

else:
    if (A[0]+A[2]) % 2 == 0:
        r.append(int((-1) * c))
    else:
        c = math.ceil(totyu) - A[1]
        r.append(c)

if A[1]==max(A):
    A.sort()
    totyu = (A[0] + A[2]) / 2
    c = A[1] - totyu

    if c > 0:
        r.append(int(c*2))

    else:
        if (A[0]+A[2]) % 2 == 0:
            r.append(int((-1) * c))
        else:
            c = math.ceil(totyu) - A[1]
            r.append(c)

print(min(r))