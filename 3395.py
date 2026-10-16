"""เข้าแถว"""

def main():
    """เข้าแถว"""
    _, _ = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in b:
        if i == 1:
            print(0)
        else:
            mx = max(a[:i - 1])
            h = a[i - 1]
            if h > mx:
                print(0)
            else:
                print(mx - h + 1)

main()
