import math
A, B, C, D = list(map(int, input().split()))

if B-C*D==0:
    print(-1)

else:
    i = A/(C*D-B)
    if i < 0:
            print(-1)
    else:
        print(math.ceil(i))
