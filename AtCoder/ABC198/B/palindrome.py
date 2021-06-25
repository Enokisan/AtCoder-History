import re

# 回文判定
def ispalindrome(str): return 1 if str == str[::-1] else 0

N = input()
N = re.sub("0+$", "", N)  # 末尾に0が1回以上続くのを消す

r = ispalindrome(N)
if r:
    print("Yes")
else:
    print("No")