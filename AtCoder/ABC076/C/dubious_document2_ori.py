S_dash = input()
T = input()

S = list(S_dash)
que_match = False
back_match = False
front_match = False
rep = False

for i in range(len(S_dash)-1, -1, -1):  # S_dashのヘッダ
    if rep:  # 置換済みなら抜ける
        break

    for j in range(len(T)-1, -1, -1):  # Tのヘッダ
        if rep:
            break

        #  ?にすっぽりおさまる時
        if S_dash[i] == "?":
            que_match = True
            for k in range(0, len(T)):
                if i-k < 0:  # underflow
                    que_match = False
                    break
                if S_dash[i-k] != "?":
                    que_match = False
                    break
                S[i-k] = T[j-k]
        
            if que_match:
                rep = True
                break

        # わかっている文字列とマッチする時
        if S_dash[i] == T[j]:
            back_match = True
            front_match = True

            for b in range(j+1, len(T)):  # Tのヘッダを後ろに動かす
                if i+b-j >= len(S):  # out of range
                    back_match = False
                    break

                if S_dash[i+b-j] != "?" and S_dash[i+b-j] != T[b]:  # not match
                    back_match = False
                    break

                S[i+b-j] = T[b]  # replace

            if not back_match:
                break
            
            for f in range(j-1, -1, -1):  # Tのヘッダを前に動かす
                if i+f-j < 0: # out of range
                    front_match = False
                    break

                if S_dash[i+f-j] != "?" and S_dash[i+f-j] != T[f]:  # not match
                    front_match = False
                    break

                S[i+f-j] = T[f]  # replace
            
            if back_match and front_match:
                rep = True
                break

# ?に全てすっぽり入る場合?

if not rep:  # not match return
    print("UNRESTORABLE")

else:  # ?の処理
    for i in range(0, len(S)):
        if S[i] == "?":
            S[i] = "a"
    print("".join(S))