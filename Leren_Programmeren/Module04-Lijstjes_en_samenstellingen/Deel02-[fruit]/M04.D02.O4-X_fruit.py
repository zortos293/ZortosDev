from fruitmand import fruitmand
from random import randint
aantal_user = int(input('Hoeveel stuks fruit wilt u ? :'))
for z in range(aantal_user):
    print(fruitmand[randint(0,6)]['name'])
    