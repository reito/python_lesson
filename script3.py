#1から200から数字を選ぶ
while True:
    n = int(input())
    if n >= 1 and n<=200:
        #1から10^9までの中からn個だけ偶数を選択する
        import random
        from random import randint, randrange
        # Even = randint(1,500000000) * 2
        # print(Even)

        # lists = []
        # for i in range(1, n + 1):
        #     lists.append(randint(1,500000000) * 2)
        lists = list(map(int, input().split())) # 入力を整数型配列として受け取る
        # print(lists)

        #配列の要素をそれぞれ偶数判定し、すべて偶数なら2で割り、そうでないなら止める
        counter = 0
        while True:
            # 偶数でない要素がリストに含まれているか確認
            if any(num % 2 != 0 for num in lists):
                break

            # リストの全ての要素を2で割る
            lists = [num // 2 for num in lists]
            counter += 1

            # print(f"ステップ{counter}:", lists)

        print(counter)
        break
    else:
        continue


#1から10^9までの中から1個だけ偶数を選び表示
# import random
# from random import randint, randrange
# Even = randint(1,500000000) * 2
# print(Even)

#選ばれた偶数が何回2で割れるか調べる
# counter = 0
# num = Even

# while True:

#     if num % 2 == 0:
#         num /= 2
#         counter += 1
#         print(num)
#     else:
#         break

# print(counter)

# #1から10^9までの中からn個だけ偶数を選択する
# import random
# from random import randint, randrange
# # Even = randint(1,500000000) * 2
# # print(Even)

# lists = []
# for i in range(1, n + 1):
#     lists.append(randint(1,500000000) * 2)
# print(lists)

# #配列の要素をそれぞれ偶数判定し、すべて偶数なら2で割り、そうでないなら止める
# counter = 0
# while True:
#     # 偶数でない要素がリストに含まれているか確認
#     if any(num % 2 != 0 for num in lists):
#         break

#     # リストの全ての要素を2で割る
#     lists = [num // 2 for num in lists]
#     counter += 1

#     print(f"ステップ{counter}:", lists)

# print(counter)
# print(f"すべての数が奇数になるまでのステップ数: {counter}")
    # for i in range(0, n):
    #     if lists[i] % 2 == 0:
    #         lists[i] /= 2
    #         print(lists)
    #         counter += 1
    #         print(counter)
    #     else:
    #         break

    # counter += 1

# print(counter)


# lists = [n / 2 for n in lists]