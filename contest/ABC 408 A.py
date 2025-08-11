# 5分以内に解けず、実行時エラー
# 理由

# ・typo...
# Nが1の時を考慮していなかった

# 問題のあるコード
# N, S = map(int, input().split())
# T = list(map(int, input().spit()))

# if T[0] >= S + 0.5:
#   print("No")
# else:
#   for i in range(N - 1):
#     if T[i + 1] - T[i] >= S + 0.5:
#       print("No")
#       exit()

# print("Yes")

# 改善したコード

N, S = map(int, input().split())
T = list(map(int, input().split()))

if T[0] >= S + 0.5:
  print("No")
  exit()
else:
  if N == 1:
    print("Yes")
    exit()
  else:
    for i in range(N - 1):
      if T[i + 1] - T[i] >= S + 0.5:
        print("No")
        exit()

print("Yes")