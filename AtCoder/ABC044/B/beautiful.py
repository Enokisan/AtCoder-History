import collections

w = input()

c = collections.Counter(w)  # dict 要素と出現回数
res = "Yes"
for i in c:
    if c[i] % 2 != 0:
        res = "No"
        break
print(res)