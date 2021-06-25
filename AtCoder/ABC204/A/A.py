a = list(map(int, input().split()))

if (a[0]==a[1]):
    print(a[0])
elif not (0 in a):
    print(0)
elif not (1 in a):
    print(1)
else:
    print(2)