"""taxi"""

s = int(input())
if s == 1:
    print(35)
elif s < 1:
    print(0)
elif s <= 10:
    print(35 + (s - 1) * 5)
elif s >10:
    print(35 + (9 * 5) + (s - 10) * 8)
