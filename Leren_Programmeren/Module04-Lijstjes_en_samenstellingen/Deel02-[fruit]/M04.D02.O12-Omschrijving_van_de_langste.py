from fruitmand import fruitmand

lettercount = 0
fruit_name = ''
fruit_color = ''
fruit_weight = 0

for fruit in fruitmand:
    if len(fruit['name']) > lettercount:
        fruit_name = fruit['name']
        fruit_color = fruit['color']
        fruit_weight = fruit['weight']
        lettercount = len(fruit['name'])


print(f'De "{fruit_name}" ({lettercount} Letters) heeft een {fruit_color} kleur en een gewicht van {fruit_weight / 100} Kg.')
