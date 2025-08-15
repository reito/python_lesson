# 回答時間 2:50
# 実力がないうちはかっこつけてスタイリッシュなコードは書こうとしないほうがいい

S = input()

for i in range(len(S)):
  if (i == 0):
    if (S[i] != "<"):
      print("No")
      exit()
  elif (i != len(S) - 1):
    if (S[i] != "="):
      print("No")
      exit()
  else:
    if(S[i] != ">"):
      print("No")
      exit()

print("Yes")