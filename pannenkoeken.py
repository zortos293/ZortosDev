import math

pannenkoeken = 1
bloem_gram = 25
eiren = 0.12
melk_ml = 40
theelepel_zout = 0.05
boter_gram = 2.5
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier
vraag_1 = int(input("hoeveel pannenkoeken wil je maken?  : "))
bloem_gram = vraag_1 * bloem_gram
eiren = vraag_1 * eiren
melk_ml = vraag_1 * melk_ml
theelepel_zout = vraag_1 * theelepel_zout
boter_gram = vraag_1 * boter_gram


print(f"""
                    Pannenkoeken Recipe
============================================================
Bloem (gram) : {bloem_gram}       Theelepel zout : {theelepel_zout}
Eiren        : {round_up(eiren,2)}    Boter in Gram  : {boter_gram}
melk in ML   : {melk_ml}
============================================================
""")




