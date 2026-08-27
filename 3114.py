"""Suvarnabhumi Airport Parking"""
def airport():
    """Suvarnabhumi Airport Parking"""
    time_in = float(input())
    time_out = float(input())
    Hour1 = int(time_in)
    m1 = round((time_in - Hour1) * 100)
    Hour2 = int(time_out)
    m2 = round((time_out - Hour2) * 100)
    park_start = (Hour1 * 60) + m1
    park_end = (Hour2 * 60) + m2
    solve = park_end - park_start
    if Hour1 >= 24 or Hour2 >= 24 or m1 >= 60 or m2 >= 60:
        print("ERROR")
    elif Hour1 < 0 or Hour2 < 0 or solve < 0:
        print("ERROR")
    elif solve <= 15:
        print("FREE")
    elif 15 < solve <= 60:
        print(25)
    elif 60 < solve <= 120:
        print(50)
    elif 120 < solve <= 180:
        print(80)
    elif 180 < solve <= 240:
        print(110)
    elif 240 < solve <= 300:
        print(145)
    elif 300 < solve <= 360:
        print(180)
    elif 360 < solve <= 1440 :
        print(250)
    else:
        print("ERROR")
airport()
