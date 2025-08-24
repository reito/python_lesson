N, M = map(int, input().split())
S = []
P = [0] * N
L = []

for _ in range(N):
  s = input()
  S.append(s)

# N人がm回投票する
# i回目のN人の投票結果で0と1どちらが多いか
# 配列Sの1からN番目において1回目の投票はS[0][0]~S[N - 1][0]、2回目の投票はS[0][1]~S[N - 1][1]のように考える
for i in range(M):
  # xとyの初期値定義の位置を間違えない！(回数ごとにリセットする必要がある)
  x = 0
  y = 0
  for j in range(N):
    
    if (S[j][i] == "0"):
      x += 1
    elif (S[j][i] == "1"):
      y += 1
    
  if (x == 0 or y == 0):
    # 全員1点加点
    for k in range(N):
      P[k] += 1
  elif (x < y):
    # 0を選んだ人に1点
    for l in range(N):
      if (S[l][i] == "0"):
        P[l] += 1
  else:
    # 1を選んだ人に1点
    for m in range(N):
      if (S[m][i] == "1"):
        P[m] += 1

max_p = max(P)
for n in range(N):
  if (P[n] == max_p):
    L.append(n + 1)

print(*L)