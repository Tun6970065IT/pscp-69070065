"""docstring"""

def main():
    """vat"""
    price = int(input())
    service = price * 0.10
    if service < 50:
        service = 50
    if service > 1000:
        service = 1000
    total_service = service + price
    vat = 0.07 * total_service
    total_vat = vat + total_service
    print(f"{total_vat:.2f}")

main()
