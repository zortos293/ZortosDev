from random import randint

mm_kleuren = ("oranje", "blauw","groen","bruin")
mm_aantal = int(input("hoeveel M&M’s moet er aan de zak toegevoegd worden?"))
mm_zak = []

for z in range(mm_aantal):
    mm_zak.append(mm_kleuren[randint(0,4)])         



print(f"je zak is gevuld met : \n{mm_zak.count('oranje')} Oranje m&m's\n{mm_zak.count('blauw')} Blauw m&m's\n{mm_zak.count('groen')} Groen m&m's\n{mm_zak.count('bruin')} Bruin m&m's")

