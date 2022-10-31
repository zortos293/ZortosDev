# name of student: Emin 
# number of student: 99072620
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) # Changes euros to cents
paid = int(float(input('Paid amount: ')) * 100) # Changes paid amount to cents
change = paid - toPay # subtract paid amount with topay

if change > 0: # als er nog terug betaald moet worden
  coinValue = 500 # the coinvalue starts 500 cents 
  
  while change > 0 and coinValue > 0: # checks if there is change and if there is stil coins that need to be given
    nrCoins = change // coinValue #
    

    if nrCoins > 0: # if there is any coins that need to be given
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # prints the amount that needs to be given in coins
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # asks how many coins that you returned
      print(f"Given {nrCoinsReturned} of {coinValue / 100} euro")
      change -= nrCoinsReturned * coinValue # subtracts given amount with change
    

# comment on code below: 
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # if there is still change 
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')