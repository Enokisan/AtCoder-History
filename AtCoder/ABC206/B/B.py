n = int(input())
i=1
r = 0
while True:
    if r >= n:
        break
    r += i
    i += 1
print(i-1)