# 3分以内に解けず実行時エラー
# 理由

# ・copy()の書き方を最初間違えていた
# ・単純に時間が足りなかった
# ・for文で毎回YesとNoを出力していた、Yesの段階で操作は終わらせなきゃいけない
# ・Bに代入するのを忘れていた

# 問題のあるコード

A = list(map(int, input().split()))

for i in range(4):
  B = copy(A)
  if not A[i] == i + 1:
    A[i], A[i + 1] = A[i + 1], A[i]
    if B == [1, 2, 3, 4, 5]:
      print("Yes")
    else:
      print("No")

# 改善したコード

A = list(map(int, input().split()))

for i in range(4):
  B = A.copy()
  if not B[i] == i + 1:
    B[i], B[i + 1] = B[i + 1], B[i]
    if B == [1, 2, 3, 4, 5]:
      print("Yes")
      exit()

print("No")