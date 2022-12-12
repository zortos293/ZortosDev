from functions import print_colorvars
from functions import getItemsAsText, getItemsValueInGold

testList1 = [{
    'name' : 'Kaars',
    'amount' : 3,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'copper'
    }
}]

if getItemsAsText(testList1) != '3x Kaars':
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

if getItemsValueInGold(testList1) != 0.24:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')



testList2 = [{
    'name' : 'Voetbal',
    'amount' : 1,
    'unit' : ' ronde',
    'price' : {
        'amount' : 2,
        'type' : 'gold'
    }
},{
    'name' : 'Patat',
    'amount' : 11,
    'unit' : 'x',
    'price' : {
        'amount' : 4,
        'type' : 'silver'
    }
},{
    'name' : 'Cola',
    'amount' : 1,
    'unit' : 'l',
    'price' : {
        'amount' : 5,
        'type' : 'copper'
    }
},{
    'name' : 'Sinas',
    'amount' : 5,
    'unit' : 'dl',
    'price' : {
        'amount' : 12,
        'type' : 'copper'
    }
}]


if getItemsAsText(testList2) != '1 ronde Voetbal, 11x Patat, 1l Cola, 5dl Sinas':
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')

if getItemsValueInGold(testList2) != 12.1:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')

testList3 = [{
    'name' : 'Diamand',
    'amount' : 1,
    'unit' : '',
    'price' : {
        'amount' : 7,
        'type' : 'platinum'
    }
}]

if getItemsAsText(testList3) != '1 Diamand':
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')

if getItemsValueInGold(testList3) != 175:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')