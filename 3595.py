"""Meteorite"""

def main():
    """Meteorite"""
    weight = float(input())
    split = int(input())
    safe = float(input())

    rocket = 0
    firstmeteo = 1
    while weight >= safe:
        rocket += firstmeteo
        firstmeteo *= split
        weight /= split
    print(rocket)

main()
