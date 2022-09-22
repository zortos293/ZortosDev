telefoons=['Samsung Galaxy S22', 'iPhone 13']
try:
    prijs_samsung=int(input(f'Hoeveel kost de {telefoons[0]}? : '))
    prijs_iphone=int(input(f'Hoeveel kost de {telefoons[1]}? : '))
except ValueError:
    print("Error : je hebt een letter of een teken ingevoerd bij een int")

if prijs_iphone < prijs_samsung: 
    print(f"De {telefoons[0]} is het duurst, de telefoon kost: {prijs_samsung}")
    print(f"De {telefoons[1]} is het goedkoopst, de telefoon kost: {prijs_iphone}")

if prijs_samsung < prijs_iphone:
    print(f"De {telefoons[1]} is het duurst, de telefoon kost: {prijs_iphone}")
    print(f"De {telefoons[0]} is het goedkoopst, de telefoon kost: {prijs_samsung}")


difrence = prijs_iphone - prijs_samsung
if difrence == 0:
    print(f'Het advies is dus de {telefoons[1]} kopen. Deze is namelijk dezelfde prijs dan de {telefoons[0]}')
elif difrence <= 0:
    print(f'Het advies is dus de {telefoons[1]} kopen. Deze is namelijk {abs(difrence)} Euro goedkoper dan de {telefoons[0]}')
elif difrence <= 50:
    print(f'Het advies is dus de {telefoons[1]} kopen. Deze is namelijk {abs(difrence)} Euro Duurder dan de {telefoons[0]}')
elif difrence >= 50:
    print(f'Het advies is dus de {telefoons[0]} kopen. Deze is namelijk {abs(difrence)} Euro goedkoper dan de {telefoons[1]}')
