from random import randint




def GameLoop():
    global gen_nummer
    global gebruiker_nummer
    global pogingen
    global rounds
    global scoreboard
    print(f"Generated Number : [{gen_nummer}]") # Debug
    try:
        gebruiker_nummer = int(input("Voer uw nummer in :"))
    except:
        print("u heeft een letter ingevoerd")
        GameLoop()
    diffrence_nummer =  gen_nummer -gebruiker_nummer
    print(diffrence_nummer)
    if gebruiker_nummer == gen_nummer:
        print("U heeft het geraden !!")
        rounds = rounds + 1
        scoreboard + scoreboard + 1
        playagain()
    elif pogingen == 10:
        rounds = rounds + 1
        print("u heeft 10 pogingen gebruikt helaas")
        playagain()
    elif gebruiker_nummer > 1000:
        print("U bent over de raadcijfer")
        pogingen = pogingen + 1
        GameLoop()


    elif diffrence_nummer < 10 or diffrence_nummer > -10 :
        print("hier 1")
        print("Je bent erg warm")
        pogingen = pogingen + 1
        GameLoop()
    elif diffrence_nummer < 20 or diffrence_nummer > -20:
        print("hier 2")
        print("Je bent warm")
        pogingen = pogingen + 1
        GameLoop()
    elif diffrence_nummer < 30 or diffrence_nummer > -30:
        print("hier 3")
        print("Je bent koud")
        pogingen = pogingen + 1
        GameLoop()
    elif diffrence_nummer < 50 or diffrence_nummer > -50 :
        print("hier 4")
        print("Je bent erg koud")
        pogingen = pogingen + 1
        GameLoop()

def playagain():
    #print(rounds)
    pogingen = 0
    if rounds == 20:
        print(f"U heeft {rounds}/20 Geraden!!")
    if input("Nog een getal raden? [Y/N]").lower() == "y":
        gen_nummer = randint(0, 100)
        GameLoop()


gen_nummer = randint(0, 100)
pogingen = 1
rounds = 0
scoreboard = 0
diffrence_nummer = 0


GameLoop()
