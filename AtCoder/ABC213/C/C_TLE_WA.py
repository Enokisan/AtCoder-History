import bisect

H, W, N = list(map(int, input().split()))

A = []
B = []
C = []

for i in range(N):
    ai, bi = list(map(int, input().split()))
    C.append([ai, bi])
    bisect.insort(A, ai)
    bisect.insort(B, bi)

for x in C:
    aa = A.index(x[0]) + 1
    bb = B.index(x[1]) + 1
    print(str(aa) + " " + str(bb))