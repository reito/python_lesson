#3分以内に解けなかった
# 理由：
# ・初手で A = list(map(int, input()))としておりsplit()を忘れていた
# ・for文が抜けてた
# ・隣り合う数字を並び替えるという条件を見落としていた
# ・単純に時間が足りなかった

import sys

A = list(map(int, input().split()))
c = 0
for i in range(4):
  if A[i] != i + 1:
    c += 1
    if not(A[i] == i + 2 and A[i + 1] == i):
      sys.exit(print("No"))


if c == 2:
  print("Yes")
else:
  print("No")
