import math
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
uur = int(input("hoelaat is het in uren : "))
minuten = int(input("hoelaat is het in minuten : "))

uur_in_muten = uur * 60 
minuten_totaal = uur_in_muten + minuten
overgebleven = 1440 - minuten_totaal
restand_tijd = round_up(overgebleven /60, 2)


print(f"je hebt nog {restand_tijd} Uur")