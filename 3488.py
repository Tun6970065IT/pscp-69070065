"""ไฟส่อง"""

def light():
    """ไฟส่อง"""
    n = int(input())

    fire = [False] * 360

    for _ in range(n):
        a, b = map(int, input().split())
        i = a
        while i != b:
            fire[i] = True
            i = (i + 1) % 360

    if all(fire):
        print(360)
    else:
        best = 0
        current = 0
        for i in range(720):
            if fire[i % 360]:
                current += 1
                best = max(best, current)
            else:
                current = 0
        print(best)

light()
