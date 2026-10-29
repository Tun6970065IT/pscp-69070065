"""hand n legs"""

def main():
    """hand n legs"""
    a = int(input())
    b = int(input())
    if b % 2:
        print("Impossible")
        return
    rab = (b-(2 * a)) // 2
    bird = a -rab
    if rab < 0 or bird < 0:
        print("Impossible")
    else:
        print(f"{rab} {bird}")

main()
