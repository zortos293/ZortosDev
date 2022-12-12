from functions import print_colorvars
from functions import getJourneyFoodCostsInGold

if getJourneyFoodCostsInGold(1,1) != 1.54:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

if getJourneyFoodCostsInGold(12,3) != 12.54:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

if getJourneyFoodCostsInGold(24,11) != 28.38:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')

if getJourneyFoodCostsInGold(0,0) != 0.0:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')

if getJourneyFoodCostsInGold(10,10) != 15.4:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')