N = int(input())
S = list(input())

for i in range(N):
    if S[i] == "1":
        break

if i % 2 != 0:
    print("Aoki")
else:
    print("Takahashi")