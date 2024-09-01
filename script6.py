import random
from random import randint, randrange

N = int(input())

#カードの数を決める
# a = [[] for _ in range(N)]

# for i in range(0, N):
#     a[i] = randint(1, 100)
#     for j in range(0, i):
#         if a[i] == a[j]:
#             continue
a = list(map(int, input().split()))

#カードを大きい順に並び替える
sort = []
counter = 0

while counter < N:
    max = 0

    for i in range(0, N):
        if a[i] > max:
            max = a[i]
        
    sort.append(max)
    id = a.index(max)
    a[id] = 0
   
    counter += 1

# print(sort)
#Aliceを奇数回目、Bobを偶数回目としてmax値を選んで足していく
Alice = 0
Bob = 0

for i in range(0, N):
    if i % 2 == 0:
        Alice += sort[i]
    else:
        Bob += sort[i]

sub = Alice - Bob
# print(f'差は{sub}点です')
print(sub)