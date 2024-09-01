N = int(input())
int_list = []
str_list = []

for i in range(N):
    A, S = input().split()
        
    # 数字と文字列をそれぞれのリストに格納
    int_list.append(int(A))
    str_list.append(S)

left_hand = []
right_hand = []

for i in range(N):
    if str_list[i] == 'L':
        left_hand.append(i)
    else:
        right_hand.append(i)

left_distance = 0
right_distance = 0

for i in range(len(left_hand) - 1): 
    left_distance += abs(int_list[int(left_hand[i + 1])] - int_list[int(left_hand[i])])

for i in range(len(right_hand) - 1): 
    right_distance += abs(int_list[int(right_hand[i + 1])] - int_list[int(right_hand[i])])

 
print(left_distance + right_distance)
