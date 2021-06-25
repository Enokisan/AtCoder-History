N = int(input())
a = list(map(int, input().split()))

avg = round(sum(a)/len(a))  # round(float)->int 四捨五入
s = 0
for i in range(N):
    s += (a[i]-avg)**2
print(int(s))