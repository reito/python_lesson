# 復習2回目だが7分内に解けなかった
理由
・iとjが2つ以上離れている必要があるという条件を見落としていた
・tが1つも含まれていない文字列の場合の処理が抜けていた

S = input()
f_max = 0
l = len(S)

for i in range(l - 2):
  for j in range(i + 2, l):
    if(S[i] == "t" and S[j] == "t") and (j - i) > 1:
      S = S[i : j + 1]
      l = len(S)
      f = (S.count("t") - 2) / (l - 2)
      if(f_max < f):
        f_max = f

print(f_max)
