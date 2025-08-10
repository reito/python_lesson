# 復習2回目だが7分内に解けず、実行時エラー

# 理由
# ・iとjが2つ以上離れている必要があるという条件を見落としていた
# ・Sは3文字以上という保証がないという要件を見落としていた
# ・for文内では毎回Sを初期値として代入する必要がある、for文を回すごとに更新されてしまっていた

# 問題のあるコード

# S = input()
# f_max = 0
# l = len(S)

# for i in range(l - 2):
#   for j in range(i + 2, l):
#     if(S[i] == "t" and S[j] == "t") and (j - i) > 1:
#       S = S[i : j + 1]
#       l = len(S)
#       f = (S.count("t") - 2) / (l - 2)
#       if(f_max < f):
#         f_max = f

# print(f_max)

# 再度復習して改善コード

S = input()
f_max = 0
l = len(S)

if l > 2:
  for i in range(l - 2):
    for j in range(i + 2, l):
      if(S[i] == "t" and S[j] == "t") and (j - i) > 1:
        S_sub = S[i : j + 1]
        l_sub = len(S_sub)
        f = (S_sub.count("t") - 2) / (l_sub - 2)
        if(f_max < f):
          f_max = f

print(f_max)