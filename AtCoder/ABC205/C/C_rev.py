A, B, C = map(int, input().split())

if C % 2 == 0:
    x = abs(A) - abs(B)
    if x == 0:
        print("=")
    elif x > 0:
        print(">")
    else:
        print("<")
else:
    if A < 0 and B >= 0:
        print("<")
    elif B < 0 and A >= 0:
        print(">")
    else:
        x = abs(A) - abs(B)
        if x == 0:
            print("=")
        elif x > 0:
            print(">")
        else:
            print("<")