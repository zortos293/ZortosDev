import time
from termcolor import colored
import math
from data import *      

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
    return copper2gold(peopleCost + horsesCost)

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
                price_gold += copper2gold(a['price']['amount'] * a['amount'])
            case "silver":
                price_gold += silver2gold(a['price']['amount']* a['amount'])
            case "gold":
                price_gold += a['price']['amount'] * a['amount']
            case "platinum":
                price_gold += platinum2gold(a['price']['amount'] * a['amount'])
    return round(price_gold,2)

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
    return round(price_gold ,2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    return [item for item in investors if item['profitReturn'] < 10]

def getAdventuringInvestors(investors:list) -> list:
    return [item for item in investors if item['adventuring'] and item['profitReturn'] < 10 ]

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    price_gold = 0
    adventuring_investors = getAdventuringInvestors(investors)
    for a in range(len(adventuring_investors)):
        price_gold += getItemsValueInGold(gear)
        
    price_gold += getJourneyFoodCostsInGold(len(adventuring_investors),len(adventuring_investors))
    price_gold += getTotalRentalCost(len(adventuring_investors), len(adventuring_investors))
    print(price_gold)
    return price_gold 

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:   
    human_per_night_Gold = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_per_night_Gold = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    return int(leftoverGold / (human_per_night_Gold + horses_per_night_Gold))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    gold_per_night = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT)
    human_per_night_Gold =  gold_per_night * people #0.6
    horses_gold_per_night = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT)
    horses_per_night_Gold = horses_gold_per_night * horses #0.1
    return round((human_per_night_Gold + horses_per_night_Gold) * nightsInInn,2)
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    emptylist = []
    for a in investors:
        if a['profitReturn'] < 10:
            emptylist.append(round(a['profitReturn'] / 100 * profitGold,2) )
    return emptylist

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    investor_cuts = 0
    for a in investorsCuts:
        investor_cuts += a
    return round((profitGold - investor_cuts) / fellowship,2)
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