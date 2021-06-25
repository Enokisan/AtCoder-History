N, Q = map(int, input().split())
A = list(map(int, input().split()))

notA = [n for n in range(1, 10**18) if not (n in A)]
len_notA = len(notA)

for i in range(Q):
    K = int(input())
    print(notA[K-1])