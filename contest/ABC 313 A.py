# 10分以内に解けなかった
# Pythonはtrue、falseではなくTrue、False
# 全部同じプログラミング力の時を考慮してなかったから時間かかった

N = int(input())
P = list(map(int, input().split()))

M = P[0]
is_max = True

for i in range(1, len(P)):
  if (M < P[i]):
    M = P[i]
    is_max = False
  elif (M == P[i]):
    is_max = False

if (is_max == True):
  print(0)
else:
  print(M - P[0] + 1)

