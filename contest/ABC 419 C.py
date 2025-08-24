import math

N = int(input())
R = []
C = []

for _ in range(N):
  part = input().split()
  r = int(part[0])
  c = int(part[1])
  R.append(r)
  C.append(c)

R_max = max(R)
R_min = min(R)
C_max = max(C)
C_min = min(C)

# かっこのくくり方注意、切り上げするポイントミスってた
Rd = int(math.ceil(abs(R_max - R_min) / 2))
Cd = int(math.ceil(abs(C_max - C_min) / 2))

if (Rd > Cd):
  print(Rd)
elif (Rd < Cd):
  print(Cd)
else:
  print(Rd)