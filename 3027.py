"""docstring"""

def main():
    """rapper"""
    space = input()
    price = int(input())
    space_split = space.split(" ")
    x = int(space_split[0])
    y = int(space_split[1])
    z = int(space_split[2])
    lenght = 2*(x+y)*z
    total = lenght * price
    print(lenght)
    print(total)

main()
