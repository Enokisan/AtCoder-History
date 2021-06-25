N, D, H = list(map(int, input().split()))

m = H/D
r = (-1) * m * D + H

for i in range(0, N):
    d, h = list(map(int, input().split()))
    divide = (h-r)/d
    if divide > m:
        m = (H-h)/(D-d)
        r = (-1) * m * D + H

if r<0:
    r = 0

print(r)