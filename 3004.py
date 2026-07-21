"""docstring"""
import math
def main():
    """3D"""
    spot1 = input()
    spot2 = input()
    spot1_split = spot1.split(" ")
    spot2_split = spot2.split(" ")
    x1 = int(spot1_split[0])
    y1 = int(spot1_split[1])
    z1 = int(spot1_split[2])
    x2 = int(spot2_split[0])
    y2 = int(spot2_split[1])
    z2 = int(spot2_split[2])
    solve = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    print(f"{solve:.2f}")

main()
