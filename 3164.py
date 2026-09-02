"""ผลรวมของค่าที่มากกว่า"""

n = int(input())
total = 0
output = ""
for _ in range(n):
    num1 = int(input())
    num2 = int(input())
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2
    total += max_num
    if not _:
        output += str(max_num)
    else:
        output += " + " + str(max_num)
if n == 1:
    print(total)
else:
    print(f"{output} = {total}")
