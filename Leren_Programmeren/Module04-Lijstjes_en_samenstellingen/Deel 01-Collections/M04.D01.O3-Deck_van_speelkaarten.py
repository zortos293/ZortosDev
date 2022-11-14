from random import randint, random,shuffle

deck_kleuren = ('harten', 'klaveren', 'schoppen' , 'ruiten')
deck_kaarten = (2,3,4,5,6,7,8,9,10,'een boer','een vrouw','een heer','een aas')
deck = []
joker_amount = 0

for l in range(4):
    for p in range(13):
        deck.append(deck_kleuren[l] + ' ' + str(deck_kaarten[p]))

for z in range(2):
    deck.append('joker')    

print(deck)
shuffle(deck)

for p in range(7):
    print(f'Kaart {p + 1}: {deck[p]}')
    deck.pop(p)

print(f'Deck {len(deck)} Kaarten: {deck}') 
