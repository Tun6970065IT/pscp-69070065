"""ticket"""

ageday = input()
ageday_split = ageday.split()
age = int(ageday_split[0])
day = ageday_split[1]
if age < 5:
    print("0")
if 5 <= age <= 18:
    if day == "Wed":
        print(int(100 / 2))
    else:
        print(100)
elif age > 18:
    if day =="Wed":
        print(int(150 /2))
    else:
        print(150)
