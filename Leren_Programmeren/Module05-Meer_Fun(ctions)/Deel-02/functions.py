import time
from termcolor import colored
import math
from data import JOURNEY_IN_DAYS , COST_FOOD_HUMAN_COPPER_PER_DAY , COST_FOOD_HORSE_COPPER_PER_DAY , COST_TENT_GOLD_PER_WEEK,COST_HORSE_SILVER_PER_DAY        

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount/10

def silver2gold(amount:int) -> float:
    return amount/5

def copper2gold(amount:int) -> float:
    return (amount/10)/5 

def platinum2gold(amount:int) -> float:
    return amount * 25  

def getPersonCashInGold(personCash:dict) -> float:
    plat = platinum2gold(personCash["platinum"])
    silver = silver2gold(personCash["silver"])
    copper = copper2gold(personCash["copper"])
    return plat + silver + copper

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    peopleCost = people * JOURNEY_IN_DAYS * COST_FOOD_HUMAN_COPPER_PER_DAY
    horsesCost = horses * JOURNEY_IN_DAYS * COST_FOOD_HORSE_COPPER_PER_DAY
    return round(copper2gold(peopleCost + horsesCost),2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item[key] == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'shareWith', True)
def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)
    pass

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)
    pass

def getTotalRentalCost(horses:int, tents:int) -> float:
    return (horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS) + (tents * (COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)) )
    pass

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    upload = ""
    for a in items:
        if upload != "":
            upload += f", {a['amount']}{a['unit']} {a['name']}"
        else:
            upload += f"{a['amount']}{a['unit']} {a['name']}"
    return upload

def getItemsValueInGold(items:list) -> float:
    price_gold = 0
    for a in items:
        match a['price']['type']:
            case "copper":
                price_gold += round(copper2gold(a['price']['amount'] * a['amount']),2)
            case "silver":
                price_gold += round(silver2gold(a['price']['amount']* a['amount']), 2)
            case "gold":
                price_gold += a['price']['amount'] * a['amount']
            case "platinum":
                price_gold += platinum2gold(a['price']['amount'] * a['amount'])
    return price_gold

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    price_gold = 0
    for a in people:
        if a['cash']['platinum'] != 0:
            price_gold += platinum2gold(a['cash']['platinum'])
        if a['cash']['gold'] != 0:
            price_gold += a['cash']['gold']
        if a['cash']['silver'] != 0:
            price_gold += silver2gold(a['cash']['silver'])
        if a['cash']['copper'] != 0:
            price_gold += copper2gold(a['cash']['copper'])
    return price_gold 
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()