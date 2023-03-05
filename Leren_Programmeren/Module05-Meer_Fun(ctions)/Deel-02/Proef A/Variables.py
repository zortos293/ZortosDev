
BOLLETJES_PRIJS = 1.10
HOORNTJES_PRIJS = 1.25
BAKJES_PRIJS = 0.75
SLAGROOM_PRIJS = 0.50
SPRINKELS_PRIJS = 0.30
CARAMEL_SAUS_HOORNTJE_PRIJS = 0.90
CARAMEL_SAUS_BAKJE_PRIJS = 0.90
smaakjes = (
    "Chocolade", 
    "Vanille",
    "Munt",
    "Aardbei",
)
toppings = (
   "Slagroom" ,
   "Sprinkels" ,
   "Caramel Saus",
)


#
#ijs_verpakking = {
#    "hoorntjes": 0,
#    "bakjes": 0
#}
#toppings = {
#    "T.Slagroom" : 0,
#    "T.Sprinkels" : 0,
#    "T.Caramel Saus": 0,
#}


def vraag_bolletjes() -> int:
    while True:
        Amount_question = int(input("Hoeveel bolletjes wilt u?\n> "))
        if Amount_question > 8:
            print("Sorry, dat is te veel.")
        elif Amount_question <= 8:
            return Amount_question
        else:
            print("Sorry, dat begrijp ik niet.")

def vraag_verpakking(amount_bolletje) -> str:
    while True:
        Question = input(f"Wilt u deze {amount_bolletje} bolletje(s) in een hoorntje of een bakje?\n> ")
        if Question.lower() == "hoorntje":
            print(f"Hier is uw hoorntje met {amount_bolletje} bolletje(s).")
            return "hoorntje"
        elif Question.lower() == "bakje":
            print(f"Hier is uw bakje met {amount_bolletje} bolletje(s).")
            return "bakje"
        else:
            print("Sorry, dat begrijp ik niet.")



def vraag_smaakje(amount_bolletjes) -> list:
    list_smaak = []
    for x in range(amount_bolletjes):
        while True:
            smaak = input(f"wat voor smaak wilt u voor uw {x+1} de bolletje? ({' '.join(smaakjes)} geen) \n>")
            if smaak in smaakjes:
                list_smaak.append(smaak)
            else:
                print("Sorry, dat begrijp ik niet.")
    return list_smaak

def vraag_topping(amount_bolletjes) -> list:
    list_topping = []
    for x in range(amount_bolletjes):
        while True:
            topping = input(f"Wilt u topping voor uw {x+1} de bolletje? {' '.join(toppings)} \n>")
            if topping in toppings or topping.lower() == "geen":
                list_topping.append(topping)
                break
            else:
                print("Sorry, dat begrijp ik niet.")
    return list_topping

def bereken_prijs(ijsje) -> float:
    prijs = 0
    if ijsje["verpakking"] == "hoorntje":
        prijs += HOORNTJES_PRIJS
        if "Caramel Saus" in ijsje["toppings"]:
            prijs += CARAMEL_SAUS_HOORNTJE_PRIJS
    elif ijsje["verpakking"] == "bakje":
        prijs += BAKJES_PRIJS
        if "Caramel Saus" in ijsje["toppings"]:
            prijs += CARAMEL_SAUS_BAKJE_PRIJS
    prijs += ijsje["bolletjes"] * BOLLETJES_PRIJS
    if "Slagroom" in ijsje["toppings"]:
        prijs += 0.50
    elif "Sprinkels" in ijsje["toppings"]:
        prijs += 0.25
    return prijs





def Bereken_Totaal(ijsjes,klant) -> dict:
    totaal_dict = {}
    if klant == "klant":
        for ijsje in ijsjes:
            totaal_dict["bolletjes"] += ijsje["bolletjes"]
            totaal_dict["hoorntjes"] += ijsje["verpakking"] == "hoorntje"
            totaal_dict["bakjes"] += ijsje["verpakking"] == "bakje"
            for ijsje in ijsjes["smaakjes"]:
                totaal_dict["B.Chocolade"] += "Chocolade" in ijsje
                totaal_dict["B.Vanille"] += "Vanille" in ijsje
                totaal_dict["B.Munt"] += "Munt" in ijsje
                totaal_dict["B.Aardbei"] += "Aardbei" in ijsje
            for ijsje in ijsjes["toppings"]:
                totaal_dict["slagroom"] += "Slagroom" in ijsje
                totaal_dict["sprinkels"] += "Sprinkels" in ijsje
                if ijsje["verpakking"] == "hoorntje":
                    totaal_dict["caramel_saus_hoorntje"] += "Caramel Saus" in ijsje
                elif ijsje["verpakking"] == "bakje":
                    totaal_dict["caramel_saus_bakje"] += "Caramel Saus" in ijsje
            totaal_dict["totaal"] += ijsje["prijs"]
        return totaal_dict
    elif klant == "zakelijk":
        print("---------[Papi Gelato]---------")
        

def vraag_klant() -> str:
    while True:
        Question = input("Bent u een klant of zakelijk?\n> ")
        if Question.lower() == "klant":
            return "klant"
        elif Question.lower() == "zakelijk":
            return "zakelijk"
        else:
            print("Sorry, dat begrijp ik niet.")

def vraag_printbonnetje() -> bool:
    while True:
        Question = input("Wilt u een bonnetje? (ja/nee)\n> ")
        if Question.lower() == "ja":
            return True
        elif Question.lower() == "nee":
            return False
        else:
            print("Sorry, dat begrijp ik niet.")

def PrintBonnetje(ijsjes):
    totaal_dict = Bereken_Totaal(ijsjes)
    print("---------[Papi Gelato]---------")
    if totaal_dict["hoorntjes"] > 0:
        print(f"{totaal_dict['hoorntjes']} x {HOORNTJES_PRIJS:.2f} = {totaal_dict['hoorntjes'] * HOORNTJES_PRIJS:.2f}")
    print(f"{totaal_dict['B.Chocolade']} x {BOLLETJES_PRIJS:.2f} = {totaal_dict['B.Chocolade'] * BOLLETJES_PRIJS:.2f}")
    print(f"{totaal_dict['B.Vanille']} x {BOLLETJES_PRIJS:.2f} = {totaal_dict['B.Vanille'] * BOLLETJES_PRIJS:.2f}")
    print(f"{totaal_dict['B.Munt']} x {BOLLETJES_PRIJS:.2f} = {totaal_dict['B.Munt'] * BOLLETJES_PRIJS:.2f}")
    print(f"{totaal_dict['B.Aardbei']} x {BOLLETJES_PRIJS:.2f} = {totaal_dict['B.Aardbei'] * BOLLETJES_PRIJS:.2f}")
    if totaal_dict["sprinkels"] > 0:
        print(f"{totaal_dict['sprinkels']} x 0.25 = {totaal_dict['sprinkels'] * 0.25:.2f}")
    if totaal_dict["slagroom"] > 0:
        print(f"{totaal_dict['slagroom']} x 0.50 = {totaal_dict['slagroom'] * 0.50:.2f}")
#    if totaal_dict["caramel_saus"] > 0:
#        print(f"{totaal_dict['caramel_saus']} x {CARAMEL_SAUS_HOORNTJE_PRIJS:.2f} = {totaal_dict['caramel_saus'] * CARAMEL_SAUS_HOORNTJE_PRIJS:.2f}")

    print("--------------------------------")
    print(f"Totaal: {totaal_dict['totaal']:.2f}")
    print("Bedankt en tot ziens!")