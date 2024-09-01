# N, Y = map(int, input().split())

# x = Y // 10000
# y = (Y - 10000 * x) // 5000
# if (Y - 10000 * x - 5000 * y) % 1000 == 0:
#     z = (Y - 10000 * x - 5000 * y) // 1000
# else:
#     x = y = z = -1

# print(x, y, z)

N, Y = map(int, input().split())

x = y = z = -1

for i in range(0, N + 1):
    for k in range(0, N - i + 1):
        if (10000 * i + 5000 * k + 1000 * (N - i - k)) == Y:
            x = i
            y = k
            z = N - i - k
            break

print(x, y, z)