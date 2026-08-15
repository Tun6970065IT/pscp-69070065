"""walk"""

way = input()
x = 0
y = 0
if "N" in way:
    y +=1
if "E" in way:
    x +=1
if "S" in way:
    y -=1
if "W" in way:
    x -=1
print(f"{x} {y} {abs(x + y)}")
