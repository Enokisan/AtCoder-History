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
r = []
for i in range(len(k)):
    if k[i]!=l[i] and not sorted([k[i], l[i]]) in r:
        r.append(sorted([k[i], l[i]]))
        
print(math.ceil(len(r)/2))

