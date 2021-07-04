import math

N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
b = sorted(a)
dic = {}
init = K // N
K = K % N

for x in a:
    dic[x] = init

for y in range(K):
    dic[b[y]] += 1

for v in dic.values():
    print(v)