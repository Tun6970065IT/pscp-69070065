"""กองชาม"""

def main():
    """ชามกอง"""
    n = int(input())
    counts = [0] * 301 #สร้างlistเก็บตั้งแต่ 1 ถึง 300
    for _ in range(n):
        size = int(input())
        counts[size] += 1
    max_dish = 0
    for i in counts:
        if i > max_dish:
            max_dish = i
    print(max_dish)

main()
