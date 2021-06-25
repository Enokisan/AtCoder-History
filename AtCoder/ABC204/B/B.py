N = int(input())
A = list(map(int, input().split()))

r = 0
for i in range(N):
    if (A[i]<=10):
        continue
    else:
        r += A[i] - 10

print(r)