# De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten
# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag

ticket = int(input("vul de ticket prijs (centen) : "))
vr_seat = int(input("vul de vr seat prijs (centen) : "))
vr_seat_minuten = int(input("vul de vr seat minuten : "))
personen = int(input("vul aantal personen : "))

totaal_ticket = ticket *personen
print (f"Totaal kost de tickets : {totaal_ticket}")
vrseat_1_persoon = vr_seat * vr_seat_minuten
totaal_vrseat = vrseat_1_persoon * personen
totaal_prijs = totaal_vrseat + totaal_ticket
print (f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {vr_seat_minuten} minuten VR kost je maar {totaal_prijs} euro")