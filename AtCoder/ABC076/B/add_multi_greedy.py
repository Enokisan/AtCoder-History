#  Greedy

N = int(input())  # 操作回数
K = int(input())  # 操作Bで足す値

m = 1  # 初期値

for i in range(0, N):
    if m*2 <= m+K:
        m = m*2
        continue
    else:
        m += K
        continue

print(m)