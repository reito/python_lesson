N, Q = map(int, input().split())
S = input()  
counter = S.count('ABC')
S = list(S) 

for _ in range(Q):
    X, C = input().split()
    X = int(X)  
    counter -= ''.join(S[max(X - 3, 0):X + 2]).count('ABC')
    S[X - 1] = C  
    counter += ''.join(S[max(X - 3, 0):X + 2]).count('ABC')
    print(counter)
