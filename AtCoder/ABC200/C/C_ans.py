N = int(input())
A = list(map(int, input().split()))
B = [0] * 200  # buccket的に。一時保管用のバケツを用意する。
r = 0

for i in A:
    B[i%200] += 1

for k in range(200):
    r += (B[k]*(B[k]-1))/2

print(int(r))