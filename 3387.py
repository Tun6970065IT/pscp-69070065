"""Tuple"""

def main():
    """Tuple"""
    num = tuple(input().split())
    numneed = input()
    index = num.index(numneed)
    count = num.count(numneed)
    for _ in range(count):
        print(*[index] * count)

main()
