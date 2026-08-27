"""birthday"""

from datetime import date

y1 = int(input())
m1 = int(input())
d1 = int(input())
y2 = int(input())
m2 = int(input())
d2 = int(input())

birth1 = date(y1, m1, d1)
birth2 = date(y2, m2, d2)

result = abs((birth1 - birth2).days)

if result <= 7:
    print(0)
elif birth1 < birth2:
    print(1)
else:
    print(2)
