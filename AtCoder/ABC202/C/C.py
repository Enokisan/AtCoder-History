N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

for i in range(N):
    A[i] -= 1
    B[i] -= 1
    C[i] -= 1

num_list = [0] * (10 ** 5)

for i in range(N):
    num_list[B[C[i]]] += 1

res = 0
for x in A:
    res += num_list[x]

print(res)