import bisect
from collections import deque
from itertools import filterfalse

def unique_everseen(iterable):
    seen = set()
    seen_add = seen.add
    for element in filterfalse(seen.__contains__, iterable):
        seen_add(element)
        yield element

H, W, N = list(map(int, input().split()))

A = []
B = []
C = deque()

for i in range(N):
    ai, bi = list(map(int, input().split()))
    C.append([ai, bi])
    bisect.insort(A, ai)
    bisect.insort(B, bi)

A = list(unique_everseen(A))
B = list(unique_everseen(B))

for _ in range(N):
    x = C.popleft()
    aa = bisect.bisect(A, x[0])
    bb = bisect.bisect(B, x[1])
    print(str(aa) + " " + str(bb))