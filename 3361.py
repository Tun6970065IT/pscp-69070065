"""ขายรถยนต์"""

def car():
    """ขายรถยนต์"""
    n = int(input())
    c = []
    for _ in range(n):
        _ , s = input().split()
        c.append(int(s))

    best = 0
    count = 0
    for i in range(n-1 ,-1,-1):
        if c[i] < best:
            count += 1
        else:
            best = c[i]
    print(count)

car()
