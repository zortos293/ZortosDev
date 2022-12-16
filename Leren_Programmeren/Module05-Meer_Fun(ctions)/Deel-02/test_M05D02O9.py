from functions import print_colorvars
from functions import getTotalInvestorsCosts

testInverstorsList1 = [{
    'profitReturn' : 5,
    'adventuring' : True
}]

testGearList1 = [{
    'amount' : 3,
    'price' : {
        'amount' : 1,
        'type' : 'gold'
    }
}]

if getTotalInvestorsCosts(testInverstorsList1, testGearList1) != 21.54:
    print_colorvars(vars=['Test 1 is False'], color='red')
else:
    print_colorvars(vars=['Test 1 is correct'], color='green')

testGearList2 = [{
    'amount' : 3,
    'price' : {
        'amount' : 3,
        'type' : 'copper'
    }
},{
    'amount' : 1,
    'price' : {
        'amount' : 10,
        'type' : 'silver'
    }
}]

if getTotalInvestorsCosts(testInverstorsList1, testGearList2) != 20.72:
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

if getTotalInvestorsCosts(testInverstorsList2, testGearList2) != 20.72:
    print_colorvars(vars=['Test 3 is False'], color='red')
else:
    print_colorvars(vars=['Test 3 is correct'], color='green')


testGearList3 = [{
    'amount' : 1,
    'price' : {
        'amount' : 2,
        'type' : 'platinum'
    }
},{
    'amount' : 5,
    'price' : {
        'amount' : 7,
        'type' : 'silver'
    }
},{
    'amount' : 19,
    'price' : {
        'amount' : 10,
        'type' : 'copper'
    }
}]

if getTotalInvestorsCosts(testInverstorsList1, testGearList3) != 79.34:
    print_colorvars(vars=['Test 4 is False'], color='red')
else:
    print_colorvars(vars=['Test 4 is correct'], color='green')


testInverstorsList3 = [{
    'profitReturn' : 5,
    'adventuring' : True
},{
    'profitReturn' : 9,
    'adventuring' : True
},{
    'profitReturn' : 1,
    'adventuring' : False
}]

if getTotalInvestorsCosts(testInverstorsList3, testGearList3) != 158.68:
    print_colorvars(vars=['Test 5 is False'], color='red')
else:
    print_colorvars(vars=['Test 5 is correct'], color='green')