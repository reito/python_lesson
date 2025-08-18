# 配列Aに含まれていない最小の正の整数を求める関数を作れ
# ただし、全て1を下回る場合は1を返す

def solution(A):
    # Implement your solution here
    t = 1
    N = len(A)

    for i in range(N):
        if (t in A):
            t += 1
        else:
            return t