N = int(input())
A = list(map(int, input().split()))

count = N + (N - 1)


while True:
    for i in range(2, N):
        for j in range(N - i):
            if not int(A[j + i]) - int(A[i]) == i *(int(A[i + 1]) - int(A[i])):
              continue
        count += (N - i)

print(count)
