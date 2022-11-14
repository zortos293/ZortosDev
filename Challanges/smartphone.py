telefoons=['Samsung Galaxy S22', 'iPhone 13', 'Asus Zenfone 9']
prices = []
try:
    budget = int(input(f'Wat is je Budget? : '))
    #prijs_samsung= int(input(f'Hoeveel kost de {telefoons[0]}? : '))
    #prijs_iphone=int(input(f'Hoeveel kost de {telefoons[1]}? : '))
    #prijs_zenfone=int(input(f'Hoeveel kost de {telefoons[2]}? : '))
    prices.append(int(input(f'Hoeveel kost de {telefoons[0]}? : ')))
    prices.append(int(input(f'Hoeveel kost de {telefoons[1]}? : ')))
    prices.append(int(input(f'Hoeveel kost de {telefoons[2]}? : ')))

except ValueError:
    print("Error : je hebt een letter of een teken ingevoerd bij een int")

if prices[0] <= prices[1] <= prices[2]: # als samsung Galaxy s22 het goedkoopst is
    print(f"De {telefoons[0]} is het goedkoopst, de telefoon kost: {prices[0]} Euro")
    
    if prices[1] >= prices[2]:
        print(f"De {telefoons[1]} is het duurst, de telefoon kost: {prices[1]} Euro")
    else:
        print(f"De {telefoons[2]} is het duurst, de telefoon kost: {prices[2]} Euro")
    
    goedkoopst = prices[0] 

if prices[1] <= prices[2] <= prices[0]: # als iPhone 13 het goedkoopst is
    print(f"De {telefoons[1]} is het goedkoopst, de telefoon kost: {prices[1]} Euro")
    
    if prices[0] >= prices[2]:
        print(f"De {telefoons[0]} is het duurst, de telefoon kost: {prices[0]} Euro")
    else:
        print(f"De {telefoons[2]} is het duurst, de telefoon kost: {prices[2]} Euro")
    goedkoopst = prices[1] 
if prices[2] <= prices[1] <= prices[0]:
    print(f"De {telefoons[2]} is het goedkoopst, de telefoon kost: {prices[2]} Euro")
    
    if prices[0] >= prices[1]:
        print(f"De {telefoons[0]} is het duurst, de telefoon kost: {prices[0]} Euro")
    else:
        print(f"De {telefoons[1]} is het duurst, de telefoon kost: {prices[1]} Euro")
    goedkoopst = prices[2]   


difrence = prices[0] - prices[1] -prices[2]
print(goedkoopst)
print(budget)
if goedkoopst > budget:
    print(f"Het advies is dus geen telefoon te kopen, ze zijn te duur.")
elif difrence == 0:
    print(f'Het advies is dus de {telefoons[1]} kopen. Deze is namelijk dezelfde prijs dan de {telefoons[0]}')
elif difrence <= 0:
    print(f'Het advies is dus de {telefoons[1]} kopen. Deze is namelijk {abs(difrence)} Euro goedkoper dan de {telefoons[0]}')
elif difrence <= 50:
    print(f'Het advies is dus de {telefoons[1]} kopen. Deze is namelijk {abs(difrence)} Euro Duurder dan de {telefoons[0]}')
elif difrence >= 50:
    print(f'Het advies is dus de {telefoons[0]} kopen. Deze is namelijk {abs(difrence)} Euro goedkoper dan de {telefoons[1]}')

