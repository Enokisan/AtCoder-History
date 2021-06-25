a, b = list(map(int, input().split()))

seki = a*b
seki = seki % 2

if seki == 0:
    print("Even")
else:
    print("Odd")