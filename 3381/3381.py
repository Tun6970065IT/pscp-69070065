"""Point Sorting"""

def main():
    """Point Sorting"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            line = ""
        while not line:
            line = input().strip()
            xny = input().split()
            x = int(xny[0])
            y = int(xny[1])
            points.append((x , y))
        points.sort(key=lambda p: (p[0] + p[1], - p[1]))
        for x , y in points:
            print(x , y)

main()
