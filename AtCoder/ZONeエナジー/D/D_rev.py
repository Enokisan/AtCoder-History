from collections import deque
S = deque()
rev = False

for i in input():
    if i == "R":
        rev = not rev
    elif rev:
        if S and S[0] == i:
            S.popleft()
        else:
            S.appendleft(i)
    else:
        if S and S[-1] == i:
            S.pop()
        else:
            S.append(i)

if rev:
    S = reversed(S)
print("".join(S))
