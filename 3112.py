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


type_h = 5 * energy_percc
type_o = 3 * energy_percc
type_j = 2 * energy_percc
