"""รูปดาว"""
def main():
    """รูปดาว"""
    n = int(input())
    print("*" * n)
    if n -2 < 1:
        print("")
    else:
        print("*" * (n-2))
    if n-4 < 1:
        print("")
    else:
        print("*" * (n-4))

main()
