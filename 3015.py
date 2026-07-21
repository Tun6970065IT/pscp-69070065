"""docstring"""

def main():
    """Pro"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    total_price = (z // x) * y + (z % x)
    total_pay = total_price * a
    print(total_pay)

main()
