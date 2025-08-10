#かかった時間 3:00

N, M = map(int, input().split())
A = list(map(int, input().split()))
S = 0
for i in range(N):
  S += A[i]

if S<= M:
  print("Yes")
else:
  print("No")