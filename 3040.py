"""exchange money"""

exchange = int(input())
coin10 = exchange // 10
exchange %= 10
coin5 = exchange // 5
exchange %= 5
coin2 = exchange // 2
exchange %= 2
coin1 = exchange
print(f"10 = {coin10}")
print(f"5 = {coin5}")
print(f"2 = {coin2}")
print(f"1 = {coin1}")
