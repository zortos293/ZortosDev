gastheer = input("Wie is de gastheer?: ")
gasten = 20
sinasappelsap = int(input("Hoeveel flessen sinasappelsap zijn er?: "))
chips = True

aanwezigen = gasten if gastheer ==  "" else gasten + 1
if gastheer != "Jouke" and (gastheer == "Emin" or (sinasappelsap >= 15 and (aanwezigen >= 4 and aanwezigen <= 20))):
    print("Start the party!")
else:
    print("No party.")
