N = int(input())
a = list(map(int, input().split()))
dic = {}

for i in range(N):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

