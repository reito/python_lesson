# # coding: utf-8
# # 自分の得意な言語で
# # Let's チャレンジ！！
# N, K = map(int, input().split())
# b = [list(map(int, input().split())) for l in range(N)]

# while True:
#     # n個の数値を横向きに入力してリストに格納
#     c = list(map(int, input().split()))

#     # ここで、入力した数が指定数と一致するか確認
#     if len(c) == K:
#         break
#     else:
#         continue

# is_bingo = 0
# c.append(0)
# d1 = []
# d2 = []
# for i in range(N):
#     for j in range(N):
#         if b[i][:] in c:
#             is_bingo += 1
#         if b[:][j] in c:
#             is_bingo += 1
#         if i == j:
#             d1 += [b[i][j]]
#         if i + j == N - 1:
#             d2 += [b[i][N - i - 1]]
# if d1 in c:
#     is_bingo += 1
# if d2 in c:
#     is_bingo += 1
# print(is_bingo)

# 入力の読み込み
N, K = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(N)]

# cの入力を受け取る
while True:
    c = list(map(int, input().split()))
    if len(c) == K:
        break

# ビンゴの数をカウントする
is_bingo = 0
c.append(0)
# 行のビンゴチェック
for i in range(N):
    row = [b[i][j] for j in range(N)]
    if all(num in c for num in row):
        is_bingo += 1

# 列のビンゴチェック
for j in range(N):
    column = [b[i][j] for i in range(N)]
    if all(num in c for num in column):
        is_bingo += 1

# 1つ目の対角線のビンゴチェック
d1 = [b[i][i] for i in range(N)]
if all(num in c for num in d1):
    is_bingo += 1

# 2つ目の対角線のビンゴチェック
d2 = [b[i][N - i - 1] for i in range(N)]
if all(num in c for num in d2):
    is_bingo += 1

# ビンゴの数を出力
print(is_bingo)
