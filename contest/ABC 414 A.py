#3分以内に解けなかった
#入力方法覚えてなかった

N, L, R = map(int, input().split())
P = 0
for i in range(N):
  X, Y = map(int, input().split())
  if X <= L and R <= Y:
    P += 1

print(P)