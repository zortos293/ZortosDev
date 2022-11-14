from random import randint

mm_kleuren = ("oranje", "blauw","groen","bruin","rood","geel")
mm_aantal = int(input("hoeveel M&M’s moet er aan de zak toegevoegd worden?"))
mm_zak = []

for z in range(mm_aantal):
    mm_zak.append(mm_kleuren[randint(0,5)])         
            

bagOfMnMs = {
    'oranje' : mm_zak.count('oranje'),
    'groen' : mm_zak.count('groen'),
    'bruin' : mm_zak.count('bruin'),
    'blauw' : mm_zak.count('blauw'),
    'rood' : mm_zak.count('rood'),
    'geel' : mm_zak.count('geel'),    
}

print(f"je zak is gevuld met : \n{bagOfMnMs['oranje']} Oranje m&m's\n{bagOfMnMs['blauw']} Blauw m&m's\n{bagOfMnMs['groen']} Groen m&m's\n{bagOfMnMs['bruin']} Bruin m&m's\n{bagOfMnMs['rood']} Rood m&m's\n{bagOfMnMs['geel']} Geel m&m's")

