#問題B(実行時エラー)
import sys
S = input()


target = "t"
first = S.find(target)
last = S.rfind(target)
l = last - first + 1



if (first == -1 or (last - first) <= 1):
  f = 0
  print(f)
  sys.exit()

f = (S.count(target, first, last) - 2) / (l - 2)

ts = S[first:last]
tl = len(ts)

for i in range(tl - 2):
  for j in range(i + 2, tl):
    if(tl[i] == 't' and tl[j] == 't'):
      first = i
      last = j
      ts = S[first:last]
      l = last - first + 1
      tc = ts.count(target, first, last)
      tf = (tc - 2) / (l - 2)
      
      if(tf > f):
        f = tf

print(f)