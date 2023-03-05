import Variables
ijsje = {}
ijsjes = []
PrintBonnetje = False

print("Welkom bij Papi Gelato")
while not PrintBonnetje:
    ijsje["klant"] = Variables.vraag_klant()
    if ijsje["klant"] == "zakelijk":
        print("testtt")
    elif ijsje["klant"] == "klant":
        ijsje["bolletjes"] = Variables.vraag_bolletjes()
        ijsje["verpakking"] = Variables.vraag_verpakking(ijsje["bolletjes"])
        ijsje["smaakjes"] = Variables.vraag_smaakje(ijsje["bolletjes"])
        ijsje["toppings"] = Variables.vraag_topping(ijsje["bolletjes"])
        ijsje["prijs"] = Variables.bereken_prijs(ijsje,ijsje["klant"])
        PrintBonnetje = Variables.vraag_printbonnetje()
        ijsjes.append(ijsje)
        print(ijsje)

Variables.PrintBonnetje(ijsjes)

