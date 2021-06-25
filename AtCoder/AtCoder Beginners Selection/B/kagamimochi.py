N = int(input())
d = []
for i in range(0, N):
    d.append(int(input()))

res = 0

while d:
    m = max(d)
    d = [i for i in d if i!=m]
    res += 1

print(res)