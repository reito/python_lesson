#7分以内に解けなかった
#理由：
# ・条件3の同じ文字が2回ずつでるという条件を時間内に実装できなかった
# ・for i in range(T)と2 * i、2 * i + 1というiのズレ方に注意できてなかった
# ・途中までif文で誤ってnotを使ってしまっていた
# ・andとor逆にしていた
# ・演算子「/」は浮動小数点で返すので、整数で返すときは「//」とするのを失念していた
# ・type...

S = input()
#条件1
if len(S) % 2 != 0:
  print("No")
  exit()

#条件2、#条件3
T = len(S) // 2
l = []
for i in range(T):
  first = 2 * i
  second = 2 * i + 1
  if not(S[first] == S[second] and not (S[first] in l)):
    print("No")
    exit()
  else:
    l.append(S[first])

print("Yes")





