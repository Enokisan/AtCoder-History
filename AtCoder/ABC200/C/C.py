# sysの方が速いらしい
def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    r = 0
    
    for i in range(0, N-1):
        ai = A[i]
        for x in set(A[i+1:N]):  # index指定より早いらしい
            d = (ai - x) % 200
            if d == 0:
                r += 1
    print(r)

main()