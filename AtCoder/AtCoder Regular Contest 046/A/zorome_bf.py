N = int(input())

cnt = 0 #ゾロ目の出てきた回数

for i in range(1, 555555 + 1):
    si = str(i)
    ok = True
    for s in si:
        if s != si[0]:
            ok = False
    if ok:
        cnt += 1
    if ok and cnt == N:
        ans = i

print(ans)