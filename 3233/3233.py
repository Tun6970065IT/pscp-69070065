"""Jackpot"""
def jackpotahh():
    """Jackpot"""
    n1 = input()
    n1_split = n1.split()
    jackpot = n1_split[0]
    jackpotnum = n1_split[1]
    n2 = input()
    n2_split = n2.split()
    buy = n2_split[0]
    buynum = n2_split[1]
    money = ""
    if buy == jackpot and jackpotnum == buynum:
        money = "1000000"
    elif buy != jackpot and jackpotnum == buynum:
        money = "100000"
    elif buy == jackpot and jackpotnum[-3:] == buynum[-3:]:
        money ="2000"
    elif buy == jackpot and jackpotnum[-2:] == buynum[-2:]:
        money = "1000"
    elif buy != jackpot and jackpotnum[-3:] == buynum[-3:]:
        money = "200"
    elif buy != jackpot and jackpotnum[-2:] == buynum[-2:]:
        money = "100"
    elif buy == jackpot:
        money = "20"
    else:
        money = "0"
    print(money)
jackpotahh()
