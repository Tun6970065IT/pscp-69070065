"""PickThemAgain"""

n = input().split()
have = False
for _ in reversed(n):
    num = int(_)
    if not num % 3 or not num % 5:
        print(_)
    have = True
    if not have:
        print("Nope")
