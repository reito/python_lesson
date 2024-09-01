# # N = int(input())
# # p = [list(map(str, input().split())) for _ in range(N)]
# N = int(input())
# t = [0] * N
# x = [0] * N
# y = [0] * N
# for i in range(N):
#     #上から順番に代入していく(t1 = t[0], tN = t[N - 1])
#     t[i], x[i], y[i] = map(int, input().split())

# is_possible = True

# #t1における(x, y)座標の整合性の確認
# if (t[0] % 2) == ((x[0] + y[0]) % 2) and (x[0] + y[0] <= t[0]):
#     for i in range(0, N - 1):
#         if not (((t[i + 1] - t[i]) % 2) == (((x[i + 1] + y[i + 1]) - (x[i] + y[i])) % 2) and ((x[i + 1] + y[i + 1]) - (x[i] + y[i]) <= (t[i + 1] - t[i])) and ((x[i + 1] + y[i + 1]) - (x[i] + y[i]) >= -(t[i + 1] - t[i]))):
#             is_possible = False
#             break
# else:
#     is_possible = False

# if is_possible == True:
#     print('YES')
# else:
#     print('NO')

N = int(input())
t = [0] * N
x = [0] * N
y = [0] * N

for i in range(N):
    t[i], x[i], y[i] = map(int, input().split())

t0 = x0 = y0 = 0
is_possible = True

for i in range(N):
    d = abs(x[i] - x0) + abs(y[i] - y0)
    dt = t[i] - t0

    if (dt - d) % 2 == 1 or d > dt:
        is_possible = False
        break

if is_possible == True:
    print('YES')
else:
    print('NO')