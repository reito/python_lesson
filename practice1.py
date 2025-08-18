
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



def CalculateFactorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial


