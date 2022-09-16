from gc import get_referents
from webbrowser import get


totaal = 0
getal = 49
som = '50'
somnummer = 1
while totaal <= 1000:
    getal = getal + 1
    somnummer = somnummer +1
    som += str(f' + {getal}')
    totaal = totaal + getal
    print(f'[{somnummer}] {som} = {totaal}')
