from functions import print_colorvars
from functions import getCashInGoldFromPeople

testList1 = [{
    'cash' : {
        'platinum' : 1,
        'gold' : 2,
        'silver' : 3,
        'copper' : 12
    }
}]

if getCashInGoldFromPeople(testList1) != 27.84:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

testList2 = [{
    'cash' : {
        'platinum' : 2,
        'gold' : 231,
        'silver' : 33,
        'copper' : 66
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 11,
        'silver' : 6,
        'copper' : 2
    }
}]

if getCashInGoldFromPeople(testList2) != 301.16:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

testList3 = [{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
},{
    'cash' : {
        'platinum' : 0,
        'gold' : 0,
        'silver' : 0,
        'copper' : 0
    }
}]

if getCashInGoldFromPeople(testList3) != 0:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')