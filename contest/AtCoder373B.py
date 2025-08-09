S = input()
d = 0

l = []

for i in range(len(S)):
  l.append([i, S[i]])

l.sort(key=lambda x: x[1])

for i in range(len(S) - 1):
  d += abs(l[i + 1][0] - l[i][0])
  
print(d)