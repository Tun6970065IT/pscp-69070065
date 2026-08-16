"""passfadtek"""

n = int(input())
p1 = input()
p2 = input()
count = 0
for _ in range(n):
    if int(p1[_]) + int(p2[_]) ==9:
        print("YES")
    else:
        count +=1
        print(f"NO {count}")
