N = int(input())
H = list(map(int, input().split()))
T = 0

# Tは1ずつ増え、Tが3の倍数なら体力が残っている最初の敵は3ダメージ、そうでないなら1ダメージ
for i in range(N):
  if H[i] % 5 == 0:
    r = 0
  elif H[i] % 5 == 1:
    r = 1
  elif H[i] % 5 == 2:
    if T % 3 == 2:
      r = 1
    else:
      r = 2
  elif H[i] % 5 == 3:
    if T % 3 == 0:
      r = 3
    elif T % 3 == 1:
      r = 2
    else:
      r = 1
  elif H[i] % 5 == 4:
    if T % 3 == 0:
      r = 3
    else:
      r = 2
  
  T += (H[i] // 5) * 3 + r
  
print(T)

# 以下、実行時間オーバーしたコード
# N = int(input())
# H = list(map(int, input().split()))
# T = 0

# # Tは1ずつ増え、Tが3の倍数なら体力が残っている最初の敵は3ダメージ、そうでないなら1ダメージ
# while len([i for i in H if i > 0]) > 0:
#   T += 1
#   if T % 3 == 0:
#     H[min((i for i in range(N) if H[i] >= 1))] -= 3
#   else:
#     H[min((i for i in range(N) if H[i] >= 1))] -= 1
    
# print(T)

# # 以下もオーバーしたもの
# N = int(input())
# H = list(map(int, input().split()))
# T = 0

# for i in range(N):
#   while H[i] > 0:
#     T += 1
#     if T % 3 == 0:
#       H[i] -= 3
#     else:
#       H[i] -= 1
      
# print(T)