s = list(input())
res = []

for i in range(len(s)):
    q = s[i]
    if q == "0":
        res.append("0")
    elif q == "1":
        res.append("1")
    else:
        res = res[:-1]  # 末尾を削除(popだと空の時にエラー)
print("".join(res))