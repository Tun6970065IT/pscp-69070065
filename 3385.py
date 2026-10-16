"""BusStop I"""

def main():
    """BusStop I"""
    p = int(input())
    n = int(input())

    stops = {}
    while True:
        try:
            sign = input().split()
        except EOFError:
            break
        if not sign:
            continue
        nums = list(map(int, sign))
        stops[nums[0]] = nums[1:]

    bus = []
    count = 0

    for i in range(1, n + 1):
        before = len(bus)
        bus = [d for d in bus if d != i]
        count += before - len(bus)

        for d in stops.get(i, []):
            if len(bus) >= p:
                break
            if d > i:
                bus.append(d)

    print(count)

main()
