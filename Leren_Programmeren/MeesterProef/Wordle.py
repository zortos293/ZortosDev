from colorama import Back
from random import randint
import lingowords

word = lingowords.words[randint(0, len(lingowords.words))]
print("The eerste letter of the word is: ", word[0])

for i in range(1, 6):
    print("Attempt", i)
    attempt = input()
    output = ""
    for j in range(word.__len__()):
        if attempt[j] == word[j]:
            output = output + Back.GREEN + attempt[j] + Back.RESET
        elif attempt[j] in word:
            output = output + Back.YELLOW + attempt[j] + Back.RESET
        else:
            output = output + attempt[j] + Back.RESET
    print(output)
    if word == attempt:
        print("Gefeliciteerd")
        break
    if i == 5:
        print("Probeer het nog eens!")
        break