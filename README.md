contest：主にAtCoderのコンテストで実際に記述したもの

reviewd：それらを元に復習して書いたもの


以下はPythonの基本構文と頻出テンプレ

# =========================================
# AtCoder Python チートシート / テンプレ集
# =========================================

# ---- 基本の入出力（高速I/O） -------------------------
import sys
input = sys.stdin.readline  # 末尾改行付き。strip()は必要に応じて。
# 1行1値
# n = int(input())
# 1行複数値
# a, b = map(int, input().split())
# 配列
# A = list(map(int, input().split()))
# 複数行
# N = int(input())
# B = [int(input()) for _ in range(N)]

# 出力
# print(x)                       # 改行あり
# print(*arr)                    # 配列を空白区切りで
# sys.stdout.write(str(x) + "\n")# さらに速く

# ---- 基本構文 -----------------------------------------
# 変数/型
x = 10
f = 3.14
s = "abc"
b = True

# 条件分岐
if x >= 10 and b:
    pass
elif x > 0 or not b:
    pass
else:
    pass

# for 文（rangeは半開区間）
for i in range(5):          # 0..4
    pass
for i in range(2, 10, 2):   # 2,4,6,8
    pass

# while 文
cnt = 0
while cnt < 5:
    cnt += 1

# 内包表記
sq = [i*i for i in range(5)]
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]

# 列挙・同時ループ
arr = [5, 2, 9]
for i, v in enumerate(arr):  # (index, value)
    pass
A, B = [1,2,3], [4,5,6]
for a, b in zip(A, B):
    pass

# ---- リスト/ソート ------------------------------------
A = [5, 1, 4, 4]
A.sort()                     # 破壊的昇順
A.sort(reverse=True)         # 降順
A2 = sorted(A, key=lambda x: (x % 2, x))  # 新リスト返す & 複合キー

# ---- 集合/辞書 ----------------------------------------
S = set([1, 2, 2, 3])
S.add(10); S.discard(2); ok = (3 in S)
D = {"a": 1}
D.get("x", 0)                # キーなければ0

# ---- 便利標準ライブラリ -------------------------------
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, product, accumulate
import math
from heapq import heappush, heappop
import bisect

# Counter/accumulateの例
cnts = Counter([1,2,2,3])        # 頻度
prefix = list(accumulate([1,2,3]))  # [1,3,6]

# ---- 累積和（1D/2D） ---------------------------------
# 1D: prefix[i] = A[0]+...+A[i-1]
def prefix_sum(A):
    ps = [0]*(len(A)+1)
    for i, v in enumerate(A, 1):
        ps[i] = ps[i-1] + v
    return ps
# 区間和 [l, r) は ps[r]-ps[l]

# 2D 累積和（1-indexで持つと楽）
def prefix_sum_2d(G):  # G: HxW
    H, W = len(G), len(G[0])
    ps = [[0]*(W+1) for _ in range(H+1)]
    for i in range(1, H+1):
        row = G[i-1]
        for j in range(1, W+1):
            ps[i][j] = ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1] + row[j-1]
    return ps
# 長方形和 (r1,r2)×(c1,c2) = ps[r2][c2]-ps[r1][c2]-ps[r2][c1]+ps[r1][c1]  (半開区間想定)

# ---- 二分探索（bisect / 答えで二分） -------------------
# 1) bisect による位置取得（昇順配列）
A = [1, 2, 4, 4, 7]
pos_left  = bisect.bisect_left(A, 4)   # 最初の4の位置(=2)
pos_right = bisect.bisect_right(A, 4)  # 4より大きい最初の位置(=4)
# 2) 条件関数(check)を使った“答えで二分探索”の基本形
def binary_search_answer(low, high, check):
    # 条件: check(x) が False→True に切り替わる単調性があるとき
    # 戻り値: 最小のTrue位置（存在すれば）
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    return low

# 例: 与えた長さでK本以上に切れる最小の長さを求める、など
# def check(x): return 本数 >= K

# ---- グリッド探索（BFS/DFS） --------------------------
# BFS（最短手数）
def bfs_grid(grid, sy, sx, wall="#"):
    H, W = len(grid), len(grid[0])
    INF = 10**18
    dist = [[INF]*W for _ in range(H)]
    q = deque()
    dist[sy][sx] = 0
    q.append((sy, sx))
    while q:
        y, x = q.popleft()
        for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny, nx = y+dy, x+dx
            if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] != wall and dist[ny][nx] == INF:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    return dist

# DFS（再帰 or スタック）
sys.setrecursionlimit(1_000_000)
def dfs_graph_rec(G, v, seen):
    seen[v] = True
    for to in G[v]:
        if not seen[to]:
            dfs_graph_rec(G, to, seen)

def dfs_graph_iter(G, s):
    N = len(G)
    seen = [False]*N
    st = [s]
    seen[s] = True
    while st:
        v = st.pop()
        for to in G[v]:
            if not seen[to]:
                seen[to] = True
                st.append(to)
    return seen

# ---- ダイクストラ（重み非負の最短路） ------------------
def dijkstra(G, s):
    # G[u] = [(cost, v), ...]
    N = len(G)
    INF = 10**18
    dist = [INF]*N
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, v = heappop(pq)
        if d != dist[v]:  # 古いエントリ
            continue
        for c, to in G[v]:
            nd = d + c
            if nd < dist[to]:
                dist[to] = nd
                heappush(pq, (nd, to))
    return dist

# ---- Union-Find（DSU） --------------------------------
class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n  # 親(負ならサイズ)
    def find(self, x):
        while self.par[x] >= 0:
            if self.par[self.par[x]] >= 0:
                self.par[x] = self.par[self.par[x]]  # 路圧縮（手動）
            x = self.par[x]
        return x
    def unite(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.par[a] > self.par[b]:  # (サイズが負なので > が小)
            a, b = b, a
        self.par[a] += self.par[b]
        self.par[b] = a
        return True
    def same(self, a, b):
        return self.find(a) == self.find(b)
    def size(self, x):
        return -self.par[self.find(x)]

# ---- DP 基本形 ----------------------------------------
# 例: 最長増加部分列(LIS)長（O(N log N)）※復元なし
def lis_length(A):
    dp = []
    for x in A:
        i = bisect.bisect_left(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)

# 例: 0/1ナップサック（価値最大） O(N*W)
def knapsack_01(items, W):
    # items: [(w, v), ...]
    dp = [-10**18]*(W+1)
    dp[0] = 0
    for w, v in items:
        for cap in range(W, w-1, -1):
            dp[cap] = max(dp[cap], dp[cap-w] + v)
    return max(dp)

# ---- 座標圧縮 -----------------------------------------
def compress(arr):
    xs = sorted(set(arr))
    idx = {x:i for i, x in enumerate(xs)}
    return [idx[x] for x in arr], xs  # 圧縮後, 復元配列

# ---- 文字列処理 ---------------------------------------
t = "abca"
# 反転
rev = t[::-1]
# 回文判定
is_pal = (t == t[::-1])
# 文字頻度
freq = Counter(t)

# ---- 余り（mod）/ べき乗・逆元 ------------------------
MOD = 10**9 + 7
# a^b mod MOD
# pow(a,b,MOD) は繰り返し二乗法で速い
# 逆元（MODが素数なら a^(MOD-2)）
def inv(a, mod=MOD):
    return pow(a, mod-2, mod)

# ---- 小数点/誤差 --------------------------------------
# 浮動小数の比較には許容誤差を使う
def eq(a, b, eps=1e-9):
    return abs(a-b) <= eps

# ---- パターン: “答えで二分探索”の雛形 -----------------
# 例: 条件を満たす最小/最大の整数解を探す
def lower_bound_ok(lo, hi):
    # Trueになる最小位置
    def ok(x):
        # x が条件を満たすか？
        return True
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

def upper_bound_ok(lo, hi):
    # Falseになる最大位置（True域の直前）を返したい等なら工夫
    pass

# ---- パターン: 多ケース処理 ----------------------------
def main_multi():
    import sys
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        # 各テストケース処理
        pass

# ---- 典型: 区間スケジューリング（終了時刻ソート） ----
def max_non_overlapping(intervals):
    # intervals: [(l, r), ...]
    intervals.sort(key=lambda x: x[1])
    res, cur = 0, -10**18
    for l, r in intervals:
        if cur <= l:
            res += 1
            cur = r
    return res

# ---- 典型: グラフ入力テンプレ --------------------------
def read_graph_undirected(N, M, one_indexed=True):
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        if one_indexed:
            a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)
    return G

def read_graph_directed(N, M, weighted=False, one_indexed=True):
    if weighted:
        G = [[] for _ in range(N)]
        for _ in range(M):
            a, b, c = map(int, input().split())
            if one_indexed:
                a -= 1; b -= 1
            G[a].append((c, b))
        return G
    else:
        G = [[] for _ in range(N)]
        for _ in range(M):
            a, b = map(int, input().split())
            if one_indexed:
                a -= 1; b -= 1
            G[a].append(b)
        return G

# ---- main テンプレ ------------------------------------
def main():
    import sys
    input = sys.stdin.readline
    # ここに問題ごとのロジックを書く
    pass

if __name__ == "__main__":
    # main()
    pass
