n, k = list(map(int, input().split()))
C = list(map(int, input().split()))

color = {}

counter = 0

for i in range(k):
    if C[i] in color:
        color[C[i]] += 1
    else:
        color[C[i]] = 1
        counter += 1

ans = counter

for i in range(n-k):
    if color[C[i]] == 1:
        counter -= 1
        color.pop(C[i])
    else:
        color[C[i]] -= 1

    if C[i+k] in color:
        color[C[i+k]] += 1
    else:
        color[C[i+k]] = 1
        counter += 1
    
    ans = max(ans, counter)

print(ans)