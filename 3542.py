"""CalculatorV2"""

def main():
    """CalculatorV2"""
    n = int(input())
    if n == 1:
        print(1)
    else:
        totalpress = 0
        total = 0
        for i in range(1 , n + 1):
            totalpress += len(str(i))
        plus = n -1
        anspress = 1
        total = totalpress + plus + anspress
    print(total)

main()
