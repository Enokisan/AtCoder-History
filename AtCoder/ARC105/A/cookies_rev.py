cookies = list(map(int, input().split()))
cookies.sort()
if cookies[0]+cookies[3] == cookies[1] + cookies[2] or cookies[0]+cookies[1]+cookies[2]==cookies[3]:
    print("Yes")
else:
    print("No")