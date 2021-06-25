N = int(input())
d = {}

for i in range(N):
    S, T = input().split()
    d[S] = int(T)

d.pop(max(d, key=d.get))
print(max(d, key=d.get))