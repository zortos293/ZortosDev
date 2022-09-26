from random import randint, random

deck_kleuren = ('harten', 'klaveren', 'schoppen' , 'ruiten')
deck_kaarten = (2,3,4,5,6,7,8,9,10,'een boer','een vrouw','een heer','een aas')
deck = []
joker_amount = 0
for z in range(45):
    randomint = randint(1,5)
    deck.append(deck_kleuren[randint(0,3)] + ' ' +str(deck_kaarten[randint(1,12)]))
    if randomint == 4:
        if joker_amount != 2:
            deck.append('joker')
            joker_amount = joker_amount + 1


for p in range(7):
    print(f'Kaart {p + 1}: {deck[p]}')
print(f'Deck {len(deck)} Kaarten: {deck}') 
