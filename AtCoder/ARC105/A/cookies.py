cookies = list(map(int, input().split()))
r = "No"
if sum(cookies) % 2 == 1:
    r = "No"
else:
    t = sum(cookies) / 2 
    for i in range(1, 4):
        if cookies[0]+cookies[i] == t:
            r = "Yes"
            break
    
print(r)