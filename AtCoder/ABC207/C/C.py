N = int(input())
l = []
s = 0

for _ in range(N):
    x = list(map(int, input().split()))
    l.append(x)

for i in range(0, N-1):
    if l[i][0] == 1:
        for j in range(i+1, N):
            if l[j][1]<l[i][1] and l[i][2] < l[j][2]:
                s += 1
                continue
            if l[j][0] == 1:
                if l[i][1]<=l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<=l[i][2]:
                    s += 1
            elif l[j][0] == 2:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<=l[i][2]:
                    s += 1
            elif l[j][0] == 3:
                if l[i][1]<=l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 4:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
    elif l[i][0] == 2:
        for j in range(i+1, N):
            if l[j][1]<l[i][1] and l[i][2] < l[j][2]:
                s += 1
                continue
            if l[j][0] == 1:
                if l[i][1]<=l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 2:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 3:
                if l[i][1]<=l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 4:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
    elif l[i][0] == 3:
        for j in range(i+1, N):
            if l[j][1]<l[i][1] and l[i][2] < l[j][2]:
                s += 1
                continue
            if l[j][0] == 1:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<=l[i][2]:
                    s += 1
            elif l[j][0] == 2:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<=l[i][2]:
                    s += 1
            elif l[j][0] == 3:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 4:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
    elif l[i][0] == 4:
        for j in range(i+1, N):
            if l[j][1]<l[i][1] and l[i][2] < l[j][2]:
                s += 1
                continue
            if l[j][0] == 1:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 2:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 3:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1
            elif l[j][0] == 4:
                if l[i][1]<l[j][2]<=l[i][2] or l[i][1]<=l[j][1]<l[i][2]:
                    s += 1

print(s)