N = int(input())
x = [0] * N
y = [0] * N

for i in range(N):
    x[i], y[i] = map(int, input().split())

count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if (y[j] - y[i]) / (x[j] - x[i]) >= -1 and (y[j]- y[i]) / (x[j] - x[i]) <= 1:
            count += 1

print(count)