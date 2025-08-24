# N, Q = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# for _ in range(Q):
#   S = 0
#   c, X, V = input().split()
#   if (c == "A"):
#     A[int(X) - 1] = int(V)
#   else:
#     B[int(X) - 1] = int(V)
  
#   for i in range(N):
#     if (A[i] < B[i]):
#       S += A[i]
#     elif (A[i] > B[i]):
#       S += B[i]
#     else:
#       S += A[i]
#   print(S)

# 上のやり方だと計算量がえげつない→さ文を考える
N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = sum(min(a, b) for a, b in zip(A, B))  # 初期値(最初のそれぞれの最小値を計算しておく)

for _ in range(Q):
    c, X, V = input().split()
    X = int(X) - 1
    V = int(V)

    old_min = min(A[X], B[X])

    if c == "A":
        A[X] = V
    else:
        B[X] = V

    new_min = min(A[X], B[X])
    S += new_min - old_min  # 差分だけ反映
    print(S)
