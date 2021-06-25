N, Q = map(int, input().split())
A = list(map(int, input().split()))

notA = [n for n in range(A[0], A[N-1]) if not (n in A)]
len_notA = len(notA)

a = len_notA+A[0]-1

for i in range(Q):
    K = int(input())
    if K <= A[0]-1:
        print(K)
        continue
    elif K <= a:
        print(notA[K-A[0]])
    else:
        print(A[N-1]+K-(a))