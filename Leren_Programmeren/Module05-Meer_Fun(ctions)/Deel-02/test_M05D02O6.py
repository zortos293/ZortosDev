from functions import print_colorvars
from functions import getNumberOfHorsesNeeded, getNumberOfTentsNeeded, getTotalRentalCost

if getNumberOfHorsesNeeded(7) != 4:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

if getNumberOfHorsesNeeded(4) != 2:
    print_colorvars(vars=['Test 2 is False'], color='red')
else:
    print_colorvars(vars=['Test 2 is correct'], color='green')

if getNumberOfTentsNeeded(7) != 3:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')

if getNumberOfTentsNeeded(8) != 3:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')

if getNumberOfTentsNeeded(6) != 2:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')
print(getTotalRentalCost(1,2))
if getTotalRentalCost(1,2) != 23.0:
    print_colorvars(vars=['Test 6 is False'], color='red')
else:
    print_colorvars(vars=['Test 6 is correct'], color='green')
print(getTotalRentalCost(5,2))
if getTotalRentalCost(5,2) != 67.0:
    print_colorvars(vars=['Test 7 is False'], color='red')
else:
    print_colorvars(vars=['Test 7 is correct'], color='green')

if getTotalRentalCost(3,11) != 99.0:
    print_colorvars(vars=['Test 8 is False'], color='red')
else:
    print_colorvars(vars=['Test 8 is correct'], color='green')