N = int(input())
d = [int(input()) for i in range(N)]

counter = 0
for i in range(1, int(max(d)) + 1):
    if i in d:
        counter += 1
print(counter)