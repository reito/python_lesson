S = str(input())

if 'eraser' in S:
    S = S.replace('eraser', '')
if 'erase' in S:
    S = S.replace('erase', '')
if 'dreamer' in S:
    S = S.replace('dreamer', '')
if 'dream' in S:
    S = S.replace('dream', '')

if S == '':
    print('YES')
else:
    print('NO')