"""ช่วย List Prime (Sieve of Eratosthenes)"""

def main():
    """ช่วย List Prime (Sieve of Eratosthenes)"""
    num = int(input())
    prime_list = []
    primenum = True
    for i in range(2 , num +1):
        for j in prime_list:
            if not i % j:
                primenum = False
                break
            primenum = True
        if primenum:
            prime_list.append(i)
    if num in prime_list:
        print("Yes")
        print(*prime_list)
    else:
        print("No")

main()
