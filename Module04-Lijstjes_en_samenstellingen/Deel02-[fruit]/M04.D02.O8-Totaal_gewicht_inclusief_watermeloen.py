from fruitmand import fruitmand

fruitmand.append({
    'name' : 'Watermeloen',
    'weight' : 1000,
    'color' : 'groen',
    'round' : True
})
totaal_weight = 0
for fruit in fruitmand:
        totaal_weight = totaal_weight + fruit['weight']
print("{totaal_weight}g")