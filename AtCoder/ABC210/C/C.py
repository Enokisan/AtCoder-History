N, K = list(map(int, input().split()))
c  = list(map(int, input().split()))

candies = []
temp = []

for x in c:
    if not x in temp and len(temp) < K:
        temp.append(x)
    else:
        candies.append(len(temp))
        temp.append(x)
        temp = temp[temp.index(x)+1:]

r = min(max(candies), K)

print(r)