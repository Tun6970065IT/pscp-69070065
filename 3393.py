"""Cave Explorer"""

def main():
    """Cave Explorer"""
    n = int(input())
    Map = list(map(int , input().split()))
    direct = input().strip()

    start = Map.index(1)
    chest = Map.index(2)

    for c in direct:
        if c == "R" and start + 1 < n:
            start += 1
        elif c == "L" and start - 1 >= n:
            start -= 1

        if start == chest:
            break

    result = [0] * n
    result[chest] = 2
    result[start] = 1
    print(*result)

main()
