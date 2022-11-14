

#Header
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('+  Sollicitatieformulier "Circusdirecteur voor Circus HotelDeBotel"  +')
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Er wordt nu een aantal relevante vragen gesteld...")
print("Gelieve die naar eer en geweten in te vullen")
print("")
# End of header

# Vragen
name = input("wat is je naam : ")
if name == 'john':
    raise NameError('John is niet welkom hier')
elif name == 'mama':
    raise NameError('dont troll plz')
elif name == 'quandele':
    raise NameError('i like cappybaras')

vraag_sex = input("Bent u een man of een vrouw [man/vrouw] ")
vraag_1 = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? : "))
vraag_2 = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? : "))
vraag_3 = input("Heeft u een fiets? [y/n] ").lower().strip() == 'y'
vraag_4 = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? : "))
vraag_5 = input("Bent u In bezit van een Diploma MBO-4 ondernemen? [y/n] ").lower().strip() == 'y'
vraag_6 = input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? [y/n] ").lower().strip() == 'y' # Maakt een input een bool als de answer y is is het true
vraag_7 = input("Bent u In bezit van een hoge hoed? [y/n] ").lower().strip() == 'y'
vraag_8 = input("Heeft u dieren thuis? [y/n] ")
if vraag_sex == "man":
    vraag_9_man = input("Heeft u een snor? [y/n] ").lower().strip() == 'y'
    vraag_9_man2 = int(input("hoe lang is uw snor? : "))
elif vraag_sex == "vrouw":
    vraag_9_vrouw = input("Wat is uw haarkleur? : ")
    vraag_9_vrouw2 = input("Heeft u krulhaar ? [y/n] ")
    vraag_9_vrouw3 = int(input("Hoelang is uw krulhaar? : "))
vraag_10 = int(input("Hoe lang bent u ? : "))
vraag_11 = input("Heeft u een auto? [y/n] ")
vraag_12 = int(input("Wat is uw lichaamsgewicht? (KG) "))
vraag_13 = input("Heeft u de Certificaat “Overleven met gevaarlijk personeel”? [y/n] ").lower().strip() == 'y'
# End of Vragen


# Vars
eisen_lengte = 150
eisen_snor = 10
eisen_snor_geslaagd =False
eisen_krulhaar = 20
eisen_krulhaar_geslaagd =False
eisen_gewicht = 90
eisen_gewicht_geslaagd = False
eisen_dieren = 4
eisen_dieren_geslaagd = False
eisen_jongleren = 5
eisen_jongleren_geslaagd = False
eisen_acrobatiek = 3
eisen_acrobatiek_geslaagd = False
questions1_geslaagd = False
questions2_geslaagd = False
questions_geslaagd = False
vraag_9_vrouw3 = 0
# End of vars

# Calculeren
eisen_lengte_geslaagd = vraag_10 > eisen_lengte
eisen_dieren_geslaagd = vraag_1 > eisen_dieren
eisen_jongleren_geslaagd = vraag_2 > eisen_jongleren
eisen_acrobatiek_geslaagd = True

if vraag_9_man2 > eisen_snor:
    eisen_snor_geslaagd = True
if vraag_9_vrouw3 == 0:
    print()
else:
    if vraag_9_vrouw3 > eisen_krulhaar:
        eisen_krulhaar_geslaagd = True

if [eisen_krulhaar_geslaagd,eisen_snor_geslaagd].count(True): # kijkt of er een van de bools True zijn
    questions1_geslaagd = True


if [eisen_dieren_geslaagd, eisen_jongleren_geslaagd, eisen_acrobatiek_geslaagd].count(True): # kijkt of er een van de bools True zijn
    questions2_geslaagd = True

if [vraag_3, vraag_5, vraag_6,vraag_7,vraag_9_man,vraag_13].count(False): # kijkt of er een van de bools false zijn
    print()
else:
    questions_geslaagd = True
#end of Calculeren



#Check of de Invuller is geslaagd of niet
if questions1_geslaagd == True and questions2_geslaagd == True and questions_geslaagd == True:
    print("U bent geslaagd")
else:
    print("U bent niet geslaagd")

