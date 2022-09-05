# De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten
# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag

Ticket = 7.45
vr_seat = 0.37 
Personen = 3

Totaal_ticket = Ticket *3
print (f"Totaal kost de tickets : {Totaal_ticket}")
Vrseat_1_Persoon = vr_seat * 9
print (f"1 persoon vr seat voor 45 minuten kost : {Vrseat_1_Persoon}")
Totaal_Vrseat = Vrseat_1_Persoon * 3
print (f"3 personen vr seat voor 45 minuten kost : {Totaal_Vrseat}")
print (f"==============================================")
Totaal_prijs = Totaal_Vrseat + Totaal_ticket
print (f"In totaal kost het  : {Totaal_prijs}")
print (f"Dit geweldige dagje-uit met {Personen} mensen in de Speelhal met 45 minuten VR kost je maar {Totaal_prijs} euro")