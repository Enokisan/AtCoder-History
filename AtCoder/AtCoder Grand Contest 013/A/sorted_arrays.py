# Not Completed!!

N = int(input())
A = list(map(int, input().split()))

i = 0
r = 1

while i < len(A)-1:
    
    if A[i] <= A[i+1]:
        i += 1
        continue
    else:
        i += 1
        r += 1
        continue

print(r)