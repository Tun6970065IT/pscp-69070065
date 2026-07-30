"""even and odd"""

even = 0
odd = 0
num1 = int(input())
num2 = int(input())
num3 = int(input())

for number in (num1 , num2 , num3):
    if not number % 2:
        odd += 1
    else:
        even += 1
print(odd)
print(even)
