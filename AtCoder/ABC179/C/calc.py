# TLE

N = int(input())
r = 0
for A in range(1, N):
    for B in range(1, N):
        if N > A * B:
            r += 1
        else:
            break

print(r)
