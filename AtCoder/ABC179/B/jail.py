N = int(input())
zoro = 0
r = "No"

for i in range(N):
    d1, d2 = map(int, input().split())
    if (d1==d2):
        zoro += 1
    else:
        zoro = 0
    if (zoro==3):
        r = "Yes"

print(r)