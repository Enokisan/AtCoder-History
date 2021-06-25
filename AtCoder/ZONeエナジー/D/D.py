S = input()

S_len = len(S)
T = []

for i in range(0, S_len):
    st = S[i]
    if st == "R":
        T.reverse()
    else:
        T.append(st)
    
j = 0
while True:
    if j >= len(T)-1:
        break

    if T[j] == T[j+1]:
        del T[j:j+2]
        if j >= 1:
            j -= 1
    
    else:
        j += 1

print("".join(T))