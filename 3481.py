"""ลอดสะพาน"""

def bridge():
    """ลอดสะพาน"""
    l , n = map(int , input().split())

    bridges = []
    for _ in range(n):
        a , b = map(int , input().split())
        bridges.append((a , b))

    ans = 0

    for x in range( 2 * l + 1):
        pos = x /2
        count = 0

        for a , b in bridges:
            if a < pos < b:
                count += 1
        if count > ans:
            ans = count

    print(ans)

bridge()
