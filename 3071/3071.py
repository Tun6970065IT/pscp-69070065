"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

a = int(input())
b = int(input())
d = int(input())
r = int(input())
count = 0
for _ in range(a , b+1):
    if _ % d == r:
        count+=1
print(count)
