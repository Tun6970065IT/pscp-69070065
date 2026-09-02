"""Primenum"""

def primenum():
    """Primenum"""
    num = input()
    num_split = num.split()
    num1 = int(num_split[0])
    num2 = int(num_split[1])
    total = 0
    prime = ""
    for num in range(num1 , num2 + 1):
        if num > 1:
            count = 0
            for _ in range(1,num+1):
                if not num % _:
                    count += 1
            if count == 2:
                total += 1
                if not prime:
                    prime  = str(num)
                else:
                    prime += " " + str(num)
    if not total:
        print(f"Total primes: {total}")
    else:
        print(prime)
        print(f"Total primes: {total}")

primenum()
