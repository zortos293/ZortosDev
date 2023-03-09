
BOLLETJES_PRIJS = 0.95
HOORNTJES_PRIJS = 1.25
BAKJES_PRIJS = 0.75
SLAGROOM_PRIJS = 0.50
SPRINKELS_PRIJS = 0.30
IJS_LITER_PRIJS = 9.80
CARAMEL_SAUS_HOORNTJE_PRIJS = 0.90
CARAMEL_SAUS_BAKJE_PRIJS = 0.90
BTW = 9
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




def vraag_bolletjes() -> int:
    while True:
        Amount_question = int(input("Hoeveel bolletjes wilt u?\n> "))
        if Amount_question > 8:
            print("Sorry, dat is te veel.")
        elif Amount_question <= 8:
            return Amount_question
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def vraag_liter() -> int:
    while True:
        Amount_question = int(input("Hoeveel liter wilt u?\n> "))
        if Amount_question >= 1:
            return Amount_question
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def vraag_liter_smaakje(amount_liter) -> list:
    list_smaak = []
    for x in range(amount_liter):
        while True:
            smaak = input(f"wat voor smaak wilt u voor uw {x+1} de liter? ({' '.join(smaakjes)} geen) \n> ")
            if smaak in smaakjes:
                list_smaak.append("L."+smaak)
                break
            else:
                print("Sorry dat is geen optie die we aanbieden...")
    return list_smaak


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
            print("Sorry dat is geen optie die we aanbieden...")



def vraag_smaakje(amount_bolletjes) -> list:
    list_smaak = []
    for x in range(amount_bolletjes):
        while True:
            smaak = input(f"wat voor smaak wilt u voor uw {x+1} de bolletje? ({' '.join(smaakjes)} geen) \n>")
            if smaak in smaakjes :
                list_smaak.append("B."+ smaak)
                break
            else:
                print("Sorry dat is geen optie die we aanbieden...")
    return list_smaak

def vraag_topping(amount_bolletjes) -> list:
    list_topping = []
    for x in range(amount_bolletjes):
        while True:
            topping = input(f"Wat voor topping wilt uw {x+1} de bolletje? ({' '.join(toppings)} geen) \n>")
            if topping in toppings or topping.lower() == "geen":
                list_topping.append(topping)
                break
            else:
                print("Sorry dat is geen optie die we aanbieden...")
    return list_topping

def bereken_prijs(ijsje,klant) -> float:
    prijs = 0
    if klant == "klant":
        for verpakking  in ijsje["verpakking"]:
            if verpakking == "hoorntje":
                prijs += HOORNTJES_PRIJS
                if "Caramel Saus" in ijsje["toppings"]:
                    prijs += CARAMEL_SAUS_HOORNTJE_PRIJS
            elif verpakking == "bakje":
                prijs += BAKJES_PRIJS
                if "Caramel Saus" in ijsje["toppings"]:
                    prijs += CARAMEL_SAUS_BAKJE_PRIJS
        
        prijs += ijsje["bolletjes"] * BOLLETJES_PRIJS
        for topping in ijsje["toppings"]:
            if topping == "Slagroom":
                prijs += SLAGROOM_PRIJS
            elif topping == "Sprinkels":
                prijs += SPRINKELS_PRIJS
        
        return prijs
    elif klant == "zakelijk":
        for smaak in ijsje["smaakjes"]:
                prijs += IJS_LITER_PRIJS
        return prijs
        





def Bereken_Totaal(ijsjes,klant) -> dict:
    totaal_dict = {}
    if klant == "klant":
        for ijsje in ijsjes:
            totaal_dict.setdefault("bolletjes", 0)
            totaal_dict["bolletjes"] += ijsje["bolletjes"]
            totaal_dict.setdefault("hoorntjes", 0)
            totaal_dict["hoorntjes"] += ijsje["verpakking"] == "hoorntje"
            totaal_dict.setdefault("bakjes", 0)
            totaal_dict["bakjes"] += ijsje["verpakking"] == "bakje"
            for smaak in ijsje["smaakjes"]:
                if "B.Chocolade" in smaak:
                    totaal_dict.setdefault("B.Chocolade", 0)
                    totaal_dict["B.Chocolade"] += 1
                if "B.Vanille" in smaak:
                    totaal_dict.setdefault("B.Vanille", 0)
                    totaal_dict["B.Vanille"] += 1
                if "B.Aardbei" in smaak:
                    totaal_dict.setdefault("B.Aardbei", 0)
                    totaal_dict["B.Aardbei"] += 1
                if "B.Munt" in smaak:
                    totaal_dict.setdefault("B.Munt", 0)
                    totaal_dict["B.Munt"] += 1
                
            for topping in ijsje["toppings"]:
                if "Slagroom" in topping:
                    totaal_dict.setdefault("Slagroom", 0)
                    totaal_dict["Slagroom"] += 1
                if "Sprinkels" in topping:
                    totaal_dict.setdefault("Sprinkels", 0)
                    totaal_dict["Sprinkels"] += 1
                if ijsje["verpakking"] == "hoorntje":
                    if "Caramel Saus" in topping:
                        totaal_dict.setdefault("Caramel_Saus_bakje", 0)
                        totaal_dict["Caramel_Saus_bakje"] += 1
                    
                elif ijsje["verpakking"] == "bakje":
                    if "Caramel Saus" in topping:
                        totaal_dict.setdefault("Caramel_Saus_bakje", 0)
                        totaal_dict["Caramel_Saus_bakje"] += 1
            totaal_dict.setdefault("totaal", 0)
            totaal_dict["totaal"] += ijsje["prijs"]
        return totaal_dict
    elif klant == "zakelijk":
        for ijsje in ijsjes:
            for smaak in ijsje["smaakjes"]:
                if "L.Chocolade" in smaak:
                    totaal_dict.setdefault("L.Chocolade", 0) # set the value of "L.Chocolade" to 0 if it does 
                    totaal_dict["L.Chocolade"] += 1
                elif "L.Vanille" in smaak:
                    totaal_dict.setdefault("L.Vanille", 0)
                    totaal_dict["L.Vanille"] += 1
                elif "L.Munt" in smaak:
                    totaal_dict.setdefault("L.Munt", 0)
                    totaal_dict["L.Munt"] += 1
                elif "L.Aardbei" in smaak:
                    totaal_dict.setdefault("L.Aardbei", 0)
                    totaal_dict["L.Aardbei"] += 1
            totaal_dict.setdefault("totaal", 0)
            totaal_dict["totaal"] += ijsje["prijs"]
        return totaal_dict
        

def vraag_klant() -> str:
    while True:
        try:
            Question = input("Bent u een klant of zakelijk?\n> ")
            if Question.lower() == "klant":
                return "klant"
            elif Question.lower() == "zakelijk":
                return "zakelijk"

        except TypeError:
                print("Sorry dat is geen optie die we aanbieden...")

def vraag_printbonnetje() -> bool:
    while True:
        Question = input("Wilt u een bonnetje? (ja/nee)\n> ")
        if Question.lower() == "ja":
            return True
        elif Question.lower() == "nee":
            return False
        else:
            print("Sorry dat is geen optie die we aanbieden...")

def PrintBonnetje(ijsjes,klant):
    totaal_dict = Bereken_Totaal(ijsjes,klant)
    print("---------[Papi Gelato]---------")
    if klant == "zakelijk":
        
        
        if "L.Chocolade" in totaal_dict and totaal_dict["L.Chocolade"] > 0 :
            print(f"{totaal_dict['L.Chocolade']} x {IJS_LITER_PRIJS:.2f}€ = {totaal_dict['L.Chocolade'] * IJS_LITER_PRIJS:.2f}€")
        if "L.Vanille" in totaal_dict and totaal_dict["L.Vanille"] > 0:
            print(f"{totaal_dict['L.Vanille']} x {IJS_LITER_PRIJS:.2f}€ = {totaal_dict['L.Vanille'] * IJS_LITER_PRIJS:.2f}€")
        if "L.Munt" in totaal_dict and totaal_dict["L.Munt"] > 0:
            print(f"{totaal_dict['L.Munt']} x {IJS_LITER_PRIJS:.2f}€ = {totaal_dict['L.Munt'] * IJS_LITER_PRIJS:.2f}€")
        if "L.Aardbei" in totaal_dict and totaal_dict["L.Aardbei"] > 0:
            print(f"{totaal_dict['L.Aardbei']} x {IJS_LITER_PRIJS:.2f}€ = {totaal_dict['L.Aardbei'] * IJS_LITER_PRIJS:.2f}€")
        
        print("--------------------------------")
        print(f"Totaal: {totaal_dict['totaal']:.2f}€")
        print(f"BTW (%{BTW}): {totaal_dict['totaal'] / 100 * BTW:.2f}€")
    else:
        if "hoorntjes" in totaal_dict and totaal_dict["hoorntjes"] > 0:
            print(f"Hoorntjes : {totaal_dict['hoorntjes']} x {HOORNTJES_PRIJS:.2f}€ = {totaal_dict['hoorntjes'] * HOORNTJES_PRIJS:.2f}€")
        if "bakjes" in totaal_dict and totaal_dict["bakjes"] > 0:
            print(f"Bakjes : {totaal_dict['bakjes']} x {BAKJES_PRIJS:.2f}€ = {totaal_dict['bakjes'] * BAKJES_PRIJS:.2f}€")
        if "B.Chocolade" in totaal_dict:
            print(f"B.Chocolade : {totaal_dict['B.Chocolade']} x {BOLLETJES_PRIJS:.2f}€ = {totaal_dict['B.Chocolade'] * BOLLETJES_PRIJS:.2f}€")
        if "B.Vanille" in totaal_dict:
            print(f"B.Vanille : {totaal_dict['B.Vanille']} x {BOLLETJES_PRIJS:.2f}€ = {totaal_dict['B.Vanille'] * BOLLETJES_PRIJS:.2f}€")
        if "B.Munt" in totaal_dict: 
            print(f"B.Munt : {totaal_dict['B.Munt']} x {BOLLETJES_PRIJS:.2f}€ = {totaal_dict['B.Munt'] * BOLLETJES_PRIJS:.2f}€")
        if "B.Aardbei" in totaal_dict:
            print(f"B.Aardbei : {totaal_dict['B.Aardbei']} x {BOLLETJES_PRIJS:.2f}€ = {totaal_dict['B.Aardbei'] * BOLLETJES_PRIJS:.2f}€")
        if "sprinkels" in totaal_dict:
            print(f"Sprinkels : {totaal_dict['sprinkels']} x {SPRINKELS_PRIJS:.2f}€ = {totaal_dict['sprinkels'] * SPRINKELS_PRIJS:.2f}€")
        if "slagroom" in totaal_dict:
            print(f"Slagroom : {totaal_dict['slagroom']} x {SLAGROOM_PRIJS:.2f}€ = {totaal_dict['slagroom'] * SLAGROOM_PRIJS:.2f}€")
        print("--------------------------------")
        print(f"Totaal: {totaal_dict['totaal']:.2f}€")
    print("Bedankt en tot ziens!")