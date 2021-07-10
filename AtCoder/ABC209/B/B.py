N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

for i in range(N):
    if (i+1) % 2 == 0:
        A[i] = A[i] - 1

if sum(A)<=X:
    print("Yes")
else:
    print("No") 