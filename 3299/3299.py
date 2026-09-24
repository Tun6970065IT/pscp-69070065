"""plantflower"""

def flower():
    """flower"""
    l , n = map(int , input().split())
    first = l * (l  + 1) // 2 #หาจำนวนในแถบแรก
    row = 0
    cross = 0
    while cross < n:
        row += 1
        cross += first + (row - 1) * (l ** 2)
        # แถบถัดไป จะจุได้มากขึ้นทีละ l ** 2 ช่อง
    print(row)
flower()
