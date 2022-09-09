import math
import sys
def round_up(n, decimals=0):
    try:
        multiplier = 10 ** decimals
        return math.ceil(n * multiplier) / multiplier
    except:
        print("An exception occurred")

pizza_small_prijs = 11.60
pizza_medium_prijs = 19.40
pizza_large_prijs = 24.70
try:
    pizza_small_amount = int(input("[-] Hoeveel small pizza's wilt u hebben? : "))
    pizza_medium_amount = int(input("[-] Hoeveel medium pizza's wilt u hebben? : "))
    pizza_large_amount = int(input("[-] Hoeveel Large pizza's wilt u hebben? : "))
except:
    print("kon niet calculeren")
try:
    pizza_small_total_price = pizza_small_prijs * pizza_small_amount
    pizza_medium_total_price = pizza_medium_prijs * pizza_medium_amount
    pizza_large_total_price = pizza_large_prijs * pizza_large_amount
    pizza_total_price = pizza_small_total_price + pizza_medium_total_price + pizza_large_total_price
except:
    print("kan geen letter omzetten in cijvers")
    sys.exit()


print (f"""
U heeft :
=========================================
{pizza_small_amount} Small pizza ({round_up(pizza_small_total_price ,3 )}€)
{pizza_medium_amount} Medium pizza ({round_up(pizza_medium_total_price ,3 )}€)
{pizza_large_amount} Large pizza ({round_up(pizza_large_total_price ,3 )}€)
==========================================
In Totaal kost het : ({round_up(pizza_total_price,3)}€)
""")   
input("press enter key to exit")







