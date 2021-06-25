S = list(input())

if S[len(S)-1]=="s":
    S.append("es")
else:
    S.append("s")

print("".join(S))