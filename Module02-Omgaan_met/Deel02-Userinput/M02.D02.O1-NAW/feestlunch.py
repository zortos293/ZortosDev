crossant = int(input("Vul de prijs van de crosanten in (centen) : "))
crossant_aantal = int (input("Vul de aantal crosanten in : "))
stokbrood = int(input("Vul de prijs van stokbrood in (centen) : "))
stokbrood_aantal = int(input("Vul de aantal stokbrood in : "))
korting = int(input("Vul de prijs van de korting in (centen) : "))
korting_aantal = int(input("Vul de aantal kortingsbonnen in : "))


totaal_prijs = crossant *crossant_aantal + stokbrood *stokbrood_aantal
# in totaal prijs
print (f"Prijs in totaal is : {totaal_prijs}")
totaal_met_korting = totaal_prijs - korting *korting_aantal
# prijs met korting
print (f"Prijs met Korting is : {totaal_met_korting}")

print (f"De feestlunch kost je bij de bakker {totaal_met_korting} cent voor de {crossant_aantal} croissantjes en de {stokbrood_aantal} stokbroden als de {korting_aantal} kortingsbonnen nog geldig zijn!")
