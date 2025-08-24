import math, cmath
a, b, d = map(int, input().split())
cos_d = math.cos(math.radians(d))
sin_d = math.sin(math.radians(d))
c = (a + b * 1j) * (cos_d + sin_d * 1j)

print(c.real, c.imag)