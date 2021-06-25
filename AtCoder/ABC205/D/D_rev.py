N, Q = map(int, input().split())
A = list(map(int, input().split()))

notA = [n for n in range(1, A[-1]) if not (n in A)]
len_notA = len(notA)

for i in range(Q):
    K = int(input())
    if K <= len_notA:
        print(notA[K-1])
    else:
        print(A[-1]+K-len_notA)