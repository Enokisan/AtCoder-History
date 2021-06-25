import math

N = int(input())
a = list(map(int, input().split()))
if N % 2 == 0:
    k = a[:math.floor(N/2)]
    l = a[math.floor(N/2):]

else:
    k = a[:math.ceil(N/2)]
    l = a[math.floor(N/2):]

l.reverse()
r = 0
for i in range(len(k)):
    if k[i]!=l[i]:
        r += 1

print(math.ceil(r/2))