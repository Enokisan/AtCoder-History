K = int(input())
A, B = list(map(int, input().split()))

for i in range(A, B+1):
    ok = False
    if i % K == 0:
        ok = True
        break

if ok:
    print("OK")
else:
    print("NG")