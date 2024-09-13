N = int(input())
A = list(map(int, input().split()))
counter = 0

while len([i for i in A if i > 0]) > 1:
  A = sorted(A, reverse=True)
  A[0] -= 1
  A[1] -= 1
  counter += 1
print(counter)