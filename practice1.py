# ■必須問題（プログラムレベル0）
# 弊社では有志によってワイン会や日本酒会、持ち寄り会などが定期的に開催されている。
# 参加費用は会により異なるが、この日は1人2,000円、5人以上のグループなら一人1,800円、20人以上の団体なら1人1,500円だった。
# 人数をもとに、参加費用の合計を計算する関数 CalculateAttendanceFee を作成せよ。

# #入力の場合
# N = int(input())
# price = 0

# if N < 5:
#     price = 2000
# elif N < 20:
#     price = 1800
# else:
#     price = 1500
# total = price * N

# print(total)

#関数の場合
def CalculateAttendanceFee(N):
    price = 0

    if N < 5:
        price = 2000
    elif N < 20:
        price = 1800
    else:
        price = 1500
    total = price * N
    return total

# print(CalculateAttendanceFee(4))

# ■選択問題２（プログラムレベル1）
# 以下、階乗の仕様を満たす関数 CalculateFactorial を作成せよ。

# 階乗とは、ある数から1までの全ての数を順番に掛け合わせたものです。
# （数学では、この数を n とすると、n の階乗は n! と記述できます。）
# 例えば、3の階乗は3 x 2 x 1で、6になります。
# 特別なルールとして、0の階乗は1と決まっています。

def CalculateFactorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

# print(CalculateFactorial(5))

