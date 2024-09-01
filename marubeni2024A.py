N, K=(int(x) for x in input().split())

import itertools

#元の数字をリストに変換
lists = []
for i in range(1, N + 1):
    lists += [i] * K

#すべての順列を生成し、重複を除く
permutations = set(itertools.permutations(lists))

#順列を昇順にソートする
sorted_permutations = sorted(permutations)

#goodな整数列の個数Sを求める
import math

denominator = 1
numerator = 1
# for i in  range(1, N * K + 1):
#     numerator *= i
numerator = math.factorial(N * K)

base = 1
# for i in range(1, K + 1):
#     base *= i
base = math.factorial(K)

for i in range(1, N + 1):
    denominator *= base

S = numerator / denominator

#何番目かを求める
x = (S + 1) // 2

#結果を表示
print(" ".join(map(str, sorted_permutations[int(x - 1)])))





