N = int(input())
r = 0
for A in range(1, N):
    r += (N-1)//A  # A固定でBの数を数える

print(r)