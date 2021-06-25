"""
リスト操作をまとめられるときはまとめてしまえ！
boolean使って反転したかどうかを管理すレバいい。
"""

N = int(input())
S = list(input())
Q = int(input())

reverse = False

for i in range(Q):
    T, A, B = map(int,input().split())
    if T==1:
        if not reverse:
            tmp = S[A-1]
            S[A-1] = S[B-1]
            S[B-1] = tmp
        else:
            if A <= N:
                A += N
            else:
                A -= N
            if B <= N:
                B += N
            else:
                B -= N
            tmp = S[A-1]
            S[A-1] = S[B-1]
            S[B-1] = tmp
    else:
        reverse = not reverse

if reverse:
    tmp = S[0:N]
    S[0:N] = S[N:2*N]
    S[N:2*N] = tmp

print("".join(S))