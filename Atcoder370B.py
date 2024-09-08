N = int(input())
data = []

for i in range(1, N + 1):
  row = list(map(int, input().split()))
  data.append(row)

element = 1

for i in range(1, N + 1):
  if element >= i:
    element = data[element - 1][i - 1]
  else:
    element = data[i - 1][element - 1]
print(element)