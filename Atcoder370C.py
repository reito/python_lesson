# 要素数が同じものの中で辞書順最小のものを選べていないプログラム

S = str(input())
T = str(input())
X = []
counter = 0

for i in range(len(S)):
  if S[i] != T[i]:
    S = list(S)
    S[i] = T[i]
    S = ''.join(S)
    X.append(S)
    counter += 1

list = sorted(X)
print(counter)
for i in range(counter):
  print(list[i])