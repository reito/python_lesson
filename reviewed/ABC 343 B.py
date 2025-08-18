

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    row = []  # その行の出力をためる
    for j in range(N):
        if A[i][j] == 1:
            row.append(str(j + 1))
    print(" ".join(row))  # 最後にまとめて出力
