"""dostring"""

def main():
    """season"""
    m = int(input())
    d = int(input())
    season = " "
    if m <= 3:
        season = "winter"
    elif m <= 6:
        season = "spring"
    elif m <= 9:
        season = "summer"
    elif m <= 12:
        season = "fall"

    if m == 3 and d >=21:
        season = "spring"
    elif m ==6 and d >= 21:
        season = "summer"
    elif m == 9 and d >= 21:
        season = "fall"
    elif m == 12 and d >= 21:
        season = "winter"
    print(season)

main()
