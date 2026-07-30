"""temp change"""

temp = float(input())
unit = input()
uneed = input()
c = " "

if unit == "C":
    c = temp
elif unit == "K":
    c = temp - 273.15
elif unit == "F":
    c = (temp - 32) * 5/9
elif unit == "R":
    c = temp * 5/9 - 273.15
ans = " "
if uneed == "C":
    ans = c
elif uneed == "K":
    ans = c + 273.15
elif uneed == "F":
    ans = c * 9/5 + 32
elif uneed == "R":
    ans = (c + 273.15) * 9/5

print(f"{ans:.2f}")
