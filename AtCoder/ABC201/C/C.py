import math

def comb(n, r):
    if n-r < 0:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

S = list(input())
n = 10
ab = 0

for i in range(10):
    if S[i] == "x":
        n -= 1
    elif S[i] == "o":
        ab += 1

r = 0
if ab == 0:
    r = n ** 4
elif ab == 4:
    r = 24
elif ab == 3:
    r = 24 * (n-ab) + 12 * ab
elif ab == 2:
    r = 24 * comb(n-ab, 2) + 12 * (n-ab) + 12 * (n-ab) * ab + 6 * comb(ab, 2) + 4 * ab
elif ab == 1:
    r = 24 * comb(n-ab, 3) + 12 * comb(n-ab, 2) + 4 * (n-ab) + 12 * comb(n-ab, 2) * ab + 6 * (n-ab) * ab + 4 * (n-ab) * ab + 1

print(r)

