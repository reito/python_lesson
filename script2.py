# number = str(input())
# print(number.count('1'))

# 文字列の入力を受け取る
s = input()

# カウンタを初期化
counter = 0

# 文字列の各文字をチェック
if s[0] == '1':
    counter += 1
if s[1] == '1':
    counter += 1
if s[2] == '1':
    counter += 1

# 結果を出力
print(counter)
