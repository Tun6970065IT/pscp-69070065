"""ราศี"""

day = int(input())
month = int(input())
if month == 1:
    print("capricorn" if day <= 19 else "aquarius")
elif month == 2:
    print("aquarius" if day <= 18 else "pisces")
elif month == 3:
    print("pisces" if day <= 20 else "aries")
elif month == 4:
    print("aries" if day <= 19 else "taurus")
elif month == 5:
    print("taurus" if day <= 20 else "gemini")
elif month == 6:
    print("gemini" if day <= 21 else "cancer")
elif month == 7:
    print("cancer" if day <= 22 else "leo")
elif month == 8:
    print("leo" if day <= 22 else "virgo")
elif month == 9:
    print("virgo" if day <= 22 else "libra")
elif month == 10:
    print("libra" if day <= 23 else "scorpio")
elif month == 11:
    print("scorpio" if day <= 21 else "sagittarius")
elif month == 12:
    print("sagittarius" if day <= 21 else "capricorn")
