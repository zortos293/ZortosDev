from random import randint

mm_kleuren = ("oranje", "blauw","groen","bruin","rood","geel")
mm_aantal = int(input("hoeveel M&M’s moet er aan de zak toegevoegd worden?"))
mm_zak = []

for z in range(mm_aantal):
    randomint = randint(1,6)
    match randomint:
        case 1:
            mm_zak.append(mm_kleuren[0])
        case 2:
            mm_zak.append(mm_kleuren[1])
        case 3:
            mm_zak.append(mm_kleuren[2])
        case 4:
            mm_zak.append(mm_kleuren[3])           
        case 5:
            mm_zak.append(mm_kleuren[4])           
        case 6:
            mm_zak.append(mm_kleuren[5])           
            

bagOfMnMs = {
    'oranje' : mm_zak.count('oranje'),
    'groen' : mm_zak.count('groen'),
    'bruin' : mm_zak.count('bruin'),
    'blauw' : mm_zak.count('blauw'),
    'rood' : mm_zak.count('rood'),
    'geel' : mm_zak.count('geel'),    
}

print(f"je zak is gevuld met : \n{bagOfMnMs['oranje']} Oranje m&m's\n{bagOfMnMs['blauw']} Blauw m&m's\n{bagOfMnMs['groen']} Groen m&m's\n{bagOfMnMs['bruin']} Bruin m&m's\n{bagOfMnMs['rood']} Rood m&m's\n{bagOfMnMs['geel']} Geel m&m's")

