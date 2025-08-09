# パターン：全探索で解く

# 方針
# ・Sの部分文字列を取り出し、最初もしくは最後がtでないならfは0
# ・fを毎回計算し最大値を更新していく

# 例外
# ・Sにtが2つもない
# ・Sが2文字以下

S = input()

l = len(S)
f_max = 0

if l > 2:
  for i in range(l):
    for j in range(i + 2, l):
      if S[i] == "t" and S[j] == "t" and j - i > 1:
        S_sub = S[i:j + 1] #終端インデックスは含まれないので+1する
        f = (S_sub.count("t") - 2) / (j - i - 1)
      
        if f > f_max:
          f_max = f

print(f_max)