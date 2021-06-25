def is_match(T, S):
    """
    文字列Tが文字列Sにマッチするかを判定する。

    Parameters
    ----------
    T : str
    S : str

    Returns
    -------
    boolean

    """

    for i in range(0, len(S)-len(T)+1):  # Sのi文字目となる部分
        ok = True

        for j in range(0, len(T)):
            if S[i+j] != T[j] and T[j] != ".":  #　.は任意の1文字の文字列
                ok = False
        
        if ok:
            return True
    
    return False

S = input()

C = "abcdefghijklmnopqrstuvwxyz."

M = [] # マッチした列を格納する

for T in C:
    if is_match(T, S):
        M.append(T)

for c1 in C:
    for c2 in C:
        T = c1 + c2
        if is_match(T, S):
            M.append(T)

for c1 in C:
    for c2 in C:
        for c3 in C:
            T = c1 + c2 + c3
            if is_match(T, S):
                M.append(T)

print(len(M))