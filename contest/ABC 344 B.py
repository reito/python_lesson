# 20分以内に解けなかった
# N指定なしの複数改行入力の方法を知らなかった
# 配列内要素を逆にする方法を知らなかった

import sys
lines = sys.stdin.read().strip().split('\n')
sub_lines = []

for i in range(len(lines)):
  sub_lines.append(lines[len(lines) - i - 1])

sub_lines = "\n".join(sub_lines)
print(sub_lines)
