from random import randint

deck_kleuren = ('harten', 'klaveren', 'schoppen' , 'ruiten')
deck_kaarten = (2,3,4,5,6,7,8,9,10,'een boer','een vrouw','een heer','een aas')
deck = []

for z in range(13):
    randomint = randint(1,5)
    randomint2 = randint(1,12)
    match randomint:
        case 1:
            deck.append(deck_kleuren[0] + ' ' +str(deck_kaarten[randomint2]))
        case 2:
            deck.append(deck_kleuren[1] + ' ' +str(deck_kaarten[randomint2]))
        case 3:
            deck.append(deck_kleuren[2] + ' ' +str(deck_kaarten[randomint2]))
        case 4:
            deck.append(deck_kleuren[3] + ' ' +str(deck_kaarten[randomint2])5)
        case 5:
            if deck.count('joker') == 2:
                z = z + 1
            else:
                deck.append('joker')

print(deck)