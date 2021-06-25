N, K = list(map(int, input().split()))

for i in range(0, K):       
    if (N % 200) == 0:
        N = int(N / 200)

    else:
        n_str = str(N) + "200"
        N = int(n_str)

print(N)