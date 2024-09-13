N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []

for i in range(N - K, N):
  B.append(A[i])

for i in range(N - K):
  B.append(A[i])

print(*B)