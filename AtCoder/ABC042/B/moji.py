N, L = list(map(int, input().split()))
word = []

for i in range(N):
    s = input()
    word.append(s)

word.sort()
print("".join(word))