from collections import deque

n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

time = min(t)
first_index = t.index(time)

s_re = s[first_index:n]+s[0:first_index]
t_re = t[first_index:n]+t[0:first_index]
ans = []

for i in range(n):
    if time+s_re[i-1]<=t_re[i]:
        time += s_re[i-1]
        ans.append(time)
    else:
        time = t_re[i]
        ans.append(t_re[i])

ans = deque(ans[n-first_index:n]+ans[0:n-first_index])

for _ in range(n):
    print(ans.popleft())