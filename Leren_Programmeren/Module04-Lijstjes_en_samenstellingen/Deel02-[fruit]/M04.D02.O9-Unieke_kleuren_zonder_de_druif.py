from fruitmand import fruitmand


totaal_weight = 0
kleuren = ''
for x,fruit in enumerate(fruitmand):
        if fruit['name'] == 'druif':
            fruitmand.pop(x)
        if fruit['color'] not in kleuren:
            kleuren +=  '\n'+   fruit['color']
print(kleuren)
