import bisect
from collections import deque

H, W, N = list(map(int, input().split()))

A = []
B = []
C = deque()

for i in range(N):
    ai, bi = list(map(int, input().split()))
    C.append([ai, bi])
    bisect.insort(A, ai)
    bisect.insort(B, bi)
    
A = list(dict.fromkeys(A))
B = list(dict.fromkeys(B))

for _ in range(N):
    x = C.popleft()
    aa = bisect.bisect(A, x[0])
    bb = bisect.bisect(B, x[1])
    print(str(aa) + " " + str(bb))