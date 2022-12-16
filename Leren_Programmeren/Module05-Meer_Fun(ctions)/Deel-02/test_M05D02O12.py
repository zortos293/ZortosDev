from functions import print_colorvars
from functions import getInvestorsCuts, getAdventurerCut
from random import randint

testInverstorsList1 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]

if getInvestorsCuts(100, testInverstorsList1) != [5.0]:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

if getInvestorsCuts(19.7, testInverstorsList1) != [0.98]:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')


testInverstorsList2 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 15,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]

if getInvestorsCuts(50, testInverstorsList2) != [2.5, 0.5]:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')


testInverstorsList3 = [{
    'profitReturn' : 100,
    'adventuring' : True
},{
    'profitReturn' : 15,
    'adventuring' : True
},{
    'profitReturn' : 20,
    'adventuring' : False
}]

if getInvestorsCuts(randint(1,1000), testInverstorsList3) != []:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')


if getInvestorsCuts(randint(1,1000), []) != []:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')

if getAdventurerCut(100, [10.0, 10.0], 4) != 20.0:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')

if getAdventurerCut(100, [], 5) != 20.0:
    print_colorvars(vars=['Test 7 is False'], color='red')
else:
    print_colorvars(vars=['Test 7 is correct'], color='green')

if getAdventurerCut(150, [2.5, 1.9, 3.4, 12.3], 14) != 9.28:
    print_colorvars(vars=['Test 8 is False'], color='red')
else:
    print_colorvars(vars=['Test 8 is correct'], color='green')