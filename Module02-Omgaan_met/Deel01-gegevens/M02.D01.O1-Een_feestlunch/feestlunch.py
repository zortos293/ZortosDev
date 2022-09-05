crossant = 0.39
stokbrood = 2.78
korting = 0.50


print (crossant *17 + stokbrood *2 )
totaal_Prijs = crossant *17 + stokbrood *2
# in totaal prijs
print (f"Prijs in totaal is : {totaal_Prijs}")
totaal_met_Korting = totaal_Prijs - korting *3
# prijs met korting
print (f"Prijs met Korting is : {totaal_met_Korting}")

print (f"De feestlunch kost je bij de bakker {totaal_met_Korting} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")
