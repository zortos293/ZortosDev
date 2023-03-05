BOLLETJES_PRIJS = 1.10
HOORNTJES_PRIJS = 1.25
BAKJES_PRIJS = 0.75

ijjes = []

def print_receipt(bolletjes,hoorntjes,bakjes): # Print de bon (Moet gemaakt worden)
    print('------["Papi Gelato"]------')
    if bolletjes > 0:
        print(f"Bolletjes: {bolletjes} x €{BOLLETJES_PRIJS} = € {round(BOLLETJES_PRIJS * bolletjes,2)}" )
    if hoorntjes > 0:
        print(f"Hoorntjes: {hoorntjes} x €{HOORNTJES_PRIJS} = € {round(HOORNTJES_PRIJS * hoorntjes,2)}" )
    if bakjes > 0:
        print(f"Bakjes: {bakjes} x €{BAKJES_PRIJS} = € {round(BAKJES_PRIJS * bakjes,2)}" )
    print("---------------------------- +")
    print("Totaal: € " + str(round(bolletjes * BOLLETJES_PRIJS + hoorntjes * HOORNTJES_PRIJS + bakjes * BAKJES_PRIJS,2)))

def stap1(bolletjes,hoorntjes,bakjes):
    Amount_question = int(input("Hoeveel bolletjes wilt u?\n> "))
    if Amount_question > 8:
        print("Sorry, dat is te veel.")
        stap1(0,hoorntjes,bakjes)
    elif Amount_question <= 3:
        stap2(Amount_question,hoorntjes,bakjes)
    elif Amount_question <= 8:
        print(f"Dan krijgt u van mij {Amount_question} bolletje(s).")
        stap3(Amount_question,hoorntjes,bakjes)
    else:
        print("Sorry, dat begrijp ik niet.")
        stap1(bolletjes,hoorntjes,bakjes)


def stap2(bolletjes,hoorntjes,bakjes):
    Question = input(f"Wilt u deze {bolletjes} bolletje(s) in een hoorntje of een bakje?\n> ")
    if Question == "hoorntje":
        hoorntjes += 1
        print(f"Hier is uw hoorntje met {bolletjes} bolletje(s).")
        
    elif Question == "bakje":
        bakjes += 1
        print(f"Hier is uw bakje met {bolletjes} bolletje(s).")
        
    else:
        print("Sorry, dat begrijp ik niet.")
        


def stap3(bolletjes,hoorntjes,bakjes):
    Question = input("Wilt u nog meer bestellen? (Ja/Nee) \n> ")
    if Question.lower() == "ja":
        stap1(bolletjes,hoorntjes,bakjes)
    elif Question.lower() == "nee":
        print("Bedankt en tot ziens!")
        print_receipt(bolletjes,hoorntjes,bakjes)
    else:
        print("Sorry, dat begrijp ik niet.")
        stap3(bolletjes,hoorntjes,bakjes)