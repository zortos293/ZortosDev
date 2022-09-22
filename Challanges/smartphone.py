import telnetlib


Telefoons=['Samsung Galaxy S22', 'iPhone 13']

prijs_samsung=int(input(f'Hoeveel kost de {Telefoons[0]}? : '))
prijs_iphone=int(input(f'Hoeveel kost de {Telefoons[1]}? : '))

if prijs_iphone < prijs_samsung: 
    print(f"De {Telefoons[0]} is het duurst, de telefoon kost: {prijs_samsung}")
    print(f"De {Telefoons[1]} is het goedkoopst, de telefoon kost: {prijs_iphone}")

if prijs_samsung < prijs_iphone:
    print(f"De {Telefoons[1]} is het duurst, de telefoon kost: {prijs_iphone}")
    print(f"De {Telefoons[0]} is het goedkoopst, de telefoon kost: {prijs_samsung}")


difrence = prijs_iphone - prijs_samsung
if difrence == 0:
    print(f'Het advies is dus de {Telefoons[1]} kopen. Deze is namelijk dezelfde prijs dan de {Telefoons[0]}')
elif difrence <= 0:
    print(f'Het advies is dus de {Telefoons[1]} kopen. Deze is namelijk {abs(difrence)} Euro goedkoper dan de {Telefoons[0]}')
elif difrence <= 50:
    print(f'Het advies is dus de {Telefoons[1]} kopen. Deze is namelijk {abs(difrence)} Euro Duurder dan de {Telefoons[0]}')
elif difrence >= 50:
    print(f'Het advies is dus de {Telefoons[0]} kopen. Deze is namelijk {abs(difrence)} Euro goedkoper dan de {Telefoons[1]}')
