"""milkteabubble"""

n = input()
n_split = n.split()
energy_type = n_split[0]
energy_percc = float(n_split[1])

x = input()
x_split = x.split()
bb_type = x_split[0]
sweet = x_split[1]
v = float(x_split[2])

total = 0
if energy_type == "H":
    total = 5 * energy_percc
elif energy_type == "O":
    total = 3 * energy_percc
elif energy_type == "J":
    total = 2 * energy_percc

if bb_type == "T":
    if sweet == "1":
        total += 15 * v
    elif sweet == "2":
        total += 20 * v
    elif sweet == "3":
        total += 30 * v
elif bb_type == "R":
    if sweet == "1":
        total += 12 * v
    elif sweet == "2":
        total += 18 * v
    elif sweet == "3":
        total += 25 * v
elif bb_type == "M":
    if sweet == "1":
        total += 10 * v
    elif sweet == "2":
        total += 15 * v
    elif sweet == "3":
        total += 20 * v

if total.is_integer():
    print(int(total))
else:
    print(total)
