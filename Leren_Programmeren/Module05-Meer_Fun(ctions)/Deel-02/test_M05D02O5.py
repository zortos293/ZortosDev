from functions import print_colorvars
from functions import getFromListByKeyIs

thingsList = [
    {
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }
]

result1 = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    }, {
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]

if getFromListByKeyIs(thingsList, 'round', True) != result1:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')


result2 = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]

if getFromListByKeyIs(thingsList, 'tasty', True) != result2:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

result3 = [{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]

if getFromListByKeyIs(thingsList, 'round', False) != result3:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')