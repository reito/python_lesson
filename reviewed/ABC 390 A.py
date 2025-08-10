#注意
# ・Bの初期値気を付ける

A = list(map(int, input().split()))

for i in range(4):
  B = A.copy()
  B[i], B[i + 1] = B[i + 1], B[i]
  if B == [1, 2, 3, 4, 5]:
    print("Yes")
    exit()
    
print("No")