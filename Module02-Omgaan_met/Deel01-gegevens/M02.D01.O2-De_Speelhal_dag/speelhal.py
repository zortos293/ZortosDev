# De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten
# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag

ticket = 7.45
vrseat = 0.37 


Totaalticket = 7.45 *3
print (f"Totaal kost de tickets : {Totaalticket}")
vrseat1persoon = 0.37 * 9
print (f"1 persoon vr seat voor 45 minuten kost : {vrseat1persoon}")
vrseatTotaal = vrseat1persoon * 3
print (f"3 personen vr seat voor 45 minuten kost : {vrseatTotaal}")
print (f"==============================================")
Totaalprijs = vrseatTotaal + Totaalticket
print (f"In totaal kost het  : {Totaalprijs}")
print (f"Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {Totaalprijs} euro")