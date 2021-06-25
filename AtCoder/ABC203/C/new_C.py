N, K = list(map(int, input().split()))
ABdict = {}

for i in range(N):
    A, B = list(map(int, input().split()))
    if A in ABdict:
        ABdict[A] = B + ABdict[A]
        continue
    ABdict[A] = B

ABdict = sorted(ABdict.items(), key=lambda x:x[0])

for i in range(len(ABdict)):
    if K >= ABdict[i][0]:
        K += ABdict[i][1]
        continue
    else:
        break

print(K)