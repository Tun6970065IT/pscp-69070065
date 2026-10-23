"""CalculatorV2"""

def main():
    """CalculatorV2"""
    n = input()
    num = int(n)
    if num == 1:
        print(1)
    else:
        k = len(n)

        total = num * k
        for i in range(1,k):
            total -= (10**i - 1)

        totalpress = total + num
        print(totalpress)

main()
