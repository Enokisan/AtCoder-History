N = int(input())
l = list(map(int, input().split()))
res = 0
loop = True

while loop:
    for i in range(0, N):
        if l[i] % 2 == 1:  # odd
            loop = False
            break
        else:  # even
            l[i] = l[i] / 2
    if loop:
        res += 1

print(res)