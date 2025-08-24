Q = int(input())
nums = []

for _ in range(Q):
  p = input().split()
  first = int(p[0])
  
  if (first == 1):
    nums.append(int(p[1]))
  elif (first == 2):
    m = min(nums)
    print(m)
    nums.remove(m)