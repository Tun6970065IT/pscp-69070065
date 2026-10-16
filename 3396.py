"""แซงรอบ"""

def main():
    """แซงรอบ"""
    n , k = map(int , input().split())
    s = [int(input()) for _ in range(n)]

    m = min(s)
    ended = k * m

    count = 0
    for i in s:
        if (k -1) * i < ended:
            count += 1

    print(count)

main()
