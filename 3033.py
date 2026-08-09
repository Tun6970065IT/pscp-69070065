"""กระดาษห่อของขวัญ"""

paper = input()
paper_split = paper.split(" ")
r = float(paper_split[0])
h = float(paper_split[1])
s = float(paper_split[2])
wide = h + (r * 2)
long = (2 * 3.14 * r) + s
print(f"{wide:.2f} {long:.2f}")
