N, K = list(map(int, input().split()))
c  = list(map(int, input().split()))

def LIS(L):
    from bisect import bisect_left
    seq = []
    for ai in L:
        pos = bisect_left(seq, ai)
        if len(seq) <= pos:
            seq.append(ai)
        else:
            seq[pos] = ai
    return len(seq)

print(LIS(c))