x = list(input())
r = False

if x[0] == x[1] and x[2] == x[3] and x[0] == x[2]:
    r = False
else:
    for i in range(3):
        if (x[i]=="9" and x[i+1]=="0") or int(x[i])+1 == int(x[i+1]):
            r = True
            break

if r:
    print("Strong")
else:
    print("Weak")