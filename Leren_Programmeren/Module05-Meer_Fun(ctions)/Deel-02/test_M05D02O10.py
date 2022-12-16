from functions import print_colorvars
from functions import getMaxAmountOfNightsInInn, getJourneyInnCostsInGold

if getMaxAmountOfNightsInInn(0, 1, 1) != 0:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

if getMaxAmountOfNightsInInn(1, 1, 1) != 1:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

if getMaxAmountOfNightsInInn(10, 2, 1) != 7:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')

if getMaxAmountOfNightsInInn(5, 100, 100) != 0:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')

if getMaxAmountOfNightsInInn(5, 2, 2) != 3:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')

if getJourneyInnCostsInGold(1,1,1) != 0.68:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')

if getJourneyInnCostsInGold(0,10,10) != 0:
    print_colorvars(vars=['Test 7 is False'], color='red')
else:
    print_colorvars(vars=['Test 7 is correct'], color='green')

if getJourneyInnCostsInGold(3,12,4) != 22.56:
    print_colorvars(vars=['Test 8 is False'], color='red')
else:
    print_colorvars(vars=['Test 8 is correct'], color='green')

if getJourneyInnCostsInGold(10,0,0) != 0.0:
    print_colorvars(vars=['Test 9 is False'], color='red')
else:
    print_colorvars(vars=['Test 9 is correct'], color='green')

if getJourneyInnCostsInGold(123,421,124) != 32289.96:
    print_colorvars(vars=['Test 10 is False'], color='red')
else:
    print_colorvars(vars=['Test 10 is correct'], color='green')
