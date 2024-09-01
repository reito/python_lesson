N, A, B = map(int, input().split())

if A > B:
    A = B
    B = A

sum = 0
for i in range(1, N + 1):
    i

    #万の位
    x = i // 10000
    #千の位
    y = (i - 10000 * x) // 1000
    #百の位
    z = (i - 10000 * x - 1000 * y) // 100
    #十の位
    w = (i - 10000 * x - 1000 * y - 100 * z) // 10
    #一の位
    u = (i - 10000 * x - 1000 * y - 100 * z - 10 * w)

    #各位の和
    s = x + y + z + w + u

    if s >= A and s <= B:
        sum += i

print(sum)