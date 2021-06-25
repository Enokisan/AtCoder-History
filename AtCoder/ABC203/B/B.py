N, K = list(map(int, input().split()))
r = 0

for i in range(1, N+1):
    for j in range(K):
        r += int(str(i)+"0"+str(j+1))
print(r)