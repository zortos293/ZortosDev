from fruitmand import fruitmand

fruitmand.pop(4)
totaal_weight = 0
kleuren = ''
for fruit in fruitmand:
        if fruit['color'] not in kleuren:
            kleuren +=  '\n'+   fruit['color']
print(kleuren)