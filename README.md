# Python Learning Repository

## 📁 ディレクトリ構成

- **contest**: 主にAtCoderのコンテストで実際に記述したもの
- **reviewed**: それらを元に復習して書いたもの

---

# 🐍 AtCoder Python チートシート

## 📋 目次

1. [基本の入出力](#基本の入出力)
2. [基本構文](#基本構文)
3. [データ構造](#データ構造)
4. [標準ライブラリ](#標準ライブラリ)
5. [アルゴリズム](#アルゴリズム)
6. [グラフ・探索](#グラフ探索)
7. [動的計画法 (DP)](#動的計画法-dp)
8. [数学・その他](#数学その他)

---

## 基本の入出力

### 高速入力
```python
import sys
input = sys.stdin.readline  # 末尾改行付き。strip()は必要に応じて
```

### 入力パターン
```python
# 1行1値
n = int(input())

# 1行複数値
a, b = map(int, input().split())

# 配列
A = list(map(int, input().split()))

# 複数行
N = int(input())
B = [int(input()) for _ in range(N)]
```

### 出力パターン
```python
print(x)                        # 改行あり
print(*arr)                     # 配列を空白区切りで
sys.stdout.write(str(x) + "\n") # さらに高速
```

---

## 基本構文

### 変数・型
```python
x = 10
f = 3.14
s = "abc"
b = True
```

### 条件分岐
```python
if x >= 10 and b:
    pass
elif x > 0 or not b:
    pass
else:
    pass
```

### ループ
```python
# for文（rangeは半開区間）
for i in range(5):          # 0..4
    pass
for i in range(2, 10, 2):   # 2,4,6,8
    pass

# while文
cnt = 0
while cnt < 5:
    cnt += 1
```

### リスト内包表記
```python
sq = [i*i for i in range(5)]
pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
```

### 列挙・同時ループ
```python
arr = [5, 2, 9]
for i, v in enumerate(arr):  # (index, value)
    pass

A, B = [1,2,3], [4,5,6]
for a, b in zip(A, B):
    pass
```

---

## データ構造

### リスト・ソート
```python
A = [5, 1, 4, 4]
A.sort()                     # 破壊的昇順
A.sort(reverse=True)         # 降順
A2 = sorted(A, key=lambda x: (x % 2, x))  # 新リスト返す & 複合キー
```

### 集合・辞書
```python
# 集合
S = set([1, 2, 2, 3])
S.add(10)
S.discard(2)
ok = (3 in S)

# 辞書
D = {"a": 1}
D.get("x", 0)  # キーなければ0
```

---

## 標準ライブラリ

### よく使うインポート
```python
from collections import deque, Counter, defaultdict
from itertools import permutations, combinations, product, accumulate
import math
from heapq import heappush, heappop
import bisect
```

### 使用例
```python
# Counter: 頻度カウント
cnts = Counter([1,2,2,3])        # {1:1, 2:2, 3:1}

# accumulate: 累積
prefix = list(accumulate([1,2,3]))  # [1,3,6]
```

---

## アルゴリズム

### 累積和

#### 1次元累積和
```python
def prefix_sum(A):
    ps = [0]*(len(A)+1)
    for i, v in enumerate(A, 1):
        ps[i] = ps[i-1] + v
    return ps
# 区間和 [l, r) は ps[r]-ps[l]
```

#### 2次元累積和
```python
def prefix_sum_2d(G):  # G: HxW
    H, W = len(G), len(G[0])
    ps = [[0]*(W+1) for _ in range(H+1)]
    for i in range(1, H+1):
        row = G[i-1]
        for j in range(1, W+1):
            ps[i][j] = ps[i][j-1] + ps[i-1][j] - ps[i-1][j-1] + row[j-1]
    return ps
# 長方形和 (r1,r2)×(c1,c2) = ps[r2][c2]-ps[r1][c2]-ps[r2][c1]+ps[r1][c1]
```

### 二分探索

#### bisect モジュール
```python
A = [1, 2, 4, 4, 7]
pos_left  = bisect.bisect_left(A, 4)   # 最初の4の位置(=2)
pos_right = bisect.bisect_right(A, 4)  # 4より大きい最初の位置(=4)
```

#### 答えで二分探索
```python
def binary_search_answer(low, high, check):
    """条件を満たす最小値を探す"""
    while low < high:
        mid = (low + high) // 2
        if check(mid):
            high = mid
        else:
            low = mid + 1
    return low
```

### 座標圧縮
```python
def compress(arr):
    xs = sorted(set(arr))
    idx = {x:i for i, x in enumerate(xs)}
    return [idx[x] for x in arr], xs  # 圧縮後, 復元配列
```

---

## グラフ・探索

### BFS（幅優先探索）
```python
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
```

### DFS（深さ優先探索）
```python
# 再帰版
sys.setrecursionlimit(1_000_000)
def dfs_graph_rec(G, v, seen):
    seen[v] = True
    for to in G[v]:
        if not seen[to]:
            dfs_graph_rec(G, to, seen)

# スタック版
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
```

### ダイクストラ法
```python
def dijkstra(G, s):
    """G[u] = [(cost, v), ...]"""
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
```

### Union-Find
```python
class UnionFind:
    def __init__(self, n):
        self.par = [-1]*n  # 親(負ならサイズ)
    
    def find(self, x):
        while self.par[x] >= 0:
            if self.par[self.par[x]] >= 0:
                self.par[x] = self.par[self.par[x]]  # 路圧縮
            x = self.par[x]
        return x
    
    def unite(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.par[a] > self.par[b]:  # サイズが小さい方を親に
            a, b = b, a
        self.par[a] += self.par[b]
        self.par[b] = a
        return True
    
    def same(self, a, b):
        return self.find(a) == self.find(b)
    
    def size(self, x):
        return -self.par[self.find(x)]
```

---

## 動的計画法 (DP)

### 最長増加部分列 (LIS)
```python
def lis_length(A):
    """O(N log N)"""
    dp = []
    for x in A:
        i = bisect.bisect_left(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)
```

### 0/1ナップサック
```python
def knapsack_01(items, W):
    """items: [(w, v), ...], O(N*W)"""
    dp = [-10**18]*(W+1)
    dp[0] = 0
    for w, v in items:
        for cap in range(W, w-1, -1):
            dp[cap] = max(dp[cap], dp[cap-w] + v)
    return max(dp)
```

---

## 数学・その他

### MOD演算
```python
MOD = 10**9 + 7

# べき乗
pow(a, b, MOD)  # a^b mod MOD

# 逆元（MODが素数の場合）
def inv(a, mod=MOD):
    return pow(a, mod-2, mod)
```

### 文字列処理
```python
t = "abca"

# 反転
rev = t[::-1]

# 回文判定
is_pal = (t == t[::-1])

# 文字頻度
freq = Counter(t)
```

### 浮動小数点
```python
def eq(a, b, eps=1e-9):
    """誤差を考慮した比較"""
    return abs(a-b) <= eps
```

### 区間スケジューリング
```python
def max_non_overlapping(intervals):
    """終了時刻でソート"""
    intervals.sort(key=lambda x: x[1])
    res, cur = 0, -10**18
    for l, r in intervals:
        if cur <= l:
            res += 1
            cur = r
    return res
```

---

## グラフ入力テンプレート

### 無向グラフ
```python
def read_graph_undirected(N, M, one_indexed=True):
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        if one_indexed:
            a -= 1; b -= 1
        G[a].append(b)
        G[b].append(a)
    return G
```

### 有向グラフ（重み付き対応）
```python
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
```

---

## メインテンプレート

```python
def main():
    import sys
    input = sys.stdin.readline
    # ここに問題ごとのロジックを書く
    pass

if __name__ == "__main__":
    main()
```