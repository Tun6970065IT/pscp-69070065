"""LEFTARROW"""

def arrow():
    """arrow"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for i in range(n):
        long = abs(mid - i)
        print(" " * long + "*" * k)

arrow()
