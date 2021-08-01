import bisect

N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A += [-2*10**9, 2*10**9] # 番兵で端の部分を考慮
A.sort()

ans = 2*10**9

for x in B:
    i = bisect.bisect(A, x)
    ans = min([ans, x-A[i-1], A[i]-x])

print(ans)