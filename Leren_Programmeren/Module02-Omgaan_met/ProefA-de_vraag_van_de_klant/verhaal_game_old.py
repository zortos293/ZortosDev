#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os

Vraag_1 = \
    input('''
je zit thuis in het avond 
je vriend gerard belt 
hij vraagt of je mee wil naar het park

[y voor ja  n voor nee]

>''')

if Vraag_1 == 'y':

    # Vraag1 JA

    Vraag_1_ja = \
        input('''
je trekt je jas aan 
je stapt uit de deur 
pak je de fiets of de bus?
1. Fiets 2.Bus

[1/2]
>''')

    if Vraag_1_ja == '1': 

# Vraag1 JA Fiets
        Vraag_1_ja_fiets = \
            input('''
je stapt op je fiets en je ziet dat je achterlicht niet werkt maar het boeit jouw niet
je bent op weg naar de park maar je ziet een politie agent
de agent stopt jouw en geeft jouw een boete omdat je achterlicht niet werkt
Ga je nog verder of ga je naar huis

y voor verder n voor huis
>''')
        if Vraag_1_ja_fiets == 'y':
            # Vraag1 JA Fiets Verder
            Vraag_1_ja_fiets_verder = \
                input('''
je stapt op je fiets en je ziet dat je achterlicht niet werkt maar het boeit jouw niet
je bent op weg naar de park maar je ziet een politie agent
de agent stopt jouw en geeft jouw een boete omdat je achterlicht niet werkt
Ga je nog verder of ga je naar huis

y voor verder n voor huis
>''')
        if Vraag_1_ja_fiets_verder == 'y':
            Vraag_1_ja_fiets_verder_Vraag_Nee = \
                input('''
je stapt op je fiets en je ziet dat je achterlicht niet werkt maar het boeit jouw niet
je bent op weg naar de park maar je ziet een politie agent
de agent stopt jouw en geeft jouw een boete omdat je achterlicht niet werkt
Ga je nog verder of ga je naar huis

y voor verder n voor huis
>''')
        else:
            Vraag_1_ja_fiets_thuis = \
                    input('''
je stapt op je fiets en je ziet dat je achterlicht niet werkt maar het boeit jouw niet
je bent op weg naar de park maar je ziet een politie agent
de agent stopt jouw en geeft jouw een boete omdat je achterlicht niet werkt
Ga je nog verder of ga je naar huis

y voor verder n voor huis
>''')

            if Vraag_1_ja_fiets_verder == 'y':
                Vraag_1_ja_fiets_verder_Vraag_Nee = \
                    input('''
je stapt op je fiets en je ziet dat je achterlicht niet werkt maar het boeit jouw niet
je bent op weg naar de park maar je ziet een politie agent
de agent stopt jouw en geeft jouw een boete omdat je achterlicht niet werkt
Ga je nog verder of ga je naar huis

y voor verder n voor huis
>''')
    else:

        # 2. Bus

        Vraag_1_ja_bus = \
            input('''
Je gaat met de bus 
de bus is rustig en je ontmoet je friend en lopen rond de park
(Goede einde unlocked)
>''')
        exit()
else:
    Vraag_1_nee = \
        input('''
Je bent thuis 
je wilt gaan slapen maar ook nog tv kijken
wat ga je doen 
1.slapen  2.tv kijken
[1/2]

>''')
    if Vraag_1_nee == '1':
        Vraag_1_ja_slapen = \
            input('''
je gaat naar bed
en opeens belt iemand jouw dat je vriend is overleden
Slechte einde unlocked )
>''')
        exit()
    else:
        Vraag_1_ja_TV = \
            input('''
Je zit tv te kijken  en je vriend belt of hij bij jouw langs kan kom
ze heeft een cadeutje bij zich
je opent het en je krijgt een waardebon van mediamarkt
(goede einde unlocked)
>''')
        exit()
