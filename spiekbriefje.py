# comment
from functools import total_ordering
import math


print("Test")
print('''
long text owo
''')


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
aantal = [3,1,1]
product = ["Appel Sap 200ml","Chips Large","APPELmoes"]
prijs = [1.20,2.20,4.10]

for x in range(len(product)):
    totaal_prijs = round_up(prijs[x] * aantal[x], 2)  
    print(f"{aantal[x]} | {product[x]} | {prijs[x]}$ | {totaal_prijs}$") # format

X = "APPPPELLL"
multiline_xin = F'''mULTIII LINENEEEE
{X}

'''

