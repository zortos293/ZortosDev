import random

namen = []
lot = []
combinatie = []

namen.append(input('Vul gebruiker in : '))

while True:
    if input('wilt u nog meer gebruikers toevoegen? [y/n] : ').lower()  == 'y':
        namen.append(input('Vul gebruiker in : '))
    else:
        break
restart = True  
while restart:
    if len(namen) > 2:
        lot = namen.copy()
        random.shuffle(lot)
        for x,naam in enumerate(namen):
            if len(lot) == 1  and lot[0] == naam:
                break
            while True:
                if lot[0] == naam:
                    random.shuffle(lot)
                else:
                    combinatie.append(f'Naam : {naam} Lot : {lot[0]}')
                    lot.pop(0)
                    break
        if len(lot) == 1 & len(naam) == 1:
            restart = True
            break
        else:
            restart = False

    else:
        print('je hebt niet genoeg vrienden (sad ;( )')
        quit()

for lijst in combinatie:
    print(lijst)