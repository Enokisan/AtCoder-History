x = list(input())
r = [False, False, False]

if x[0] == x[1] and x[2] == x[3] and x[0] == x[2]:
    r = [True, True, True]
else:
    for i in range(3):
        if x[i] == "9" and x[i+1] == "0":
            r[i] = True
            continue
        elif int(x[i])+1 == int(x[i+1]):
            r[i] = True
            continue

if all(r):
    print("Weak")
else:
    print("Strong")