"""ฟิลเตอร์ AR TikTok"""

circle = input()
circle_split = circle.split(" ")
r = int(circle_split[0])
x = int(circle_split[1])
y = int(circle_split[2])
solve = (x**2) + (y**2)
solve_r = r**2
if solve > solve_r:
    print("OUT")
elif solve == solve_r:
    print("ON")
elif solve < solve_r:
    print("IN")
