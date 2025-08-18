

def CalculateWineFee(n):
    x = n // 20
    y = (n - 20 * x) // 5
    z = n - 20 * x - 5 * y
    total = 3000 * 20 * x + 3600 * 5 * y + 4000 * z

    return total



def CalculateTaxInclusivePrice(n):
    lists = []
    lists += [round(n * 1.08), round(n * 1.1), round(n * 1.15)]

    return lists


def IsFreeShipping(post_code):
    lists = ['100-0100', '100-0400']

    return not post_code in lists

