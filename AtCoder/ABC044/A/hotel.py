N = int(input())
K = int(input())
X = int(input())
Y = int(input())

res = 0
if N <= K:
    res = N*X
else:
    res = K*X + (N-K)*Y
print(res)