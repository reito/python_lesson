# 必須問題１（プログラムレベル１）】
# 弊社では有志によってワイン会や日本酒会、持ち寄り会などが定期的に開催されている。
# この日のために、とある通販サイトでワインを購入することにした。通常は1本4,000円、5本単位だと1本あたり3,600円、20本単位だと1本あたり3,000円だった。
# ワインの購入本数をもとに、商品の合計金額を計算する関数 CalculateWineFee を作成せよ。
# 　※n本「以上」ではないことに注意すること。

def CalculateWineFee(n):
    x = n // 20
    y = (n - 20 * x) // 5
    z = n - 20 * x - 5 * y
    total = 3000 * 20 * x + 3600 * 5 * y + 4000 * z

    return total

# print(CalculateWineFee(10))

# 選択問題B　税込金額算出】
# [税抜価格の商品金額]を税率8%、10%、15%でそれぞれの[税込価格の商品金額]を算出し、
# 結果を配列に格納する関数 CalculateTaxInclusivePrice を作成せよ。

# ※関数の引数には[税抜価格の商品金額]を指定すること
# ※[税込価格の商品金額]は四捨五入すること
# 　※ヒント：四捨五入は言語で用意している関数を利用してもよいが、不明な場合は0.5を足してから切り捨てることでも実現してもよい。

# 入出力例） ※C#の場合　引数：decimal(第1引数)　戻り値：decimal[]
# CalculateTaxInclusivePrice(100) -> [108, 110, 115]
# CalculateTaxInclusivePrice(120) -> [130, 132, 138]

def CalculateTaxInclusivePrice(n):
    lists = []
    lists += [round(n * 1.08), round(n * 1.1), round(n * 1.15)]

    return lists

# print(CalculateTaxInclusivePrice(120))

# 選択問題C　配送料判定】
# [商品小計(税込)]が5,000円(税込)以上で配送料無料となる仕組みを作成したい。
# 配送料が無料となる判定結果を真偽値（true：配送料無料、false：配送料無料の対象外）で返却する関数 IsFreeShipping を作成せよ。
# ※ただし、離島は配送料無料の対象外とする。
# 　離島かどうかの判定は郵便番号を用いる。この問題では郵便番号が "100-0100"(東京都大島町) および "100-0400"(東京都新島村) の場合だけ離島扱いとする(郵便番号はハイフンなしも許容) 。
# 　判定に用いる郵便番号は増えることも想定し、配列で定義しておくこと。

def IsFreeShipping(post_code):
    lists = ['100-0100', '100-0400']

    return not post_code in lists
# print(IsFreeShipping('100-0100'))
