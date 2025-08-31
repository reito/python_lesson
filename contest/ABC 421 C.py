# # AABBBA
# # ABABBA
# # ABABAB
# # 連続する三つについて1、2は同じ、3が違う場合だけ2と3入れ替えるを繰り返す-条件1

# # AAABBB
# # AABABB
# # ABAABB
# # ABABAB

# # 前から条件1に当てはまる部分が出たら入れ替えして再度頭からチェックしていく or 一旦けつまでいくか？

# # AAABABABBBA
# # AABAABABBBA
# # AABABAABBBA
# # AABABABABBA
# # AABABABABAB


# N = int(input())
# S = input()
# count = 0
# count2 = 0

# while (not (S == "AB" * N or S == "BA" * N)):
#   for i in range(N - 2):
#     if (S[i] == S[i + 1] and S[i] != S[i + 2]):
#       ex = S[i + 1]
#       S[i + 1] = S[i + 2]
#       S[i + 2] = ex
#       count += 1
# print(count)
  
  N = int(input())
S = list(input().strip())  # ← 文字列→リストに
count = 0

target1 = "AB" * N
target2 = "BA" * N

while ("".join(S) != target1 and "".join(S) != target2):
    for i in range(len(S) - 2):  # 元のロジックのまま3連続を見る
        if (S[i] == S[i + 1] and S[i] != S[i + 2]):
            # swap
            S[i + 1], S[i + 2] = S[i + 2], S[i + 1]
            count += 1

print(count)




