N = int(input())
s = []
f = []
t = []
time = []

for i in range(N):
    value_s, value_f, value_t = map(int, input().split())
    
    s.append(value_s)
    f.append(value_f)
    t.append(value_t)

for i in range(N):
    time.append(s[i] + f[i] + (24 - t[i]))

print(min(time))
print(max(time))