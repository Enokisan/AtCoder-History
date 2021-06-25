import itertools

N, K = list(map(int, input().split()))

D = list(input().split())
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
use_number = list(set(numbers) - set(D))

N_digit = len(str(N))
i = 0
loop = True
mx = 88888  # N < 10000 より払う金額の最大値はこれ

while loop:
    c = itertools.product(use_number, repeat=N_digit+i)  # 重複あり順列N_digit+i個分
    for n in c:
        r = int("".join(n))
        if r >= N and r <= mx:
            loop = False
            mx = r

    i += 1

print(mx)