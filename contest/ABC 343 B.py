# 20分以内に解けずRE
# 理由
# ・split()はスペース区切りの入力を前提としていてそぐわなかった
# listに代入するのをN回繰り返せばいい

N = int(input())
A = [[int(x) for x in input().split()] for i in range(N)]

for i in range(N):
  row = []
  for j in range(N):
    if (A[i][j] == 1):
      print(j + 1, end = " ")
  print("")
