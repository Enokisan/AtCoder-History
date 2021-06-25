from operator import mul
from functools import reduce

def comb(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

n = int(input())
l = list(map(int, input().split()))
dic = {}

for i in l:
    if i in dic.keys():
        dic[i] += 1
    else:
        dic[i] = 1

v = list(dic.values())
s = sum(v)
r = 0


for i in v:
    if i > 1:
        r -= comb(i, 2)

print(comb(s, 2)+r)