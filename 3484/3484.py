"""หุ่นยนต์เคาะเสียงกระเบื้อง"""

def robot():
    """หุ่นยนต์เคาะเสียงกระเบื้อง"""
    n, p = input().split()
    n = int(n)
    p = float(p)

    a = []
    total_tiles = 0
    total_points = 0

    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)

        tiles = 0
        points = 0

        for x in row:
            if x > 0:
                tiles += 1
            points += x

        total_tiles += tiles
        total_points += points

        print(*row, tiles, points)

    for j in range(n):
        tiles = 0
        for i in range(n):
            if a[i][j] > 0:
                tiles += 1
        print(tiles, end=" ")
    print()

    for j in range(n):
        points = 0
        for i in range(n):
            points += a[i][j]
        print(points, end=" ")
    print()

    print(total_tiles, total_points, f"{total_points * p:.2f}")

robot()
