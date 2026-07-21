"""หารลงตัว"""

n1 = int(input())
n2 = int(input())
if n1 and n2 < 0:
    n1 = 0
    n2 = 0
if n1 and n2 >1000:
    n1 = 1000
    n2 = 1000
if not n1 % n2  :
    print("yes")
else:
    print("no")
