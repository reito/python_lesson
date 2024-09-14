# 入力の受け取り
N, M = map(int, input().split())
int_list = [[] for _ in range(M)]  # int_list をリストのリストとして初期化
str_list = []
boy_list = []
taro = []

for i in range(M):
    A, B = input().split()
    # 数字をリストに格納
    int_list[i].append(int(A))
    # 文字列をリストに格納
    str_list.append(B)

# 男の子が何番目か特定
for i in range(M):
    if str_list[i] == 'M':
        boy_list.append(i)

# taro を構成する
for j in range(1, N + 1):
    indices = []
    for k in range(len(boy_list)):
        boy_index = boy_list[k]
        # boy_index が int_list のインデックスとして有効であることを確認
        if boy_index < len(int_list):
            # int_list[boy_index] から j のインデックスを探す
            index = next((i for i, num in enumerate(int_list[boy_index]) if num == j), None)
            if index is not None:
                indices.append(boy_index)  # boy_index を記録
    # 最初のインデックスが見つかった場合、そのインデックスを taro に追加
    if indices:
        taro.append(indices[0])

for i in range(N):
  if i in taro:
    print('Yes')
  else:
    print('No')


# N, M = map(int, input().split())
# int_list = []
# str_list = []
# boy_list = []
# taro = []

# for i in range(M):
#     A, B = input().split()
#     # 数字と文字列をそれぞれのリストに格納
#     int_list.append(int(A))
#     str_list.append(B)

# # 男の子が何番目か特定
# for i in range(M):
#   if str_list[i] == 'M':
#     boy_list.append(i)
    
# for j in range(1, N + 1):
#   # taro.append(min(i for i in range(len(boy_list)) if boy_list[i] == j))
#   for k in range(len(boy_list)):
#     index = next((i for i, num in enumerate(int_list[int(boy_list[k])]) if num == j), None)
#   taro.append(index)

# print(taro)

# # for i in range(M):
# #   if i in taro:
# #     print('Yes')
# #   else:
# #     print('No')