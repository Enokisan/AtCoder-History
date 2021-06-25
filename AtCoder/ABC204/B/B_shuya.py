N = int(input())
A = list(map(int, input().split()))
kinomi = 0
result = 0
for i in range(N):
    if A[i] <= 10:
        continue
    else:
        kinomi = A[i] - 10
        result += kinomi
print(result)