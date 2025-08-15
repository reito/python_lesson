#10分以内に解けずWAだった

S = input()

for i in range(len(S)):
  if (i == 0) and S[i] != "<":
    print("No")
    exit()
  elif (i != len(S) - 1) and S[i] != "=":
    print("No")
    exit()
  else:
    if (S[i] != ">"):
      print("No")
      exit()
  
print("Yes")
    