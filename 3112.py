"""milkteabubble"""
n = input()
n_split = n.split(" ")
energy_type = n_split[0]
energy_percc = int(n_split[1])

x = input()
x_split = x.split(" ")
bb_type = x_split[0]
sweet = x_split[1]
v = int(x_split[2])

lowS = 0
medS = 0
highS = 0
total = 0
type_h = 5 * energy_percc
type_o = 3 * energy_percc
type_j = 2 * energy_percc


if energy_type == "H":
    if bb_type =="R":
        if sweet == "1":
            total = type_h + (12 * v)
            print(total)
        elif sweet =="2":
            total = type_h + (18 * v)
            print(total)
        elif sweet =="3":
            total = type_h + (25 * v)
            print(total)
    elif bb_type =="T":
        if sweet =="1":
            total = type_h + (15 * v)
            print(total)
        elif sweet =="2":
            total = type_h + (20 * v)
            print(total)
        elif sweet =="3":
            total = type_h + (30 * v)
            print(total)
    elif bb_type =="M":
            if sweet =="1":
                total = type_h + (10 * v)
                print(total)
            elif sweet =="2":
                total = type_h + (15 * v)
                print(total)
            elif sweet =="3":
                total = type_h + (20 * v)
                print(total)

elif energy_type == "O":
    if bb_type =="T":
        if sweet == "1":
            total = type_o + (15 * v)
            print(total)
        elif sweet =="2":
            total = type_o + (20 * v)
            print(total)
        elif sweet =="3":
            total = type_o + (25 * v)
            print(total)
    elif bb_type =="T":
        if sweet =="1":
            total = type_o + (15 * v)
            print(total)
        elif sweet =="2":
            total = type_o + (20 * v)
            print(total)
        elif sweet =="3":
            total = type_o + (30 * v)
            print(total)
    elif bb_type =="M":
            if sweet =="1":
                total = type_o + (10 * v)
                print(total)
            elif sweet =="2":
                total = type_o + (15 * v)
                print(total)
            elif sweet =="3":
                total = type_o + (20 * v)
                print(total)

elif energy_type == "J":
    if bb_type =="T":
        if sweet == "1":
            total = type_j + (15 * v)
            print(total)
        elif sweet =="2":
            total = type_j + (20 * v)
            print(total)
        elif sweet =="3":
            total = type_j + (25 * v)
            print(total)
    elif bb_type =="T":
        if sweet =="1":
            total = type_j + (15 * v)
            print(total)
        elif sweet =="2":
            total = type_j + (20 * v)
            print(total)
        elif sweet =="3":
            total = type_j + (30 * v)
            print(total)
    elif bb_type =="M":
            if sweet =="1":
                total = type_j + (10 * v)
                print(total)
            elif sweet =="2":
                total = type_j + (15 * v)
                print(total)
            elif sweet =="3":
                total = type_j + (20 * v)
                print(total)
