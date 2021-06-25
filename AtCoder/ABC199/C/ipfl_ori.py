N = int(input())
S = list(input())
Q = int(input())

for i in range(Q):
    T, A, B = map(int,input().split())
    if T==1:
        tmp = S[A-1]
        S[A-1] = S[B-1]
        S[B-1] = tmp
    else:
        tmp = S[0:N]
        S[0:N] = S[N:2*N]
        S[N:2*N] = tmp

print("".join(S))