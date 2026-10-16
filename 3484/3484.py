"""หุ่นยนต์เคาะเสียงกระเบื้อง"""

def robot():
    """หุ่นยนต์เคาะเสียงกระเบื้อง"""
    n, p = input().split()
    n = int(n)
    p = float(p)

    grid = []
    for _ in range(n):
        line = input().split()
        while not line:
            line = input().split()
        grid.append(list(map(int, line)))

    col_breaks = [0] * n
    col_points = [0] * n
    total_breaks = 0
    total_points = 0

    for i in range(n):
        row_breaks = 0
        row_points = 0
        for j in range(n):
            x = grid[i][j]
            if x > 0:
                row_breaks += 1
                col_breaks[j] += 1
            row_points += x
            col_points[j] += x
        total_breaks += row_breaks
        total_points += row_points
        print(*grid[i], row_breaks, row_points)

    print(*col_breaks)
    print(*col_points)
    print(total_breaks, total_points, f"{total_points * p:.2f}")

robot()
