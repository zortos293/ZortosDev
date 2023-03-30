from colorama import Back
from random import randint
import lingowords

word = lingowords.words[randint(0, len(lingowords.words) - 1)]
print("The first letter of the word is:", word[0])
print(word)
for i in range(1, 6):
    print("Attempt", i)
    attempt = input()
    output = ""
    for j in range(min(len(word), len(attempt))):
        if attempt[j].lower() == word[j]:
            output += Back.GREEN + attempt[j] + Back.RESET
        elif attempt[j].lower() in word[j+1:]:
            output += Back.YELLOW + attempt[j] + Back.RESET
        else:
            output += attempt[j] + Back.RESET
    print(output)
    if word == attempt.lower():
        print("Gefeliciteerd")
        break
    if i == 5:
        print("Probeer het nog eens!")
        print("Het woord was:", word)
        break