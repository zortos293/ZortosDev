from random import randint

mm_kleuren = ("oranje", "blauw","groen","bruin")
mm_aantal = int(input("hoeveel M&M’s moet er aan de zak toegevoegd worden?"))
mm_zak = []

for z in range(mm_aantal):
    randomint = randint(1,4)
    match randomint:
        case 1:
            mm_zak.append(mm_kleuren[0])
        case 2:
            mm_zak.append(mm_kleuren[1])
        case 3:
            mm_zak.append(mm_kleuren[2])
        case 4:
            mm_zak.append(mm_kleuren[3])           



print(f"je zak is gevuld met : \n{mm_zak.count('oranje')} Oranje m&m's\n{mm_zak.count('blauw')} Blauw m&m's\n{mm_zak.count('groen')} Groen m&m's\n{mm_zak.count('bruin')} Bruin m&m's")

