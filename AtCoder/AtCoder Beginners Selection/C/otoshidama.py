N, Y = list(map(int, input().split()))

loop = True
res = ["-1", "-1", "-1"]

for x in range(0, N+1):  # 10,000yen
    if not loop:
        break
    
    yukichi = 10000*x

    for y in range(0, N-x+1):  # 5,000yen
        higuchi = 5000*y

        z = N-x-y  # 1,000yen
        noguchi = 1000*z

        sum = yukichi + higuchi + noguchi

        if sum == Y:
            loop = False
            res[0] = str(x)
            res[1] = str(y)
            res[2] = str(z)
            break

print(" ".join(res))