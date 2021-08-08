N = int(input())
A = list(map(int, input().split()))

B = sorted(A)

for i in range(N):
    if B[N-2] == A[i]:
        print(i+1)
        break