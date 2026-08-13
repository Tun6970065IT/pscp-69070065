"""castle"""

n = int(input())
line = 0
x = 1
y = 1
for _ in range(1,n):
    if _ == x:
        line += 1
        x += y + 2
        y += 2
if line % 2 == 1:
    if not n %2:
        print(line * 2)
    elif n % 2 == 1:
        print(line *2 -1)
elif not line % 2:
    if not n % 2:
        print(line * 2 -1)
    elif n % 2 == 1:
        print(line * 2)
