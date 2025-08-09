S_AB, S_AC, S_BC = map(str, input().split())
Y = []

if S_AB == '<' and S_AC == '<' and S_BC == '<':
  Y.append('C')
  Y.append('B')
  Y.append('A')
elif S_AB == '<' and S_AC == '<' and S_BC == '>':
  Y.append('B')
  Y.append('C')
  Y.append('A')
elif S_AB == '<' and S_AC == '>' and S_BC == '>':
  Y.append('B')
  Y.append('A')
  Y.append('C')
elif S_AB == '>' and S_AC == '<' and S_BC == '<':
  Y.append('C')
  Y.append('A')
  Y.append('B')
elif S_AB == '>' and S_AC == '>' and S_BC == '<':
  Y.append('A')
  Y.append('C')
  Y.append('B')
elif S_AB == '>' and S_AC == '>' and S_BC == '>':
  Y.append('A')
  Y.append('B')
  Y.append('C')

print(Y[1])
