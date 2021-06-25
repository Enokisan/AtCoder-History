N = int(input())
A = list(map(int, input().split()))

r = 0

for i in range(N - 1):
    for j in  range(i+1, N):
        d = A[i] - A[j]

        if d % 200 == 0:
            r += 1

print(r)