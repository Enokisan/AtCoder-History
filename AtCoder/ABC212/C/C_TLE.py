N, M = list(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

r = float('inf')
c = A+B
c.sort()

for i in range(len(c)-1):
    if (c[i] in A and c[i+1] in B) or (c[i] in B and c[i+1] in A):
        tmp = c[i+1] - c[i]
        if tmp < r:
            r = tmp
print(r)