prijs = 55
if input("PC/Console :").lower() == "pc": prijs = 45
else: 
    if input("bent u een member? [Y/N] ").lower() == "y": prijs = prijs - 15
print(f"dan kost de game : {prijs}")