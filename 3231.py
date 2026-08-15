"""GuessTao"""

g = int(input())
r = int(input())
if 1 < g > 6 or 1 < r > 6:
    print("Invalid")
elif 1 <= g <= 6  and 1 <= r <= 6:
    if g == r:
        print("Correct!")
    elif g != r:
        print("Wrong!")
