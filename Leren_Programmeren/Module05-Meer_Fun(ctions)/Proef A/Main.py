import Variables
ijsje = {}
ijsjes = []
PrintBonnetje = False

print("Welkom bij Papi Gelato")
while not PrintBonnetje:
    ijsje["klant"] = Variables.vraag_klant()
    if ijsje["klant"] == "zakelijk":
        ijsje["liters"] = Variables.vraag_liter()
        ijsje["smaakjes"] = Variables.vraag_liter_smaakje(ijsje["liters"])
        ijsje["prijs"] = Variables.bereken_prijs(ijsje,ijsje["klant"])
        PrintBonnetje = True
    else:
        ijsje["bolletjes"] = Variables.vraag_bolletjes()
        ijsje["verpakking"] = Variables.vraag_verpakking(ijsje["bolletjes"])
        ijsje["smaakjes"] = Variables.vraag_smaakje(ijsje["bolletjes"])
        ijsje["toppings"] = Variables.vraag_topping(ijsje["bolletjes"])
        ijsje["prijs"] = Variables.bereken_prijs(ijsje,ijsje["klant"])
        PrintBonnetje = Variables.vraag_printbonnetje()
    ijsjes.append(ijsje)

Variables.PrintBonnetje(ijsjes,ijsje["klant"])

