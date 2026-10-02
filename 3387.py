"""Tuple"""

def main():
    """Tuple"""
    num = tuple(input().split())
    numneed = input()
    index = num.index(numneed)
    count = num.count(numneed)
    picture = "".join([str(index)] * count)
    for _ in range(count):
        print(picture)

main()
