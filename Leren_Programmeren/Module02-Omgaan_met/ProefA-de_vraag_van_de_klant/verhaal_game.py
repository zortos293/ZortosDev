restart = True
slechte_einde_count = 0
goede_einde_count = 0
while (restart == True):
    Vraag_1 = input('je zit thuis in het avond\n je vriend gerard belt\nhij vraagt of je mee wil naar het park\n\n[y voor ja  n voor nee]\n>').lower()
    if Vraag_1 == 'y': 
        Vraag_1_ja = input('je trekt je jas aan\n je stapt uit de deur\n pak je de fiets of de bus?\n1. Fiets 2.Bus\n\n[1/2]\n>').lower()
        if Vraag_1_ja == '1':
            Vraag_1_ja_fiets = input('je stapt op je fiets en je ziet dat je achterlicht niet werkt maar het boeit jouw niet\nje bent op weg naar de park maar je ziet een politie agent\nde agent stopt jouw en geeft jouw een boete omdat je achterlicht niet werkt\nGa je nog verder of ga je naar huis\n\ny voor verder n voor huis\n>').lower()
            if Vraag_1_ja_fiets == 'y':
                Vraag_1_ja_fiets_verder = print('je fietst verder naar je vriend toe en hij zegt dat de park gesloten is\nhij vraagt of jij de sleutels heb meegenomen\nmaar je hebt het thuis vergeten\n')
                Vraag_1_ja_fiets_verder_vraag = input('Je bent thuis\n\nwat ga je doen\n1.slapen of nog\n2.tv kijken\n3. Sleutels pakken\n[1/2/3] \n>').lower()
                if Vraag_1_ja_fiets_verder_vraag == '1':
                    Vraag_1_ja_fiets_verder_vraag_slapen = print('Je gaat naar bed\nen opeens belt iemand jouw dat je vriend is overleden\n(Slechte einde unlocked)')
                    slechte_einde_count = slechte_einde_count +1
                elif Vraag_1_ja_fiets_verder_vraag == '2':
                    Vraag_1_ja_fiets_verder_vraag_tv = input('je zit tv te kijken en je vriend vraagt of hij langs kan komen omdat hij wilt met je chillen omdat je niet naar de park gaat \nwil je dat hij komt?\n[Y/N]\n>').lower()
                    if Vraag_1_ja_fiets_verder_vraag_tv == 'y':
                        Vraag_1_ja_fiets_verder_vraag_tv_ja = print('je zit met je vriend de hele nacht films aan het kijken op netflix\n(goede einde Unlocked)')
                        goede_einde_count = goede_einde_count +1
                    elif Vraag_1_ja_fiets_verder_vraag_tv != 'y':
                        Vraag_1_ja_fiets_verder_vraag_tv_nee = print('je zegt tegen je vriend dat je niet beschikbaar bent\nje vriend is nu boos omdat je liegt\n(slechte einde)') 
                        slechte_einde_count = slechte_einde_count +1
                elif Vraag_1_ja_fiets_verder_vraag == '3':    
                    Vraag_1_ja_fiets_verder_vraag_sleutels = print('Je hebt de sleutels en jullie gingen lekker chillen in de park\n\n(Goede Einde Unlocked)')
                    goede_einde_count = goede_einde_count +1
        elif Vraag_1_ja != 'y':
            Vraag_1_ja_fiets_thuis = print('Je gaat met de bus\nde bus is rustig en je ontmoet je friend en lopen rond de park\n(Goede einde unlocked)')
            goede_einde_count = goede_einde_count +1
    if not Vraag_1 == 'y':
        vraag_1_nee = input('Je bent thuis\nje wilt gaan slapen maar nook nog tv kijken\nwat ga je doen 1.slapen of nog 2.tv kijken\n[1/2]\n>').lower()
        if vraag_1_nee == '1':
            vraag_1_nee_slapen = int(input('hoelang wil je gaan slapen?\n\n>'))
            if vraag_1_nee_slapen <= 9:
                vraag_1_nee_slapen_hoger = print('je word wakker\n je vriend heeft je 10 keer gebeld\n je belt hem terug \n je hoort dat je vriend is overleden bij een aanrijding met een auto\n (Slechte einde unlocked)')
            elif vraag_1_nee_slapen >= 10: 
                vraag_1_nee_slapen_hoger_tien = print('je wordt wakker voor een nieuwe dag je vrienden wachten op je voor je deur om naar school te gaan \n (Goede einde unlocked )')
        elif vraag_1_nee != 'y':
            vraag_1_nee_tv = input('je zit tv te kijken en je vriend vraagt of hij langs kan komen omdat hij wilt met je chillen omdat je niet naar de park gaat \nwil je dat hij komt?\n[Y/N]\n>').lower() 
            if vraag_1_nee_tv == 'y':
                vraag_1_nee_tv_ja = input('je zit met je vriend de hele nacht films aan het kijken op netflix\ngoede einde Unlocked)').lower()
            elif vraag_1_nee_tv != 'y':
                vraag_1_nee_tv_nee = print('je zegt tegen je vriend dat je niet beschikbaar bent\nje vriend is nu boos omdat je liegt\n(slechte einde)') 
    print(f'Je hebt ({goede_einde_count}/3) gevonden \n Je hebt ({slechte_einde_count}/2) Slechte Einde gevonden ')
    question_restart = input('Wil je opnieuw spelen? [y/n]')
    if question_restart == 'y':
        restart = True
    else:
        restart = False