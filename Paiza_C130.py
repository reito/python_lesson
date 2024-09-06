N = int(input())
A = []
B = []

for i in range(N):
    value_a, value_b = map(str, input().split())
    
    A.append(value_a)
    B.append(value_b)

M = 0
c = []

for i in range(N):
    if not A[i] == B[i] == 'y':
        M += 1
        c.append(i + 1)

print(M)
for i in range(M):
    print(c[i])