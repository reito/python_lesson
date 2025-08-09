N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

list_A = [0] * N
list_B = [0] * N

for i in range(N):
  list_A[i] = A[i]
  list_B[i] = B[i]
print(max(list_A) + max(list_B))