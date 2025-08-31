X, Y = map(int, input().split())

a3 = int(str(X + Y)[::-1])
a4 = int(str(Y + a3)[::-1])
a5 = int(str(a3 + a4)[::-1])
a6 = int(str(a4 + a5)[::-1])
a7 = int(str(a5 + a6)[::-1])
a8 = int(str(a6 + a7)[::-1])
a9 = int(str(a7 + a8)[::-1])
a10 = int(str(a8 + a9)[::-1])

print(a10)
