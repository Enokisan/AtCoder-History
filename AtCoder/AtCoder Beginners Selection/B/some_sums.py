N, A, B = list(map(int, input().split()))

res = 0

for i in range(1, N+1):
    i_str = str(i)
    tmp = 0
    for j in range(0, len(i_str)):  # 格桁の和を求める
        tmp += int(i_str[j])

    if tmp >= A and tmp <= B:
        res += i

print(res)