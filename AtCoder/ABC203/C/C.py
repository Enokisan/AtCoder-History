N, K = list(map(int, input().split()))
friends = [0]*(10**4)
res = 0

for i in range(N):
    A, B = list(map(int, input().split()))
    friends[A] += B

while K > 0:
    res += 1
    K -= 1
    K += friends[res]

print(res)