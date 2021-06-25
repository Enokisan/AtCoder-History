A = int(input())  # 500yen
B = int(input())  # 100yen
C = int(input())  # 50yen
X = int(input())  # sum

l = []
res = 0

for i in range(0, A+1):
    for j in range(0, B+1):
        for k  in range(0, C+1):
            price = 500*i + 100*j + 50*k
            l.append(price)

for i in range(0, len(l)-1):
    if l[i] == X:
        res += 1

print(res)