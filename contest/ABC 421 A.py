N = int(input())
S = []
for _ in range(N):
  s = input()
  S.append(s)

X, Y = input().split()
Y = int(Y)

if(S[X - 1] == Y):
  print("Yes")
else:
  print("No")