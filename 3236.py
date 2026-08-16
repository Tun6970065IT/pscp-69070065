"""passfadtek"""

n = int(input())
p1 = input()
p2 = input()
count = 0
for _ in range(n):
    if int(p1[_]) + int(p2[_]) != 9:
        count+=1

if not count:
    print("YES")
else:
    print(f"NO {count}")
