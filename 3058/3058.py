"""BrickBridge"""

a = int(input())
b = int(input())
goal = int(input())

bb_used = min(b , goal // 5)
remain = goal - (bb_used * 5)

if remain <= a:
    print(remain)
else:
    print("-1")
