M = int(input())
S = M
A = []
num = 0

while S > 2 :
  counter = 0
  while True:
    counter += 1
    if 3 ** counter <= S:
      continue
    else:
      counter -= 1
      break
  
  A.append(counter)
  S -= 3 ** counter
  num += 1

if S == 2:
  A.append(0)
  A.append(0)
  num += 2
elif S == 1:
  A.append(0)
  num += 1

print(num)
for i in range(len(A)):
  print(A[i], end=" ")
