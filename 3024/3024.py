"""dostring"""

def main():
    """Sur"""
    score = float(input())
    Ma = float(input())
    solve = score - (2 * Ma)
    if solve < 0:
        solve = 0
    if Ma - solve > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
