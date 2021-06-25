import numpy
import pandas

H, W = map(int, input().split())
A = []
B = [[0]*W]*H

for i in range(H):
    A.append(list(map(int, input().split())))

for i in range(H):
    for j in range(W):
        B[i][j] = sum(A[i])
