import math

N = int(input())

x = math.ceil(N/9) #x桁の数
y = N % 9 #ゾロ目の数

if y == 0:
    y = 9

res = ""

for i in range(0, x):
    res += str(y)

print(res)