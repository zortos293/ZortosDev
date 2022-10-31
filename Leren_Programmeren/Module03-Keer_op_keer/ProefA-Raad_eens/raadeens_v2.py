from random import randint
ROUNDS_INT = 20
POGINEN_INT = 10

def rounds(poginen: int) -> bool:
    pogingen = 1
    diffrence_nummer = 0
    while pogingen <= poginen:
        try:
            gebruiker_nummer = int(input("Voer uw nummer in :"))
        except:
            print("u heeft een letter ingevoerd")
            pogingen = pogingen +1
        diffrence_nummer =  abs(gen_nummer -gebruiker_nummer)
        if diffrence_nummer == 0:
            print("gewonnen!!")
            return True
        elif gebruiker_nummer > 1000:
            print("U bent over de raadcijfer")
            pogingen = pogingen + 1
        elif diffrence_nummer <= 10 :
            print("Je bent erg warm")
            pogingen = pogingen + 1
        elif diffrence_nummer <= 20 :
            print("Je bent warm")
            pogingen = pogingen + 1
        elif diffrence_nummer <= 30:
            print("Je bent koud")
            pogingen = pogingen + 1
        elif diffrence_nummer <= 50:
            print("Je bent erg koud")
            pogingen = pogingen + 1            
    return False

round_game = 0
scoreboard = 0
gen_nummer = randint(0, 100)

while round_game != ROUNDS_INT:
    if rounds(POGINEN_INT):
        scoreboard = scoreboard + 1
    else:
        print("je hebt meer dan 10 keer probeerd RIP")
    round_game = round_game + 1
    if input("Nog een getal raden? [Y/N]").lower() == "y":
        gen_nummer = randint(0, 100)
    else:
        break
print(f"U heeft {scoreboard}/20 Geraden!!")

