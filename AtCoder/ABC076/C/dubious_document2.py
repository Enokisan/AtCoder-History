s = input()
t = input()
 
slen = len(s)
tlen = len(t)
 
if tlen > slen:
    print('UNRESTORABLE')
else:
    for i in range(slen - tlen, -1, -1):
        j = 0
        while j < tlen and (s[i+j] == '?' or s[i+j] == t[j]):
            j += 1
        if j == tlen:
            s = s[:i].replace('?', 'a') + t + s[i+tlen:].replace('?', 'a')
            print(s)
            break
    else:
        print('UNRESTORABLE')