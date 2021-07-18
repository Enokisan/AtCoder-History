a = list(map(int, input().split()))
a.sort()

x1 = 2*a[2] - a[1] - a[0]
x2 = 2*a[1] - a[2] - a[0]
avg = a[1] + a[2]
if avg % 2 == 0:
    avg = int(avg / 2 - a[0])
    if x1 >= 0 and x2 >= 0:
        print(min(x1, x2, avg))
    elif x1 < 0 and x2 >= 0:
        print(min(x2, avg))
    elif x1 >= 0 and x2 < 0:
        print(min(x1, avg))
    else:
        print(avg)
else:
    if x1 >= 0 and x2 >= 0:
        print(min(x1, x2))
    elif x1 < 0 and x2 >= 0:
        print(x2)
    elif x1 >= 0 and x2 < 0:
        print(x1)
    else:
        print("error")
