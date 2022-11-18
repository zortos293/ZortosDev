from functions import *
from data import *

totalCost = 0
chapterNr = 1

print_title('A Treasure Hunt Adventure Story')
print_chapter(chapterNr, 'THE FELLOWSHIP')

cashInGold      = getPersonCashInGold(mainCharacter['cash'])
rentStuff       = False
party           = [mainCharacter]

if len(mainCharacter['name']) > 0:
    print_colorvars('Er was een jonge avonturier genaamd {} die een schatkaart had gevonden.', [mainCharacter['name']])
else:
    print_colorvars('Er was een jonge avonturier die een schatkaart had gevonden.')

if cashInGold != None and cashInGold > 0:
    print_colorvars('{} had maar {} goud op zak, dus was wel geinterreseerd in meer.', [mainCharacter['name'], cashInGold])

if len(friends) > 0:
    shareWithFriends    = getShareWithFriends(friends)
    adventuringFriends  = getAdventuringFriends(friends)
    shareFriendText     = ifOne(len(shareWithFriends), 'vriend', 'vrienden')
    comigFriendText     = ifOne(len(adventuringFriends), 'vriend gaat', 'vrienden gaan')
    party               += adventuringFriends

    print_colorvars('{} besloot het met {} te delen, en {} mee op avontuur.',[mainCharacter['name'], shareFriendText, comigFriendText])
    
    horses = getNumberOfHorsesNeeded(len(party))
    if len(shareWithFriends) > 0 and horses != None:
        rentStuff = True
        horses -= 1
    else:
        horses = 0

elif len(mainCharacter['name']) > 0:
    print_colorvars('{} besloot de schat zelf te gaan zoeken.', [mainCharacter['name']])

startPrepwork = True
if rentStuff:
    chapterNr += 1
    print_chapter(chapterNr, 'RENTING HORSES AND TENTS')

    tents       = getNumberOfTentsNeeded(len(party))
    horses      = getNumberOfHorsesNeeded(len(party)) - 1 #MainCharacter owns a horse
    
    rentalCost  = getTotalRentalCost(horses, tents)
    horseText   = ifOne(horses, 'paard',  'paarden')
    tentText    = ifOne(tents, 'tent',  'tenten') 
    totalCost   = round(totalCost + rentalCost, 2)
    print_colorvars('Het {}-tal huurde {} en {} voor {} goud.',[len(party), horseText, tentText, rentalCost])

    if len(adventurerGear)  > 0:
        chapterNr += 1
        print_chapter(chapterNr, 'SHOPPING FOR GEAR')

        gearCost                = getItemsValueInGold(adventurerGear)
        shoppingCost            = round(gearCost * len(party), 2)
        adventurerGearAsText    = getItemsAsText(adventurerGear)
        totalCost               = round(totalCost + shoppingCost, 2)
        adventurersText         = ifOne(len(party), 'avonturier',  'avonturiers')
        
        cashPeople = party
        interestingInvestors = getInterestingInvestors(investors)
        if interestingInvestors != None:
            cashPeople = cashPeople + interestingInvestors

        cashInGold = getCashInGoldFromPeople(cashPeople)

        print_colorvars('Iedere avonturier heeft de volgende uitrusting nodig: {}.', [adventurerGearAsText])
        print_colorvars('Er werd berekend dat dit nog eens {} goud kost.', [shoppingCost])
        
        if cashInGold == None:
            print_colorvars('Kunnen we dit wel betalen? vroeg {} zich af.', [mainCharacter['name']])
        else:
            if totalCost < cashInGold:
                if len(investors) == 0:
                    print_colorvars('We hebben geen investeerders nodig voor deze reis, we hebben genoeg op zak.')
                else:
                    chapterNr += 1
                    print_chapter(chapterNr, 'GETTING INVESTORS')

                    interestingInvestors    = getInterestingInvestors(investors)
                    investorsAdventuring    = getAdventuringInvestors(investors)
                    investorCosts           = getTotalInvestorsCosts(investors, adventurerGear)
                    totalCost               = round(totalCost + investorCosts, 2)
                    party                   += investorsAdventuring
                    
                    amountOfInvestorsCommingAlong = len(investorsAdventuring)
                    horses += amountOfInvestorsCommingAlong
                    tents += amountOfInvestorsCommingAlong
                    
                    horseText       = ifOne(horses, 'gehuurd paard',  'gehuurde paarden')
                    tentText        = ifOne(tents, 'gehuurd tent',  'gehuurde tenten') 
                    investorsText   = ifOne(amountOfInvestorsCommingAlong, 'investeerder aan sluit',  'investerders aan sluiten', '1') 

                    print_colorvars('Er werd gezocht naar investeerders en vonden er {} waarvan er {}.', [len(interestingInvestors), investorsText])
                    print_colorvars('Het is gebruikelijk dat een investeerder zijn eigen paard, tent en uitrusting krijgt, dat maakt het totaal nu {} en {}', [horseText, tentText])
            
            if totalCost > cashInGold:
                startPrepwork = False
                print_colorvars('De totale kosten tot nu toe {} goud',[totalCost])
                print_colorvars('Zoveel heeft de groep niet, ze hebben maar {} goud, dus ze bleven maar thuis.', [cashInGold])
            else:
                print_colorvars('De totale kosten tot nu toe {} goud, gelukkig heeft de groep {} goud te besteden.',[totalCost, cashInGold])

adventureStarted = False
nightsInInn = 0

if startPrepwork:
    chapterNr += 1
    print_chapter(chapterNr, 'THE PREPWORK')

    if JOURNEY_IN_DAYS == 0:
        if len(mainCharacter['name']) == 0:
            print_colorvars('Ongeduldig als de jonge avonturier werd de reis direct gestart.')
        else:
            print_colorvars('De schatkaart is nog niet voldoende bestudeerd om te weten hoe de reis gaat verlopen, maar wat maakt het uit, dacht {}, gewoon gaan!', [mainCharacter['name']])
        adventureStarted = True
    else:
        foodPeople = party
        if len(party) == 1:
            horses = 0
            cashInGold = getPersonCashInGold(mainCharacter['cash'])
        else:
            foodPeople = [mainCharacter] + getAdventuringFriends(friends)
            cashPeople = [mainCharacter] + getAdventuringFriends(friends)
            
            interestingInvestors = getInterestingInvestors(investors)
            if interestingInvestors != None:
                cashPeople = cashPeople + interestingInvestors

            cashInGold = getCashInGoldFromPeople(cashPeople)

        journeyFoodCost = getJourneyFoodCostsInGold(len(foodPeople), horses + 1)
        journeyText     = ifOne(JOURNEY_IN_DAYS, 'dag', 'dagen')
        print_colorvars('Aan de hand van de schatkaart was te lezen dat de reis {} zou duren.', [journeyText])
        
        if journeyFoodCost != None and journeyFoodCost > 0:
            horseText       = ifOne(horses + 1, 'paard',  'paarden')
            adventurerText  = ifOne(len(party), 'avonturier', 'avonturiers')
            totalCost = round(totalCost + journeyFoodCost,2)
            print_colorvars('Het eten voor {} en {} tijdens de reis gaat {} goud kosten.', [adventurerText, horseText, journeyFoodCost])
        
        if len(investors) > 0:
            leftoverGold    = round(cashInGold - totalCost ,2)
            nightsInInn     = getMaxAmountOfNightsInInn(leftoverGold, len(party), horses + 1)
            nightsText      = ifOne(JOURNEY_IN_DAYS - 1, 'nacht', 'nachten')

            if nightsInInn == None:
                nightsInInn = 0

            if nightsInInn > 0:
                journeyInnCost  = getJourneyInnCostsInGold(nightsInInn, len(party), horses + 1)
                totalCost       = round(totalCost + journeyInnCost,2)
                print_colorvars('Er werd uitgerekend dat met het overgebleven {} goud er {} van de {} in een herberg overnacht kon worden.', [leftoverGold, nightsInInn, nightsText])
                print_colorvars('Dat kost nog eens {} goud extra.', [journeyInnCost])
            
            print_colorvars('De totale kosten inmiddels op {} goud.', [totalCost])
        
        if cashInGold != None and totalCost > cashInGold:
            print_colorvars('Helaas is goud {} (nog) niet genoeg om de reis te starten.', [cashInGold])
        elif cashInGold == None and len(adventurerGear) > 0:
            print_colorvars('Het {}-tal kan helaas niet vertrekken, voordat ze weten of het wel te betalen is.', [len(party)])
        else:
            print_colorvars('De reis kon dus (eindelijk) beginnen.')
            adventureStarted = True

if adventureStarted:
    chapterNr += 1
    print_chapter(chapterNr, 'THE JOURNEY')

    if len(mainCharacter['name']) == 0:
        print_colorvars('Maar als onbekende avonturier zonder geld kom je nerges ... ')
    elif JOURNEY_IN_DAYS == 0:
        print_colorvars('Een reis zonder het bestuderen van de kaart bleek toch geen goed idee, ineens zag {} daar weer het beginpunt en kon er opnieuw begonnen worden.', [mainCharacter['name']])
    elif journeyFoodCost == None or journeyFoodCost == 0:
        print_colorvars('Reizen zonder eten doet {} geen goed en hij keerde al snel terug naar huis.', [mainCharacter['name']])
    elif len(party) == 1:
        print_colorvars('Al gouw kwam {} er achter dat een avontuur in je eentje niet leuk is en keerde terug naar huis.', [mainCharacter['name']])
    elif rentStuff == False:
        adventurersText = ifOne(len(party), 'avonturier', 'avonturiers')
        horseText       = ifOne(horses + 1, 'paard',  'paarden', '1')
        print_colorvars('Op de tweede dag, kwam de groep van {} er achter dat een avontuur zonder tenten en {} je niet een prettige reis hebt, dus gingen weer terug.', [adventurersText, horseText])
    elif len(adventurerGear) == 0:
        adventurersText = ifOne(len(party), 'avonturier', 'avonturiers')
        print_colorvars('Bij het eerste de best obstakel, kwam de groep van {} er achter dat een avontuur zonder uitrusting niet heel handig was en ze keerde terug naar huis.', [adventurersText])
    elif nightsInInn == 0:
        investorsAdventuring = getAdventuringInvestors(investors)
        investorsText = ifOne(len(investorsAdventuring), 'investeerder', 'investeerders', '')
        print_colorvars('Het blijkt echter geen goed idee om met de {} iedere nacht in een tent slapen, dus ze keren terug naar huis om een nieuw plan te maken.', [investorsText])
    else:
        print_colorvars('De reis voorloop spoedig voor het {}-tal en ze komen op tijd aan bij de bestemming.', [len(party)])
        
        if len(treasure) == 0:
            print_colorvars('Helaas blijkt de schat al te zijn opgegraven door iemand anders en keren ze met lege handen terug naar huis.')
        else:    
            print_colorvars('Ze starten meteen met graven en vinden een kist.')
            print_colorvars('Er wordt besloten om deze mee naar huis te nemen en daar pas open te maken.')

            chapterNr += 1
            print_chapter(chapterNr, 'THE TREASURE')
            people = [mainCharacter] + getAdventuringFriends(friends) + getInterestingInvestors(investors)

            cashInGold      = getCashInGoldFromPeople(people)
            treasureItems   = getItemsAsText(treasure)
            treasureValue   = getItemsValueInGold(treasure)

            leftoverGold    = round(cashInGold - totalCost, 2)
            totalGold       = round(treasureValue + leftoverGold, 2)
            profitGold      = round(totalGold - cashInGold, 2)

            investorsCuts       = getInvestorsCuts(profitGold, investors)
            adventurerGoldCut   = getAdventurerCut(profitGold, investorsCuts, len(party))
    
            print_colorvars('Als ze de kist open maken vinden ze {}.', [treasureItems])
            print_colorvars('Er wordt uitgerekend dat de schat een waarde heeft van {} goud.', [treasureValue])
            print_colorvars('Samen met al het {} goud is dat {} goud om te verdelen.', [leftoverGold, totalGold])
            print_colorvars('Iedereen kreeg eerst zijn geinvesteerde goud terug en zo bleef er nog {} goud winst over.', [profitGold])
      
            if profitGold <= 0:
                print_colorvars('Helaas is er niets overgebleven om te verdelen ... ')
            elif investorsCuts == None and adventurerGoldCut == None :
                print_colorvars('Het enige wat nu nog moest gebeuren is de winst verdelen.')
            else:
                chapterNr += 1
                print_chapter(chapterNr, 'DEVIDING THE PROFIT')

                if len(investors) > 0 and investorsCuts != None:
                    print_colorvars('Als investeerder krijg je altijd eerst geld voordat de rest eerlijk verdeeld wordt, dat ziet er zo uit:')

                    index = 0
                    for investor in getInterestingInvestors(investors):
                        print_colorvars('{} krijgt {}{}, dat is {} goud.', [investor['name'], investor['profitReturn'], '%', investorsCuts[index]])
                        index += 1
                elif len(investors) > 0 and investorsCuts == None:
                    investorsText = ifOne(len(investors), 'investeerder moest', 'investeerders moesten', '')
                    print_colorvars('De {} eerst hun geld krijgen voordat er verder gerekend kan worden.', [investorsText])
                else:
                    adventurersText = ifOne(len(party), 'avonturier', 'avonturiers', 'ene')
                    print_colorvars('Er zijn geen investeerders, dus dan blijft alles over voor de {}.')

                if adventurerGoldCut == None:
                    leftoverGold = profitGold - sum(investorsCuts)
                    adventurersText = ifOne(len(party), 'persoon die op avontuur is geweest', 'personen die op avontuur zijn geweest', 'ene')
                    print_colorvars('Nu alleen noog het overgebleven {} goud verdelen over die {}.', [leftoverGold, adventurersText])
                elif adventurerGoldCut <= 0:
                    print_colorvars('Helaas bleef er geen goud over om te verdelen ...')
                elif len(party) == 1:
                    earnings = getEarnigs(profitGold, mainCharacter, friends, investors)
                    personalProfit = earnings[0]['end'] - earnings[0]['start']
                    if earnings != None:
                        print_colorvars('Dat betekend dat {} eerst {} goud hand en nu {} goud heeft, wat {} goud winst is.', [earnings[0]['name'], earnings[0]['start'], earnings[0]['end'], personalProfit])
                    else:
                        print_colorvars('Dat betekend dat al het goud voor {} is.', [mainCharacter['name']])
                    
                else:
                    if len(investors) > 0:
                        print_colorvars('Na het uitbetalen komt er op neer dat er {} goud winst aan iedere van de {} avonturiers gegeven kan worden.', [adventurerGoldCut, len(party)])
                    else:
                        print_colorvars('Dat krijgt ieder van de {} avonturiers {} goud.', [adventurerGoldCut, len(party)])

                    earnings = getEarnigs(profitGold, mainCharacter, friends, investors)

                    if earnings == None:
                        print_colorvars('Het enige wat nog te doen is, is de balance op maken.')
                    else:
                        chapterNr += 1
                        print_chapter(chapterNr, 'THE BALANCE')

                        if len(friends) > 0:
                            if len(friends) == 1:
                                print_colorvars('De vriend van {0} besluit om {0} 10 goud van zijn verdiensten te geven.', [mainCharacter['name']])
                            else:
                                print_colorvars('De vrienden van {0} besluiten om 10 goud van hun verdiensten af te staan aan {0}', [mainCharacter['name']])

                        print_colorvars('Waardoor de eindstand er zo uit komt te zien:')
                
                        for earning in earnings:
                            personalProfit = round(earning['end'] - earning['start'],2)
                            print_colorvars('{} had eerst {} goud en heeft nu {} goud, dat betekend {} goud winst.', [earning['name'], earning['start'], earning['end'], personalProfit])
                    
nextStep()
print_title('THE END')