"""ตำบลกระสุนตก"""

def main():
    """ตำบลกระสุนตก"""
    n = int(input())
    data = []

    for _ in range(n):
        x , y ,d = map(int , input().split())
        data.append((x , y ,d))

    found = False

    for i in range(1000):
        for j in range(1000):
            ok = True

            for x , y ,d in data:
                if (i - x)**2 + (j - y)**2 != d ** 2:
                    ok = False
                    break
            if ok and not found:
                print(i , j)
                found = True

main()
