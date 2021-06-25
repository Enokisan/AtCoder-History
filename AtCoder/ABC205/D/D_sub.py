import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

C = [a-1-i for i, a in enumerate(A)]

for _ in range(Q):
    K = int(input())
    if C[-1] < K:
        print(A[-1]+K-C[-1])
    else:
        i = bisect.bisect_left(C, K)
        print(A[i]-1-C[i]+K)