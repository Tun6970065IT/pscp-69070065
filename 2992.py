"""docstring"""

def main():
    """change"""
    num = int(input())
    if num < 10:
        num = 10
    oper = input()
    back =int(str(num)[::-1])
    solve1 = num + back
    solve2 = num * back
    if oper == "+":
        print(f"{num} + {back} = {int(solve1)}")
    if oper == "*":
        print(f"{num} * {back} = {int(solve2)}")

main()
