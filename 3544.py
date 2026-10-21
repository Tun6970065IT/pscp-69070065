"""ระบบจัดการคลังสินค้า"""

def main():
    "ระบบจัดการคลังสินค้า"
    stock = {}
    while True:
        line = input()

        if line == "END":
            break
        parts = line.split()
        op = parts[0]
        if op == "ADD":
            items = parts[1]
            amount = int(parts[2])
            stock[items] = stock.get(items , 0) + amount
        elif op == "REMOVE":
            items = parts[1]
            amount = int(parts[2])
            if items in stock and stock[items] >= amount:
                stock[items] -= amount
            else:
                stock[items] = 0
                print(f"Not enough stock for {items}")
        elif op == "CHECK":
            low_stock = sorted([item for item, amount in stock.items() if amount < 5])
            if low_stock:
                for item in low_stock:
                    print(item)
            else:
                print("All stocks are sufficient")
        elif op == "REPORT":
            for i in sorted(stock.keys()):
                count = stock[i]
                print(f"{i}: {count}")

main()
