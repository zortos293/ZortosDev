from fruitmand import fruitmand
question_1 = input("Vul uw kleur in : ")
round_true = 0
round_false = 0

def check_color():
    for fruit in fruitmand:
            if fruit['color'] in question_1:
                return True
    return False



if check_color():
    for fruit in fruitmand:
        if fruit['color'] in question_1:
            if fruit['round'] == True:
                round_true += 1
            else:
                round_false += 1
    if round_true == round_false:
        print(f"Er zijn {round_true} ronde vruchten en {round_false} niet ronde vruchten in de kleur {question_1}")
    elif round_true > round_false:
        print(f"Er zijn {round_true - round_false} meer ronde vruchten dan niet ronde vruchten in de kleur {question_1}")
    elif round_true < round_false:
        print(f"Er zijn {abs(round_true - round_false)} minder ronde vruchten dan niet ronde vruchten in de kleur {question_1}")    
    exit()
else:
    print(f"De kleur {question_1} zit er niet in de fruitmand")
