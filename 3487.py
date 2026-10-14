"""ติดตั้งหลอดไฟ"""

def main():
    """ติดตั้งหลอดไฟ"""
    n = int(input())
    height = [int(input()) for _ in range(n)]
    height.sort()
    h = 0
    total = 0
    for i in height:
        h += i
        total += h * 2
    print(total)

main()
