"""ARROWaaa"""

tid = input().strip()
n = int(input())

def r_arrow(num):
    """rightarrow"""
    for i in range(num , 0 ,-1):
        space = " " * ((num - i) * 2)
        star = "*" * i
        print(f"{space}{star}")
    for i in range(2 , num + 1):
        space = " " * ((num - i) * 2)
        star = "*" * i
        print(f"{space}{star}")

def l_arrow(num):
    """leftarrow"""
    for i in range(num , 0 ,-1):
        space = " " * (i -1)
        star = "*" * i
        print(f"{space}{star}")
    for i in range(2 , num + 1):
        space = " " * (i - 1)
        star = "*" * i
        print(f"{space}{star}")
for j , char in enumerate(tid):
    if j > 0:
        print()

    if char == "R":
        r_arrow(n)
    elif char == "L":
        l_arrow(n)
