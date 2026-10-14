"""Bus Seat"""

def main():
    """Bus Seat"""
    row = int(input())
    n = int(input())
    broseat = int(input())
    i = 1
    while i <= row:
        j = 1
        s = ""
        while j <= n:
            seat = (j-1) * row + (row - i +1)
            if seat == broseat:
                v = "XX"
            elif seat < 10:
                v = "0" + str(seat)
            else:
                v = str(seat)

            if not s:
                s = v
            else:
                s += " " + v
            j += 1
        print(s)
        if not i % 2 and i < row:
            print()
        i += 1

main()
