# De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten
# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag

ticket = 7.45
vr_seat = 0.37 
personen = 3

totaal_ticket = ticket *3
print (f"Totaal kost de tickets : {totaal_ticket}")
vrseat_1_Persoon = vr_seat * 9
print (f"1 persoon vr seat voor 45 minuten kost : {vrseat_1_Persoon}")
totaal_Vrseat = vrseat_1_Persoon * 3
print (f"3 personen vr seat voor 45 minuten kost : {totaal_Vrseat}")
print (f"==============================================")
totaal_prijs = totaal_Vrseat + totaal_ticket
print (f"In totaal kost het  : {totaal_prijs}")
print (f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met 45 minuten VR kost je maar {totaal_prijs} euro")