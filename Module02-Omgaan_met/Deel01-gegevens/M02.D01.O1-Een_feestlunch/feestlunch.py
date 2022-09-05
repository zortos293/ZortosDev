crossant = 0.39
stokbrood = 2.78
korting = 0.50


print (crossant *17 + stokbrood *2 )
totaalprijs = crossant *17 + stokbrood *2
# in totaal prijs
print (f"Prijs in totaal is : {totaalprijs}")
totaalmetkorting = totaalprijs - korting *3
# prijs met korting
print (f"prijs met Korting is : {totaalmetkorting}")

print (f"De feestlunch kost je bij de bakker {totaalmetkorting} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")
