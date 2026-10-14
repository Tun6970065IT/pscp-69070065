"""diff"""

def different():
    """diff"""
    a = int(input())
    b = int(input())
    A_mem = {int(input()) for _ in range(a)}
    B_mem = {int(input()) for _ in range(b)}
    diff = sorted(A_mem - B_mem)
    print(*diff)

different()
