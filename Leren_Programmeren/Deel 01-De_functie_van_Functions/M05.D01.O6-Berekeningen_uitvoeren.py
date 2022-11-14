def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def increment(a):
    return a + 1

def decrement(a):
    return a - 1

def double(a):
    return a * 2

def halve(a):
    return a / 2

def answering_machine(question):
    global answer
    if question == "A":
        if answer != 0:
            a = answer
            b = int(input("geef een getal: "))
            print(f'{a} + {b} = {addition(a, b)}')
            answer = addition(a, b)
        else:
            a = int(input("geef een getal: "))
            b = int(input("geef een getal: "))
            print(f'{a} + {b} = {addition(a, b)}')
            answer = addition(a, b)
    elif question == "B":
        if answer != 0:
            a = answer
            b = int(input("geef een getal: "))
            print(f'{a} - {b} = {subtraction(a, b)}')
            answer = subtraction(a, b)
        else:
            a = int(input("geef een getal: "))
            b = int(input("geef een getal: "))
            print(f'{a} - {b} = {subtraction(a, b)}')
            answer = subtraction(a, b)
    elif question == "C":
        if answer != 0:
            a = answer
            b = int(input("geef een getal: "))
            print(f'{a} * {b} = {multiplication(a, b)}')
            answer = multiplication(a, b)
        else:
            a = int(input("geef een getal: "))
            b = int(input("geef een getal: "))
            print(f'{a} * {b} = {multiplication(a, b)}')
            answer = multiplication(a, b)
    elif question == "D":
        if answer != 0:
            a = answer
            b = int(input("geef een getal: "))
            print(f'{a} / {b} = {division(a, b)}')
            answer = division(a, b)
        else:
            a = int(input("geef een getal: "))
            b = int(input("geef een getal: "))
            print(f'{a} / {b} = {division(a, b)}')
            answer = division(a, b)
    elif question == "E":
        if answer != 0:
            print(f'{answer} + 1 = {increment(answer)}')
            answer = increment(answer)
        else:
            a = int(input("geef een getal: "))
            print(f'{a} + 1 = {increment(a)}')
            answer = increment(a)
    elif question == "F":
        if answer != 0:
            print(f'{answer} - 1 = {decrement(answer)}')
            answer = decrement(answer)
        else:
            a = int(input("geef een getal: "))
            print(f'{a} - 1 = {decrement(a)}')
            answer = decrement(a)
    elif question == "G":
        if answer != 0:
            print(f'{answer} * 2 = {double(answer)}')
            answer = double(answer)
        else:
            a = int(input("geef een getal: "))
            print(f'{a} * 2 = {double(a)}')
            answer = double(a)
    elif question == "H":
        if answer != 0:
            print(f'{answer} / 2 = {halve(answer)}')
            answer = halve(answer)
        else:
            a = int(input("geef een getal: "))
            print(f'{a} / 2 = {halve(a)}')
            answer = halve(a)   
    elif question == 'l':
        quit()

answer = 0


while True:
    if answer != 0:
        question = input(f"Wil je wat met het antwoord ({answer}) doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren? I) Nee?\n >>")
        answering_machine(question.capitalize())
    else:
        question = input("wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?\n >>")
        answering_machine(question.capitalize())
