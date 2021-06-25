import math

N, K = list(map(int, input().split()))
A_list = []
median_index = math.floor((K**2)/2)+1

for i in range(N):
    A = list(map(int, input().split()))
    A_list.append(A)

i = 0
median_list = []
while i+K-1 < N:
    tmp = A_list[i]
    for j in range(K):
        median_list.append(tmp[j])
    for 

