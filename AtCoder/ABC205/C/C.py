A, B, C = map(int, input().split())

A_pow = pow(A, C)
B_pow = pow(B, C)

if A_pow == B_pow:
    print("=")
elif A_pow > B_pow:
    print(">")
else:
    print("<")