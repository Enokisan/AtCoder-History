n = list(map(int, input().split()))

for i in range(len(n)):
    n[i] = 7 - n[i]

print(sum(n))
