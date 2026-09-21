"""RIGHTARROW"""

def arrow():
    """drawrightarrow"""
    k = int(input())
    n = int(input())
    mid = n // 2
    for i in range(n):
        wang = mid - abs(mid - i)
        print(" " * wang + "*" * k)

arrow()
