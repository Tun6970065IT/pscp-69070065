"""Coke V2"""

def main():
    """Coke V2"""
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())

    if not d:
        print(0)
    elif not b:
        print(a * d)
    else:
        ex = (d - 1) // b
        lowest_cost = (d - ex) * a + ex * c
        print(lowest_cost)

main()
