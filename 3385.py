"""busstop I"""

def main():
    """Busstop I"""
    p= int(input())
    n = int(input())
    s = []
    i = 1
    while i <= n:
        sign = input().split()
        dest = []
        for x in sign:
            dest.append(int(x))
        s.append(dest)
        i += 1

    bus = []
    arr = 0
    current = 1
    while current <= n:
        rem = []
        for d in bus:
            if d == current:
                arr += 1
            else:
                rem.append(d)
        bus = rem
        for d in s[current - 1]:
            if d > current:
                if len(bus) < p:
                    bus.append(d)
        current += 1

    print(arr)

main()
