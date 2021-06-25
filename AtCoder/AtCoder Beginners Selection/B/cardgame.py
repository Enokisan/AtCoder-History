N = int(input())
a = list(map(int, input().split()))

alice = 0
bob = 0
while 1:
    if not a:
        break
    m = max(a)
    alice += m
    a.remove(m)

    if not a:
        break
    m = max(a)
    bob += m
    a.remove(m)

res = alice - bob

print(res)
    