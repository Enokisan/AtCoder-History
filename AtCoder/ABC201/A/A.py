A = list(map(int,input().split()))

if 2*A[0] == A[1]+A[2]:
    print("Yes")
elif 2*A[1] == A[0]+A[2]:
    print("Yes")
elif 2*A[2] == A[0]+A[1]:
    print("Yes")
else:
    print("No")