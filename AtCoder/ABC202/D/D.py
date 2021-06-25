import math

def narabi(a, b):
    return math.factorial(a+b)/(math.factorial(a)*math.factorial(b))

def search(a, b, k, res):
    if a==0:
        for _ in range(b):
            res += "b"
        return res

    if b==0:
        for _ in range(a):
            res += "a"
        return res

    siki = narabi(a-1, b)  # 閾値

    if k == siki:
        res += "a"
        for _ in range(b):
            res += "b"
        for _ in range(a-1):
            res += "a"
        return res

    elif k > siki:  # bが決定
        res += "b"
        search(a, b-1, k-siki, res)
    
    else:
        res += "a"
        search(a-1, b, k, res)

if __name__ == "__main__":
    A, B, K = map(int, input().split())
    res = ""

    print(search(A, B, K, res))