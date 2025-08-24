# AC × 7 TLE × 9

N, M = map(int, input().split())
S = list(input().strip())
T = list(input().strip())
A = []

for _ in range(M):
  parts = input().split()
  L = int(parts[0])
  R = int(parts[1])
  
  for i in range(L, R + 1):
    A = S.copy()
    S[i - 1] = T[i - 1]
    T[i - 1] = A[i - 1]

print("".join(S))