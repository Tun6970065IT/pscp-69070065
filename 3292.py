"""ARROWaaa"""

def arrow():
    """ARROWaaa"""
    num = int(input())
    for i in range(num , 0 ,-1):
        space = " " * ((num - i) * 2)
        star = "*" * i
        print(f"{space}{star}")
    for i in range(2 , num + 1):
        space = " " * ((num - i) * 2)
        star = "*" * i
        print(f"{space}{star}")
    for i in range(num , 0 ,-1):
        space = " " * (i -1 )
        star = "*" * i
        print(f"{space}{star}")
    for i in range(2 , num + 1):
        space = " " * (i - 1)
        star = "*" * i
        print(f"{space}{star}")
arrow()
